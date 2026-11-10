# Trabajo Final — Torassa Colombero, Valentín

- **Alumno:** Valentín Torassa Colombero
- **Comisión:** T1-23-47 — Seminario de Trabajo Final de Ingeniería
- **Carrera:** Ingeniería en Sistemas Informáticos — Facultad de Tecnología Informática, UAI Rosario
- **Dirección:** María Eugenia Casco y Santiago Enrique Roatta
- **Versión:** 5 (Tercera Entrega, 2.º cuatrimestre 2026). Actualiza la versión 4 (PR #17).

## De qué se trata el trabajo

Línea de investigación aplicada en Ingeniería de Software sobre Go, software libre
y Podman. El componente de negocio se desarrolla como **vinculación tecnológica**
—transferencia mediante guías, laboratorios reproducibles, talleres y diagnósticos—
y no como un emprendimiento.

## Contenido de esta entrega

| Archivo | Descripción |
|---|---|
| Torassa_Valentin_E3-2C_v2.pdf | Plan de Desarrollo Tecnológico completo, puntos 1 a 11, 86 páginas (versión 1.9 del documento). |
| seguimiento-checklist.md | Informe de seguimiento: ubicación de los puntos 7, 8 y 9, de la checklist tecnológica y de los enlaces de la solución, con la numeración de la versión 1.9. |
| registro-revision-prototipo.md | Registro anónimo de las tres pruebas individuales del prototipo (Sección 10.9), sin cambios desde la versión 3. |
| modelo/modelo_financiero.py | Modelo mensual reproducible del punto 8, sin cambios desde la versión 4. Genera las tablas y las cifras que cita el texto. |

## Dónde está la solución tecnológica

La Sección 10.1 del documento (pág. 55) reúne los enlaces:

| Qué | Enlace |
|---|---|
| Sitio en producción (Open Security Labs) | https://securitylabs.valentorassa.com |
| Repositorio del sitio y los laboratorios | https://github.com/ValentinTorassa/Open-Security-Labs |
| Repositorio de parches y debdiffs | https://github.com/ValentinTorassa/VT-Security-Fixes |
| Contribución a Podman | https://github.com/containers/podman/pull/28637 |
| Contribuciones a Debian | https://bugs.debian.org/1152837 y https://bugs.debian.org/1153126 |

## Qué incorpora la versión 5

- **Enlaces y repositorios en la documentación (10.1).** La carátula del punto 10
  lista el sitio publicado, los repositorios, las contribuciones *upstream* y
  esta carpeta de entrega.
- **Contribuciones de seguridad a Debian (5.3.3, pág. 24, y Anexo 11.4, págs. 82 a 85).**
  En `gdcm`, el reporte de una regresión con su parche (bug #1152837) y el pedido
  de actualización de Debian 13 por seis CVE (bug #1153126), aceptado por el
  equipo Debian Med y en revisión. En `invesalius` y `pydicom`, dos
  actualizaciones preparadas y probadas que todavía no se presentaron. Ninguna
  está aún en el archivo de Debian; el documento las presenta como
  contribuciones en revisión.
- **Estado del PR de Podman.** El PR #28637 figura como mergeado el 23-06-2026
  también en el alcance (10.4.3) y en la bibliografía.
- **Historial de revisión (10.3)** completado con las versiones 1.5 a 1.9.
- **Corrección tipográfica.** Las opciones de línea de comandos (`--retry`,
  `--user`) se imprimían con una raya en lugar de dos guiones.
- Los puntos 7, 8 y 9 no cambian de contenido. Cambia su ubicación: tres páginas
  más adelante, y las tablas posteriores a la 9 suman uno. `seguimiento-checklist.md`
  ya usa la numeración nueva.

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
Se detiene si algún escenario supera el tope de horas del autor de la Tabla 23.

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
- Debian: seguir los bugs #1152837 y #1153126 hasta que la actualización de `gdcm`
  entre en la versión estable, y presentar las de `invesalius` y `pydicom`.
