# ¿Qué es ICONIX?

## Definición

**ICONIX** es una metodología de ingeniería de software orientada a objetos que se sitúa entre los métodos ágiles (como XP o Scrum) y los métodos pesados (como el Proceso Unificado Rational — RUP). Fue desarrollada por **Doug Rosenberg** y **Kendall Scott** a principios de los 90, y refinada en sucesivas ediciones de su libro *Use Case Driven Object Modeling with UML*.

A diferencia de RUP o del método del Proceso Unificado, ICONIX **no se obsesiona con la documentación exhaustiva**, pero tampoco cae en el "codificar sin diseño" del agilismo extremo. En su lugar, propone un **camino mínimo y práctico** desde los requisitos hasta el código, usando UML como lenguaje común.

## Las 9 fases de ICONIX

A pesar de su nombre, ICONIX tiene 9 fases (no 3). El "IX" del nombre se refiere a "eXtremidad", porque el método es "extremo" en su enfoque minimalista: solo lo esencial, sin ceremonias.

```text
Requisitos
    ↓
Casos de uso (texto + diagrama)
    ↓
Modelo de dominio (conceptos del negocio)
    ↓
Prototipos de interfaz (bocetos de pantallas)
    ↓
Análisis de robustez (¿qué objetos intervienen?)
    ↓
Actualización del modelo de dominio
    ↓
Diagramas de secuencia (interacciones en el tiempo)
    ↓
Diagramas de clases (estructura del sistema)
    ↓
Validación de coherencia
```

Cada fase **alimenta** a la siguiente y mantiene **trazabilidad** con las anteriores. No se salta ninguna.

## El flujo en detalle

### Fase 1: Requisitos

- Identificar **qué** tiene que hacer el sistema.
- Recopilar requisitos funcionales y no funcionales.
- Identificar **actores** (humanos y sistemas externos).
- Producto: documento de requisitos (puede ser informal).

### Fase 2: Casos de uso

- Para cada objetivo del actor, escribir un **caso de uso**.
- Cada CU tiene: nombre, objetivo, precondiciones, flujo principal, flujos alternativos, excepciones.
- Producto: tabla de CU + **diagrama de CU** (UML).

### Fase 3: Modelo de dominio

- Identificar **conceptos del negocio**, no de la solución.
- Conceptos como: Cliente, Producto, Pedido, Factura, Pago.
- No incluir campos técnicos, solo atributos del dominio.
- Producto: **diagrama de clases conceptual**.

### Fase 4: Prototipos de interfaz

- Bocetos de las pantallas principales.
- No incluir detalles visuales, solo estructura.
- Mostrar campos, botones, navegación.
- Producto: wireframes o mockups.

### Fase 5: Análisis de robustez

- Para cada CU, identificar **qué objetos intervienen**.
- Tres tipos de objetos:
  - **boundary** (vista, formulario, API)
  - **control** (coordinador, validador)
  - **entity** (objeto persistente)
- Producto: **diagrama de robustez** por CU.

### Fase 6: Actualización del dominio

- Refinar el modelo de dominio con conceptos descubiertos en robustez.

### Fase 7: Diagramas de secuencia

- Para cada CU relevante, derivar la **secuencia temporal**.
- Mostrar interacciones entre actor, vistas, controles, entidades.
- Incluir transacciones, validaciones, errores.
- Producto: **diagrama de secuencia** por CU.

### Fase 8: Diagramas de clases

- **Conceptual**: conceptos del dominio (reutiliza el modelo de dominio).
- **Técnico**: clases reales del sistema, con sus campos y métodos.
- Producto: **dos diagramas de clases** por subsistema.

### Fase 9: Validación

- Verificar coherencia entre todos los artefactos.
- Cada CU debe tener su diagrama de robustez, secuencia y clases.
- Cada regla de negocio debe estar trazada.

## Reglas clave de ICONIX

1. **Trabajar desde los casos de uso hacia el diseño** (no al revés).
2. **Centrarse en objetivos del actor**, no en funciones del sistema.
3. **No describir detalles internos del código** en los CU.
4. **Usar robustez como puente** entre requisitos y diseño.
5. **Distinguir boundary, control, entity** explícitamente.
6. **Derivar operaciones de clase desde los mensajes de secuencia**.
7. **Mantener trazabilidad explícita** entre todos los artefactos.
8. **Actualizar el modelo de dominio** a medida que se descubre nueva información.

## Por qué ICONIX es ideal para ingeniería inversa

Cuando uno hace **ingeniería inversa** (analizar un sistema existente), ICONIX funciona muy bien porque:

- Los **diagramas de secuencia** que produce coinciden con los métodos reales del código.
- El **modelo de clases técnico** se construye leyendo el código, no inventando.
- La **trazabilidad** permite mapear cada artefacto a su evidencia en el código.

En este proyecto (SAP-TFI-2026), usamos ICONIX para **documentar** Odoo 19.0, no para **construirlo**. Cada afirmación tiene un código de evidencia que apunta a la línea exacta del código fuente.

## Diferencias con otros métodos

| Aspecto | ICONIX | RUP | Scrum |
|---------|--------|-----|-------|
| Rigurosidad | Media-alta | Muy alta | Baja |
| Documentación | Moderada | Exhaustiva | Mínima |
| UML | Sí, en el camino crítico | Sí, en todas las fases | No obligatorio |
| Casos de uso | Sí, centrales | Sí, conductores | Opcionales |
| Iterativo | Opcional | Sí | Sí |
| Tamaño del equipo | 1-5 personas | 5-30 personas | 3-9 personas |
| Tiempo por iteración | Semanas | Meses | Semanas |

## Recursos externos

- Libro original: *Use Case Driven Object Modeling with UML* (Rosenberg & Scott).
- Sitio oficial: http://www.iconixprocess.com/
- Resumen en español: https://es.wikipedia.org/wiki/ICONIX

## Próxima sección

→ [Aplicación a Odoo](02_aplicacion_a_odoo.md) — cómo se adaptó ICONIX específicamente para este proyecto.