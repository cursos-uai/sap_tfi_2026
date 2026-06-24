# CU-ENT-004 — Validar Entrega

## Nombre

**Validar Entrega de Productos**

## Objetivo

El operario de almacén confirma la salida física de los productos del almacén, completando el picking y actualizando el stock cuantitativo.

## Pre-condición

- El picking está en estado `assigned` o `partially_available`.
- Las cantidades reservadas o a entregar son válidas.

## Post-condición

- El estado del picking cambia a `done`.
- El stock cuantitativo (`stock.quant`) se actualiza con las cantidades entregadas.
- Se crea un backorder si hay cantidades pendientes (opcional).

## Pasos trascendentes (camino feliz, en voz activa)

1. El operario **presiona** "Validar" en el form del picking.
2. El sistema **invoca** `button_validate()`.
3. El sistema **abre** el wizard de validación inmediata (`stock.immediate.transfer`).
4. El operario **confirma** las cantidades reales entregadas.
5. El sistema **actualiza** `stock.move` con las cantidades reales.
6. El sistema **crea** `stock.move.line` definitivos.
7. El sistema **actualiza** el stock cuantitativo en `stock.quant`.
8. El sistema **cambia** el estado del picking a `done`.
9. El sistema **muestra** el resultado al operario.

## Caminos alternativos (en voz activa)

### FA-01 — El operario hace entrega parcial (extiende CU-ENT-004-BACK)

1. El operario **confirma** cantidades menores a las reservadas.
2. El sistema **crea** un nuevo picking (backorder) con las cantidades pendientes.
3. El sistema **completa** el picking original con las cantidades entregadas.
4. El sistema **deja** el backorder en estado `assigned` o `confirmed`.
5. El operario **procesa** el backorder posteriormente.

### FA-02 — El sistema crea la factura automáticamente

1. El sistema **detecta** que está configurada la facturación automática al validar.
2. El sistema **invoca** `_create_invoices()` desde el picking.
3. El sistema **crea** la factura (`account.move`).
4. El sistema **vincula** la salida de stock con la factura.

### FA-03 — El sistema valida sin wizard

1. El operario **presiona** "Validar" sin necesidad de wizard (configuración).
2. El sistema **ejecuta** la validación directa.
3. El sistema **completa** el picking.

## Excepciones (en voz activa)

### EX-01 — La cantidad excede lo reservado

1. El operario **intenta** entregar más cantidad de la reservada.
2. El sistema **valida** y **rechaza** si excede.
3. El sistema **muestra** el error.

### EX-02 — El picking está en estado inválido

1. El picking está en estado `draft` o `cancel`.
2. El sistema **detecta** el estado inválido.
3. El sistema **impide** la validación.

## Reglas de negocio

- **RN-ENT-004**: Al validar, las cantidades reservadas pasan a `done`.
- **RN-ENT-005**: El backorder automático depende de `stock.backorder_confirmation_policy`.

## Relaciones con otros CU

- **<<extend>> CU-ENT-004-BACK**: Crea backorder cuando hay entrega parcial (opcional).

## Diagrama de robustez asociado

`diagrams/plantuml/d_rob_ven_001_crear_presupuesto.puml` (compartido conceptualmente; este CU no tiene ROB dedicado en la primera iteración)

## Verbos clave (para validar la voz activa)

| Verbo | Actor | Acción sobre |
|-------|-------|--------------|
| **presiona** | Operario | Botón "Validar" |
| **invoca** | Sistema | `button_validate()` |
| **abre** | Sistema | Wizard de validación |
| **confirma** | Operario | Cantidades reales |
| **actualiza** | Sistema | `stock.move`, `stock.quant` |
| **crea** | Sistema | `stock.move.line`, backorder, factura |
| **cambia** | Sistema | Estado del picking |
| **muestra** | Sistema | Resultado |
| **completa** | Sistema | Picking original |
| **deja** | Sistema | Backorder |
| **procesa** | Operario | Backorder |
| **detecta** | Sistema | Configuración de facturación |
| **vincula** | Sistema | Salida de stock con factura |
| **ejecuta** | Sistema | Validación directa |
| **intenta** | Operario | Entregar cantidad |
| **rechaza** | Sistema | Cantidad excedida |
| **impide** | Sistema | Validación |