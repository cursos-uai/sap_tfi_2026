# Informe de seguimiento del Trabajo Práctico

- **Alumno/a o equipo:** Valentín Torassa Colombero
- **Comisión:** T1-23-47 — Seminario de Trabajo Final de Ingeniería
- **Documento de esta entrega:** [Torassa_Valentin_E2-2C_v2.pdf](Torassa_Valentin_E2-2C_v2.pdf)
- **Fecha de generación:** 14/10/2026
- **Avance referenciado:** 58/59 criterios de la checklist tecnológica documentados; la revisión del prototipo con usuarios sigue pendiente. Punto 7 verificado aparte.


## Punto 7 — Operaciones (guía del Plan de Desarrollo Tecnológico)

| Apartado | Ubicación en el documento | Evidencia |
|---|---|---|
| 7.1 Organización | Sección 7.1, pág. 28 | Articulación de I+D, tres frentes P1–P4 y condición para contratar. |
| 7.2 Grupo promotor y dirección | Sección 7.2, pág. 29; Tabla 20 | Personas identificadas; no se presume directorio ni accionistas. |
| 7.3 Staff y perfiles | Sección 7.3, págs. 29-30; Tabla 21 | Funciones, cobertura inicial, perfiles faltantes y programas P1–P5. |
| 7.4 Estructura y evolución | Sección 7.4, págs. 30-31; Figura 6 | Tres etapas alineadas con el cronograma y el límite de P4. |
| 7.5 Filosofía y sistema | Sección 7.5, pág. 31 | Flujo de contribución y transferencia con revisión y mantenimiento. |
| 7.6 RRHH por etapa | Sección 7.6, págs. 31-32; Tabla 22 | Horas del autor confirmadas (16/10/2026); horas externas condicionales. |

Las horas del autor en 7.6 fueron confirmadas el 16/10/2026; las externas dependen de un acuerdo previo.

## Requerimientos

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Funcionales identificados, numerados y sin decisiones de implementación | Sección | Sección 10.4.2 — requerimientos funcionales RF-01 a RF-05 (pág. 33) |
| ✅ Cumple | No funcionales clasificados | Sección | Sección 10.4.2 — requerimientos no funcionales RNF-01 a RNF-06 (pág. 33) |
| ✅ Cumple | Alcance, actores y glosario acordados | Sección | Secciones 10.4.3 (alcance) y 10.4.4 (definiciones y acrónimos), pág. 33 |
| ✅ Cumple | Cada requisito se vincula con casos de uso | Tabla | Tabla 24, Sección 10.6.2 — matriz de trazabilidad REQ → CU (pág. 45) |
| ✅ Cumple | Al menos un criterio de aceptación por requisito | Tabla | Tabla 23, Sección 10.6.1 — criterios de aceptación por RF (pág. 45) |

## Casos de uso y especificaciones

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Diagrama general con actores, casos y límite del sistema | Figura o diagrama | Figura 20, Sección 10.7 — diagrama general con límite del sistema y actores (pág. 46) |
| ✅ Cumple | include y extend usados con sentido | Sección | Sección 10.5.3 — relaciones include y extend entre CU-001 a CU-006 (págs. 35-40) |
| ✅ Cumple | Una especificación por caso relevante | Sección | Sección 10.5.3 — una ficha por caso, CU-001 a CU-006 (págs. 35-40) |
| ✅ Cumple | Curso básico escrito en voz activa | Sección | Sección 10.8 — curso básico en voz activa de CU-001-001 a CU-001-006 (págs. 46-48) |
| ✅ Cumple | Alternativos, excepciones y reglas documentados | Sección | Sección 10.8 — alternativos, excepciones E1/E2 y reglas por caso (págs. 46-48) |
| ✅ Cumple | Hito RRR revisado con interesados | Sección | Sección 10.15, Tabla 32 — hito RRR revisado y aprobado por la dirección |

## Modelo de dominio

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Clases tomadas del lenguaje del negocio | Figura o diagrama | Sección 10.5.7 — diagrama de clases / modelo de dominio de Podman (pág. 43) |
| ✅ Cumple | Atributos conceptuales relevantes | Figura o diagrama | Sección 10.5.7 — atributos conceptuales del modelo de dominio (pág. 43) |
| ✅ Cumple | Relaciones y multiplicidades justificadas | Figura o diagrama | Figura 35, Sección 10.12 — multiplicidades 1–7 y 1..* justificadas (pág. 53) |
| ✅ Cumple | Nombres sin sinónimos ni ambigüedades | Sección | Secciones 10.4.4 y 10.12 — vocabulario único entre dominio, robustez y clases |
| ✅ Cumple | Modelo actualizado después de robustez | Sección | Sección 10.10, párrafo de consistencia — el dominio se actualizó tras robustez (pág. 50) |

## Prototipo

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Pantallas y estados relevantes representados | Figura o diagrama | Figura 21, Sección 10.9 — pantallas P-01 a P-04 (pág. 48) |
| ✅ Cumple | Cada pantalla se vincula con casos y actores | Tabla | Tabla 25, Sección 10.9 — pantalla ↔ caso de uso ↔ actor (pág. 48) |
| ✅ Cumple | Controles y datos coinciden con las especificaciones | Tabla | Tabla 25, Sección 10.9 — datos y controles derivados de los cursos básicos (pág. 48) |
| 🟡 Pendiente | Prototipo revisado con usuarios | Párrafo | Sección 10.9, cierre — revisión prevista en el objetivo O4 del Plan de Marketing; falta evidencia de la sesión con usuarios. |
| ✅ Cumple | Se usa como especificación, no como producto final | Párrafo | Sección 10.9, apertura — declarado como especificación de interacción, no producto final |

## Arquitectura

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Vistas funcional, de datos y del sistema separadas | Sección | Secciones 10.5.5 paquetes, 10.5.6 componentes, 10.5.8 entidad-relación y 10.5.9 despliegue (págs. 41-44) |
| ✅ Cumple | Componentes, capas, responsabilidades e interfaces visibles | Figura o diagrama | Sección 10.5.6 — diagrama de componentes e interfaces (pág. 42) |
| ✅ Cumple | Despliegue, nodos y tecnologías documentados | Figura o diagrama | Sección 10.5.9 — diagrama de despliegue, nodos y tecnologías (pág. 44) |
| ✅ Cumple | Decisiones justificadas por requerimientos | Sección | Sección 10.12 — interfaz RepositorioUpstream justificada por RF-01 y RF-04 (pág. 53) |
| ✅ Cumple | Calidad y testing considerados | Sección | Sección 10.5.10 (casos de prueba) y Sección 11.1 (normas de calidad), págs. 44-45 |

## Diagramas de robustez

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Un diagrama por caso de uso diseñado | Figura o diagrama | Figuras 23 a 28, Sección 10.10 — un diagrama por cada caso de uso (págs. 49-50) |
| ✅ Cumple | Actor, Boundary, Control y Entity diferenciados | Figura o diagrama | Figura 22, Sección 10.10 — notación con Actor, Boundary, Control y Entity (pág. 49) |
| ✅ Cumple | Reglas de comunicación respetadas | Sección | Sección 10.10, encabezado — reglas de comunicación declaradas y respetadas (pág. 49) |
| ✅ Cumple | Una frontera clara por pantalla o interfaz | Párrafo | Sección 10.10, cierre — una frontera por interfaz, según Tabla 25 (pág. 50) |
| ✅ Cumple | Entidades consistentes con el dominio | Párrafo | Sección 10.10, cierre — entidades coinciden con el modelo de dominio 10.5.7 (pág. 50) |
| ✅ Cumple | Controles cubren cursos básicos y alternativos | Párrafo | Sección 10.10, cierre — un control para curso básico y otro para alternativos (pág. 50) |
| ✅ Cumple | Hito PDR aprobado | Sección | Sección 10.15, Tabla 32 — hito PDR aprobado por la dirección |

## Diagramas de secuencia

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Un diagrama por caso de uso | Figura o diagrama | Figuras 29 a 34, Sección 10.11 — un diagrama por caso de uso (págs. 51-52) |
| ✅ Cumple | Participantes derivados de robustez | Sección | Sección 10.11 — participantes derivados de los controles y entidades de robustez |
| ✅ Cumple | Texto del caso mapeado a mensajes | Sección | Sección 10.11 — cada mensaje corresponde a una oración del curso básico |
| ✅ Cumple | Controles asignados a operaciones u objetos | Figura o diagrama | Figuras 29 a 34 — los controles de robustez aparecen como objetos operación |
| ✅ Cumple | Mensajes respetan arquitectura y patrones | Párrafo | Sección 10.11, cierre — ningún mensaje salta de frontera a entidad sin control |
| ✅ Cumple | Errores y resultados observables representados | Párrafo | Sección 10.11, cierre — retorno ok/error y resultado observable explícitos |

## Diagrama de clases

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Clases con responsabilidades, atributos y operaciones | Figura o diagrama | Sección 10.5.7 — clases con responsabilidades y atributos (pág. 43) |
| ✅ Cumple | Tipos, visibilidad y firmas especificados | Tabla | Tabla 26, Sección 10.12 — visibilidad, tipos y firmas de operaciones (pág. 53) |
| ✅ Cumple | Relaciones y multiplicidades correctas | Figura o diagrama | Figura 35, Sección 10.12 — relaciones y multiplicidades (pág. 53) |
| ✅ Cumple | Alta cohesión y bajo acoplamiento revisados | Párrafo | Sección 10.12, cierre — una razón de cambio por clase; acoplamiento acotado |
| ✅ Cumple | Interfaces aíslan decisiones que pueden cambiar | Figura o diagrama | Figura 35 — la interfaz RepositorioUpstream aísla la API externa |
| ✅ Cumple | Consistencia con dominio, secuencias y código | Sección | Secciones 10.5.7, 10.11 y 10.12 — mismas entidades en dominio, secuencias y diseño |
| ✅ Cumple | Hito CDR aprobado | Sección | Sección 10.15, Tabla 32 — hito CDR aprobado por la dirección y la cátedra |

## Patrones de diseño

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Cada patrón resuelve un problema concreto | Tabla | Tabla 27, Sección 10.13 — problema concreto por patrón (pág. 54) |
| ✅ Cumple | Participantes y colaboraciones identificados | Tabla | Tabla 27, Sección 10.13 — participantes y colaboraciones (pág. 54) |
| ✅ Cumple | Clases reflejan la estructura del patrón | Párrafo | Sección 10.13 — reflejo de cada patrón en la Figura 35 de clases |
| ✅ Cumple | Secuencias reflejan su comportamiento | Párrafo | Sección 10.13 — reflejo de cada patrón en los diagramas de secuencia |
| ✅ Cumple | Alternativas, beneficios y costos documentados | Tabla | Tabla 28, Sección 10.13 — alternativas descartadas, beneficios y costos (pág. 54) |

## Testing estructural

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Unidad, especificación y dominio de entrada definidos | Sección | Sección 10.5.10 — casos de prueba CP-001 a CP-009 (pág. 44) |
| ✅ Cumple | Grafo de flujo de control construido | Figura o diagrama | Figura 36, Sección 10.14.2 — grafo de flujo de control (pág. 55) |
| ✅ Cumple | Criterio de cobertura declarado | Sección | Sección 10.14.3 — criterio de cobertura de decisión declarado y justificado (pág. 55) |
| ✅ Cumple | Conjunto de pruebas satisface el criterio | Tabla | Tabla 30, Sección 10.14.3 — TP-01 a TP-04 cubren los 4 caminos independientes |
| ✅ Cumple | Cobertura medida y evidencia adjunta | Tabla | Tabla 31, Sección 10.14.4 — cobertura medida: 7/7 nodos, 6/6 ramas, 4/4 caminos |
| ✅ Cumple | Casos normales, límites y fallas incluidos | Sección | Sección 10.5.10 — CP-001 a CP-009 cubren validación, firma, CI y paridad funcional (pág. 44) |
| ✅ Cumple | Pruebas re-ejecutables y resultado registrado | Sección | Sección 10.5.10 — CP-003/CP-004 se re-ejecutan en el pipeline de CI (pág. 44) |
| ✅ Cumple | Trazabilidad hasta TEST comprobada | Párrafo | Sección 10.14.4, cierre — cadena RF-03 → CU-001-006 → control → operación → TP |

## Entrega final por GitHub

- **Fork:** Entrega 1 disponible en el repositorio del curso; esta versión E2 aún no se ha subido.
- **Carpeta de entrega:** `trabajo_final/TorassaColombero_Valentin/`
- **Pull request:** Pendiente
- **Política de actualización:** abrir un nuevo pull request por cada actualización de la entrega.

---

Informe generado con la checklist interactiva SAP-TFI-2026.
