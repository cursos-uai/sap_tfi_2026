# Trabajo Final — Torassa Colombero, Valentín

- **Alumno:** Valentín Torassa Colombero
- **Comisión:** T1-23-47 — Seminario de Trabajo Final de Ingeniería
- **Carrera:** Ingeniería en Sistemas Informáticos — Facultad de Tecnología Informática, UAI Rosario
- **Dirección:** María Eugenia Casco y Santiago Enrique Roatta
- **Versión:** 7 (Tercera Entrega, 2.º cuatrimestre 2026). Actualiza la versión 6 (PR #19).

## De qué se trata el trabajo

Línea de investigación aplicada en Ingeniería de Software sobre Go, software libre
y Podman. El componente de negocio se desarrolla como **vinculación tecnológica**
—transferencia mediante guías, laboratorios reproducibles, talleres y diagnósticos—
y no como un emprendimiento.

## Contenido de esta entrega

| Archivo | Descripción |
|---|---|
| Torassa_Valentin_E3-2C_v4.pdf | Plan de Desarrollo Tecnológico completo, puntos 1 a 11, 94 páginas (versión 1.11 del documento). |
| seguimiento-checklist.md | Informe de seguimiento: ubicación de los puntos 7, 8 y 9, de la checklist tecnológica y de los enlaces de la solución, con la numeración de la versión 1.11. |
| registro-revision-prototipo.md | Registro anónimo de las tres pruebas individuales del prototipo (Sección 10.9), sin cambios desde la versión 3. |
| modelo/modelo_financiero.py | Modelo mensual reproducible del punto 8, sin cambios desde la versión 4. Genera las tablas y las cifras que cita el texto. |

## Dónde está la solución tecnológica

La Sección 10.1 del documento (pág. 58) reúne los enlaces:

| Qué | Enlace |
|---|---|
| Sitio en producción (Open Security Labs) | https://securitylabs.valentorassa.com |
| Repositorio del sitio y los laboratorios | https://github.com/ValentinTorassa/Open-Security-Labs |
| Repositorio de parches y debdiffs | https://github.com/ValentinTorassa/VT-Security-Fixes |
| Contribución a Podman | https://github.com/containers/podman/pull/28637 |
| Contribuciones a Debian | https://bugs.debian.org/1152837 y https://bugs.debian.org/1153126 |
| Herramienta propia (`blackice`) | https://github.com/ValentinTorassa/blackice |
| Aportes a Vercel Labs, sin integrar | https://github.com/vercel-labs/deepsec/pull/137 y https://github.com/vercel-labs/fx/pull/1659 |

## Qué incorpora la versión 7

- **`blackice` (Sección 5.3.5, págs. 26 y 27, y Anexo 11.5, pág. 90).** Cortafuegos de
  aplicaciones para macOS, publicado como software libre (Apache 2.0) con Esteban Suárez.
  Retiene cada conexión saliente que ninguna regla cubre hasta que una persona o un agente
  de programación la aprueba o la niega. 21 versiones entre el 3 y el 10 de noviembre,
  554 pruebas automáticas y 25 corridas registradas en una Mac real.
- **Colaboración con Vercel (Sección 5.3.6, págs. 27 y 28, y Anexo 11.5, págs. 91 y 92).**
  Dos aportes de código a proyectos abiertos de Vercel Labs, `deepsec` (PR #137) y `fx`
  (PR #1659, que su mantenedor retomó en el PR #1747), y el sorteo de cinco cupones de v0
  en la comunidad. No hay convenio ni patrocinio.
- La carátula y la Figura 1 (pág. 9) suman el ícono de `blackice` y el logo de Vercel.
- El historial de revisión suma la fila de la versión 1.11.
- Los puntos 7, 8 y 9 no cambian de contenido; quedan tres páginas más adelante. Las tablas
  conservan su número. `seguimiento-checklist.md` usa la numeración nueva. El documento pasa
  de 87 a 94 páginas.

Ninguno de los dos aportes a Vercel Labs está integrado: el documento los presenta como
contribuciones en revisión, igual que las de Debian. `blackice` corrió en una sola Mac y
sus corridas las hicieron sus autores.

## Qué incorporó la versión 6

- **Estado de los aportes a Debian (Tabla 9, pág. 24, y Anexo 11.4, págs. 84 y 85).**
  El 10 de noviembre se enviaron el parche de `invesalius` con los resultados de
  las pruebas al bug [#1136204](https://bugs.debian.org/1136204) y el debdiff de
  `pydicom` a la lista del equipo Debian Med. El documento deja de darlos como
  «sin presentar». Siguen sin estar en el archivo de Debian.
- **Historial de revisión (pág. 3)** con la fila de la versión 1.10.
- La numeración de secciones, tablas y páginas es la de la versión 1.9: el índice
  no cambia y `seguimiento-checklist.md` conserva sus referencias. El documento
  pasa de 86 a 87 páginas porque la bibliografía termina una página después.

## Qué incorporó la versión 5

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
  entre en la versión estable; seguir el bug #1136204 de `invesalius` y la respuesta
  del equipo sobre `pydicom`, y pedir después sus actualizaciones para Debian 13.
- `blackice`: probarlo en otras Macs, con macOS 14 y 15, y con corridas de otras personas.
- Vercel Labs: seguir el PR #137 de `deepsec` y el PR #1747 de `fx`.
