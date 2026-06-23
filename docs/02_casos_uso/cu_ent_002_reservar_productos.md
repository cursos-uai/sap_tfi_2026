# CU-ENT-002 — Reservar productos

## Objetivo

Reservar las cantidades pedidas de cada producto en el almacén, asegurando disponibilidad antes de la entrega.

## Alcance

Módulo `stock` de Odoo 19.0. Aplica al modelo `stock.picking`.

## Nivel

Primario (esencial para garantizar disponibilidad).

## Actor principal

Sistema (operador de inventario puede forzarlo manualmente).

## Actores secundarios

- Sistema de Odoo (acción automática al confirmar pedido de venta).

## Interesados

- Operador de inventario.
- Vendedor (necesita saber si hay stock).
- Cliente (recibe confirmación de entrega).

## Disparador

- Confirmación de un pedido de venta (CU-VEN-004) — sistema dispara automáticamente.
- Botón manual "Reservar" en el picking (interfaz de inventario).

## Precondiciones

- El picking está en estado `draft` o `waiting` o `confirmed`.
- Los productos tienen stock disponible o se puede conseguir (vía reglas de abastecimiento).

## Garantías mínimas

El sistema intenta reservar las cantidades; si no puede, deja el picking en `partially_available` o `confirmed`.

## Garantías de éxito

- Estado del picking: `assigned`.
- Las cantidades reservadas se reflejan en `stock.move.line` con `reserved_availability`.

## Flujo principal

1. Sistema invoca `action_assign()` sobre el picking (ver `addons/stock/models/stock_picking.py:1195`).
2. Sistema busca cantidades disponibles por cada línea.
3. Si hay stock disponible, sistema crea `stock.move.line` con `product_qty = reserved_availability`.
4. Si NO hay stock, sistema busca reglas de reabastecimiento (MTO, MTS, etc.).
5. Si se reabastece, sistema programa una orden de compra.
6. Si nada funciona, sistema deja el picking en estado `partially_available`.
7. Estado del picking cambia a `assigned` cuando todas las líneas tienen reserva.

## Flujos alternativos

### FA-01 — Reserva parcial

1. Sistema reserva parte de las cantidades.
2. Líneas con reserva quedan con `assigned`.
3. Líneas sin reserva quedan con `partially_available`.
4. El picking NO cambia a `assigned` global.

### FA-02 — Backorder automático

1. Al validar (CU-ENT-004), si hay líneas pendientes, sistema crea un nuevo picking con backorder.

## Excepciones

### EX-01 — Sin stock y sin regla de reabastecimiento

1. Sistema no encuentra stock ni reglas aplicables.
2. Sistema deja el picking en `partially_available` o `confirmed`.
3. Operador debe decidir acción manual.

## Reglas de negocio

- **RN-ENT-002**: La reserva no afecta disponibilidad para otros pedidos hasta que se confirme el picking.
- **RN-ENT-003**: Las reservas se liberan automáticamente al cancelar el pedido o el picking.

## Datos de entrada

- Picking con líneas (`stock.move`).

## Datos de salida

- Stock.move.line con reservas.
- Estado del picking actualizado.
- Posibles órdenes de compra generadas.

## Estados involucrados

- `draft` → `confirmed` → `assigned` (reserva completa).
- `draft` → `confirmed` → `partially_available` (reserva parcial).

## Pantallas involucradas

- `view_picking_form` — form del picking.
- `view_stock_move_line_tree` — vista tree de movimientos reservados.

## Modelos de Odoo relacionados

- `stock.picking` (principal).
- `stock.move` (líneas del picking).
- `stock.move.line` (reservas).
- `stock.warehouse.orderpoint` (reglas de reabastecimiento).
- `procurement.order` (orden de compra generada).

## Métodos de Odoo relacionados

- `action_assign()` — entry point (ver `addons/stock/models/stock_picking.py:1195`).
- `action_confirm()` — confirma el picking (ver `addons/stock/models/stock_picking.py:1186`).

## Permisos requeridos

- `stock.group_stock_user` — para reservar.
- Sistema automático al confirmar pedido.

## Configuraciones relevantes

- Reglas de reabastecimiento (`stock.warehouse.orderpoint`).
- Política de stock (MTO, MTS, etc.).

## Casos de uso relacionados

- CU-VEN-004 Confirmar pedido de venta (disparador).
- CU-ENT-004 Validar entrega (siguiente paso).

## Criterios de aceptación

- [ ] Al confirmar un pedido, el picking cambia a `assigned` si hay stock.
- [ ] Si no hay stock, el picking queda en `partially_available`.
- [ ] Las reservas se reflejan en `stock.move.line`.

## Evidencias de ingeniería inversa

- **EV-COD-010**: `addons/stock/models/stock_picking.py:1195` — método `action_assign`.
- **EV-COD-011**: `addons/stock/models/stock_picking.py:1186` — método `action_confirm`.

## Supuestos y aspectos pendientes de validación

- **EV-INF-006**: La lógica interna de `action_assign()` (cómo busca stock, cómo aplica reglas de reabastecimiento) no fue leída en detalle. Solo se confirmó que existe.
- **EV-INF-007**: La integración con `procurement.order` requiere verificación adicional.