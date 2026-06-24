# CU-VEN-004 — Confirmar pedido de venta

## Objetivo

Confirmar un presupuesto, transformándolo de `draft`/`sent` a `sale` (Sales Order) y disparando el flujo downstream (reserva de stock, preparación, facturación).

## Alcance

Módulo `sale` de Odoo 19.0. Aplica al modelo `sale.order`.

## Nivel

Primario (esencial — dispara todo el flujo operativo).

## Actor principal

Vendedor o Responsable de ventas (usuario con permisos `sales_team.group_sale_salesman` o `sales_team.group_sale_manager`).

## Actores secundarios

- Sistema de stock (reserva cantidades).
- Sistema de cuenta (crea factura al confirmar).

## Interesados

- Operador de inventario (debe preparar pedidos).
- Responsable de facturación (debe emitir facturas).
- Administración (visualiza pipeline confirmado).

## Disparador

El vendedor hace clic en "Confirmar" en la vista form del pedido.

## Precondiciones

- El pedido está en estado `draft` o `sent`.
- Cada línea tiene un `product_id` definido (validado por `_confirmation_error_message()`).
- El cliente tiene una dirección de entrega válida.
- Si `sale.group_auto_done_setting` está activo, el pedido se lockea automáticamente al confirmar.

## Garantías mínimas

El sistema cambia el estado del pedido de `draft`/`sent` a `sale` o muestra un error explicativo.

## Garantías de éxito

- Estado del pedido: `sale`.
- `date_order` queda con la fecha/hora actual.
- Si `sale.group_auto_done_setting` está activo, el pedido queda `locked=True`.
- Se ejecutan los efectos downstream (`_action_confirm`): reserva de stock, programación de entregas.

## Flujo principal

1. Vendedor hace clic en "Confirmar" → sistema invoca `action_confirm()`.
2. Sistema valida cada pedido con `_confirmation_error_message()`:
   - Si el estado no es `draft` o `sent`, retorna error.
   - Si alguna línea no tiene `product_id`, retorna error.
3. Si pasa validación, sistema prepara valores con `_prepare_confirmation_values()`:
   - `state = 'sale'`
   - `date_order = fields.Datetime.now()`
4. Sistema escribe esos valores con `self.write(...)`.
5. Sistema llama a `self.with_context(context)._action_confirm()` que dispara el flujo downstream.
6. Si `sale.group_auto_done_setting` está activo, sistema invoca `action_lock()` sobre los pedidos filtrados.
7. Si el contexto trae `send_email=True`, sistema envía email de confirmación.
8. Retorna `True`.

## Flujos alternativos

### FA-01 — Confirmación masiva

1. Vendedor selecciona múltiples presupuestos desde vista tree.
2. Hace clic en "Confirmar" (acción masiva).
3. Sistema itera sobre cada pedido y aplica el flujo principal.
4. Si alguno falla, sistema retorna UserError con el mensaje del primer pedido que falló.

### FA-02 — Lock automático

1. Sistema detecta que `sale.group_auto_done_setting` está activo.
2. Después de confirmar, llama a `action_lock()`.
3. Pedido queda `locked=True`, no se puede modificar.

## Excepciones

### EX-01 — Estado inválido

1. El pedido está en estado `sale` o `cancel`.
2. Sistema retorna `_("Some orders are not in a state requiring confirmation.")`.

### EX-02 — Líneas sin producto

1. Alguna línea tiene `display_type` vacío y `is_downpayment=False` y `product_id` vacío.
2. Sistema retorna `_("Some order lines are missing a product, you need to correct them before going further.")`.

## Reglas de negocio

- **RN-VEN-004**: Solo se puede confirmar un pedido en estado `draft` o `sent`.
- **RN-VEN-005**: Toda línea debe tener un producto antes de confirmar.
- **RN-VEN-006**: Al confirmar, se dispara el flujo de stock (CU-ENT-002) y luego de cuenta (CU-FAC-001).

## Datos de entrada

- Pedido en estado `draft` o `sent`.
- Contexto opcional: `send_email=True` (envía email de confirmación).

## Datos de salida

- Pedido en estado `sale`.
- Reservas de stock (CU-ENT-002).
- Programación de entregas (CU-ENT-004).

## Estados involucrados

- `draft` → `sale` (transición principal).
- `sent` → `sale` (transición alternativa).
- Opcionalmente `locked=True` si `sale.group_auto_done_setting` está activo.

## Pantallas involucradas

- `view_sale_order_form` — botón "Confirmar" en el header del form.

## Modelos de Odoo relacionados

- `sale.order` (principal).
- `sale.order.line` (líneas validadas).
- `stock.picking` (entregas generadas).
- `account.move` (facturas generadas).

## Métodos de Odoo relacionados

- `action_confirm()` — entry point (ver `addons/sale/models/sale_order.py:1166`).
- `_confirmation_error_message()` — valida (ver `addons/sale/models/sale_order.py:1203`).
- `_prepare_confirmation_values()` — prepara valores (ver `addons/sale/models/sale_order.py:1218`).
- `_action_confirm()` — lógica de confirmación (interno, dispara stock y cuenta).
- `_should_be_locked()` — determina si lockea (ver `addons/sale/models/sale_order.py:1198`).
- `action_lock()` — lockea el pedido.

## Permisos requeridos

- `sales_team.group_sale_salesman` (puede confirmar sus propios pedidos).
- `sales_team.group_sale_manager` (puede confirmar cualquier pedido).

## Configuraciones relevantes

- `sale.group_auto_done_setting` — si está activo, lockea automáticamente al confirmar.

## Casos de uso relacionados

- CU-VEN-001 Crear presupuesto (precondición).
- CU-ENT-002 Reservar productos (downstream).
- CU-FAC-001 Crear factura (downstream).

## Criterios de aceptación

- [ ] Un pedido en `draft` puede confirmarse si todas las líneas tienen producto.
- [ ] Un pedido sin productos en alguna línea muestra error claro.
- [ ] El estado cambia correctamente a `sale`.
- [ ] Si auto_done está activo, el pedido queda `locked=True`.
- [ ] Las reservas de stock se generan automáticamente.

## Evidencias de ingeniería inversa

- **EV-COD-006**: `addons/sale/models/sale_order.py:1166-1196` — método `action_confirm` completo.
  ```python
  def action_confirm(self):
      for order in self:
          error_msg = order._confirmation_error_message()
          if error_msg:
              raise UserError(error_msg)
      self.order_line._validate_analytic_distribution()
      self.write(self._prepare_confirmation_values())
      ...
      self.with_context(context)._action_confirm()
      self.filtered(lambda so: so._should_be_locked()).action_lock()
      ...
  ```
- **EV-COD-007**: `addons/sale/models/sale_order.py:1203-1216` — método `_confirmation_error_message` (validaciones).
- **EV-COD-008**: `addons/sale/models/sale_order.py:1218-1229` — método `_prepare_confirmation_values` (devuelve `{'state': 'sale', 'date_order': fields.Datetime.now()}`).
- **EV-COD-009**: `addons/sale/models/sale_order.py:1198-1201` — método `_should_be_locked` (chequea `sale.group_auto_done_setting`).

## Supuestos y aspectos pendientes de validación

- **EV-INF-004**: `_action_confirm()` (sin guion bajo prefijo público) es el método que dispara el flujo downstream de stock y cuenta. Su implementación interna no fue leída en detalle.
- **EV-INF-005**: El efecto sobre `stock.picking` y `account.move` se valida en CU-ENT-002 y CU-FAC-001 respectivamente.