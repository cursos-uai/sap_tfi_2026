#!/usr/bin/env python3
"""Modelo financiero del punto 8 del Plan de Desarrollo Tecnologico (E3-2C).

Reproducible y sin dependencias externas (solo biblioteca estandar).
Calcula, mes a mes durante 36 meses (2027-2029), ingresos, cobranzas,
egresos, impuestos, flujo de fondos, capital de trabajo, VAN, TIR,
periodo de repago, punto de equilibrio, escenarios y sensibilidad.
Escribe las tablas LaTeX en ../generado/ para que el texto del documento
y los cuadros usen exactamente los mismos numeros.

Uso (desde la carpeta de la entrega):
    python3 modelo/modelo_financiero.py

Todos los importes estan en USD constantes de octubre de 2026.
Cada valor de PARAMETROS es un supuesto declarado en la Seccion 8.
"""

from __future__ import annotations

import copy
import math
import os
from dataclasses import dataclass

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(AQUI, "..", "generado")

MESES = 36                      # enero 2027 (mes 1) a diciembre 2029 (mes 36)
ANIOS = (2027, 2028, 2029)
SEMANAS_POR_MES = 52 / 12

# ---------------------------------------------------------------------------
# Supuestos (todos se exponen en el documento)
# ---------------------------------------------------------------------------
PARAMETROS = {
    # Tiempo del autor y de terceros
    "valor_hora_autor": 12.0,       # USD/h, costo de oportunidad imputado
    "valor_hora_revisor": 25.0,     # USD/h, honorarios contra factura
    "valor_hora_instructor": 25.0,  # USD/h, instructor invitado (optimista)
    "horas_fijas_mes": {            # horas del autor no ligadas al volumen
        "produccion": 4.0,          # mantenimiento incremental del catalogo
        "comercializacion": 2.0,    # cotizaciones, contactos, seguimiento
        "administracion": 2.0,      # facturacion, cobranzas, registros
    },
    # Capacidad (Tabla 7.6): tope semanal del autor y fraccion para P4
    "tope_semanal": {"2027Q1-Q3": 12.0, "desde 2027Q4": 16.0},
    "fraccion_p4": 0.5,
    # Costos fijos en efectivo
    "contador_mes": 30.0,
    "infra_fija_mes": 8.0,
    "viajes_anuales": ((5, 100.0), (10, 100.0)),   # (mes del anio, USD)
    "aportes_autonomo_mes": 78271.56 / 1550.0,     # Cat. I, oct-2026
    # Impuestos
    "iibb": 0.045,                  # Santa Fe, alicuota basica (art. 6 LIA)
    "drei": 0.010,                  # Rosario, supuesto a validar
    "idc": 0.012,                   # Ley 25.413: 0,6 % credito + 0,6 % debito
    "ganancias": 0.35,              # alicuota maxima (arts. 73 y 94 LIG)
    "tipo_cambio": 1550.0,          # ARS por USD, BNA vendedor, oct-2026
    # Monotributo (servicios), valores vigentes ago-2026 a ene-2027 en ARS
    "monotributo": (                # (tope anual de facturacion, cuota mensual)
        (12009410.45, 49527.18),    # A
        (17595182.74, 56379.08),    # B
        (24670494.31, 66020.12),    # C
        (30628651.43, 84612.93),    # D
    ),
    "contador_mes_monotributo": 15.0,
    # Tasa de corte (modelo de acumulacion, USD nominales -> reales)
    "tasa_libre_riesgo": 0.050,     # Bono del Tesoro EE.UU. a 10 anios
    "beta": 1.0,
    "prima_mercado": 0.045,         # ERP implicita (Damodaran 2026)
    "riesgo_pais": 0.070,           # EMBI Argentina, 707 pb al 23/10/2026
    "prima_especifica": 0.050,      # tamano, unipersonalidad, iliquidez
    "inflacion_usd": 0.025,         # para pasar a USD constantes
}

INVERSION = {
    "activos_fijos": (
        ("Servidor de laboratorio dedicado (mini PC, 32 GB RAM, 1 TB NVMe)", 750.0),
        ("Disco externo de respaldo cifrado (2 TB)", 100.0),
        ("Equipo de transmisi\\'on y dictado remoto (existente)", 0.0),
        ("Software (sistema operativo, Podman, Go y herramientas)", 0.0),
        ("Redes, muebles y \\'utiles (se usan los existentes)", 0.0),
        ("Terreno, edificios, veh\\'iculos y maquinaria (no corresponden)", 0.0),
    ),
    "activos_diferidos": (
        ("Estudios legales: modelo de contrato, confidencialidad y licencias", 300.0),
        ("Inscripci\\'on fiscal y asesoramiento contable (sin constituci\\'on societaria)", 120.0),
        ("Capacitaci\\'on del autor en facilitaci\\'on y dictado", 200.0),
        ("Puesta en marcha: cat\\'alogo P4 y materiales (36 h del autor)", None),
    ),
    "horas_puesta_en_marcha": 36.0,   # enero y febrero de 2027, 18 h por mes
    "meses_puesta_en_marcha": (1, 2),
    "vida_util_anios": 3,
}


@dataclass(frozen=True)
class Paquete:
    clave: str
    nombre: str
    precio: float
    horas_autor: tuple          # horas por mes desde el inicio
    horas_revisor: float        # total, distribuidas como las del autor
    infra: float                # entorno temporal por servicio
    devengo: int                # mes (desde el inicio) en que se devenga
    cobranza: tuple             # ((meses desde el inicio, fraccion), ...)
    segmento: str               # institucional | pyme
    horas_instructor: float = 0.0


PAQUETES = {
    "taller": Paquete("taller", "Taller introductorio", 450.0, (10.0,), 0.0,
                      15.0, 0, ((0, 0.30), (2, 0.50), (3, 0.20)), "institucional"),
    "taller_gratis": Paquete("taller_gratis", "Taller de validaci\\'on (precio cero)",
                             0.0, (10.0,), 0.0, 15.0, 0, (), "institucional"),
    "taller_invitado": Paquete("taller_invitado", "Taller con instructor invitado",
                               450.0, (2.0,), 0.0, 15.0, 0,
                               ((0, 0.30), (2, 0.50), (3, 0.20)), "institucional",
                               horas_instructor=8.0),
    "taller_abierto": Paquete("taller_abierto", "Taller en cohorte abierta (inscripci\\'on previa)",
                              450.0, (10.0,), 0.0, 15.0, 0, ((0, 1.0),), "institucional"),
    "diagnostico": Paquete("diagnostico", "Diagn\\'ostico t\\'ecnico", 1000.0, (18.0,),
                           4.0, 10.0, 0, ((0, 0.50), (1, 0.50)), "pyme"),
    "piloto": Paquete("piloto", "Piloto corto (hasta 4 semanas)", 1600.0, (14.0, 14.0),
                      8.0, 20.0, 1, ((0, 0.30), (2, 0.70)), "pyme"),
    "acompanamiento": Paquete("acompanamiento", "Acompa\\~namiento (abono mensual)",
                              180.0, (4.0,), 0.0, 0.0, 0, ((1, 1.0),), "pyme"),
}

ORDEN_PAQUETES = ("taller", "taller_abierto", "taller_invitado", "diagnostico", "piloto",
                  "acompanamiento", "taller_gratis")


def mes(anio: int, m: int) -> int:
    """Indice 1..36 de un mes calendario del horizonte."""
    return (anio - 2027) * 12 + m


def abono(desde: int, hasta: int = MESES) -> list:
    return [("acompanamiento", t) for t in range(desde, hasta + 1)]


# Calendario base: respeta el pico academico (abril-mayo y agosto-septiembre),
# el receso de enero y julio, el primer servicio pago en 2027 Q2 (Tabla 5.2)
# y el tope mensual de horas P4 (se verifica en verificar_capacidad).
EVENTOS_BASE = [
    # 2027
    ("taller_gratis", mes(2027, 3)), ("taller", mes(2027, 4)),
    ("diagnostico", mes(2027, 5)), ("piloto", mes(2027, 6)),
    ("taller", mes(2027, 8)), ("diagnostico", mes(2027, 9)),
    ("taller", mes(2027, 11)),
    # 2028
    ("taller_gratis", mes(2028, 3)), ("taller", mes(2028, 4)),
    ("diagnostico", mes(2028, 5)), ("piloto", mes(2028, 6)),
    ("taller", mes(2028, 8)), ("diagnostico", mes(2028, 9)),
    ("piloto", mes(2028, 10)), ("taller", mes(2028, 12)),
    # 2029
    ("diagnostico", mes(2029, 2)), ("taller_gratis", mes(2029, 3)),
    ("taller", mes(2029, 4)), ("diagnostico", mes(2029, 5)),
    ("piloto", mes(2029, 6)), ("taller", mes(2029, 8)),
    ("diagnostico", mes(2029, 9)), ("piloto", mes(2029, 10)),
    ("taller", mes(2029, 12)),
] + abono(mes(2027, 12)) + abono(mes(2028, 8))


ESCENARIO_BASE = {
    "nombre": "Base",
    "eventos": EVENTOS_BASE,
    "factor_precio": {},            # clave -> factor
    "factor_cantidad": 1.0,         # sensibilidad: escala eventos pagos
    "cobranza": {},                 # clave -> perfil alternativo
    "incobrables": {"pyme": 0.0, "institucional": 0.0},
    "regimen": {2027: "general", 2028: "general", 2029: "general"},
    "horas_fijas_factor": {},       # mes desde -> factor sobre horas fijas
    "sin_viajes_desde": None,       # mes desde el cual no hay viajes
    "parametros": {},               # reemplazos puntuales de PARAMETROS
}


def escenario(**cambios) -> dict:
    esc = copy.deepcopy(ESCENARIO_BASE)
    for k, v in cambios.items():
        esc[k] = v
    return esc


# ---------------------------------------------------------------------------
# Motor de calculo
# ---------------------------------------------------------------------------
def tasa_de_corte(p: dict) -> dict:
    nominal = (p["tasa_libre_riesgo"] + p["beta"] * p["prima_mercado"]
               + p["riesgo_pais"] + p["prima_especifica"])
    real = (1 + nominal) / (1 + p["inflacion_usd"]) - 1
    return {"nominal": nominal, "real": round(real, 3)}


def inversion_inicial(p: dict) -> dict:
    af = sum(v for _, v in INVERSION["activos_fijos"])
    ad_items = []
    for nombre, v in INVERSION["activos_diferidos"]:
        if v is None:
            v = INVERSION["horas_puesta_en_marcha"] * p["valor_hora_autor"]
        ad_items.append((nombre, v))
    ad = sum(v for _, v in ad_items)
    return {"af": af, "ad": ad, "ad_items": ad_items,
            "amort_af": af / INVERSION["vida_util_anios"],
            "amort_ad": ad / INVERSION["vida_util_anios"]}


def anio_de(t: int) -> int:
    return 2027 + (t - 1) // 12


def cuota_monotributo(p: dict, facturacion_usd: float) -> float:
    ars = facturacion_usd * p["tipo_cambio"]
    for tope, cuota in p["monotributo"]:
        if ars <= tope:
            return cuota / p["tipo_cambio"]
    raise ValueError("La facturaci\u00f3n excede la categor\u00eda D del monotributo")


def tope_p4_mensual(p: dict, t: int) -> float:
    semanal = p["tope_semanal"]["2027Q1-Q3"] if t <= 9 else p["tope_semanal"]["desde 2027Q4"]
    return semanal * p["fraccion_p4"] * SEMANAS_POR_MES


def simular(esc: dict) -> dict:
    p = copy.deepcopy(PARAMETROS)
    p.update(esc["parametros"])
    n = MESES + 6                      # meses extra para lo que vence despues
    z = lambda: [0.0] * (n + 1)        # noqa: E731
    r = {k: z() for k in (
        "ventas", "cobranzas", "incobrables", "h_autor_var", "h_revisor",
        "h_instructor", "infra_var", "rem_var", "rem_fija", "revisor",
        "instructor", "infra_fija", "contador", "viajes", "cargas", "iibb_dev",
        "drei_dev", "iibb_pago", "drei_pago", "idc", "ganancias_pago", "h_fijas")}
    r["ventas_paquete"] = {k: [0.0] * (n + 1) for k in PAQUETES}
    r["cobranza_paquete"] = {k: [0.0] * (n + 1) for k in PAQUETES}
    r["unidades"] = {k: {a: 0.0 for a in ANIOS} for k in PAQUETES}
    r["horas_paquete"] = {k: {a: 0.0 for a in ANIOS} for k in PAQUETES}

    for clave, t0 in esc["eventos"]:
        paq = PAQUETES[clave]
        q = 1.0 if clave == "taller_gratis" else esc["factor_cantidad"]
        precio = paq.precio * esc["factor_precio"].get(clave, 1.0) * q
        perfil = esc["cobranza"].get(clave, paq.cobranza)
        incob = esc["incobrables"][paq.segmento]
        td = t0 + paq.devengo
        r["ventas"][td] += precio
        r["ventas_paquete"][clave][td] += precio
        r["unidades"][clave][anio_de(td)] += q
        r["incobrables"][td] += precio * incob
        for off, frac in perfil:
            monto = precio * frac * (1 - incob)
            r["cobranzas"][t0 + off] += monto
            r["cobranza_paquete"][clave][t0 + off] += monto
        tot_h = sum(paq.horas_autor)
        for off, h in enumerate(paq.horas_autor):
            t = t0 + off
            r["h_autor_var"][t] += h * q
            r["h_revisor"][t] += paq.horas_revisor * h / tot_h * q
            r["horas_paquete"][clave][anio_de(min(t, MESES))] += h * q
        r["h_instructor"][t0] += paq.horas_instructor * q
        r["infra_var"][t0] += paq.infra * q

    inv = inversion_inicial(p)
    hf = sum(p["horas_fijas_mes"].values())
    factores = sorted(esc["horas_fijas_factor"].items())
    for t in range(1, MESES + 1):
        f = 1.0
        for desde, fac in factores:
            if t >= desde:
                f = fac
        r["rem_fija"][t] = hf * f * p["valor_hora_autor"]
        r["h_fijas"][t] = hf * f
        r["rem_var"][t] = r["h_autor_var"][t] * p["valor_hora_autor"]
        r["revisor"][t] = r["h_revisor"][t] * p["valor_hora_revisor"]
        r["instructor"][t] = r["h_instructor"][t] * p["valor_hora_instructor"]
        r["infra_fija"][t] = p["infra_fija_mes"]
        reg = esc["regimen"][anio_de(t)]
        r["contador"][t] = p["contador_mes"] if reg == "general" else p["contador_mes_monotributo"]
        m_cal = (t - 1) % 12 + 1
        sin_viajes = esc["sin_viajes_desde"]
        for mv, monto in p["viajes_anuales"]:
            if m_cal == mv and not (sin_viajes and t >= sin_viajes):
                r["viajes"][t] += monto
        r["iibb_dev"][t] = r["ventas"][t] * p["iibb"]
        r["drei_dev"][t] = r["ventas"][t] * p["drei"]
        r["iibb_pago"][t + 1] += r["iibb_dev"][t]
        r["drei_pago"][t + 1] += r["drei_dev"][t]

    # Cargas sociales del autor: autonomo (regimen general) o cuota de
    # monotributo segun la facturacion anual (sustituye Ganancias y aportes).
    for a in ANIOS:
        meses = range(mes(a, 1), mes(a, 12) + 1)
        fact = sum(r["ventas"][t] for t in meses)
        cuota = (p["aportes_autonomo_mes"] if esc["regimen"][a] == "general"
                 else cuota_monotributo(p, fact))
        for t in meses:
            r["cargas"][t] = cuota

    for t in range(1, n + 1):
        r["idc"][t] = r["cobranzas"][t] * p["idc"]

    # Estado de resultados anual (devengado) y Ganancias
    er = {}
    quebranto = 0.0
    for a in ANIOS:
        ms = range(mes(a, 1), mes(a, 12) + 1)
        s = lambda k: sum(r[k][t] for t in ms)  # noqa: E731
        ventas = s("ventas")
        cv = {"rem_var": s("rem_var"), "revisor": s("revisor"),
              "instructor": s("instructor"), "infra_var": s("infra_var"),
              "iibb": s("iibb_dev"), "drei": s("drei_dev"), "idc": s("idc"),
              "incobrables": s("incobrables")}
        cf = {"rem_fija": s("rem_fija"), "contador": s("contador"),
              "infra_fija": s("infra_fija"), "viajes": s("viajes"),
              "cargas": s("cargas")}
        amort = inv["amort_af"] + inv["amort_ad"]
        rai = ventas - sum(cv.values()) - sum(cf.values()) - amort
        if esc["regimen"][a] == "general":
            base = rai - quebranto
            if base < 0:
                quebranto = -base
                impuesto = 0.0
            else:
                quebranto = 0.0
                impuesto = base * p["ganancias"]
        else:
            impuesto = 0.0
        er[a] = {"ventas": ventas, "cv": cv, "cf": cf, "amort": amort,
                 "rai": rai, "ganancias": impuesto,
                 "resultado": rai - impuesto, "quebranto_fin": quebranto,
                 "h_var": s("h_autor_var"), "h_fijas": s("h_fijas"),
                 "h_revisor": s("h_revisor"), "h_instructor": s("h_instructor")}

    # Pago de Ganancias (persona humana): saldo de la DDJJ en junio del anio
    # siguiente y cinco anticipos del 20 % (ago, oct, dic, feb, abr) a cuenta
    # del ejercicio siguiente, calculados sobre el impuesto del anterior.
    anticipos_pagados = {a: 0.0 for a in ANIOS + (2030,)}
    for a in ANIOS:
        imp = er[a]["ganancias"]
        siguiente = a + 1
        for (anio_pago, m_pago) in ((siguiente, 8), (siguiente, 10), (siguiente, 12),
                                    (siguiente + 1, 2), (siguiente + 1, 4)):
            t = mes(anio_pago, m_pago)
            r["ganancias_pago"][min(t, MESES)] += 0.2 * imp if siguiente <= 2029 else 0.0
            if siguiente <= 2029:
                anticipos_pagados[siguiente] += 0.2 * imp
        saldo = imp - anticipos_pagados[a]
        t = mes(a + 1, 6)
        r["ganancias_pago"][min(t, MESES)] += saldo
    # Lo que vence despues de diciembre de 2029 se cancela al cierre (mes 36).
    for k in ("iibb_pago", "drei_pago"):
        r[k][MESES] += sum(r[k][MESES + 1:])
        for t in range(MESES + 1, n + 1):
            r[k][t] = 0.0
    # La IDC de cobranzas posteriores al cierre se descuenta del recupero.
    pendiente_cobro = sum(r["cobranzas"][MESES + 1:])
    idc_pendiente = sum(r["idc"][MESES + 1:])

    # Flujo de caja mensual operativo (sin inversion)
    grupos_pago = ("rem_var", "rem_fija", "revisor", "instructor", "infra_var",
                   "infra_fija", "contador", "viajes", "cargas", "iibb_pago",
                   "drei_pago", "idc", "ganancias_pago")
    # Capital de trabajo: deficit acumulado maximo dentro de cada anio.
    # Los deficits o excedentes anuales ya forman parte del flujo de fondos
    # (el autor los cubre o los retira al cierre de cada anio); el capital de
    # trabajo es el colchon que cubre el desfasaje entre pagos y cobranzas
    # dentro del anio. Asi no se cuenta dos veces una perdida estructural.
    neto = [0.0] * (MESES + 1)
    minimo, mes_minimo = 0.0, 0
    for t in range(1, MESES + 1):
        pagos = sum(r[k][t] for k in grupos_pago)
        neto[t] = r["cobranzas"][t] - pagos
    deficit_anual = {}
    for a in ANIOS:
        acumulado, peor = 0.0, 0.0
        for t in range(mes(a, 1), mes(a, 12) + 1):
            acumulado += neto[t]
            if acumulado < peor:
                peor = acumulado
                if peor < minimo:
                    minimo, mes_minimo = peor, t
        deficit_anual[a] = -peor
    capital_trabajo = math.ceil(max(0.0, -minimo) / 50.0) * 50.0

    return {"esc": esc, "p": p, "r": r, "er": er, "inv": inv, "neto": neto,
            "kt": capital_trabajo, "mes_deficit": mes_minimo,
            "deficit_max": -minimo, "deficit_anual": deficit_anual,
            "grupos_pago": grupos_pago,
            "pendiente_cobro": pendiente_cobro, "idc_pendiente": idc_pendiente,
            "tasa": tasa_de_corte(p)}


# ---------------------------------------------------------------------------
# Indicadores
# ---------------------------------------------------------------------------
def van(flujos, k):
    return sum(f / (1 + k) ** t for t, f in enumerate(flujos))


def tir(flujos):
    lo, hi = -0.99, 10.0
    if van(flujos, lo) * van(flujos, hi) > 0:
        return None
    for _ in range(200):
        mid = (lo + hi) / 2
        if van(flujos, lo) * van(flujos, mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def repago(flujos, k=None):
    acum = 0.0
    for t, f in enumerate(flujos):
        fd = f if k is None else f / (1 + k) ** t
        previo = acum
        acum += fd
        if t > 0 and acum >= 0 > previo:
            return t - 1 + (-previo) / fd
    return None


def anual(res, clave, a):
    return sum(res["r"][clave][t] for t in range(mes(a, 1), mes(a, 12) + 1))


def flujo_de_fondos(res):
    """Devuelve las lineas anuales redondeadas (la tabla y el VAN coinciden)."""
    inv = res["inv"]
    lineas = {}
    lineas["inv_af"] = [-round(inv["af"]), 0, 0, 0]
    lineas["inv_ad"] = [-round(inv["ad"]), 0, 0, 0]
    lineas["inv_kt"] = [-round(res["kt"]), 0, 0, 0]
    lineas["cobranzas"] = [0] + [round(anual(res, "cobranzas", a)) for a in ANIOS]
    grupos = {
        "pag_rem": ("rem_var", "rem_fija"),
        "pag_terceros": ("revisor", "instructor"),
        "pag_cargas": ("cargas",),
        "pag_operativos": ("infra_var", "infra_fija", "contador", "viajes"),
        "pag_iibb": ("iibb_pago", "drei_pago", "idc"),
        "pag_ganancias": ("ganancias_pago",),
    }
    for nombre, claves in grupos.items():
        lineas[nombre] = [0] + [-round(sum(anual(res, c, a) for c in claves))
                                for a in ANIOS]
    recupero = round(res["kt"] + res["pendiente_cobro"] - res["idc_pendiente"])
    lineas["recupero"] = [0, 0, 0, recupero]
    total = [sum(v[i] for v in lineas.values()) for i in range(4)]
    lineas["total"] = total
    return lineas


def indicadores(res):
    ff = flujo_de_fondos(res)["total"]
    k = res["tasa"]["real"]
    return {"ff": ff, "van": van(ff, k), "tir": tir(ff),
            "repago": repago(ff), "repago_desc": repago(ff, k), "k": k}


def equilibrio(res, a):
    e = res["er"][a]
    ventas = e["ventas"]
    cv = sum(e["cv"].values())
    cf = sum(e["cf"].values()) + e["amort"]
    rc = (ventas - cv) / ventas if ventas else 0.0
    pe = cf / rc if rc > 0 else float("inf")
    horas = e["h_var"]
    contrib_hora = (ventas - cv) / horas if horas else 0.0
    return {"ventas": ventas, "cv": cv, "cf": cf, "rc": rc, "pe": pe,
            "cobertura": ventas / pe if pe else 0.0,
            "margen_seg": (ventas - pe) / ventas if ventas else 0.0,
            "contrib_hora": contrib_hora,
            "horas_pe": cf / contrib_hora if contrib_hora > 0 else float("inf"),
            "horas_pe_sem": (cf / contrib_hora / 52) if contrib_hora > 0 else float("inf")}


def mes_equilibrio(res):
    """Primer mes en que la contribucion de los ultimos 12 meses cubre los
    costos fijos (con amortizaciones) de esos mismos 12 meses."""
    r = res["r"]
    amort_mes = (res["inv"]["amort_af"] + res["inv"]["amort_ad"]) / 12
    cv_claves = ("rem_var", "revisor", "instructor", "infra_var", "iibb_dev",
                 "drei_dev", "idc", "incobrables")
    cf_claves = ("rem_fija", "contador", "infra_fija", "viajes", "cargas")
    for t in range(12, MESES + 1):
        ms = range(t - 11, t + 1)
        contrib = sum(r["ventas"][m] - sum(r[k][m] for k in cv_claves) for m in ms)
        fijos = sum(sum(r[k][m] for k in cf_claves) + amort_mes for m in ms)
        if contrib >= fijos:
            return t
    return None


def verificar_capacidad(res):
    p = res["p"]
    excesos = []
    uso_max = 0.0
    pm = INVERSION["meses_puesta_en_marcha"]
    for t in range(1, MESES + 1):
        h = res["r"]["h_autor_var"][t] + res["r"]["h_fijas"][t]
        if t in pm:
            h += INVERSION["horas_puesta_en_marcha"] / len(pm)
        tope = tope_p4_mensual(p, t)
        uso_max = max(uso_max, h / tope)
        if h > tope + 1e-9:
            excesos.append((t, h, tope))
    return excesos, uso_max


# ---------------------------------------------------------------------------
# Escenarios
# ---------------------------------------------------------------------------
LENTO = ((3, 0.50), (4, 0.50))        # instituciones a 90 y 120 dias

ESCENARIOS = {
    "base": ESCENARIO_BASE,
    "optimista": escenario(
        nombre="Optimista",
        factor_precio={k: 1.10 for k in PAQUETES},
        # El segundo abono empieza en abril de 2028 (cuatro meses antes) y un
        # instructor invitado dicta dos talleres extra por anio desde 2028.
        eventos=EVENTOS_BASE
        + abono(mes(2028, 4), mes(2028, 7))
        + [("taller_invitado", mes(2028, 6)), ("taller_invitado", mes(2028, 11)),
           ("taller_invitado", mes(2029, 6)), ("taller_invitado", mes(2029, 11))],
    ),
    "pesimista_1": escenario(
        nombre="Pesimista 1: demora y menor conversi\\'on",
        eventos=[
            ("taller_gratis", mes(2027, 3)), ("taller", mes(2027, 8)),
            ("diagnostico", mes(2027, 9)), ("taller", mes(2027, 11)),
            ("taller_gratis", mes(2028, 3)), ("taller", mes(2028, 4)),
            ("diagnostico", mes(2028, 5)), ("taller", mes(2028, 8)),
            ("diagnostico", mes(2028, 9)), ("piloto", mes(2028, 10)),
            ("taller_gratis", mes(2029, 3)), ("taller", mes(2029, 4)),
            ("diagnostico", mes(2029, 5)), ("piloto", mes(2029, 6)),
            ("taller", mes(2029, 8)), ("diagnostico", mes(2029, 9)),
        ] + abono(mes(2028, 7)),
        cobranza={"taller": LENTO},
    ),
    "pesimista_2": escenario(
        nombre="Pesimista 2: sin demanda PyME y presi\\'on de precio",
        eventos=[
            ("taller_gratis", mes(2027, 3)), ("taller", mes(2027, 8)),
            ("taller", mes(2027, 11)),
            ("taller_gratis", mes(2028, 3)), ("taller", mes(2028, 4)),
            ("taller", mes(2028, 8)), ("diagnostico", mes(2028, 9)),
            ("taller", mes(2028, 11)),
            ("taller_gratis", mes(2029, 3)), ("taller", mes(2029, 4)),
            ("taller", mes(2029, 8)), ("diagnostico", mes(2029, 9)),
            ("taller", mes(2029, 11)),
        ],
        factor_precio={"taller": 0.80, "diagnostico": 0.80},
        cobranza={"taller": LENTO},
        incobrables={"pyme": 0.05, "institucional": 0.0},
    ),
}

# Plan de contingencia aplicado al Pesimista 1 (Seccion 8.11)
_p1 = ESCENARIOS["pesimista_1"]
ESCENARIOS["contingencia"] = escenario(
    nombre="Pesimista 1 con plan de contingencia",
    # Desde 2028 los talleres se ofrecen en cohortes abiertas con inscripcion
    # previa (cobro al contado) en lugar de esperar el pago institucional.
    eventos=[("taller_abierto", t) if (c == "taller" and t >= mes(2028, 1)) else (c, t)
             for c, t in _p1["eventos"]],
    cobranza={"taller": LENTO,
              "diagnostico": ((0, 0.50), (1, 0.50)),
              "piloto": ((0, 0.50), (2, 0.50))},
    regimen={2027: "general", 2028: "monotributo", 2029: "monotributo"},
    horas_fijas_factor={mes(2027, 10): 0.5},
    sin_viajes_desde=mes(2028, 1),
)

# Alternativa de encuadre fiscal sobre el escenario base (Seccion 8.5)
ESCENARIOS["base_monotributo"] = escenario(
    nombre="Base con monotributo",
    regimen={2027: "monotributo", 2028: "monotributo", 2029: "monotributo"},
)


# ---------------------------------------------------------------------------
# Plan de salida: cierre ordenado al terminar un mes dado
# ---------------------------------------------------------------------------
def salida(res, hasta=12, recupero_af=0.40):
    """Perdida si se cierra al fin del mes `hasta`, cumpliendo lo contratado.

    Se cobran las ventas ya devengadas, se pagan los impuestos pendientes,
    se vende el equipamiento al `recupero_af` de su costo y el capital de
    trabajo remanente vuelve al autor. Separa la perdida monetaria de la
    remuneracion imputada al tiempo del autor (que no es un desembolso).
    """
    r, inv, p = res["r"], res["inv"], res["p"]
    ms = range(1, hasta + 1)
    ventas = sum(r["ventas"][t] for t in ms)
    cobrado = sum(r["cobranzas"][t] for t in ms)
    pendiente = 0.0
    for clave, t0 in res["esc"]["eventos"]:
        paq = PAQUETES[clave]
        if t0 + paq.devengo > hasta:
            continue
        for off, frac in res["esc"]["cobranza"].get(clave, paq.cobranza):
            if t0 + off > hasta:
                pendiente += paq.precio * res["esc"]["factor_precio"].get(clave, 1.0) * frac \
                    * (1 - res["esc"]["incobrables"][paq.segmento])
    pagos = sum(sum(r[k][t] for k in res["grupos_pago"]) for t in ms)
    iibb_pend = (r["iibb_dev"][hasta] + r["drei_dev"][hasta])
    venta_equipo = recupero_af * inv["af"]
    neto = (cobrado + pendiente * (1 - p["idc"]) - pagos - iibb_pend
            - inv["af"] - inv["ad"] + venta_equipo)
    imputado = (sum(r["rem_var"][t] + r["rem_fija"][t] for t in ms)
                + INVERSION["horas_puesta_en_marcha"] * p["valor_hora_autor"])
    return {"perdida": -neto, "imputado": imputado, "monetaria": -neto - imputado,
            "ventas": ventas, "venta_equipo": venta_equipo}


# ---------------------------------------------------------------------------
# Sensibilidad: umbrales que anulan el VAN
# ---------------------------------------------------------------------------
def van_de(esc):
    return indicadores(simular(esc))["van"]


def umbral(fabricar, lo, hi):
    """Biseccion sobre un parametro escalar hasta VAN = 0."""
    vlo, vhi = van_de(fabricar(lo)), van_de(fabricar(hi))
    if vlo * vhi > 0:
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        vm = van_de(fabricar(mid))
        if vlo * vm <= 0:
            hi, vhi = mid, vm
        else:
            lo, vlo = mid, vm
    return (lo + hi) / 2


def sensibilidad():
    base = ESCENARIO_BASE
    precio = umbral(lambda f: escenario(factor_precio={k: f for k in PAQUETES}), 0.3, 1.0)
    cantidad = umbral(lambda f: escenario(factor_cantidad=f), 0.2, 1.0)
    hora = umbral(lambda h: escenario(parametros={"valor_hora_autor": h}), 12.0, 60.0)
    filas = []
    for etiqueta, esc in (
        ("Precios $-$20\\,\\%", escenario(factor_precio={k: 0.8 for k in PAQUETES})),
        ("Precios +20\\,\\%", escenario(factor_precio={k: 1.2 for k in PAQUETES})),
        ("Volumen $-$20\\,\\%", escenario(factor_cantidad=0.8)),
        ("Volumen +20\\,\\%", escenario(factor_cantidad=1.2)),
        ("Valor hora del autor USD~16", escenario(parametros={"valor_hora_autor": 16.0})),
        ("Valor hora del autor USD~8", escenario(parametros={"valor_hora_autor": 8.0})),
        ("Tasa de corte +5 p.p.", None),
        ("Tasa de corte $-$5 p.p.", None),
    ):
        if esc is None:
            ind = indicadores(simular(base))
            dk = 0.05 if "+5" in etiqueta else -0.05
            filas.append((etiqueta, van(ind["ff"], ind["k"] + dk)))
        else:
            filas.append((etiqueta, indicadores(simular(esc))["van"]))
    return {"precio": precio, "cantidad": cantidad, "hora": hora, "filas": filas}


# ---------------------------------------------------------------------------
# Formato
# ---------------------------------------------------------------------------
def num(x, dec=0):
    if x is None:
        return "--"
    if isinstance(x, float) and math.isinf(x):
        return "--"
    s = f"{abs(x):,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if round(x, dec) == 0:
        return "0" if dec == 0 else s
    return ("$-$" + s) if x < 0 else s


def pct(x, dec=1):
    if x is None:
        return "--"
    return num(100 * x, dec) + "\\,\\%"


def pct_tir(x):
    if x is None:
        return "no existe"
    return "negativa" if x < 0 else pct(x)


def anios_txt(x):
    return "no se recupera" if x is None else num(x, 1) + " a\\~nos"


def escribir(nombre, contenido):
    os.makedirs(SALIDA, exist_ok=True)
    with open(os.path.join(SALIDA, nombre), "w", encoding="utf-8") as fh:
        fh.write("% Generado por modelo/modelo_financiero.py. No editar a mano.\n")
        fh.write(contenido)


def fila(*celdas):
    return " & ".join(celdas) + "\\\\\n"


# ---------------------------------------------------------------------------
# Tablas
# ---------------------------------------------------------------------------
def tabla_ingresos(res):
    r = res["r"]
    filas = ""
    tot = {a: 0.0 for a in ANIOS}
    for k in ORDEN_PAQUETES:
        paq = PAQUETES[k]
        u = r["unidades"][k]
        if sum(u.values()) == 0:
            continue
        ventas = {a: round(sum(r["ventas_paquete"][k][t]
                               for t in range(mes(a, 1), mes(a, 12) + 1))) for a in ANIOS}
        celdas = [paq.nombre, num(paq.precio)]
        for a in ANIOS:
            celdas += [num(u[a]), num(ventas[a])]
            tot[a] += ventas[a]
        celdas.append(num(sum(ventas.values())))
        filas += fila(*celdas)
    total = fila("\\textbf{Total ventas}", "", "", "\\textbf{" + num(tot[2027]) + "}",
                 "", "\\textbf{" + num(tot[2028]) + "}", "",
                 "\\textbf{" + num(tot[2029]) + "}",
                 "\\textbf{" + num(sum(tot.values())) + "}")
    return filas + "\\midrule\n" + total


def tabla_paquetes(p):
    filas = ""
    for k in ("taller", "diagnostico", "piloto", "acompanamiento", "taller_gratis"):
        paq = PAQUETES[k]
        h = sum(paq.horas_autor)
        meses = len(paq.horas_autor)
        costo_directo = (h * p["valor_hora_autor"] + paq.horas_revisor * p["valor_hora_revisor"]
                         + paq.infra)
        por_hora = paq.precio / h if paq.precio else 0.0
        filas += fila(paq.nombre, num(h), num(paq.horas_revisor), str(meses),
                      num(round(costo_directo)), num(paq.precio),
                      num(por_hora, 1) if paq.precio else "--")
    return filas


def tabla_cobranzas_perfil():
    filas = ""
    for k in ("taller", "diagnostico", "piloto", "acompanamiento"):
        paq = PAQUETES[k]
        perfil = dict(paq.cobranza)
        if k == "piloto":
            cont, d30, d60, d90 = perfil.get(0, 0), perfil.get(2, 0), 0, 0
            nota = "anticipo al iniciar; saldo a 30 d\\'ias de la aceptaci\\'on"
        else:
            cont, d30, d60, d90 = (perfil.get(0, 0), perfil.get(1, 0),
                                   perfil.get(2, 0), perfil.get(3, 0))
            nota = {"taller": "instituci\\'on: 60 d\\'ias, con 20\\,\\% de atraso a 90",
                    "diagnostico": "anticipo al aceptar la propuesta",
                    "acompanamiento": "abono mes vencido"}[k]
        filas += fila(paq.nombre, pct(cont, 0), pct(d30, 0), pct(d60, 0), pct(d90, 0), nota)
    return filas


def tabla_cobranzas_anual(res):
    r = res["r"]
    filas = ""
    for a in ANIOS:
        ms = range(mes(a, 1), mes(a, 12) + 1)
        ventas = round(sum(r["ventas"][t] for t in ms))
        cob = round(sum(r["cobranzas"][t] for t in ms))
        filas += fila(str(a), num(ventas), num(cob), num(cob - ventas))
    pend = round(res["pendiente_cobro"])
    filas += fila("Cobranzas posteriores al cierre (2030)", "--", num(pend), "--")
    return filas


def tabla_egresos(res):
    er = res["er"]
    p = res["p"]
    vh = p["valor_hora_autor"]
    hf = p["horas_fijas_mes"]
    tot_hf = sum(hf.values())

    def por_anio(f):
        return [round(f(a)) for a in ANIOS]

    lineas = [
        ("\\textit{Costos de producci\\'on (prestaci\\'on de los servicios)}", None, None),
        ("Horas del autor por paquete", "V", por_anio(lambda a: er[a]["cv"]["rem_var"])),
        ("Revisor externo e instructor invitado", "V",
         por_anio(lambda a: er[a]["cv"]["revisor"] + er[a]["cv"]["instructor"])),
        ("Entornos temporales de laboratorio", "V", por_anio(lambda a: er[a]["cv"]["infra_var"])),
        ("Mantenimiento incremental del cat\\'alogo (autor)", "F",
         por_anio(lambda a: er[a]["cf"]["rem_fija"] * hf["produccion"] / tot_hf)),
        ("\\textit{Costos de comercializaci\\'on y ventas}", None, None),
        ("Gesti\\'on comercial (autor)", "F",
         por_anio(lambda a: er[a]["cf"]["rem_fija"] * hf["comercializacion"] / tot_hf)),
        ("Viajes a \\emph{meetups} y congresos", "F", por_anio(lambda a: er[a]["cf"]["viajes"])),
        ("Ingresos Brutos y DReI", "V",
         por_anio(lambda a: er[a]["cv"]["iibb"] + er[a]["cv"]["drei"])),
        ("Incobrables", "V", por_anio(lambda a: er[a]["cv"]["incobrables"])),
        ("\\textit{Costos de administraci\\'on}", None, None),
        ("Gesti\\'on administrativa (autor)", "F",
         por_anio(lambda a: er[a]["cf"]["rem_fija"] * hf["administracion"] / tot_hf)),
        ("Honorarios contables", "F", por_anio(lambda a: er[a]["cf"]["contador"])),
        ("Aportes previsionales del autor", "F", por_anio(lambda a: er[a]["cf"]["cargas"])),
        ("Servicios digitales fijos", "F", por_anio(lambda a: er[a]["cf"]["infra_fija"])),
        ("Impuesto a los d\\'ebitos y cr\\'editos", "V", por_anio(lambda a: er[a]["cv"]["idc"])),
    ]
    filas = ""
    tot_f = [0, 0, 0]
    tot_v = [0, 0, 0]
    for nombre, tipo, valores in lineas:
        if tipo is None:
            filas += nombre + " & & & & & \\\\\n"
            continue
        if sum(valores) == 0 and tipo == "V" and nombre == "Incobrables":
            continue
        for i, v in enumerate(valores):
            (tot_f if tipo == "F" else tot_v)[i] += v
        filas += fila("\\quad " + nombre, tipo, *[num(v) for v in valores], num(sum(valores)))
    filas += "\\midrule\n"
    filas += fila("Total costos variables", "V", *[num(v) for v in tot_v], num(sum(tot_v)))
    filas += fila("Total costos fijos (erogables)", "F", *[num(v) for v in tot_f], num(sum(tot_f)))
    filas += fila("\\textbf{Total egresos operativos}", "",
                  *["\\textbf{" + num(tot_v[i] + tot_f[i]) + "}" for i in range(3)],
                  "\\textbf{" + num(sum(tot_v) + sum(tot_f)) + "}")
    return filas, tot_v, tot_f


def tabla_inversion(res):
    inv = res["inv"]
    filas = "\\textit{Activos fijos} & & \\\\\n"
    for nombre, v in INVERSION["activos_fijos"]:
        filas += fila("\\quad " + nombre, "3 a\\~nos" if v else "--", num(v))
    filas += fila("\\quad \\textbf{Subtotal activos fijos}", "", "\\textbf{" + num(inv["af"]) + "}")
    filas += "\\textit{Activos diferidos} & & \\\\\n"
    for nombre, v in inv["ad_items"]:
        filas += fila("\\quad " + nombre, "3 a\\~nos", num(v))
    filas += fila("\\quad \\textbf{Subtotal activos diferidos}", "", "\\textbf{" + num(inv["ad"]) + "}")
    filas += "\\textit{Capital de trabajo} & & \\\\\n"
    filas += fila("\\quad D\\'eficit acumulado m\\'aximo de caja, redondeado", "se recupera", num(res["kt"]))
    filas += "\\midrule\n"
    total = inv["af"] + inv["ad"] + res["kt"]
    filas += fila("\\textbf{Inversi\\'on total (momento 0)}", "", "\\textbf{" + num(total) + "}")
    return filas, total


def tabla_amortizaciones(res):
    inv = res["inv"]
    filas = ""
    vu = INVERSION["vida_util_anios"]
    for etiqueta, base, cuota in (("Activos fijos (depreciaci\\'on)", inv["af"], inv["amort_af"]),
                                  ("Activos diferidos (amortizaci\\'on)", inv["ad"], inv["amort_ad"])):
        filas += fila(etiqueta, num(base), str(vu), *[num(cuota) for _ in ANIOS], "0")
    total = inv["amort_af"] + inv["amort_ad"]
    filas += "\\midrule\n"
    filas += fila("\\textbf{Total}", "\\textbf{" + num(inv["af"] + inv["ad"]) + "}", "",
                  *["\\textbf{" + num(total) + "}" for _ in ANIOS], "0")
    return filas


def tabla_resultados(res):
    er = res["er"]
    rows = []
    v = [round(er[a]["ventas"]) for a in ANIOS]
    cv = [round(sum(er[a]["cv"].values())) for a in ANIOS]
    cf = [round(sum(er[a]["cf"].values())) for a in ANIOS]
    am = [round(er[a]["amort"]) for a in ANIOS]
    rai = [v[i] - cv[i] - cf[i] - am[i] for i in range(3)]
    gan = [round(er[a]["ganancias"]) for a in ANIOS]
    neto = [rai[i] - gan[i] for i in range(3)]
    queb = [round(er[a]["quebranto_fin"]) for a in ANIOS]
    rows.append(("Ventas netas de IVA", v))
    rows.append(("($-$) Costos variables", [-x for x in cv]))
    rows.append(("\\textbf{Contribuci\\'on marginal}", [v[i] - cv[i] for i in range(3)]))
    rows.append(("($-$) Costos fijos erogables", [-x for x in cf]))
    rows.append(("($-$) Amortizaciones", [-x for x in am]))
    rows.append(("\\textbf{Resultado antes de Ganancias}", rai))
    rows.append(("Quebranto a trasladar al cierre", queb))
    rows.append(("($-$) Impuesto a las ganancias determinado (35\\,\\%)", [-x for x in gan]))
    rows.append(("\\textbf{Resultado neto}", neto))
    out = ""
    for nombre, vals in rows:
        out += fila(nombre, *[num(x) for x in vals], num(sum(vals)) if "Quebranto" not in nombre else "--")
    return out, {"rai": rai, "gan": gan, "neto": neto}


def tabla_ganancias_pagos(res):
    r = res["r"]
    er = res["er"]
    filas = ""
    for a in ANIOS:
        filas += fila(str(a), num(round(er[a]["rai"])), num(round(er[a]["ganancias"])),
                      num(round(anual(res, "ganancias_pago", a))))
    return filas


def tabla_iibb(res):
    filas = ""
    for a in ANIOS:
        ventas = round(res["er"][a]["ventas"])
        iibb = round(res["er"][a]["cv"]["iibb"])
        drei = round(res["er"][a]["cv"]["drei"])
        pago = round(anual(res, "iibb_pago", a) + anual(res, "drei_pago", a))
        filas += fila(str(a), num(ventas), num(iibb), num(drei), num(pago))
    return filas


def tabla_remuneraciones(res):
    er = res["er"]
    p = res["p"]
    filas = ""
    filas += fila("Horas del autor ligadas al volumen", *[num(er[a]["h_var"]) for a in ANIOS],
                  num(sum(er[a]["h_var"] for a in ANIOS)))
    filas += fila("\\quad Remuneraci\\'on imputada (USD~" + num(p["valor_hora_autor"]) + "/h)",
                  *[num(round(er[a]["cv"]["rem_var"])) for a in ANIOS],
                  num(sum(round(er[a]["cv"]["rem_var"]) for a in ANIOS)))
    filas += fila("Horas del autor no ligadas al volumen", *[num(er[a]["h_fijas"]) for a in ANIOS],
                  num(sum(er[a]["h_fijas"] for a in ANIOS)))
    filas += fila("\\quad Remuneraci\\'on imputada (USD~" + num(p["valor_hora_autor"]) + "/h)",
                  *[num(round(er[a]["cf"]["rem_fija"])) for a in ANIOS],
                  num(sum(round(er[a]["cf"]["rem_fija"]) for a in ANIOS)))
    filas += fila("Horas del revisor externo", *[num(er[a]["h_revisor"]) for a in ANIOS],
                  num(sum(er[a]["h_revisor"] for a in ANIOS)))
    filas += fila("\\quad Honorarios (USD~" + num(p["valor_hora_revisor"]) + "/h)",
                  *[num(round(er[a]["cv"]["revisor"])) for a in ANIOS],
                  num(sum(round(er[a]["cv"]["revisor"]) for a in ANIOS)))
    filas += fila("Aportes previsionales del autor (aut\\'onomo, cat. I)",
                  *[num(round(er[a]["cf"]["cargas"])) for a in ANIOS],
                  num(sum(round(er[a]["cf"]["cargas"]) for a in ANIOS)))
    filas += fila("Contribuciones patronales", "0", "0", "0", "0")
    tot = [round(er[a]["cv"]["rem_var"]) + round(er[a]["cf"]["rem_fija"])
           + round(er[a]["cv"]["revisor"]) + round(er[a]["cf"]["cargas"]) for a in ANIOS]
    filas += "\\midrule\n"
    filas += fila("\\textbf{Total remuneraciones, honorarios y cargas}",
                  *["\\textbf{" + num(x) + "}" for x in tot], "\\textbf{" + num(sum(tot)) + "}")
    return filas


def tabla_capacidad(res):
    p = res["p"]
    filas = ""
    pm = INVERSION["meses_puesta_en_marcha"]
    extra = lambda t: INVERSION["horas_puesta_en_marcha"] / len(pm) if t in pm else 0.0  # noqa: E731
    for a in ANIOS:
        ms = range(mes(a, 1), mes(a, 12) + 1)
        h = sum(res["r"]["h_autor_var"][t] + res["r"]["h_fijas"][t] + extra(t) for t in ms)
        tope = sum(tope_p4_mensual(p, t) for t in ms)
        pico = max((res["r"]["h_autor_var"][t] + res["r"]["h_fijas"][t] + extra(t))
                   / tope_p4_mensual(p, t) for t in ms)
        filas += fila(str(a), num(h), num(tope), pct(h / tope, 0), pct(pico, 0))
    return filas


def tabla_presupuesto(res, ff):
    """Presupuesto financiero anual: entradas, salidas y saldo de caja."""
    inv = res["inv"]
    aporte = round(inv["af"]) + round(inv["ad"]) + round(res["kt"])
    filas = ""
    entradas = [aporte] + ff["cobranzas"][1:]
    salidas_inv = [-(round(inv["af"]) + round(inv["ad"])), 0, 0, 0]
    netos = []
    saldos_ini = []
    saldo = 0
    for i in range(4):
        saldos_ini.append(saldo)
        neto = (entradas[i] + salidas_inv[i] + ff["pag_rem"][i] + ff["pag_terceros"][i]
                + ff["pag_cargas"][i] + ff["pag_operativos"][i] + ff["pag_iibb"][i]
                + ff["pag_ganancias"][i])
        netos.append(neto)
        saldo += neto
    saldos_fin = [saldos_ini[i] + netos[i] for i in range(4)]
    lineas = [
        ("Saldo inicial de caja", saldos_ini),
        ("(+) Aporte del autor", [aporte, 0, 0, 0]),
        ("(+) Cobranzas", ff["cobranzas"]),
        ("($-$) Inversi\\'on en activos fijos y diferidos", salidas_inv),
        ("($-$) Remuneraci\\'on del autor", ff["pag_rem"]),
        ("($-$) Revisor externo e instructor", ff["pag_terceros"]),
        ("($-$) Aportes previsionales del autor", ff["pag_cargas"]),
        ("($-$) Gastos operativos", ff["pag_operativos"]),
        ("($-$) IIBB, DReI y d\\'ebitos y cr\\'editos", ff["pag_iibb"]),
        ("($-$) Impuesto a las ganancias", ff["pag_ganancias"]),
        ("\\textbf{Flujo neto del per\\'iodo}", netos),
        ("\\textbf{Saldo final de caja}", saldos_fin),
    ]
    for nombre, vals in lineas:
        filas += fila(nombre, *[num(x) for x in vals])
    return filas, saldos_fin


def tabla_flujo_trimestral_2027(res):
    r = res["r"]
    filas = ""
    acum = 0.0
    for q in range(4):
        ms = range(q * 3 + 1, q * 3 + 4)
        cob = sum(r["cobranzas"][t] for t in ms)
        pag = sum(sum(r[k][t] for k in res["grupos_pago"]) for t in ms)
        acum += cob - pag
        filas += fila(f"2027 Q{q + 1}", num(round(cob)), num(-round(pag)),
                      num(round(cob - pag)), num(round(acum)))
    return filas


def tabla_flujo_fondos(ff):
    nombres = [
        ("inv_af", "Inversi\\'on en activos fijos"),
        ("inv_ad", "Inversi\\'on en activos diferidos"),
        ("inv_kt", "Inversi\\'on en capital de trabajo"),
        ("cobranzas", "Cobranzas"),
        ("pag_rem", "Remuneraci\\'on del autor"),
        ("pag_terceros", "Revisor externo e instructor"),
        ("pag_cargas", "Aportes previsionales"),
        ("pag_operativos", "Gastos operativos"),
        ("pag_iibb", "IIBB, DReI y d\\'ebitos y cr\\'editos"),
        ("pag_ganancias", "Impuesto a las ganancias pagado"),
        ("recupero", "Recupero de capital de trabajo y cobranzas al cierre"),
    ]
    filas = ""
    for k, nombre in nombres:
        filas += fila(nombre, *[num(x) for x in ff[k]])
    filas += "\\midrule\n"
    filas += fila("\\textbf{Flujo de fondos del proyecto}", *["\\textbf{" + num(x) + "}" for x in ff["total"]])
    acum = []
    s = 0
    for x in ff["total"]:
        s += x
        acum.append(s)
    filas += fila("Flujo acumulado", *[num(x) for x in acum])
    return filas, acum


def tabla_flujo_descontado(ind):
    k = ind["k"]
    filas = ""
    acum = 0.0
    for t, f in enumerate(ind["ff"]):
        fd = f / (1 + k) ** t
        acum += fd
        filas += fila(str(t) + (" (inicio 2027)" if t == 0 else f" ({2026 + t})"),
                      num(f), num(1 / (1 + k) ** t, 4), num(round(fd)), num(round(acum)))
    return filas


def tabla_equilibrio(res):
    filas = ""
    for a in ANIOS:
        e = equilibrio(res, a)
        filas += fila(str(a), num(round(e["cf"])), pct(e["rc"]), num(round(e["pe"])),
                      num(round(e["ventas"])), pct(e["margen_seg"]),
                      num(round(e["horas_pe"])), num(e["horas_pe_sem"], 1))
    return filas


def tabla_escenarios(resultados):
    filas = ""
    for clave in ("optimista", "base", "pesimista_1", "pesimista_2"):
        res, ind = resultados[clave]
        ventas = sum(round(res["er"][a]["ventas"]) for a in ANIOS)
        e29 = equilibrio(res, 2029)
        filas += fila(res["esc"]["nombre"], num(ventas), num(round(res["kt"])),
                      num(round(ind["van"])), pct_tir(ind["tir"]),
                      anios_txt(ind["repago"]), pct(e29["cobertura"], 0))
    return filas


def tabla_sensibilidad(sens, van_base):
    filas = ""
    for etiqueta, v in sens["filas"]:
        filas += fila(etiqueta, num(round(v)), num(round(v - van_base)))
    return filas


def tabla_tasa(p, tasa):
    filas = ""
    filas += fila("Tasa libre de riesgo (bono del Tesoro de EE.UU. a 10 a\\~nos)", pct(p["tasa_libre_riesgo"]))
    filas += fila("Beta $\\times$ prima de riesgo de mercado (" + num(p["beta"], 1) + " $\\times$ "
                  + pct(p["prima_mercado"]) + ")", pct(p["beta"] * p["prima_mercado"]))
    filas += fila("Riesgo pa\\'is (EMBI Argentina)", pct(p["riesgo_pais"]))
    filas += fila("Prima espec\\'ifica (escala, unipersonalidad, iliquidez)", pct(p["prima_especifica"]))
    filas += "\\midrule\n"
    filas += fila("Tasa nominal en USD", pct(tasa["nominal"]))
    filas += fila("Inflaci\\'on esperada en USD (para pasar a moneda constante)", pct(p["inflacion_usd"]))
    filas += fila("\\textbf{Tasa de corte real en USD constantes}", "\\textbf{" + pct(tasa["real"]) + "}")
    return filas


# ---------------------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------------------
def main():
    resultados = {}
    for clave, esc in ESCENARIOS.items():
        res = simular(esc)
        resultados[clave] = (res, indicadores(res))
        excesos, uso = verificar_capacidad(res)
        if excesos and clave in ("base", "optimista", "pesimista_1", "pesimista_2",
                                 "contingencia"):
            raise SystemExit(f"{clave}: excede el tope P4 en {excesos}")

    res, ind = resultados["base"]
    p = res["p"]
    ff = flujo_de_fondos(res)
    sens = sensibilidad()

    egresos_filas, tot_v, tot_f = tabla_egresos(res)
    inv_filas, inv_total = tabla_inversion(res)
    resultados_filas, er_disp = tabla_resultados(res)
    presup_filas, saldos = tabla_presupuesto(res, ff)
    ff_filas, ff_acum = tabla_flujo_fondos(ff)

    escribir("tab_ingresos.tex", tabla_ingresos(res))
    escribir("tab_cobranzas_perfil.tex", tabla_cobranzas_perfil())
    escribir("tab_paquetes.tex", tabla_paquetes(p))
    escribir("tab_cobranzas_anual.tex", tabla_cobranzas_anual(res))
    escribir("tab_egresos.tex", egresos_filas)
    escribir("tab_inversion.tex", inv_filas)
    escribir("tab_amortizaciones.tex", tabla_amortizaciones(res))
    escribir("tab_resultados.tex", resultados_filas)
    escribir("tab_ganancias.tex", tabla_ganancias_pagos(res))
    escribir("tab_iibb.tex", tabla_iibb(res))
    escribir("tab_remuneraciones.tex", tabla_remuneraciones(res))
    escribir("tab_capacidad.tex", tabla_capacidad(res))
    escribir("tab_presupuesto.tex", presup_filas)
    escribir("tab_trimestral2027.tex", tabla_flujo_trimestral_2027(res))
    escribir("tab_flujo.tex", ff_filas)
    escribir("tab_descontado.tex", tabla_flujo_descontado(ind))
    escribir("tab_equilibrio.tex", tabla_equilibrio(res))
    escribir("tab_escenarios.tex", tabla_escenarios(resultados))
    escribir("tab_sensibilidad.tex", tabla_sensibilidad(sens, ind["van"]))
    escribir("tab_tasa.tex", tabla_tasa(p, res["tasa"]))

    # Macros con las cifras que cita el texto
    e28, e29 = equilibrio(res, 2028), equilibrio(res, 2029)
    mono = resultados["base_monotributo"][1]
    cont = resultados["contingencia"]
    p1 = resultados["pesimista_1"]
    p2 = resultados["pesimista_2"]
    opt = resultados["optimista"]
    ventas = {a: round(res["er"][a]["ventas"]) for a in ANIOS}
    _, uso_base = verificar_capacidad(res)
    uso_anual = []
    for a in ANIOS:
        ms = range(mes(a, 1), mes(a, 12) + 1)
        pm = INVERSION["meses_puesta_en_marcha"]
        h = sum(res["r"]["h_autor_var"][t] + res["r"]["h_fijas"][t]
                + (INVERSION["horas_puesta_en_marcha"] / len(pm) if t in pm else 0.0) for t in ms)
        uso_anual.append(h / sum(tope_p4_mensual(p, t) for t in ms))
    caja, caja_min = res["kt"], res["kt"]
    for a in ANIOS:
        for t in range(mes(a, 1), mes(a, 12) + 1):
            caja += res["neto"][t]
            caja_min = min(caja_min, caja)
    m_def = res["mes_deficit"]
    meses_txt = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
                 "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    p2_res = p2[0]
    sal = salida(p2_res, hasta=12)
    macros = {
        "finTasaReal": pct(res["tasa"]["real"]),
        "finTasaNominal": pct(res["tasa"]["nominal"]),
        "finVAN": num(round(ind["van"])),
        "finTIR": pct(ind["tir"]),
        "finRepago": num(ind["repago"], 1),
        "finRepagoDesc": num(ind["repago_desc"], 1),
        "finInversionTotal": num(inv_total),
        "finInversionAF": num(res["inv"]["af"]),
        "finInversionAD": num(res["inv"]["ad"]),
        "finKT": num(res["kt"]),
        "finDeficitMes": meses_txt[(m_def - 1) % 12] + f" de {2027 + (m_def - 1) // 12}",
        "finDeficitMax": num(round(res["deficit_max"])),
        "finAmortAnual": num(round(res["inv"]["amort_af"] + res["inv"]["amort_ad"])),
        "finVentasA": num(ventas[2027]), "finVentasB": num(ventas[2028]),
        "finVentasC": num(ventas[2029]), "finVentasTotal": num(sum(ventas.values())),
        "finPEB": num(round(e28["pe"])), "finPEC": num(round(e29["pe"])),
        "finPEA": num(round(equilibrio(res, 2027)["pe"])),
        "finCoberturaA": pct(equilibrio(res, 2027)["cobertura"], 0),
        "finMargenSegB": pct(e28["margen_seg"], 0), "finMargenSegC": pct(e29["margen_seg"], 0),
        "finHorasPESemB": num(e28["horas_pe_sem"], 1), "finHorasPESemC": num(e29["horas_pe_sem"], 1),
        "finRCB": pct(e28["rc"]), "finContribHoraB": num(e28["contrib_hora"], 1),
        "finRAIA": num(er_disp["rai"][0]), "finRAIB": num(er_disp["rai"][1]),
        "finRAIC": num(er_disp["rai"][2]),
        "finGanB": num(er_disp["gan"][1]), "finGanC": num(er_disp["gan"][2]),
        "finSaldoFinal": num(saldos[-1]),
        "finUsoMax": pct(uso_base, 0),
        "finVANMono": num(round(mono["van"])), "finTIRMono": pct(mono["tir"]),
        "finVANOpt": num(round(opt[1]["van"])), "finTIROpt": pct(opt[1]["tir"]),
        "finVANPuno": num(round(p1[1]["van"])), "finTIRPuno": pct_tir(p1[1]["tir"]),
        "finVANPdos": num(round(p2[1]["van"])), "finTIRPdos": pct_tir(p2[1]["tir"]),
        "finVANCont": num(round(cont[1]["van"])), "finTIRCont": pct(cont[1]["tir"]),
        "finRepagoCont": anios_txt(cont[1]["repago"]),
        "finRepagoPuno": anios_txt(p1[1]["repago"]),
        "finKTPuno": num(round(p1[0]["kt"])), "finKTPdos": num(round(p2_res["kt"])),
        "finKTCont": num(round(cont[0]["kt"])),
        "finUmbralPrecio": pct(1 - sens["precio"], 0) if sens["precio"] else "--",
        "finUmbralVolumen": pct(1 - sens["cantidad"], 0) if sens["cantidad"] else "--",
        "finUmbralHora": num(sens["hora"], 1) if sens["hora"] else "--",
        "finSalidaPerdida": num(round(sal["perdida"])),
        "finSalidaImputada": num(round(sal["imputado"])),
        "finSalidaMonetaria": num(round(sal["monetaria"])),
        "finSalidaEquipo": num(round(sal["venta_equipo"])),
        "finKTanioA": num(round(res["deficit_anual"][2027])),
        "finKTanioB": num(round(res["deficit_anual"][2028])),
        "finKTanioC": num(round(res["deficit_anual"][2029])),
        "finMesPE": (lambda t: "--" if t is None else
                     meses_txt[(t - 1) % 12] + f" de {2027 + (t - 1) // 12}")(mes_equilibrio(res)),
        "finCajaMin": num(round(caja_min)),
        "finQuebrantoA": num(max(0, -er_disp["rai"][0])),
        "finKTMitad": num(res["kt"] / 2),
        "finUsoAnualMin": pct(min(uso_anual), 0).replace("\\,\\%", ""),
        "finUsoAnualMax": pct(max(uso_anual), 0),
        "finReduccionCont": pct(1 - cont[1]["van"] / p1[1]["van"], 0) if p1[1]["van"] < 0 else "--",
        "finValorHora": num(p["valor_hora_autor"]),
        "finValorHoraRevisor": num(p["valor_hora_revisor"]),
        "finTipoCambio": num(p["tipo_cambio"]),
        "finAportesMes": num(p["aportes_autonomo_mes"], 1),
        "finCuotaMonoB": num(p["monotributo"][1][1] / p["tipo_cambio"], 1),
    }
    contenido = "".join(f"\\newcommand{{\\{k}}}{{{v}}}\n" for k, v in macros.items())
    escribir("macros.tex", contenido)

    # Resumen por consola
    print(f"Tasa de corte real: {res['tasa']['real']:.3f} (nominal {res['tasa']['nominal']:.3f})")
    print(f"Inversion total: {inv_total:.0f}  (AF {res['inv']['af']:.0f}, AD {res['inv']['ad']:.0f}, KT {res['kt']:.0f})")
    print(f"Deficit maximo {res['deficit_max']:.0f} en el mes {m_def}")
    print("Flujo:", ind["ff"], " acumulado:", ff_acum)
    for clave, (rr, ii) in resultados.items():
        print(f"{clave:18s} VAN {ii['van']:8.0f}  TIR {ii['tir'] if ii['tir'] is None else round(ii['tir'],3)}"
              f"  repago {ii['repago']}  KT {rr['kt']:.0f}  ventas {[round(rr['er'][a]['ventas']) for a in ANIOS]}"
              f"  FF {ii['ff']}")
    for a in ANIOS:
        e = equilibrio(res, a)
        print(a, {k: round(v, 2) for k, v in e.items()})
    print("Umbrales:", {k: v for k, v in sens.items() if k != "filas"})
    print("Uso maximo de capacidad P4:", round(uso_base, 2))
    print("Mes de equilibrio (12 meses moviles):", mes_equilibrio(res))
    print("Deficit intra-anual base:", {a: round(v) for a, v in res["deficit_anual"].items()})
    print("Salida P2 fin 2027:", {k: round(v) for k, v in sal.items()})


if __name__ == "__main__":
    main()
