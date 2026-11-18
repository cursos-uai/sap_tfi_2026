# Informe de seguimiento del Trabajo Práctico

- **Alumno/a o equipo:** Valentín Torassa Colombero
- **Comisión:** T1-23-47 — Seminario de Trabajo Final de Ingeniería
- **Documento de esta entrega:** [Torassa_Valentin_E3-2C_v5.pdf](Torassa_Valentin_E3-2C_v5.pdf) (versión 1.12)
- **Última actualización:** 17/11/2026
- **Solución tecnológica:** `blackice`, el software propio de la línea. El punto 10 se escribió de nuevo sobre `blackice`; la especificación anterior, del marco y del kit, sale del documento.
- **Avance referenciado:** documento completo, puntos 1 a 11. De los 59 criterios de la checklist tecnológica, 58 están documentados y 1 no se incluye por criterio de la cátedra en clase. Los puntos 7, 8 y 9 se verificaron aparte contra la guía.
- **Criterio de la cátedra en clase:** no van los diagramas de paquetes, de componentes, de despliegue ni entidad-relación. La checklist se sigue con ese criterio.
- **Ubicaciones:** por sección, tabla y figura, con la numeración del PDF de la versión 1.12. Las páginas están en el índice del PDF. Las tablas y las figuras de los puntos 1 a 9 conservan el número de la versión 1.11. En el punto 10, la arquitectura es el primer apartado de la Sección 10.5 y no lleva número propio.

## Punto 7 — Operaciones (guía del Plan de Desarrollo Tecnológico)

| Apartado | Ubicación en el documento | Evidencia |
|---|---|---|
| 7.1 Organización | Sección 7.1 | Articulación de I+D, tres frentes P1–P4 y condición para contratar. |
| 7.2 Grupo promotor y dirección | Sección 7.2; Tabla 21 | Personas identificadas; no se presume directorio ni accionistas. |
| 7.3 Staff y perfiles | Sección 7.3; Tabla 22 | Funciones, cobertura inicial, perfiles faltantes y programas P1–P5. |
| 7.4 Estructura y evolución | Sección 7.4; Figura 6 | Tres etapas alineadas con el cronograma y el límite de P4. |
| 7.5 Filosofía y sistema | Sección 7.5 | Flujo de contribución y transferencia con revisión y mantenimiento; nombra las siete fases del marco de contribución. |
| 7.6 RRHH por etapa | Sección 7.6; Tabla 23 | Horas del autor confirmadas (16/10/2026); horas externas condicionales. |

## Punto 8 — Plan Financiero-Económico (guía del Plan de Desarrollo Tecnológico)

| Apartado | Ubicación en el documento | Evidencia |
|---|---|---|
| Supuestos generales | Sección 8; Tabla 24 | Objeto (frente P4), horizonte 2027–2029, USD constantes, tipo de cambio, IVA, financiamiento propio, valor hora del autor y capacidad. |
| 8.1 Modelo de Ingresos | Sección 8.1; Tablas 25 a 28 | Paquetes y precios de referencia, unidades por año, apertura teórica de cobranzas y cobranzas netas. |
| 8.2 Modelo de Egresos | Sección 8.2; Tabla 29 | Producción, comercialización y administración, fijos y variables; sin costos financieros. |
| 8.3 Modelo de Inversión | Sección 8.3; Tabla 30 | Activos fijos, activos diferidos y capital de trabajo por déficit acumulado máximo. |
| 8.4 Amortizaciones | Sección 8.4; Tabla 31 | Línea recta a tres años; valor residual nulo. |
| 8.5 Impuesto a las ganancias | Sección 8.5; Tablas 32 y 33 | Estado de resultados, quebranto, impuesto determinado y erogado; alternativa de monotributo. |
| 8.6 Ingresos Brutos | Sección 8.6; Tabla 34 | IIBB Santa Fe 4,5 %, DReI Rosario 1 % (supuesto) e impuesto a los débitos y créditos. |
| 8.7 Remuneraciones y cargas sociales | Sección 8.7; Tablas 35 y 36 | Horas ligadas y no ligadas al volumen, revisor externo, aportes del autor y control de capacidad contra la Tabla 23. |
| 8.8 Presupuesto Financiero | Sección 8.8; Tablas 37 a 39 | Tasa de corte calculada (18,5 % real), flujo de caja anual con saldo de cierre y detalle trimestral de 2027. |
| 8.9 Evaluación de la Inversión | Sección 8.9; Tablas 40 a 42 | Flujo de fondos, VAN, TIR, repago simple y descontado, punto de equilibrio en ventas y en horas. |
| 8.10 Escenarios de Riesgo | Sección 8.10; Tablas 43 a 45 | Un escenario optimista y dos pesimistas, sensibilidad y umbrales que anulan el VAN. |
| 8.11 Plan de Contingencia | Sección 8.11; Tabla 46 | Indicadores de alerta y cinco medidas; resultado del Pesimista 1 con contingencia. |
| 8.12 Plan de Salida | Sección 8.12 | Disparadores, cierre ordenado y pérdida máxima acotada. |

Todas las cifras del punto 8 salen de `modelo_financiero.py` (incluido en el paquete); al ejecutarlo se regeneran las tablas. El punto 8 no cambia en la versión 1.12: no cuenta ningún financiamiento de Vercel.

## Punto 9 — Factibilidades

| Apartado | Ubicación en el documento | Evidencia |
|---|---|---|
| 9.1 Técnica | Sección 9.1; Tabla 47 | Parque instalado (suma la Mac con que se hizo `blackice`), ampliación necesaria (ya en la inversión), capacitación, y diseño y verificación del punto 10. |
| 9.2 Comercial | Sección 9.2 | Mercado necesario frente a la audiencia medida, competencia actual y futura, estrategia de comercialización. |
| 9.3 Administrativa | Sección 9.3; Tabla 48 | Procesos mínimos, responsables y frecuencia. |
| 9.4 Legal | Sección 9.4; Tablas 49 a 51 | Formas de organización y su evolución, normas y régimen tributario, propiedad intelectual, marcas, datos personales y política sobre LLMs. |

## Requerimientos

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Funcionales identificados, numerados y sin decisiones de implementación | Tabla | Sección 10.4.2 — RF-01 a RF-09, tabla «Requerimientos de sistema: funcionales» |
| ✅ Cumple | No funcionales clasificados | Tabla | Sección 10.4.2 — RNF-01 a RNF-06 por clase y RE-01 a RE-03 de entorno; los de usuario son RU-01 a RU-04 |
| ✅ Cumple | Alcance, actores y glosario acordados | Sección | Secciones 10.4.3 (alcance y tabla «Actores») y 10.4.4 (glosario) |
| ✅ Cumple | Cada requisito se vincula con casos de uso | Tabla | Sección 10.4.2 — columna «Casos» de cada tabla; Sección 10.12, tabla «Trazabilidad por caso de uso central» |
| ✅ Cumple | Al menos un criterio de aceptación por requisito | Tabla | Sección 10.4.2 — columna «Criterio de aceptación» en las tablas de usuario y de sistema, y «Cómo se verifica» en la de entorno |

## Casos de uso y especificaciones

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Diagrama general con actores, casos y límite del sistema | Figura o diagrama | Sección 10.5.2 — dos figuras «Diagrama general»: actores y casos centrales, y relaciones |
| ✅ Cumple | include y extend usados con sentido | Figura o diagrama | Secciones 10.5.2 y 10.5.3 — cinco casos incluidos y seis extensiones, cada extensión con su condición; un diagrama por caso central |
| ✅ Cumple | Una especificación por caso relevante | Sección | Sección 10.5.3 — fichas de CU-002-001 a 004; tablas de casos incluidos y de extensiones |
| ✅ Cumple | Curso básico escrito en voz activa | Sección | Sección 10.5.3 — campo «Camino ideal» de cada ficha: cada paso dice quién actúa («Usuario:», «Sistema:») |
| ✅ Cumple | Alternativos, excepciones y reglas documentados | Sección | Sección 10.5.3 — campo «Caminos alternativos» (paso, respuesta y cierre) y tabla «Reglas que citan las fichas» (RN-01 a RN-07) |
| ✅ Cumple | Hito RRR revisado con interesados | Tabla | Sección 10.13, tabla «Hitos de revisión» — revisado por la dirección el 17/11/2026 |

## Modelo de dominio

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Clases tomadas del lenguaje del negocio | Figura o diagrama | Sección 10.5.4, figura «Modelo de dominio» — cosas del problema, con los nombres del glosario |
| ✅ Cumple | Atributos conceptuales relevantes | Figura o diagrama | Sección 10.5.4, figura «Modelo de dominio» |
| ✅ Cumple | Relaciones y multiplicidades justificadas | Figura o diagrama | Sección 10.5.4 — cada línea lleva su nombre y cuántos participan de cada lado |
| ✅ Cumple | Nombres sin sinónimos ni ambigüedades | Sección | Sección 10.4.4 — un significado por término, en el texto y en los diagramas |
| ✅ Cumple | Modelo actualizado después de robustez | Sección | Secciones 10.5.4 y 10.7 — las entidades de robustez son los conceptos del dominio, con el mismo nombre |

## Prototipo

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Pantallas y estados relevantes representados | Figura o diagrama | Sección 10.6 — bosquejos P-01 a P-05 y tabla «Bosquejos de pantalla y sus estados» |
| ✅ Cumple | Cada pantalla se vincula con casos y actores | Tabla | Sección 10.6, tabla «Bosquejos de pantalla y sus estados»; campo «Prototipo» de cada ficha (10.5.3) |
| ✅ Cumple | Controles y datos coinciden con las especificaciones | Figura o diagrama | Sección 10.6 — cada bosquejo muestra los datos y las acciones que nombra su ficha; las notas numeradas explican cada parte |
| ✅ Cumple | Prototipo revisado con usuarios | Tabla | Sección 10.6, tabla «Cambios que salieron del uso real»; `registro-revision-prototipo.md` |
| ✅ Cumple | Se usa como especificación, no como producto final | Párrafo | Sección 10.6, apertura — son bosquejos dibujados para la especificación, no capturas |

## Arquitectura

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Vistas funcional, de datos y del sistema separadas | Sección | Funcional: 10.5.2 y 10.5.3. Datos: 10.5.4. Sistema: 10.5, apartado «Arquitectura: tipo, estilo y patrón», con una vista estática y una de ejecución. Los diagramas de paquetes y entidad-relación no se incluyen, por criterio de la cátedra en clase. |
| ✅ Cumple | Componentes, capas, responsabilidades e interfaces visibles | Figura o diagrama | Sección 10.5, apartado «Arquitectura» — estratos con su responsabilidad y procesos con la comunicación rotulada en cada flecha. El diagrama de componentes no se incluye, por criterio de la cátedra en clase. |
| ➖ No se incluye | Despliegue, nodos y tecnologías documentados | — | No se incluye, por criterio de la cátedra en clase. Dónde corre cada parte y con qué tecnología: Secciones 10.4.5 y 10.5 (apartado «Arquitectura»). |
| ✅ Cumple | Decisiones justificadas por requerimientos | Párrafo | Sección 10.5, apartado «Arquitectura», «Por qué estos estilos» — cada decisión cita su requerimiento; tipo, estilo y patrón según el catálogo de Cristiá |
| ✅ Cumple | Calidad y testing considerados | Sección | Sección 10.11 (pruebas) y Sección 11.1 (normas de calidad) |

## Diagramas de robustez

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Un diagrama por caso de uso diseñado | Figura o diagrama | Sección 10.7 — un diagrama por caso central, CU-002-001 a 004 |
| ✅ Cumple | Actor, Boundary, Control y Entity diferenciados | Figura o diagrama | Sección 10.7, apertura — los tres símbolos y qué es cada uno |
| ✅ Cumple | Reglas de comunicación respetadas | Párrafo | Sección 10.7, apertura — los actores sólo tocan fronteras; fronteras y entidades se conectan a través de controles |
| ✅ Cumple | Una frontera clara por pantalla o interfaz | Figura o diagrama | Sección 10.7 — cada frontera es un bosquejo del prototipo (P-01 a P-05) o el *hook* del agente |
| ✅ Cumple | Entidades consistentes con el dominio | Párrafo | Secciones 10.5.4 (cierre) y 10.7 — cada entidad es un concepto del modelo de dominio |
| ✅ Cumple | Controles cubren cursos básicos y alternativos | Figura o diagrama | Sección 10.7 — cada camino alternativo de la ficha figura junto al control que lo atiende |
| ✅ Cumple | Hito PDR aprobado | Tabla | Sección 10.13, tabla «Hitos de revisión» — revisado por la dirección el 17/11/2026 |

## Diagramas de secuencia

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Un diagrama por caso de uso | Figura o diagrama | Sección 10.8 — un diagrama por caso central |
| ✅ Cumple | Participantes derivados de robustez | Párrafo | Sección 10.8, apertura — fronteras y entidades pasan a ser clases |
| ✅ Cumple | Texto del caso mapeado a mensajes | Figura o diagrama | Sección 10.8 — cada diagrama sigue el camino ideal de su ficha |
| ✅ Cumple | Controles asignados a operaciones u objetos | Párrafo | Sección 10.8, apertura — los controles pasan a ser operaciones, con los nombres del código |
| ✅ Cumple | Mensajes respetan arquitectura y patrones | Figura o diagrama | Secciones 10.8 y 10.10 — los mensajes entre procesos van por XPC; la tabla de patrones dice en qué secuencia se ve cada uno |
| ✅ Cumple | Errores y resultados observables representados | Figura o diagrama | Sección 10.8 — un fragmento *alt* por diagrama con el camino alternativo que más pesa |

## Diagrama de clases

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Clases con responsabilidades, atributos y operaciones | Figura o diagrama | Sección 10.9 — un diagrama por caso central, con los atributos y las operaciones que ese caso usa |
| ✅ Cumple | Tipos, visibilidad y firmas especificados | Figura o diagrama | Sección 10.9 — firmas del código de la versión 1.1.1; `+` público, `-` privado |
| ✅ Cumple | Relaciones y multiplicidades correctas | Figura o diagrama | Sección 10.9 — relaciones entre las clases de cada caso, con la multiplicidad donde hay más de una |
| ✅ Cumple | Alta cohesión y bajo acoplamiento revisados | Tabla | Sección 10.5, apartado «Arquitectura», tabla de los dos estilos — un módulo sólo usa a los inferiores y lo comprueba el compilador; en 10.9 cada diagrama tiene sólo las clases de su caso |
| ✅ Cumple | Interfaces aíslan decisiones que pueden cambiar | Figura o diagrama | Sección 10.9 — los protocolos de Swift van como interfaces; Sección 10.10, patrón Adapter |
| ✅ Cumple | Consistencia con dominio, secuencias y código | Sección | Secciones 10.8 y 10.9 — mismas clases en la secuencia y en el diagrama de cada caso, con los nombres del código |
| ✅ Cumple | Hito CDR aprobado | Tabla | Sección 10.13, tabla «Hitos de revisión» — revisado por la dirección el 17/11/2026 |

## Patrones de diseño

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Cada patrón resuelve un problema concreto | Tabla | Sección 10.10, tabla «Patrones de diseño» — columna «Problema que resuelve acá» |
| ✅ Cumple | Participantes y colaboraciones identificados | Tabla | Sección 10.10 — columna «Participantes en el código» |
| ✅ Cumple | Clases reflejan la estructura del patrón | Figura o diagrama | Sección 10.9 — una nota marca en cada diagrama dónde aparece el patrón |
| ✅ Cumple | Secuencias reflejan su comportamiento | Tabla | Sección 10.10 — columna «Patrón y dónde se ve», con la figura de secuencia de cada uno |
| ✅ Cumple | Alternativas, beneficios y costos documentados | Tabla | Sección 10.10 — columnas «Alternativa descartada» y «Costo» |

## Testing estructural

| Estado | Criterio | Tipo de referencia | Ubicación en el documento |
|---|---|---|---|
| ✅ Cumple | Unidad, especificación y dominio de entrada definidos | Sección | Sección 10.11.2 — unidad `HookAnswer.parse`: decide si lo que imprimió un agente cuenta como respuesta; código con el nodo de cada línea |
| ✅ Cumple | Grafo de flujo de control construido | Figura o diagrama | Sección 10.11.2, figura «Grafo de flujo de control de `HookAnswer.parse`» |
| ✅ Cumple | Criterio de cobertura declarado | Párrafo | Sección 10.11.2, «Criterio de cobertura» — los seis caminos independientes y todas las regiones |
| ✅ Cumple | Conjunto de pruebas satisface el criterio | Tabla | Sección 10.11.2, tabla «Casos de la prueba estructural» — TP-01 a TP-11 |
| ✅ Cumple | Cobertura medida y evidencia adjunta | Tabla | Sección 10.11.2, tabla «Cobertura medida» — 14 de 14 regiones y 16 de 16 líneas; `evidencia/cobertura-hookanswer-2026-11-17.txt` |
| ✅ Cumple | Casos normales, límites y fallas incluidos | Tabla | Sección 10.11.2, tabla «Casos de la prueba estructural»; Sección 10.11.1, casos CP |
| ✅ Cumple | Pruebas re-ejecutables y resultado registrado | Tabla | Sección 10.11.2, tabla «Cobertura medida» — comando, equipo, versión, fecha y resultado; Sección 10.11.1, «Resultado» |
| ✅ Cumple | Trazabilidad hasta TEST comprobada | Tabla | Sección 10.12, tabla «Un caso de punta a punta: CU-002-004» |

## Repositorio y enlaces de la solución

| Qué | Ubicación en el documento | Enlace |
|---|---|---|
| Solución tecnológica: `blackice` | Sección 10.1; Sección 5.3.5; Anexo 11.5 | https://github.com/ValentinTorassa/blackice y https://blackice-macos.vercel.app |
| Otros repositorios de la línea | Secciones 5.3.1 y 5.3.2 | https://github.com/ValentinTorassa/Open-Security-Labs y https://github.com/ValentinTorassa/VT-Security-Fixes |
| Contribuciones *upstream* | Sección 5.3.3; Anexos 11.3 y 11.4 | https://github.com/containers/podman/pull/28637, https://bugs.debian.org/1152837 y https://bugs.debian.org/1153126 |
| Aportes a Vercel Labs (sin integrar) | Sección 5.3.6; Anexo 11.5 | https://github.com/vercel-labs/deepsec/pull/137 y https://github.com/vercel-labs/fx/pull/1659 |
| Evidencia de la prueba estructural | Sección 10.11.2 | `evidencia/cobertura-hookanswer-2026-11-17.txt` |
| Entrega técnica | Sección 10.1 | Esta carpeta, `trabajo_final/TorassaColombero_Valentin/` |

## Entrega final por GitHub

- **Carpeta de entrega:** `trabajo_final/TorassaColombero_Valentin/`
- **Pull request:** pendiente; se abre uno nuevo para esta versión, como pide `trabajo_final/README.md`.
- **Política de actualización:** abrir un nuevo pull request por cada actualización de la entrega.

---

Informe generado con la checklist interactiva SAP-TFI-2026 y actualizado para la versión 1.12.
