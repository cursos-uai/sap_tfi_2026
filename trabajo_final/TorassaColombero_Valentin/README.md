# Trabajo Final — Torassa Colombero, Valentín

- **Alumno:** Valentín Torassa Colombero
- **Comisión:** T1-23-47 — Seminario de Trabajo Final de Ingeniería
- **Carrera:** Ingeniería en Sistemas Informáticos — Facultad de Tecnología Informática, UAI Rosario
- **Dirección:** María Eugenia Casco y Santiago Enrique Roatta
- **Versión:** 8 (Tercera Entrega, 2.º cuatrimestre 2026). Actualiza la versión 7 (PR #20).

## De qué se trata el trabajo

Línea de investigación aplicada en Ingeniería de Software sobre Go, software libre
y Podman. El componente de negocio se desarrolla como **vinculación tecnológica**
—transferencia mediante guías, laboratorios reproducibles, talleres y diagnósticos—
y no como un emprendimiento.

La solución tecnológica es **`blackice`**, el software propio de la línea: un cortafuegos
de aplicaciones para macOS, publicado como software libre. El punto 10 del documento lo
especifica con ICONIX.

## Contenido de esta entrega

| Archivo | Descripción |
|---|---|
| [Torassa_Valentin_E3-2C_v5.pdf](Torassa_Valentin_E3-2C_v5.pdf) | Plan de Desarrollo Tecnológico completo, puntos 1 a 11, 102 páginas (versión 1.12 del documento). |
| [seguimiento-checklist.md](seguimiento-checklist.md) | Informe de seguimiento: ubicación de los puntos 7, 8 y 9, de los 59 criterios de la checklist tecnológica y de los enlaces de la solución, con la numeración de la versión 1.12. |
| [registro-revision-prototipo.md](registro-revision-prototipo.md) | Quiénes usaron `blackice` y qué cambios de la interfaz salieron de ese uso (Sección 10.6). Reemplaza al registro del prototipo anterior. |
| [evidencia/cobertura-hookanswer-2026-11-17.txt](evidencia/cobertura-hookanswer-2026-11-17.txt) | Salida de la medición de cobertura de la prueba estructural (Sección 10.11.2). |
| [modelo/modelo_financiero.py](modelo/modelo_financiero.py) | Modelo mensual reproducible del punto 8, sin cambios desde la versión 4. Genera las tablas y las cifras que cita el texto. |

## Dónde está la solución tecnológica

El punto 10 del documento (págs. 58 a 91) especifica `blackice`. La Sección 10.1 (pág. 58)
reúne sus datos:

| Qué | Dónde |
|---|---|
| Repositorio | https://github.com/ValentinTorassa/blackice |
| Sitio y documentación | https://blackice-macos.vercel.app |
| Versión especificada | 1.1.1, del 16 de noviembre de 2026 (*commit* `d94ef85`) |

Los demás enlaces de la línea están en el punto 5.3 y en los Anexos 11.3 a 11.5:

| Qué | Enlace |
|---|---|
| Sitio en producción (Open Security Labs) | https://securitylabs.valentorassa.com |
| Repositorio del sitio y los laboratorios | https://github.com/ValentinTorassa/Open-Security-Labs |
| Repositorio de parches y debdiffs | https://github.com/ValentinTorassa/VT-Security-Fixes |
| Contribución a Podman | https://github.com/containers/podman/pull/28637 |
| Contribuciones a Debian | https://bugs.debian.org/1152837 y https://bugs.debian.org/1153126 |
| Aportes a Vercel Labs, sin integrar | https://github.com/vercel-labs/deepsec/pull/137 y https://github.com/vercel-labs/fx/pull/1659 |

## Qué incorpora la versión 8

- **El punto 10 se escribe de nuevo (págs. 58 a 91).** Especifica `blackice` 1.1.1 con
  ICONIX completo: requerimientos clasificados (de usuario, funcionales, no funcionales y
  de entorno), arquitectura con su tipo, estilo y patrón, cuatro casos de uso centrales con
  cinco casos incluidos y seis extensiones, modelo de dominio, bosquejos del prototipo,
  robustez, secuencia, clases de diseño, patrones, pruebas con cobertura medida,
  trazabilidad e hitos.
- **Un diagrama por caso de uso central** en robustez, secuencia y clases. No se incluyen
  diagramas de paquetes, de componentes, de despliegue ni entidad-relación, por criterio de
  la cátedra en clase.
- **Sale la especificación anterior del punto 10**, la del marco de contribución y el kit
  de laboratorios. El marco y los laboratorios siguen descriptos en los puntos 5 a 7.
- **Debian (Sección 5.3.3 y Anexo 11.4), al 17 de noviembre.** El equipo Debian Med integró
  en sus repositorios los cuatro pedidos de integración presentados (`invesalius`, `pydicom`
  y dos de `gdcm`). La corrección de `invesalius` ya está en *unstable*. Ninguna
  actualización llegó todavía a una versión estable.
- **`blackice` (Sección 5.3.5 y Anexo 11.5), al 17 de noviembre.** 25 versiones en 14 días,
  662 pruebas automáticas en 77 *suites* y 29 corridas registradas.
- **Vercel (Sección 5.3.6).** El documento dice que `blackice` se desarrolló con Vercel y
  se va a integrar a su equipo de desarrollo. Mantiene tres aclaraciones: ningún aporte de
  código a repositorios de Vercel está integrado, los cupones de v0 se sortearon y no son
  un ingreso, y el punto 8 no cuenta financiamiento de Vercel.
- **Ficha de seguimiento e hitos (Sección 10.13).** Fila de la versión 1.12 y revisión de
  la dirección del 17 de noviembre sobre los hitos RRR, PDR y CDR.
- El punto 9.1 cita la especificación nueva. Los puntos 7 y 8 y el modelo financiero no
  cambian. Las tablas y las figuras de los puntos 1 a 9 conservan su número.
  `seguimiento-checklist.md` usa la numeración nueva. El documento pasa de 94 a 102 páginas.

Las corridas registradas de `blackice` son de una sola Mac y las hicieron sus autores:
ninguna es una prueba independiente. Las devoluciones de quienes lo usaron fueron
informales y no hay minutas; `registro-revision-prototipo.md` dice qué se puede comprobar
en público.

## Versiones anteriores

| Versión | PR | Qué incorporó |
|---|---|---|
| 7 | [#20](https://github.com/cursos-uai/sap_tfi_2026/pull/20) | `blackice` (Sección 5.3.5), la colaboración con Vercel (Sección 5.3.6) y su evidencia (Anexo 11.5). |
| 6 | [#19](https://github.com/cursos-uai/sap_tfi_2026/pull/19) | Estado de los aportes a Debian después de presentar `invesalius` y `pydicom`. |
| 5 | [#18](https://github.com/cursos-uai/sap_tfi_2026/pull/18) | Enlaces y repositorios de la solución (Sección 10.1) y contribuciones de seguridad a Debian (Sección 5.3.3 y Anexo 11.4). |
| 4 | [#17](https://github.com/cursos-uai/sap_tfi_2026/pull/17) | Puntos 8 (plan financiero-económico) y 9 (factibilidades). |

## Indicadores del punto 8 (escenario base)

| Indicador | Valor |
|---|---|
| Inversión inicial | USD 2.952 |
| Tasa de corte | 18,5 % real |
| VAN | USD 1.938 |
| TIR | 45,5 % |
| Período de repago | 1,9 años (2,2 descontado) |

El punto 8.10 plantea un escenario optimista y dos pesimistas, como pide la guía.
Todos los importes son supuestos de evaluación y están declarados en cada apartado.
El punto 8 no cambia en esta versión.

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
| RRR | Requerimientos, casos de uso, modelo de dominio y bosquejos | Revisado por la dirección el 17/11/2026 |
| PDR | Arquitectura y robustez | Revisado por la dirección el 17/11/2026 |
| CDR | Secuencia, clases, patrones y pruebas | Revisado por la dirección el 17/11/2026 |

Las tres revisiones se hicieron sobre `blackice` (Sección 10.13 del documento).

## Seguimiento posterior a esta entrega

- O4 del Plan de Marketing: validación con cohortes en cátedra y equipo técnico,
  con devolución escrita de participantes.
- Encuadre fiscal de los servicios (régimen general o monotributo), alícuotas de
  Ingresos Brutos y DReI: a confirmar con un contador antes del primer servicio pago.
- Debian: seguir los bugs abiertos (#1152837, #1153126 y #1148120) hasta que la primera
  actualización de la versión estable sea aceptada. Es el hito pendiente del programa P2.
- `blackice`: probarlo en otras Macs, con macOS 14 y 15, y con corridas de otras personas.
- Vercel Labs: seguir el PR #137 de `deepsec` y el PR #1747 de `fx`.
