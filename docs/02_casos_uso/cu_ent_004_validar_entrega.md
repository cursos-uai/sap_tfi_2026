# CU-ENT-004 — Validar entrega

## Objetivo

Confirmar la salida física de los productos del almacén, completando el picking y disparando los efectos downstream (actualización de stock, facturación).

## Alcance

Módulo `stock` de Odoo 19.0. Aplica al modelo `stock.picking`.

## Nivel

Primario (esencial para cerrar el flujo de inventario).

## Actor principal

Operador de almacén (usuario con permisos `stock.group_stock_user` o `stock.group_stock_manager`).

## Actores secundarios

- Sistema de cuenta (puede disparar facturación al validar).

## Interesados

- Operador de almacén.
- Cliente (recibe productos).
- Responsable de facturación (recibe señal para facturar).

## Disparador

El operador hace clic en "Validar" en la vista form del picking.

## Precondiciones

- El picking está en estado `assigned` (con todas las reservas) o `partially_available` (parcial).
- Las cantidades reservadas o a entregar son válidas.

## Garantías mínimas

El sistema cambia el estado del picking a `done` o muestra un error explicativo.

## Garantías de éxito

- Estado del picking: `done`.
- Stock actualizado (las cantidades reservadas se descuentan del stock disponible).
- Posible creación automática de factura si está configurado.

## Flujo principal

1. Operador hace clic en "Validar" → sistema invoca `button_validate()` (ver `addons/stock/models/stock_picking.py:1398`).
2. Sistema muestra wizard de validación con cantidades (permite ajustar).
3. Operador confirma las cantidades reales entregadas.
4. Sistema actualiza `stock.move` con las cantidades reales.
5. Sistema crea `stock.move.line` definitivos.
6. Sistema actualiza el stock cuantitativo (`stock.quant`).
7. Estado del picking cambia a `done`.

## Flujos alternativos

### FA-01 — Entrega parcial con backorder

1. Operador entrega solo una parte de las cantidades.
2. Sistema crea un nuevo picking (backorder) con las cantidades pendientes.
3. Picking original queda en `done` con las cantidades entregadas.
4. Backorder queda en `assigned` o `confirmed` para entrega posterior.

### FA-02 — Crear factura al validar

1. Si está configurado, al validar, sistema crea automáticamente una factura (`account.move`).
2. Esto vincula la salida de stock con la facturación inmediata.

## Excepciones

### EX-01 — Cantidad excede lo reservado

1. Operador intenta entregar más cantidad de la que está reservada.
2. Sistema valida y rechaza si excede.
3. Sistema muestra error claro.

### EX-02 — Picking no asignable

1. Picking en estado `draft` o `cancel`.
2. Sistema no permite validar.

## Reglas de negocio

- **RN-ENT-004**: Al validar, las cantidades reservadas pasan a `done`.
- **RN-ENT-005**: Backorder automático configurable vía `stock.backorder_confirmation_policy`.

## Datos de entrada

- Picking en estado `assigned` o `partially_available`.
- Cantidades reales (pueden diferir de las reservadas).

## Datos de salida

- Picking en `done`.
- Stock actualizado.
- Posible factura generada.

## Estados involucrados

- `assigned` → `done` (validación completa).
- `partially_available` → `done` (validación parcial, genera backorder).

## Pantallas involucradas

- `view_picking_form` — botón "Validar".
- `view_stock_immediate_transfer` — wizard de validación.

## Modelos de Odoo relacionados

- `stock.picking` (principal).
- `stock.move` (movimientos).
- `stock.move.line` (líneas definitivas).
- `stock.quant` (stock cuantitativo actualizado).
- `stock.backorder.confirmation` (wizard de backorder).

## Métodos de Odoo relacionados

- `button_validate()` — entry point (ver `addons/stock/models/stock_picking.py:1398`).

## Permisos requeridos

- `stock.group_stock_user` (puede validar pickings simples).
- `stock.group_stock_manager` (puede validar pickings complejos o cancelar reservas).

## Configuraciones relevantes

- `stock.backorder_confirmation_policy` — política de backorder.
- `stock.move.auto_fill` — auto-llenar cantidades.

## Casos de uso relacionados

- CU-ENT-002 Reservar productos (precondición).
- CU-FAC-001 Crear factura (downstream, opcional).

## Criterios de aceptación

- [ ] Al validar un picking completo, el stock se descuenta correctamente.
- [ ] Al validar parcialmente, se crea un backorder automático.
- [ ] El estado del picking cambia a `done`.

## Evidencias de ingeniería inversa

- **EV-COD-012**: `addons/stock/models/stock_picking.py:1398` — método `button_validate`.

## Supuestos y aspectos pendientes de validación

- **EV-INF-008**: La lógica interna de `button_validate()` (cómo ajusta cantidades, cómo crea backorder) no fue leída en detalle.
- **EV-INF-009**: La integración con facturación automática al validar requiere verificación.