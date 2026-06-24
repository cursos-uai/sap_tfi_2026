# Ejercicios Prácticos

## Objetivo

Estos ejercicios te ayudan a **fijar los conceptos** de ICONIX aplicados a Odoo. Trabajan sobre los artefactos reales de este proyecto.

## Antes de empezar

Asegurate de tener:
1. El código fuente de Odoo 19.0 clonado (en `~/proyectos/odoo_src/odoo`).
2. Los CU de este proyecto (en `docs/02_casos_uso/`).
3. Un editor de texto y PlantUML instalados.

## Ejercicio 1: Validar una afirmación con código

**Objetivo**: entender el flujo de evidencia EV-COD.

**Tarea**:
1. Abrí el archivo `docs/02_casos_uso/cu_ven_001_crear_presupuesto.md`.
2. Buscá la evidencia `EV-COD-001`.
3. Abrí el archivo `addons/sale/models/sale_order.py` en `~/proyectos/odoo_src/odoo/`.
4. Andá a las líneas 34-36.
5. Verificá que el código realmente coincide con lo que dice la evidencia.

**Pregunta para responder**:
- ¿Qué patrón sigue la herencia de `SaleOrder`? ¿Por qué creés que se eligieron esos mixins?

## Ejercicio 2: Diferenciar modelo conceptual de técnico

**Objetivo**: entender por qué mantenemos dos diagramas separados.

**Tarea**:
1. Abrí `diagrams/plantuml/d_cla_con_gen_001_modelo_dominio.puml` (modelo conceptual).
2. Abrí `diagrams/plantuml/d_cla_int_001_integracion_ven_stock_cont.puml` (modelo técnico).
3. Compilá ambos con PlantUML: `java -jar plantuml.jar -tpdf archivo.puml`.
4. Compará los PDFs.

**Preguntas para responder**:
- ¿Qué conceptos están en el conceptual pero NO en el técnico? ¿Por qué?
- ¿Qué campos del técnico NO están en el conceptual? ¿Por qué?
- ¿Cuándo usarías uno y cuándo el otro?

## Ejercicio 3: Seguir un flujo de punta a punta

**Objetivo**: trazar el flujo completo del CU-VEN-001 al código real.

**Tarea**:
1. Abrí el CU-VEN-001 (`docs/02_casos_uso/cu_ven_001_crear_presupuesto.md`).
2. Abrí `diagrams/plantuml/d_sec_ven_001_crear_presupuesto.puml` (secuencia).
3. Compilá ambos y mirá los PDFs.
4. Para cada paso del flujo principal, identificá:
   - Qué archivo y método de Odoo se ejecuta.
   - Qué tabla de BD se modifica.
   - Qué evidencia (EV-COD) lo respalda.

**Output esperado**: una tabla con columnas `Paso | Método Odoo | Tabla BD | Evidencia`.

## Ejercicio 4: Crear un CU nuevo

**Objetivo**: aplicar ICONIX para agregar un caso que NO está en la primera iteración.

**Tarea**: elegí UNO de los siguientes CU y documentalo siguiendo la plantilla:

### Opción A: CU-VEN-005 Cancelar pedido

**Contexto**: el vendedor necesita cancelar un pedido que ya estaba confirmado.

**Pasos**:
1. Leé CU-VEN-001 y CU-VEN-004 para entender el contexto.
2. Investigá el método `action_cancel()` en `addons/sale/models/sale_order.py:1324`.
3. Investigá también cómo `sale_stock` extiende la cancelación.
4. Escribí `docs/02_casos_uso/cu_ven_005_cancelar_pedido.md`.
5. Generá el diagrama de robustez y secuencia.
6. Generá EV-COD para cada afirmación.

### Opción B: CU-FAC-005 Emitir nota de crédito

**Contexto**: el facturador necesita revertir una factura publicada.

**Pasos**:
1. Investigá el flujo de notas de crédito en Odoo 19.
2. Buscá `_reverse_moves()` o `action_reverse()` en `addons/account/models/account_move.py`.
3. Documentá el CU.
4. Generá los diagramas y las evidencias.

### Opción C: CU-INV-001 Consultar existencias

**Objetivo**: el operador de inventario quiere ver cuántas unidades hay de un producto.

**Pasos**:
1. Investigá el modelo `stock.quant` en `addons/stock/models/stock_quant.py`.
2. Investigá cómo se accede desde el form de producto.
3. Documentá el CU.
4. Generá los diagramas y las evidencias.

## Ejercicio 5: Validar una EV-INF

**Objetivo**: cerrar el ciclo de evidencia.

**Tarea**:
1. Abrí `evidence/index.md`.
2. Elegí UNA EV-INF pendiente (ejemplo: EV-INF-008 sobre `button_validate`).
3. Buscá el código relevante en Odoo:
   - `grep -n "def button_validate" addons/stock/models/stock_picking.py`
   - Leé el método completo (~50 líneas).
4. Verificá si la inferencia es correcta.
5. Si es correcta: convertila en EV-COD con la ruta y línea exacta.
6. Si es incorrecta: marcala como obsoleta y proponé una EV-COD corregida.

## Ejercicio 6: Mejorar la trazabilidad

**Objetivo**: entender la matriz de trazabilidad.

**Tarea**:
1. Abrí `docs/09_trazabilidad/matriz_trazabilidad.md`.
2. Agregá una fila para CU-VEN-005 (cancelación).
3. Definí las relaciones:
   - ¿Qué reglas de negocio aplica?
   - ¿A qué modelo Odoo apunta?
   - ¿Qué evidencia EV-COD lo respalda?
4. Actualizá la matriz.

## Criterios de evaluación

| Criterio | Excelente | Aceptable | Necesita mejora |
|----------|-----------|------------|-----------------|
| Uso de evidencia | Cada afirmación tiene EV-COD con línea exacta | Algunas EV-INF | Muchas afirmaciones sin evidencia |
| Separación conceptual/técnico | Clara y justificada | Presente pero confusa | Mezclados |
| Compilabilidad PlantUML | Todos los .puml compilan sin error | Algunos fallan | Muchos fallan |
| Trazabilidad | Matriz completa y consistente | Algunas relaciones | Sin matriz |
| Aplicación de ICONIX | Las 9 fases reflejadas en artefactos | Algunas fases | Solo CU, sin resto |

## Recursos para profundizar

- **Libros**:
  - *Use Case Driven Object Modeling with UML* — Rosenberg & Scott.
  - *Applying UML and Patterns* — Craig Larman.
  - *OCA Odoo Development Essentials* — Daniel Reis (para Odoo técnico).

- **Sitios web**:
  - https://www.odoo.com/documentation/19.0/ — docs oficiales de Odoo 19.
  - https://github.com/odoo/odoo/tree/19.0 — código fuente.

- **Herramientas**:
  - PlantUML: https://plantuml.com/
  - Odoo CLI: https://www.odoo.com/documentation/19.0/administration/install/cli.html