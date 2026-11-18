# Registro de revisión del prototipo con usuarios

**Referencia:** versión 1.12 del documento, Sección 10.6: bosquejos P-01 a P-05 y tabla «Cambios que salieron del uso real».

**Fuente:** relato de Valentín Torassa Colombero del 17/11/2026 e historial público de `blackice` (versiones, *pull requests* y `CHANGELOG.md`). No hay minutas ni devoluciones escritas de quienes lo usaron.

## Qué se revisó

`blackice` no tiene ventanas: su interfaz es la terminal, el menú de la barra y el cuadro de Touch ID. La revisión no fue sobre una maqueta. Fue de uso: otras personas usaron las versiones publicadas.

## Quiénes lo usaron

| Quién | Relación con el proyecto |
|---|---|
| Esteban Suárez | Coautor de `blackice`. |
| Gente de la comunidad | Usuarios de la herramienta. |
| Compañeros o conocidos del autor | Usuarios de la herramienta. |

Según el autor, a quienes lo usaron les gustó. De ese uso salieron cuatro cambios de la interfaz.

## Cambios que salieron de ese uso

| N.º | Lo que se observó | Cambio | Versión | PR | Fecha | Bosquejo |
|---|---|---|---|---|---|---|
| 1 | Para iniciar por primera vez había que escribir antes el archivo de configuración. | El primer `blackice start` hace preguntas y escribe el archivo. | 0.2.0 | #23 | 03/11/2026 | P-01 |
| 2 | Durante el arranque no se veía en qué parte se estaba. | El primer arranque va en pasos numerados y dice qué hacer en cada uno. | 0.2.1 | #24 | 03/11/2026 | P-01 |
| 3 | El menú tenía más opciones que las que se usaban. | Menú más chico: las decisiones recientes ocupan una línea y se quitan cuatro opciones (abrir la configuración, ver el registro, documentación y abrir al inicio). | 0.4.2 | #53 | 05/11/2026 | P-03 |
| 4 | Si no se elegían a mano, el VPN y las aplicaciones de todos los días quedaban esperando respuesta. | En el primer arranque, el VPN y las aplicaciones de uso común ya vienen tildados. | 1.0.0 | #70 | 06/11/2026 | P-01 |

Los cuatro cambios se pueden comprobar en https://github.com/ValentinTorassa/blackice: cada uno tiene su *pull request* y figura en `CHANGELOG.md` en la versión indicada. La fecha es la de integración del *pull request*. En el cambio 3, el `CHANGELOG.md` de la versión 0.4.2 deja escrito que lo pidió un *tester* («asked for by the same tester»).

## Límites

- No se registró cuántas personas lo usaron, ni las fechas de cada uso, ni tiempos.
- Las devoluciones fueron informales. Este registro las toma del relato del autor.
- Lo que sí es público y verificable es el cambio que siguió a cada observación.
- Las corridas de la carpeta `evidence/` del repositorio las hicieron quienes desarrollan `blackice`: no son pruebas independientes.
