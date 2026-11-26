# Aeromentor — Trabajo Final de Ingeniería

- **Alumno:** Franco Pignatelli
- **Legajo:** B00064378-T1
- **Carrera:** Ingeniería en Sistemas Informáticos
- **Sede:** UAI Regional Rosario (campus 120)
- **Comisión:** Turno Noche, letra A

## Documento

- [Franco_Pignatelli_E3_02.02.pdf](Franco_Pignatelli_E3_02.02.pdf): documento final, versión 02.02 (378 páginas).
- [Franco_Pignatelli_E3_02.02.docx](Franco_Pignatelli_E3_02.02.docx): el mismo documento en formato editable.
- [seguimiento-checklist.md](seguimiento-checklist.md): recorrido de los 59 ítems del checklist del curso, con la sección y la figura del documento donde se cumple cada uno.
- [diagramas/](diagramas/): fuentes PlantUML de los diagramas del documento (casos de uso, dominio, robustez, actividad, entidad relación, secuencia, clases, patrones, arquitectura, bocetos y mapa de navegación) y el grafo de flujo de control de la prueba de caja blanca (`caja-blanca-cfg.dot`). Todos usan el estilo común `estilo.iuml`.

## Descripción de la versión

Primera entrega por pull request. Corresponde a la versión 02.02 del documento. La 02.00 reorganizó la solución tecnológica (capítulo 10) según la guía vigente y el método ICONIX:

- Requerimientos en cinco tipos, con criterio de aceptación y matriz de trazabilidad REQ → CU → TEST.
- Cuatro casos de uso core con IA, especificados en 17 sub-casos: evaluación pre-vuelo (CU-001), planificación de navegación (CU-002), monitoreo del cumplimiento operativo como lazo MAPE-K (CU-003) y registro de certificaciones por lectura automática de documentos (CU-004).
- Modelo de dominio, prototipo (bocetos y capturas), robustez, actividad, secuencia, clases con ocultamiento de información, patrones de diseño (Composite, Observer, Strategy y MAPE-K por analogía), arquitectura en componentes y conectores, y modelo de datos con su diccionario.
- Casos de prueba de caja negra, prueba de caja blanca con cobertura medida, pruebas de los requerimientos no funcionales y de entorno, y auditoría de seguridad del backend.

La 02.01 clasifica por categoría los requerimientos no funcionales y suma los de desempeño y de portabilidad, agrega las pruebas de los requerimientos no funcionales y de entorno con las que la matriz de trazabilidad queda completa, y documenta las alternativas, los beneficios y los costos de cada patrón de diseño. La 02.02 registra en la tabla «Revisiones» de la ficha de seguimiento la revisión de interesados de la 02.01: el Jefe de Instructores del Círculo de Aviación revisó el prototipo, los casos de uso y los requerimientos, y un ingeniero en sistemas revisó el diseño; los dos la aprobaron sin observaciones.

El sistema está desplegado en https://aeromentor.com.ar.
