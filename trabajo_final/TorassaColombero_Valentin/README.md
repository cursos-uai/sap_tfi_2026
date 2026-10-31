# Trabajo Final — Torassa Colombero, Valentín

- **Alumno:** Valentín Torassa Colombero
- **Comisión:** T1-23-47 — Seminario de Trabajo Final de Ingeniería
- **Carrera:** Ingeniería en Sistemas Informáticos — Facultad de Tecnología Informática, UAI Rosario
- **Dirección:** María Eugenia Casco y Santiago Enrique Roatta
- **Versión:** 4 (Tercera Entrega, 2.º cuatrimestre 2026). Actualiza la versión 3 (PR #16).

## De qué se trata el trabajo

Línea de investigación aplicada en Ingeniería de Software sobre Go, software libre
y Podman. El componente de negocio se desarrolla como **vinculación tecnológica**
—transferencia mediante guías, laboratorios reproducibles, talleres y diagnósticos—
y no como un emprendimiento.

## Contenido de esta entrega

| Archivo | Descripción |
|---|---|
| Torassa_Valentin_E3-2C_v1.pdf | Plan de Desarrollo Tecnológico completo, puntos 1 a 11, 80 páginas (versión 1.8 del documento). |
| seguimiento-checklist.md | Informe de seguimiento: ubicación de los puntos 7, 8 y 9 y de la checklist tecnológica. |
| registro-revision-prototipo.md | Registro anónimo de las tres pruebas individuales del prototipo (Sección 10.9), sin cambios desde la versión 3. |
| modelo/modelo_financiero.py | Modelo mensual reproducible del punto 8. Genera las tablas y las cifras que cita el texto. |

## Qué incorpora la versión 4

- **Punto 8, Plan Financiero-Económico (8.1 a 8.12).** Evalúa el frente de
  servicios de transferencia (P4) entre 2027 y 2029, en dólares constantes de
  octubre de 2026. La investigación, las contribuciones y la difusión quedan
  fuera del flujo de fondos.
- **Punto 9, Factibilidades (9.1 a 9.4):** técnica, comercial, administrativa y
  legal, cada una apoyada en evidencia del documento.
- Los puntos 1 a 7, 10 y 11 de la versión 3 se conservan. Se ajustaron las
  remisiones al punto 8 en el resumen ejecutivo, 5.2, 6.2, 6.5, 7.6 y 10.1.

| Indicador (escenario base) | Valor |
|---|---|
| Inversión inicial | USD 2.952 |
| Tasa de corte | 18,5 % real |
| VAN | USD 1.938 |
| TIR | 45,5 % |
| Período de repago | 1,9 años (2,2 descontado) |

El punto 8.10 plantea un escenario optimista y dos pesimistas, como pide la guía.
Todos los importes son supuestos de evaluación y están declarados en cada apartado.

## Modelo financiero

Usa sólo la biblioteca estándar de Python. Desde esta carpeta:

```sh
python3 modelo/modelo_financiero.py
```

Escribe en `generado/` las tablas LaTeX y las macros con las cifras del punto 8.
Se detiene si algún escenario supera el tope de horas del autor de la Tabla 22.

## Estado de los hitos

| Hito | Alcance | Estado |
|---|---|---|
| RRR | Requerimientos, casos de uso y prototipo | Revisado y aprobado |
| PDR | Robustez y modelo de dominio | Revisado y aprobado |
| CDR | Secuencia, clases, patrones y testing | Revisado y aprobado |

## Seguimiento posterior a esta entrega

- O4 del Plan de Marketing: validación con cohortes en cátedra y equipo técnico,
  con devolución escrita de participantes.
- Encuadre fiscal de los servicios (régimen general o monotributo), alícuotas de
  Ingresos Brutos y DReI: a confirmar con un contador antes del primer servicio pago.
