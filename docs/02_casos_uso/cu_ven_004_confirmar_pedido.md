# CU-VEN-004 — Confirmar Pedido

## Nombre

**Confirmar Pedido de Venta**

## Objetivo

El vendedor transforma un presupuesto en estado `draft` o `sent` a un pedido de venta confirmado (`state='sale'`), disparando el flujo downstream de stock y facturación.

## Pre-condición

- El vendedor tiene sesión iniciada (`CU-AUTH-001`).
- El pedido está en estado `draft` o `sent`.
- Cada línea tiene un `product_id` definido.
- El cliente tiene una dirección de entrega válida (`partner_shipping_id`).

## Post-condición

- El pedido queda en estado `sale`.
- El campo `date_order` queda con la fecha/hora de confirmación.
- Si `sale.group_auto_done_setting` está activo, el pedido queda `locked=True`.
- Se generan las entregas (`stock.picking`) automáticamente.

## Pasos trascendentes (camino feliz, en voz activa)

1. El vendedor **presiona** "Confirmar" en el form del pedido.
2. El sistema **invoca** `action_confirm()`.
3. El sistema **valida** el pedido con `_confirmation_error_message()`.
4. El sistema **lee** el estado y las líneas del pedido.
5. El sistema **verifica** que cada línea tenga `product_id`.
6. Si todo está OK, el sistema **prepara** los valores de confirmación con `_prepare_confirmation_values()`.
7. El sistema **escribe** `state='sale'` y `date_order=now` en el pedido.
8. El sistema **dispara** `_action_confirm()` que **genera** los pickings de stock.
9. El sistema **genera** las entregas (`stock.picking`) con sus movimientos (`stock.move`).
10. El sistema **retorna** `True`.

## Caminos alternativos (en voz activa)

### FA-01 — El vendedor confirma múltiples pedidos

1. El vendedor **selecciona** varios presupuestos desde la vista tree.
2. El vendedor **presiona** "Confirmar" (acción masiva).
3. El sistema **itera** sobre cada pedido.
4. Para cada pedido, el sistema **ejecuta** los pasos trascendentes.
5. Si alguno falla, el sistema **muestra** el error del primer pedido que falló.

### FA-02 — El sistema lockea el pedido automáticamente

1. El sistema **detecta** que `sale.group_auto_done_setting` está activo.
2. Después de confirmar, el sistema **invoca** `action_lock()` sobre los pedidos filtrados.
3. El sistema **marca** `locked=True` en el pedido.
4. El sistema **impide** modificaciones futuras.

### FA-03 — El sistema envía email de confirmación

1. El sistema **detecta** que el contexto trae `send_email=True`.
2. El sistema **invoca** `_send_order_confirmation_mail()`.
3. El sistema **busca** el template de email de confirmación.
4. El sistema **envía** el email al cliente.

## Excepciones (en voz activa)

### EX-01 — El pedido está en estado inválido

1. El pedido está en estado `sale` o `cancel`.
2. El sistema **detecta** el estado inválido.
3. El sistema **muestra** el error "Some orders are not in a state requiring confirmation".

### EX-02 — Alguna línea no tiene producto

1. Alguna línea tiene `display_type` vacío, `is_downpayment=False` y `product_id` vacío.
2. El sistema **detecta** la línea inválida.
3. El sistema **muestra** el error "Some order lines are missing a product".

## Reglas de negocio

- **RN-VEN-004**: Solo se puede confirmar un pedido en estado `draft` o `sent`.
- **RN-VEN-005**: Toda línea debe tener un producto antes de confirmar.
- **RN-VEN-006**: Al confirmar, se dispara el flujo de stock (CU-ENT-002).

## Relaciones con otros CU

- **<<include>> CU-AUTH-001**: Valida la sesión.
- **<<include>> CU-GENPICK-001**: Genera los pickings de entrega.

## Diagrama de robustez asociado

`diagrams/plantuml/d_rob_ven_004_confirmar_pedido.puml`

## Verbos clave (para validar la voz activa)

| Verbo | Actor | Acción sobre |
|-------|-------|--------------|
| **presiona** | Vendedor | Botón "Confirmar" |
| **invoca** | Sistema | `action_confirm()` |
| **valida** | Sistema | `_confirmation_error_message()` |
| **lee** | Sistema | Estado y líneas |
| **verifica** | Sistema | `product_id` por línea |
| **prepara** | Sistema | `_prepare_confirmation_values()` |
| **escribe** | Sistema | `state='sale'`, `date_order` |
| **dispara** | Sistema | `_action_confirm()` |
| **genera** | Sistema | `stock.picking`, `stock.move` |
| **retorna** | Sistema | `True` |
| **iterar** | Sistema | Lista de pedidos |
| **detecta** | Sistema | Estado / configuración |
| **marca** | Sistema | `locked=True` |
| **impide** | Sistema | Modificaciones |
| **busca** | Sistema | Template de email |
| **envía** | Sistema | Email de confirmación |
| **muestra** | Sistema | Error |