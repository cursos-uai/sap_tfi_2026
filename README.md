# SAP-TFI-2026

Ingeniería inversa ICONIX de los módulos nativos de Odoo (Ventas, Facturación, Entregas, Inventario).

## Estado

- **Versión:** 0.1.0 (primera iteración)
- **Odoo analizado:** 19.0 Community
- **Estado:** en revisión (primera iteración completada)

## Estructura del repo

```
sap_tfi_2026/
├── README.md
├── docs/
│   ├── 00_plan/                  # plan del proyecto
│   ├── 01_contexto/              # contexto y stack
│   ├── 02_casos_uso/             # 7 especificaciones de CU
│   ├── 03_dominio/               # modelo de dominio conceptual
│   ├── 04_arquitectura/          # C4 general
│   ├── 05_prototipos/            # prototipo del form de presupuesto
│   ├── 06_robustez/              # (próxima iteración)
│   ├── 07_secuencia/             # (próxima iteración)
│   ├── 08_clases/                # (próxima iteración)
│   ├── 09_trazabilidad/           # matriz de trazabilidad
│   ├── 10_material_estudio/      # (próxima iteración)
│   └── 11_validacion/            # (próxima iteración)
├── diagrams/
│   ├── plantuml/                 # 4 archivos .puml
│   └── pdf/                      # (se compilará cuando se instale PlantUML)
└── evidence/                     # (próxima iteración)
```

## Artefactos de la primera iteración

### Documentación (`docs/`)

- ✅ `docs/00_plan/README.md` — plan del proyecto
- ✅ `docs/01_contexto/README.md` — contexto de Odoo 19.0
- ✅ `docs/02_casos_uso/cu_ven_001_crear_presupuesto.md`
- ✅ `docs/02_casos_uso/cu_ven_004_confirmar_pedido.md`
- ✅ `docs/02_casos_uso/cu_ent_002_reservar_productos.md`
- ✅ `docs/02_casos_uso/cu_ent_004_validar_entrega.md`
- ✅ `docs/02_casos_uso/cu_fac_001_crear_factura.md`
- ✅ `docs/02_casos_uso/cu_fac_002_publicar_factura.md`
- ✅ `docs/02_casos_uso/cu_fac_003_registrar_pago.md`
- ✅ `docs/03_dominio/modelo_dominio_inicial.md`
- ✅ `docs/04_arquitectura/arquitectura_general.md`
- ✅ `docs/05_prototipos/prototipo_formulario_presupuesto.md`
- ✅ `docs/09_trazabilidad/matriz_trazabilidad.md`

### Diagramas (`diagrams/plantuml/`)

- ✅ `d_cu_gen_001_casos_uso_principales.puml` — diagrama general de CU
- ✅ `d_cla_con_gen_001_modelo_dominio.puml` — modelo de dominio conceptual
- ✅ `d_rob_ven_004_confirmar_pedido.puml` — robustez de CU-VEN-004
- ✅ `d_sec_ven_004_confirmar_pedido.puml` — secuencia de CU-VEN-004
- ✅ `d_cla_int_001_integracion_ven_stock_cont.puml` — clases de integración

### Evidencias generadas

- **20 EV-COD** (código fuente verificado)
- **22 EV-INF** (inferencias pendientes de validar)

## Cómo verificar los diagramas

```bash
# Instalar PlantUML + Java (si no está)
sudo apt-get install -y plantuml default-jre

# Validar todos los .puml
plantuml -checkonly diagrams/plantuml/**/*.puml

# Generar PDFs
plantuml -tpdf diagrams/plantuml/**/*.puml
# Resultado en diagrams/pdf/
```

## Cómo regenerar la matriz

Ver `docs/09_trazabilidad/matriz_trazabilidad.md`.

## Cómo continuar

Próximas iteraciones deberían:
1. Validar las 22 EV-INF en iteraciones siguientes.
2. Generar diagramas de robustez y secuencia para los CU restantes.
3. Generar diagramas de clases conceptuales y técnicas para cada CU.
4. Agregar material educativo (sección `10_material_estudio/`).
5. Validar todos los diagramas con PlantUML.

## Reglas del proyecto

- **No inventar** información sobre Odoo. Marcar como `EV-INF` lo que sea inferencia.
- **No incluir** credenciales ni secretos.
- **No modificar** código nativo de Odoo.
- **Trazabilidad** obligatoria entre artefactos.
- **Convención de naming**: `CU-{AREA}-{NNN}`, `RN-{AREA}-{NNN}`, `D-{TYPE}-{AREA}-{NNN}`.

## Contacto

- **Operador:** Ale Sartorio (alejandro.sartorio@gmail.com)
- **Repo:** https://github.com/cursos-uai/sap_tfi_2026
- **Issues:** https://github.com/cursos-uai/sap_tfi_2026/issues