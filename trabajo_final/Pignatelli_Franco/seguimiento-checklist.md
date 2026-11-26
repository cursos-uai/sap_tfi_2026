# Seguimiento del checklist — Aeromentor (documento 02.02)

Recorrido de los 59 ítems del [checklist del curso](https://cursos-uai.github.io/sap_tfi_2026/checklist.html) sobre el documento [Franco_Pignatelli_E3_02.02.pdf](Franco_Pignatelli_E3_02.02.pdf). Cada ítem cita la sección y la figura donde se cumple. Un ítem se tilda solo si el documento lo muestra; lo que no se cumple, o se cumple en parte, queda sin tildar y con su motivo.

**Resumen:** los 59 ítems cumplidos. Los hitos de revisión (ui-3, cu-5, rob-6 y class-6) se registran en la tabla «Revisiones» de la «Ficha de Seguimiento y Revisión».

## Requerimientos

- [x] **req-0. Funcionales identificados, numerados y sin decisiones de implementación.** 10.4.2.1: RF-01 a RF-11, cada uno expresado como una capacidad observable. Las decisiones técnicas quedan en la arquitectura (10.5.6) y en las clases (10.5.7).
- [x] **req-1. No funcionales clasificados.** 10.4.2.2: RNF-01 a RNF-09, cada uno con su categoría: seguridad (RNF-01, RNF-04, RNF-05), confiabilidad (RNF-02, RNF-07), disponibilidad (RNF-03), usabilidad (RNF-06), desempeño (RNF-08) y portabilidad (RNF-09).
- [x] **req-2. Alcance, actores y glosario acordados.** 10.4.3: alcance con lo que entra, lo que queda fuera (con su motivo) y la operatividad básica no core. Actores en el diagrama general (Fig. 10) y en cada ficha. Glosario del dominio en 10.4.4.1 (43 términos, con noción e impacto) y diccionario de atributos conceptuales en 10.4.4.2. Fichas, dominio, robustez y secuencias usan el mismo vocabulario.
- [x] **req-3. Cada requisito se vincula con casos de uso.** Columna «Caso de uso» en las cinco tablas de 10.4.2.1 a 10.4.2.5 y matriz REQ → CU → TEST de 10.4.2.6, con los 40 requerimientos.
- [x] **req-4. Al menos un criterio de aceptación por requisito.** Los 40 requerimientos de 10.4.2.1 a 10.4.2.5 tienen su columna «Criterio de aceptación» con un resultado comprobable.

## Casos de uso y especificaciones

- [x] **cu-0. Diagrama general con actores, casos y límite del sistema.** 10.5.2.1, Fig. 10. Diagramas por caso de uso: Figs. 16 (CU-001), 30 (CU-002), 48 (CU-003) y 66 (CU-004).
- [x] **cu-1. include y extend usados con sentido.** Índice de casos de uso (10.5.2): cada relación indica su condición; include para lo obligatorio que se reutiliza y extend para lo opcional o condicionado. CU-001: 5 include y 5 extend; CU-002: 5 y 6; CU-003: 6 y 8; CU-004: 5 y 6.
- [x] **cu-2. Una especificación por caso relevante.** 10.5.3.1: 17 fichas de sub-casos (CU-001: 4, CU-002: 4, CU-003: 5, CU-004: 4) con objetivo, identificador, descripción, precondiciones y poscondiciones, actores primarios y secundarios, eventos disparadores, extensiones, escenario principal, caminos alternativos y prototipo.
- [x] **cu-3. Curso básico escrito en voz activa.** Escenario principal de éxito de cada ficha (10.5.3.1), en pasos numerados donde el actor o el Sistema realiza la acción.
- [x] **cu-4. Alternativos, excepciones y reglas documentados.** Sección «Caminos alternativos» de cada ficha (10.5.3.1): cada desvío se numera por el paso de origen (por ejemplo, 7.a) y tiene condición, respuesta del Sistema y cierre.
- [x] **cu-5. Hito RRR revisado con interesados.** «Ficha de Seguimiento y Revisión», tabla «Revisiones»: el 26/11/2026, Antonio Panarisi, Jefe de Instructores del Círculo de Aviación, revisó los casos de uso, los requerimientos y el prototipo de la versión 02.01 y consideró que cubren las necesidades del aeroclub para un producto mínimo viable. Aprobada sin observaciones. El dominio se revisó en el hito PDR (rob-6).

## Modelo de dominio

- [x] **dom-0. Clases tomadas del lenguaje del negocio.** 10.5.2.2: Figs. 11 (vista general) y 12 a 15 (una por caso de uso). Solo conceptos del negocio, sin pantallas, controles ni detalles técnicos.
- [x] **dom-1. Atributos conceptuales relevantes.** 10.4.4.2: diccionario de atributos conceptuales de 22 conceptos, en lenguaje natural, sin tipos ni claves. Por convención, los diagramas de dominio no llevan atributos y remiten a ese diccionario.
- [x] **dom-2. Relaciones y multiplicidades justificadas.** Figs. 11 a 15: cada asociación lleva un nombre que expresa un hecho del dominio (por ejemplo, «el aeroclub agrupa a los pilotos») y sus multiplicidades.
- [x] **dom-3. Nombres sin sinónimos ni ambigüedades.** Un único vocabulario, el del glosario 10.4.4.1, en el dominio, las fichas, la robustez, las secuencias y los bocetos.
- [x] **dom-4. Modelo actualizado después de robustez.** Cada entidad de los diagramas de robustez (Figs. 27, 44, 62 y 77) aparece en el modelo de dominio (Figs. 11 a 15).

## Prototipo

- [x] **ui-0. Pantallas y estados relevantes representados.** 13 bocetos y 40 capturas en el «Prototipo de la interfaz Gráfica» de cada caso de uso (10.5.3.1): CU-001, bocetos en las Figs. 17 a 19 y capturas en las 20 a 26; CU-002, Figs. 31 a 33 y 34 a 43; CU-003, Figs. 49 a 52 y 53 a 61; CU-004, Figs. 67 a 69 y 70 a 76. Estados de error, confirmación y aviso: Figs. 18, 19, 25, 37, 42, 52, 54, 56, 68, 73, 74 y 75. Pantallas generales en 10.5 (Figs. 2 a 8).
- [x] **ui-1. Cada pantalla se vincula con casos y actores.** Cada boceto lleva su leyenda con caso de uso, actor, pantalla y estados, y cada ficha cita su boceto y sus capturas por número de figura. El mapa de navegación (10.5.1.1, Fig. 9) muestra las rutas del sistema con las pantallas de los casos de uso resaltadas.
- [x] **ui-2. Controles y datos coinciden con las especificaciones.** Los bocetos usan los nombres de pantalla y los controles de las fichas (por ejemplo, el botón «Correr monitoreo ahora», Figs. 49 y 53, y el aviso «Monitoreo terminado», Fig. 54, citados en CU-003.001); las capturas son del sistema desplegado.
- [x] **ui-3. Prototipo revisado con usuarios.** «Ficha de Seguimiento y Revisión», tabla «Revisiones»: el 26/11/2026, Antonio Panarisi, Jefe de Instructores del Círculo de Aviación, revisó el prototipo (bocetos y sistema) de la versión 02.01. Aprobado sin observaciones.
- [x] **ui-4. Se usa como especificación, no como producto final.** Los bocetos (Figs. 17 a 19, 31 a 33, 49 a 52 y 67 a 69) son simbólicos, sin el estilo del producto, y van en cada ficha antes que las capturas. Los nombres de las pantallas de los bocetos son las fronteras de la robustez y de la secuencia.

## Arquitectura

- [x] **arch-0. Vistas funcional, de datos y del sistema separadas.** 10.5.6: vista funcional (Figs. 94 y 95), vista de datos (Fig. 96) y vista del sistema (Fig. 97), cada una con su texto.
- [x] **arch-1. Componentes, capas, responsabilidades e interfaces visibles.** 10.5.6, «Estilo arquitectónico»: estilo Cliente–Servidor de tres capas con el subestilo de invocación implícita, y desvíos del estilo puro declarados. Conectores con protocolo y mensaje (Fig. 94), tabla de eventos con quién los anuncia y quién los escucha, y tabla «Qué provee cada componente» con la capa y la justificación de los 28 componentes.
- [x] **arch-2. Despliegue, nodos y tecnologías documentados.** Vista del sistema (Fig. 97): servidor, contenedores, base de datos PostgreSQL, Redis, proceso de jobs e integraciones externas (Gemini, aviationweather.gov, Open-Meteo, OpenAIP). Entorno y producción en 10.4.5.
- [x] **arch-3. Decisiones justificadas por requerimientos.** 10.5.6, «Pros y contras»: cada ventaja y cada costo aceptado se liga a su requerimiento (RNF-01, RNF-03, RNF-05, RNF-06, RF-01, RF-07, RE-05 y RE-06).
- [x] **arch-4. Calidad y testing considerados.** 10.5.6, «Pros y contras»: cambio (presentación independiente de la lógica de negocio), seguridad (autorización centralizada y aislamiento entre aeroclubes) y rendimiento (llamadas sincrónicas al modelo de IA y su tiempo de espera). Comprobabilidad: casos de prueba y caja blanca en 10.5.10; prácticas de calidad y auditoría de seguridad en 11.1.

## Diagramas de robustez

- [x] **rob-0. Un diagrama por caso de uso diseñado.** Figs. 27 (CU-001), 44 (CU-002), 62 (CU-003) y 77 (CU-004), en la ficha de cada caso de uso (10.5.3.1).
- [x] **rob-1. Actor, Boundary, Control y Entity diferenciados.** Cada diagrama va con su tabla Frontera / Control / Entidad. Las fronteras y las entidades son sustantivos; los controles, acciones.
- [x] **rob-2. Reglas de comunicación respetadas.** La convención está declarada junto a los diagramas: solo aristas Actor–Frontera, Frontera–Control y Control–Entidad, sin aristas Control–Control y sin numeración ni orden en las líneas.
- [x] **rob-3. Una frontera clara por pantalla o interfaz.** Cada frontera es una pantalla con el mismo nombre que en el boceto, la captura y la ficha (por ejemplo, «Evaluación pre-vuelo», «Elegí una ruta», «Monitoreo», «Confirmá los datos»).
- [x] **rob-4. Entidades consistentes con el dominio.** Toda entidad de las Figs. 27, 44, 62 y 77 está en el modelo de dominio (Figs. 11 a 15).
- [x] **rob-5. Controles cubren cursos básicos y alternativos.** Los controles recorren el escenario principal y los caminos alternativos de cada ficha, sin asignar métodos ni algoritmos (eso queda para la secuencia y las clases).
- [x] **rob-6. Hito PDR aprobado.** «Ficha de Seguimiento y Revisión», tabla «Revisiones»: el 26/11/2026, Pedro Bustos, Ingeniero en Sistemas, revisó la consistencia entre el texto de los casos de uso, la robustez, el dominio, el modelo de datos y la arquitectura de la versión 02.01. Aprobado sin observaciones.

## Diagramas de secuencia

- [x] **seq-0. Un diagrama por caso de uso.** 10.5.4: CU-001 en las Figs. 80 y 81; CU-002 en las Figs. 82 a 84; CU-003 en las Figs. 85 a 87; CU-004 en las Figs. 88 y 89. Los caminos alternativos van como bloques alt, opt y loop dentro de las mismas figuras.
- [x] **seq-1. Participantes derivados de robustez.** Las fronteras son las pantallas de la robustez (Figs. 27, 44, 62 y 77) y los servicios externos; no hay participantes genéricos del tipo «Frontend» o «API». Cada participante con clase está en los diagramas de clases (10.5.7).
- [x] **seq-2. Texto del caso mapeado a mensajes.** Cada paso del escenario de la ficha tiene sus mensajes en el mismo orden, con las condiciones como alt u opt y los ciclos como loop (CU-002, Figs. 82 a 84; CU-003, Figs. 85 a 87, con las dos vueltas del lazo de monitoreo).
- [x] **seq-3. Controles asignados a operaciones u objetos.** Cada mensaje con operación corresponde a una operación de la clase destino en el diagrama de clases del mismo caso de uso (Figs. 98 a 107), y esa operación existe en el código.
- [x] **seq-4. Mensajes respetan arquitectura y patrones.** Los patrones se ven en las secuencias: Composite en las Figs. 80 y 85, Observer en las 81, 84, 87 y 89, Strategy en la 86 y MAPE-K en las 85 a 87. Las capas son las de 10.5.6: controlador delgado, servicios y políticas de autorización.
- [x] **seq-5. Errores y resultados observables representados.** Los retornos vuelven a la pantalla que hizo el pedido. Hay errores y degradaciones en todos los casos de uso: rol sin permiso y reserva ajena (Fig. 80), respaldo sin IA (Figs. 81 y 83), pedido inválido (Fig. 82), tramo inválido (Fig. 84), lazo ocupado (Fig. 85), plan determinista sin IA (Fig. 86), formato no permitido (Fig. 88) y certificación existente (Fig. 89).

## Diagrama de clases

- [x] **class-0. Clases con responsabilidades, atributos y operaciones.** 10.5.7: diez figuras de clases (CU-001, Figs. 98 y 99; CU-002, Figs. 100 y 101; CU-003, Figs. 102 a 105; CU-004, Figs. 106 y 107), con las clases reales del código, sus atributos y las operaciones que usan las secuencias.
- [x] **class-1. Tipos, visibilidad y firmas especificados.** Figs. 98 a 107: operaciones con visibilidad, parámetros tipados y tipo de retorno.
- [x] **class-2. Relaciones y multiplicidades correctas.** Figs. 98 a 107: asociaciones con multiplicidad, composición y herencia; la herencia de certificaciones (licencia, habilitación y certificado médico) se justifica en el patrón Composite (Fig. 90).
- [x] **class-3. Alta cohesión y bajo acoplamiento revisados.** 10.5.7, «Ocultamiento de información»: cada módulo protege un secreto coherente, con su interfaz, su función y sus relaciones (17 módulos). Controladores delgados y servicios con una sola responsabilidad (10.5.6).
- [x] **class-4. Interfaces aíslan decisiones que pueden cambiar.** La misma tabla de 10.5.7 lista la decisión que puede cambiar en cada módulo y la interfaz que la aísla (por ejemplo, el proveedor del modelo de IA, el servicio meteorológico o las reglas del monitoreo).
- [x] **class-5. Consistencia con dominio, secuencias y código.** Los conceptos del dominio (Figs. 11 a 15) se corresponden con las clases; las operaciones de las secuencias están en las clases; las tablas del modelo de datos (10.5.8, Figs. 108 a 110) son las del esquema real.
- [x] **class-6. Hito CDR aprobado.** «Ficha de Seguimiento y Revisión», tabla «Revisiones»: el 26/11/2026, Pedro Bustos, Ingeniero en Sistemas, revisó el diseño de clases, secuencias y patrones de la versión 02.01 y lo consideró completo e implementado. Aprobado sin observaciones.

## Patrones de diseño

- [x] **patterns-0. Cada patrón resuelve un problema concreto.** «Documentación de la aplicación de Patrones de Diseño»: cada caja explica en «because» los cambios previstos, la funcionalidad y las restricciones de diseño que llevan a elegir el patrón (Composite, Fig. 90; Observer, Fig. 91; Strategy, Fig. 92; MAPE-K por analogía, Fig. 93).
- [x] **patterns-1. Participantes y colaboraciones identificados.** Campo «where» de cada caja: cada elemento del diseño, con el rol del patrón que cumple. Lo que el patrón prevé y el diseño no tiene se declara como «no existe», con su motivo.
- [x] **patterns-2. Clases reflejan la estructura del patrón.** Figs. 90 a 93, con las clases reales del sistema (por ejemplo, `Certifications::Composite` y sus hojas, o `Monitoring::Planner` con sus dos estrategias).
- [x] **patterns-3. Secuencias reflejan su comportamiento.** Cada patrón remite a las figuras de secuencia donde se ve su comportamiento: Composite en las Figs. 80 y 85; Observer en las 81, 84, 87 y 89; Strategy en la 86; MAPE-K en las 85 a 87.
- [x] **patterns-4. Alternativas, beneficios y costos documentados.** Después de la caja de cada patrón, un párrafo «Alternativas, beneficios y costos» compara el patrón con la alternativa que se descartó y evalúa acoplamiento, extensión y complejidad: Composite contra recorrer las certificaciones tipo por tipo, Observer contra llamadas directas desde los modelos, Strategy contra un condicional en el Planner y MAPE-K contra una tarea programada por regla.

## Testing estructural

- [x] **test-0. Unidad, especificación y dominio de entrada definidos.** 10.5.10, «Pruebas de caja blanca», «Unidad bajo prueba»: el método `evaluate` de `Monitoring::Rules::CertificationExpiry` (regla de vencimiento de certificaciones de CU-003), con entradas y salidas esperadas concretas. Las fichas de caja negra de 10.5.10 traen datos de entrada, pasos, resultado esperado y obtenido.
- [x] **test-1. Grafo de flujo de control construido.** Fig. 111: 17 nodos, 23 aristas y 7 decisiones, cada nodo con su línea del código; complejidad ciclomática V(G) = 8 calculada por tres métodos.
- [x] **test-2. Criterio de cobertura declarado.** 10.5.10: caminos básicos más cobertura de ramas; la condición compuesta se separa en dos decisiones y el ciclo sobre los umbrales se recorre con 0, 1, 2 y 3 iteraciones.
- [x] **test-3. Conjunto de pruebas satisface el criterio.** Tabla «Caminos independientes»: 7 caminos factibles, que recorren las 23 aristas, con su entrada, la salida esperada y la prueba que lo ejecuta; el octavo camino del conjunto básico se justifica como infactible.
- [x] **test-4. Cobertura medida y evidencia adjunta.** 10.5.10, «Cobertura medida y ambiente»: SimpleCov da 34 de 34 líneas y 16 de 16 ramas del archivo bajo prueba.
- [x] **test-5. Casos normales, límites y fallas incluidos.** 21 pruebas de caja blanca: 7 de caminos, 9 de límites a ambos lados de los umbrales de 90, 30 y 7 días y del vencimiento, y 5 de falla (tabla «Casos de límite y de falla»).
- [x] **test-6. Pruebas re-ejecutables y resultado registrado.** 10.5.10, «Cobertura medida y ambiente»: commit, versiones de Ruby, Rails, PostgreSQL, SimpleCov y RSpec, comando de ejecución, fecha (25/11/2026) y resultado (21 pruebas sin fallas).
- [x] **test-7. Trazabilidad hasta TEST comprobada.** La matriz REQ → CU → TEST (10.4.2.6) vincula los 40 requerimientos con su prueba: una ficha de caso de prueba, un spec del backend o una de las pruebas PE-01 a PE-06 de «Pruebas de los requerimientos no funcionales y de entorno» (10.5.10), cada una con su procedimiento, su resultado y su fecha. No queda ningún requerimiento sin prueba.
