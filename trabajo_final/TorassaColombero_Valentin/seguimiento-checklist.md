# Informe de seguimiento del Trabajo Práctico

- **Alumno/a o equipo:** Valentín Torassa Colombero
- **Comisión:** T1-23-47 — Seminario de Trabajo Final de Ingeniería
- **Documento de esta entrega:** [Torassa_Valentin_E3-2C_v3.pdf](Torassa_Valentin_E3-2C_v3.pdf)
- **Última actualización:** 10/11/2026
- **Avance referenciado:** documento completo, puntos 1 a 11. 59/59 criterios de la checklist tecnológica documentados; los puntos 7, 8 y 9 se verificaron aparte contra la guía.
- **Cambios de numeración respecto de la versión 4:** la Sección 5.3.3 y la Tabla 9 son nuevas, así que los puntos 7 a 11 quedan tres páginas más adelante (10.4.3 y 10.4.4, cuatro) y las tablas posteriores a la 9 suman uno. Las figuras conservan su número.

## Punto 7 — Operaciones (guía del Plan de Desarrollo Tecnológico)

| Apartado | Ubicación en el documento | Evidencia |
|---|---|---|
| 7.1 Organización | Sección 7.1, pág. 33 | Articulación de I+D, tres frentes P1–P4 y condición para contratar. |
| 7.2 Grupo promotor y dirección | Sección 7.2, pág. 34; Tabla 21 | Personas identificadas; no se presume directorio ni accionistas. |
| 7.3 Staff y perfiles | Sección 7.3, pág. 34; Tabla 22 | Funciones, cobertura inicial, perfiles faltantes y programas P1–P5. |
| 7.4 Estructura y evolución | Sección 7.4, pág. 35; Figura 6 | Tres etapas alineadas con el cronograma y el límite de P4. |
| 7.5 Filosofía y sistema | Sección 7.5, pág. 36 | Flujo de contribución y transferencia con revisión y mantenimiento. |
| 7.6 RRHH por etapa | Sección 7.6, pág. 36; Tabla 23 | Horas del autor confirmadas (16/10/2026); horas externas condicionales. |

## Punto 8 — Plan Financiero-Económico (guía del Plan de Desarrollo Tecnológico)

| Apartado | Ubicación en el documento | Evidencia |
|---|---|---|
| Supuestos generales | Sección 8, pág. 38; Tabla 24 | Objeto (frente P4), horizonte 2027–2029, USD constantes, tipo de cambio, IVA, financiamiento propio, valor hora del autor y capacidad. |
| 8.1 Modelo de Ingresos | Sección 8.1, pág. 38; Tablas 25 a 28 | Paquetes y precios de referencia, unidades por año, apertura teórica de cobranzas (contado, 30, 60 y 90 días) y cobranzas netas. |
| 8.2 Modelo de Egresos | Sección 8.2, pág. 40; Tabla 29 | Producción, comercialización y administración, fijos y variables; sin costos financieros (no hay deuda). |
| 8.3 Modelo de Inversión | Sección 8.3, pág. 41; Tabla 30 | Activos fijos, activos diferidos y capital de trabajo por déficit acumulado máximo. |
| 8.4 Amortizaciones | Sección 8.4, pág. 42; Tabla 31 | Línea recta a tres años; valor residual nulo. |
| 8.5 Impuesto a las ganancias | Sección 8.5, pág. 42; Tablas 32 y 33 | Estado de resultados, quebranto, impuesto determinado y erogado (saldo de DDJJ y anticipos); alternativa de monotributo. |
| 8.6 Ingresos Brutos | Sección 8.6, pág. 43; Tabla 34 | IIBB Santa Fe 4,5 %, DReI Rosario 1 % (supuesto) e impuesto a los débitos y créditos. |
| 8.7 Remuneraciones y cargas sociales | Sección 8.7, pág. 44; Tablas 35 y 36 | Horas ligadas y no ligadas al volumen, revisor externo, aportes del autor y control de capacidad contra la Tabla 23. |
| 8.8 Presupuesto Financiero | Sección 8.8, pág. 45; Tablas 37 a 39 | Tasa de corte calculada (18,5 % real), flujo de caja anual con saldo de cierre y detalle trimestral de 2027. |
| 8.9 Evaluación de la Inversión | Sección 8.9, pág. 46; Tablas 40 a 42 | Flujo de fondos, VAN, TIR, repago simple y descontado, punto de equilibrio en ventas y en horas. |
| 8.10 Escenarios de Riesgo | Sección 8.10, pág. 47; Tablas 43 a 45 | Un escenario optimista y dos pesimistas, sensibilidad y umbrales que anulan el VAN. |
| 8.11 Plan de Contingencia | Sección 8.11, pág. 48; Tabla 46 | Indicadores de alerta y cinco medidas; resultado del Pesimista 1 con contingencia. |
| 8.12 Plan de Salida | Sección 8.12, pág. 49 | Disparadores, cierre ordenado y pérdida máxima acotada. |

Todas las cifras del punto 8 salen de `modelo_financiero.py` (incluido en el paquete); al ejecutarlo se regeneran las tablas.

## Punto 9 — Factibilidades

| Apartado | Ubicación en el documento | Evidencia |
|---|---|---|
| 9.1 Técnica | Sección 9.1, pág. 50; Tabla 47 | Parque instalado, ampliación necesaria (ya en la inversión), capacitación e instalaciones. |
| 9.2 Comercial | Sección 9.2, pág. 51 | Mercado necesario frente a la audiencia medida, competencia actual y futura, estrategia de comercialización. |
| 9.3 Administrativa | Sección 9.3, pág. 51; Tabla 48 | Procesos mínimos, responsables y frecuencia. |
| 9.4 Legal | Sección 9.4, pág. 52; Tablas 49 a 51 | Formas de organización y su evolución, normas y régimen tributario, propiedad intelectual, marcas, datos personales y política sobre LLMs. |

## Requerimientos

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Funcionales identificados, numerados y sin decisiones de implementación | Sección | Sección 10.4.2 — requerimientos funcionales RF-01 a RF-05 (pág. 56) |
| ✅ Cumple | No funcionales clasificados | Sección | Sección 10.4.2 — requerimientos no funcionales RNF-01 a RNF-06 (pág. 56) |
| ✅ Cumple | Alcance, actores y glosario acordados | Sección | Secciones 10.4.3 (alcance) y 10.4.4 (definiciones y acrónimos), pág. 57 |
| ✅ Cumple | Cada requisito se vincula con casos de uso | Tabla | Tabla 53, Sección 10.6.2 — matriz de trazabilidad REQ → CU (pág. 68) |
| ✅ Cumple | Al menos un criterio de aceptación por requisito | Tabla | Tabla 52, Sección 10.6.1 — criterios de aceptación por RF (pág. 68) |

## Casos de uso y especificaciones

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Diagrama general con actores, casos y límite del sistema | Figura o diagrama | Figura 20, Sección 10.7 — diagrama general con límite del sistema y actores (pág. 69) |
| ✅ Cumple | include y extend usados con sentido | Sección | Sección 10.5.3 — relaciones include y extend entre CU-001 a CU-006 (págs. 58-63) |
| ✅ Cumple | Una especificación por caso relevante | Sección | Sección 10.5.3 — una ficha por caso, CU-001 a CU-006 (págs. 58-63) |
| ✅ Cumple | Curso básico escrito en voz activa | Sección | Sección 10.8 — curso básico en voz activa de CU-001-001 a CU-001-006 (págs. 69-71) |
| ✅ Cumple | Alternativos, excepciones y reglas documentados | Sección | Sección 10.8 — alternativos, excepciones E1/E2 y reglas por caso (págs. 69-71) |
| ✅ Cumple | Hito RRR revisado con interesados | Sección | Sección 10.15, Tabla 61 — hito RRR revisado y aprobado por la dirección (pág. 80) |

## Modelo de dominio

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Clases tomadas del lenguaje del negocio | Figura o diagrama | Sección 10.5.7 — diagrama de clases / modelo de dominio de Podman (pág. 66) |
| ✅ Cumple | Atributos conceptuales relevantes | Figura o diagrama | Sección 10.5.7 — atributos conceptuales del modelo de dominio (pág. 66) |
| ✅ Cumple | Relaciones y multiplicidades justificadas | Figura o diagrama | Figura 35, Sección 10.12 — multiplicidades 1–7 y 1..* justificadas (pág. 76) |
| ✅ Cumple | Nombres sin sinónimos ni ambigüedades | Sección | Secciones 10.4.4 y 10.12 — vocabulario único entre dominio, robustez y clases |
| ✅ Cumple | Modelo actualizado después de robustez | Sección | Sección 10.10, párrafo de consistencia — el dominio se actualizó tras robustez (pág. 73) |

## Prototipo

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Pantallas y estados relevantes representados | Figura o diagrama | Figura 21, Sección 10.9 — pantallas P-01 a P-04 (pág. 71) |
| ✅ Cumple | Cada pantalla se vincula con casos y actores | Tabla | Tabla 54, Sección 10.9 — pantalla ↔ caso de uso ↔ actor (pág. 71) |
| ✅ Cumple | Controles y datos coinciden con las especificaciones | Tabla | Tabla 54, Sección 10.9 — datos y controles derivados de los cursos básicos (pág. 71) |
| ✅ Cumple | Prototipo revisado con usuarios | Párrafo | Sección 10.9, cierre — revisión exploratoria del 14, 16 y 17/10/2026 con tres perfiles y cobertura de P-01 a P-04; devolución verbal positiva y sin cambios sugeridos. O4 permanece como seguimiento de alcance. |
| ✅ Cumple | Se usa como especificación, no como producto final | Párrafo | Sección 10.9, apertura — declarado como especificación de interacción, no producto final |

## Arquitectura

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Vistas funcional, de datos y del sistema separadas | Sección | Secciones 10.5.5 paquetes, 10.5.6 componentes, 10.5.8 entidad-relación y 10.5.9 despliegue (págs. 64-67) |
| ✅ Cumple | Componentes, capas, responsabilidades e interfaces visibles | Figura o diagrama | Sección 10.5.6 — diagrama de componentes e interfaces (pág. 65) |
| ✅ Cumple | Despliegue, nodos y tecnologías documentados | Figura o diagrama | Sección 10.5.9 — diagrama de despliegue, nodos y tecnologías (pág. 67) |
| ✅ Cumple | Decisiones justificadas por requerimientos | Sección | Sección 10.12 — interfaz RepositorioUpstream justificada por RF-01 y RF-04 (pág. 76) |
| ✅ Cumple | Calidad y testing considerados | Sección | Sección 10.5.10 (casos de prueba) y Sección 11.1 (normas de calidad), págs. 67-68 |

## Diagramas de robustez

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Un diagrama por caso de uso diseñado | Figura o diagrama | Figuras 23 a 28, Sección 10.10 — un diagrama por cada caso de uso (págs. 72-73) |
| ✅ Cumple | Actor, Boundary, Control y Entity diferenciados | Figura o diagrama | Figura 22, Sección 10.10 — notación con Actor, Boundary, Control y Entity (pág. 72) |
| ✅ Cumple | Reglas de comunicación respetadas | Sección | Sección 10.10, encabezado — reglas de comunicación declaradas y respetadas (pág. 72) |
| ✅ Cumple | Una frontera clara por pantalla o interfaz | Párrafo | Sección 10.10, cierre — una frontera por interfaz, según Tabla 54 (pág. 73) |
| ✅ Cumple | Entidades consistentes con el dominio | Párrafo | Sección 10.10, cierre — entidades coinciden con el modelo de dominio 10.5.7 (pág. 73) |
| ✅ Cumple | Controles cubren cursos básicos y alternativos | Párrafo | Sección 10.10, cierre — un control para curso básico y otro para alternativos (pág. 73) |
| ✅ Cumple | Hito PDR aprobado | Sección | Sección 10.15, Tabla 61 — hito PDR aprobado por la dirección |

## Diagramas de secuencia

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Un diagrama por caso de uso | Figura o diagrama | Figuras 29 a 34, Sección 10.11 — un diagrama por caso de uso (págs. 74-75) |
| ✅ Cumple | Participantes derivados de robustez | Sección | Sección 10.11 — participantes derivados de los controles y entidades de robustez |
| ✅ Cumple | Texto del caso mapeado a mensajes | Sección | Sección 10.11 — cada mensaje corresponde a una oración del curso básico |
| ✅ Cumple | Controles asignados a operaciones u objetos | Figura o diagrama | Figuras 29 a 34 — los controles de robustez aparecen como objetos operación |
| ✅ Cumple | Mensajes respetan arquitectura y patrones | Párrafo | Sección 10.11, cierre — ningún mensaje salta de frontera a entidad sin control |
| ✅ Cumple | Errores y resultados observables representados | Párrafo | Sección 10.11, cierre — retorno ok/error y resultado observable explícitos |

## Diagrama de clases

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Clases con responsabilidades, atributos y operaciones | Figura o diagrama | Sección 10.5.7 — clases con responsabilidades y atributos (pág. 66) |
| ✅ Cumple | Tipos, visibilidad y firmas especificados | Tabla | Tabla 55, Sección 10.12 — visibilidad, tipos y firmas de operaciones (pág. 76) |
| ✅ Cumple | Relaciones y multiplicidades correctas | Figura o diagrama | Figura 35, Sección 10.12 — relaciones y multiplicidades (pág. 76) |
| ✅ Cumple | Alta cohesión y bajo acoplamiento revisados | Párrafo | Sección 10.12, cierre — una razón de cambio por clase; acoplamiento acotado |
| ✅ Cumple | Interfaces aíslan decisiones que pueden cambiar | Figura o diagrama | Figura 35 — la interfaz RepositorioUpstream aísla la API externa |
| ✅ Cumple | Consistencia con dominio, secuencias y código | Sección | Secciones 10.5.7, 10.11 y 10.12 — mismas entidades en dominio, secuencias y diseño |
| ✅ Cumple | Hito CDR aprobado | Sección | Sección 10.15, Tabla 61 — hito CDR aprobado por la dirección y la cátedra |

## Patrones de diseño

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Cada patrón resuelve un problema concreto | Tabla | Tabla 56, Sección 10.13 — problema concreto por patrón (pág. 77) |
| ✅ Cumple | Participantes y colaboraciones identificados | Tabla | Tabla 56, Sección 10.13 — participantes y colaboraciones (pág. 77) |
| ✅ Cumple | Clases reflejan la estructura del patrón | Párrafo | Sección 10.13 — reflejo de cada patrón en la Figura 35 de clases |
| ✅ Cumple | Secuencias reflejan su comportamiento | Párrafo | Sección 10.13 — reflejo de cada patrón en los diagramas de secuencia |
| ✅ Cumple | Alternativas, beneficios y costos documentados | Tabla | Tabla 57, Sección 10.13 — alternativas descartadas, beneficios y costos (pág. 77) |

## Testing estructural

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Unidad, especificación y dominio de entrada definidos | Sección | Sección 10.5.10 — casos de prueba CP-001 a CP-009 (pág. 67) |
| ✅ Cumple | Grafo de flujo de control construido | Figura o diagrama | Figura 36, Sección 10.14.2 — grafo de flujo de control (pág. 78) |
| ✅ Cumple | Criterio de cobertura declarado | Sección | Sección 10.14.3 — criterio de cobertura de decisión declarado y justificado (pág. 78) |
| ✅ Cumple | Conjunto de pruebas satisface el criterio | Tabla | Tabla 59, Sección 10.14.3 — TP-01 a TP-04 cubren los 4 caminos independientes |
| ✅ Cumple | Cobertura medida y evidencia adjunta | Tabla | Tabla 60, Sección 10.14.4 — cobertura medida: 7/7 nodos, 6/6 ramas, 4/4 caminos |
| ✅ Cumple | Casos normales, límites y fallas incluidos | Sección | Sección 10.5.10 — CP-001 a CP-009 cubren validación, firma, CI y paridad funcional (pág. 67) |
| ✅ Cumple | Pruebas re-ejecutables y resultado registrado | Sección | Sección 10.5.10 — CP-003/CP-004 se re-ejecutan en el pipeline de CI (pág. 67) |
| ✅ Cumple | Trazabilidad hasta TEST comprobada | Párrafo | Sección 10.14.4, cierre — cadena RF-03 → CU-001-006 → control → operación → TP |

## Repositorio y enlaces de la solución

| Qué | Ubicación en el documento | Enlace |
|---|---|---|
| Sitio en producción | Sección 10.1, pág. 55 | https://securitylabs.valentorassa.com |
| Repositorios de la solución | Sección 10.1, pág. 55 | https://github.com/ValentinTorassa/Open-Security-Labs y https://github.com/ValentinTorassa/VT-Security-Fixes |
| Contribuciones *upstream* | Sección 10.1, pág. 55; Anexos 11.3 y 11.4, págs. 81 a 85 | https://github.com/containers/podman/pull/28637, https://bugs.debian.org/1152837 y https://bugs.debian.org/1153126 |
| Entrega técnica | Sección 10.1, pág. 55 | Esta carpeta, `trabajo_final/TorassaColombero_Valentin/` |

## Entrega final por GitHub

- **Carpeta de entrega:** `trabajo_final/TorassaColombero_Valentin/`
- **Pull request:** pendiente; se abre uno nuevo para esta versión, como pide `trabajo_final/README.md`.
- **Política de actualización:** abrir un nuevo pull request por cada actualización de la entrega.

---

Informe generado con la checklist interactiva SAP-TFI-2026 y actualizado con la numeración de la versión 1.9, que la versión 1.10 conserva.
