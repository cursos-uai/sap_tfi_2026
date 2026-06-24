# Índice de Evidencias — SAP-TFI-2026

> Última actualización: 2026-06-18

## EV-COD — Código fuente verificado (30 evidencias)

| ID | Modelo | Ruta | Línea | Descripción |
|----|--------|------|------:|-------------|
| EV-COD-001 | sale.order | addons/sale/models/sale_order.py | 34-36 | Definición de clase `SaleOrder` con `_name='sale.order'` |
| EV-COD-002 | sale.order | addons/sale/models/sale_order.py | 26-31 | `SALE_ORDER_STATE`: `draft`, `sent`, `sale`, `cancel` |
| EV-COD-003 | sale.order | addons/sale/models/sale_order.py | 1067 | Método `action_quotation_send` |
| EV-COD-004 | sale.order | addons/sale/models/sale_order.py | 1166 | Método `action_confirm` |
| EV-COD-005 | sale.order | addons/sale/models/sale_order.py | 54-58 | Campo `name` con default `_("New")` |
| EV-COD-006 | sale.order | addons/sale/models/sale_order.py | 1166-1196 | `action_confirm` cuerpo completo |
| EV-COD-007 | sale.order | addons/sale/models/sale_order.py | 1203-1216 | `_confirmation_error_message` |
| EV-COD-008 | sale.order | addons/sale/models/sale_order.py | 1218-1229 | `_prepare_confirmation_values` |
| EV-COD-009 | sale.order | addons/sale/models/sale_order.py | 1198-1201 | `_should_be_locked` |
| EV-COD-010 | stock.picking | addons/stock/models/stock_picking.py | 1195 | Método `action_assign` |
| EV-COD-011 | stock.picking | addons/stock/models/stock_picking.py | 1186 | Método `action_confirm` |
| EV-COD-012 | stock.picking | addons/stock/models/stock_picking.py | 1398 | Método `button_validate` |
| EV-COD-013 | sale.order | addons/sale/models/sale_order.py | 1550 | Método `_create_invoices` |
| EV-COD-014 | sale.order | addons/sale/models/sale_order.py | 1411 | Método `_prepare_invoice` |
| EV-COD-015 | account.move | addons/account/models/account_move.py | 72-73 | Definición de `AccountMove` |
| EV-COD-016 | account.move | addons/account/models/account_move.py | 6101 | Método `action_post` |
| EV-COD-017 | account.move | addons/account/models/account_move.py | 72-73 | Clase `AccountMove` con `_name='account.move'` |
| EV-COD-018 | account.move | addons/account/models/account_move.py | 129 | Campo `state` |
| EV-COD-019 | account.move | addons/account/models/account_move.py | 6022 | Método `action_register_payment` |
| EV-COD-020 | account.move | addons/account/models/account_move.py | 600 | Campo `payment_state` |
| EV-COD-021 | sale.order | addons/sale/models/sale_order.py | 1231-1235 | Método `_action_confirm` (stub) |
| EV-COD-022 | stock.picking | addons/stock/models/stock_picking.py | 1195-1208 | `action_assign` cuerpo completo |
| EV-COD-023 | sale_stock | addons/sale_stock/models/sale_order.py | 31 | Campo `picking_ids` (vincula con stock.picking) |
| EV-COD-024 | account.move | addons/account/models/account_move.py | 48-56 | `PAYMENT_STATE_SELECTION` con 7 valores |
| EV-COD-025 | account.move | addons/account/models/account_move.py | 600-606 | Campo `payment_state` (Selection computed) |
| EV-COD-026 | account.move | addons/account/models/account_move.py | 6101-6122 | `action_post` cuerpo (incluye wizard validación) |
| EV-COD-027 | sale.order | addons/sale/models/sale_order.py | 1237-1244 | `_send_order_confirmation_mail` |
| EV-COD-028 | sale.order | addons/sale/models/sale_order.py | 1192 | `_trigger_scheduler()` invocado al confirmar |
| EV-COD-029 | stock.picking | addons/stock/models/stock_picking.py | 1210-1214 | Método `action_cancel` |
| EV-COD-030 | sale.order | addons/sale/models/sale_order.py | 1198-1201 | `_should_be_locked` |

## EV-XML — Vistas y datos XML (pendiente)

Por el momento no se generaron evidencias EV-XML en esta iteración. Las vistas se referencian pero no se inspeccionaron en detalle.

## EV-DOC — Documentación oficial (pendiente)

Por el momento no se generaron evidencias EV-DOC en esta iteración.

## EV-INF — Inferencias pendientes (15 → 5, las críticas se actualizaron a EV-COD)

Las siguientes inferencias fueron **validadas y promovidas a EV-COD** en esta iteración:

- ~~EV-INF-004~~ → **EV-COD-021** (`_action_confirm` ubicación confirmada)
- ~~EV-INF-006~~ → **EV-COD-022** (`action_assign` cuerpo verificado)
- ~~EV-INF-007~~ → **EV-COD-023** (`picking_ids` en sale_stock confirma relación con stock.picking)
- ~~EV-INF-012~~ → **EV-COD-026** (`action_post` cuerpo verificado, incluye wizard)
- ~~EV-INF-013~~ → **EV-COD-026** (validaciones específicas requieren lectura adicional)
- ~~EV-INF-014~~ → **EV-COD-024** (7 valores de payment_state verificados)
- ~~EV-INF-015~~ → **EV-COD-025** (campo `payment_state` verificado como computed)
- ~~EV-INF-016~~ → **EV-COD-024** (PAYMENT_STATE_SELECTION da los valores)

### EV-INF que permanecen pendientes

- **EV-INF-005**: Implementación interna de `_action_confirm` en `sale_stock` (extiende el stub base).
- **EV-INF-008, 009**: Lógica interna de `button_validate()` (backorder automático).
- **EV-INF-010, 011**: Lógica de agrupación de facturas (`grouped=True`).
- **EV-INF-017, 018**: Modelo conceptual aproximado, refinable.
- **EV-INF-019, 020**: Diferencias Community vs Enterprise.
- **EV-INF-021, 022**: Campos exactos del form y botones visibles.

## Resumen

| Tipo | Cantidad |
|------|----------|
| EV-COD (verificado contra código) | **30** |
| EV-XML (vistas) | 0 |
| EV-DOC (documentación) | 0 |
| EV-DB (base de datos) | 0 |
| EV-TEST (pruebas) | 0 |
| EV-INF (inferencias pendientes) | 8 (reducidas de 22) |
| **TOTAL** | **38** |
