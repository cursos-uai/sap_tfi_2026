# Trabajo Final — Regiardo, Manuel

- **Alumno:** Regiardo, Manuel
- **Comisión:** T1-23-47 — Trabajo Final de Ingeniería
- **Carrera:** Ingeniería en Sistemas Informáticos — Facultad de Tecnología Informática, UAI Rosario
- **Versión:** 1.0 (Tercera Entrega, 2.º cuatrimestre 2026).

## El proyecto

**DNDManager** es una plataforma para gestionar campañas de rol de mesa (Dungeons & Dragons): campañas, personajes, sesiones, notas, enemigos y reglas propias, con generación de diálogos de NPC asistida por IA. El documento es el Plan de Desarrollo Tecnológico: análisis del negocio y estratégico (cap. 1 a 9) y la solución tecnológica (cap. 10).

## Contenido

- `Regiardo_Manuel_TFI_1.0.pdf`: documento compilado de la versión 1.0.
- `Regiardo_Manuel_Seminario_1.0.pdf`: documento del Seminario compilado (`main.tex`), para consulta rápida.
- `documentation/regiardo_manuel/`: fuentes LaTeX propias (`main_tfi.tex` es el documento del TFI).
- `documentation/master/`: preámbulo y capítulos compartidos (necesarios para compilar).
- `documentation/assets/`: logos, imágenes y diagramas (PDF) usados por el documento.

Para compilar: `cd documentation/regiardo_manuel && pdflatex main_tfi.tex && biber main_tfi && pdflatex main_tfi.tex && pdflatex main_tfi.tex`.

## Cambios técnicos desde la versión 0.5

- **Carpeta técnica (cap. 10)** completa, con cinco casos de uso núcleo (CU-002-001, 004, 005, 006 y 007). Cada uno incluye ficha de especificación y diagramas de casos de uso, robustez, secuencia y clases.
- **Arquitectura:** diagrama de componentes, componente del servicio de diálogo de NPC y diagrama de dominio. El backend y la base de datos corren en contenedores LXC sobre Proxmox VE.
- **Patrones de diseño** documentados con problema, solución, alternativas y comparación canónica: Strategy, Decorator (overrides del conjunto de reglas) y Facade (proveedor de IA).
- **Requisitos, índice de casos de uso y glosario** técnicos.
- **Ficha de seguimiento y revisión** actualizada con las iteraciones hasta la 1.0.
- Pendientes declarados: prototipos de interfaz y especificación de casos de prueba estructurales (10.5.7).
