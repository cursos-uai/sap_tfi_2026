# CU-VEN-001 — Crear presupuesto

## Objetivo

Crear un presupuesto de venta (sales quotation) para un cliente en estado `draft`.

## Alcance

Módulo `sale` de Odoo 19.0. Aplica al modelo `sale.order`.

## Nivel

Primario (esencial para el proceso de ventas).

## Actor principal

Vendedor (usuario con permisos `sales_team.group_sale_salesman`).

## Actores secundarios

- Cliente (consulta estado).
- Servicio de correo (envía presupuesto).

## Interesados

- Responsable de ventas (aprueba descuentos).
- Administración (visualiza pipeline).

## Disparador

El vendedor hace clic en "Nuevo" desde la vista kanban o tree de `sale.order`, o desde el menú Ventas → Presupuestos.

## Precondiciones

- El usuario tiene acceso al módulo `sale`.
- Existe al menos un cliente activo en `res.partner`.
- El catálogo de productos contiene productos publicables.
- La compañía del usuario tiene configurada la secuencia de presupuestos en `ir.sequence`.

## Garantías mínimas

El sistema crea un registro `sale.order` en estado `draft` sin errores.

## Garantías de éxito

- El presupuesto tiene un `name` único asignado por la secuencia `sale.order`.
- Los totales se calculan automáticamente con impuestos.
- Se puede confirmar el presupuesto (cambio de estado a `sale`).

## Flujo principal

1. Vendedor hace clic en "Nuevo" → sistema crea `sale.order` en estado `draft`.
2. Sistema asigna `name` con valor por defecto `_("New")` (será reemplazado por la secuencia al guardar).
3. Vendedor selecciona `partner_id` → sistema carga `pricelist_id` por defecto del cliente.
4. Vendedor agrega líneas en `sale.order.line` con productos.
5. Sistema calcula `amount_untaxed`, `amount_tax`, `amount_total` (método `_compute_amounts()`).
6. Vendedor hace clic en "Enviar por email" → sistema invoca `action_quotation_send()` que abre un wizard de email.
7. Estado cambia de `draft` a `sent` (al confirmar el envío).
8. Vendedor confirma → estado cambia a `sale` (ver CU-VEN-004).

## Flujos alternativos

### FA-01 — Aplicar descuento

1. Vendedor edita `discount` en una línea de `sale.order.line`.
2. Sistema recalcula el monto de la línea.
3. Si supera el descuento máximo permitido, sistema puede bloquear o notificar.

### FA-02 — Duplicar presupuesto

1. Vendedor selecciona un presupuesto existente y elige "Duplicar".
2. Sistema crea un nuevo `sale.order` copiando las líneas.
3. Estado del nuevo registro: `draft`.

## Excepciones

### EX-01 — Cliente sin dirección de entrega

1. Al intentar confirmar (estado `sale`), sistema valida que exista `partner_shipping_id`.
2. Si no existe, sistema muestra error "Configure la dirección de entrega".

### EX-02 — Líneas sin producto

1. Al confirmar, sistema valida que cada línea tenga `product_id`.
2. Si falta, sistema muestra error "Some order lines are missing a product".

## Reglas de negocio

- **RN-VEN-001**: `state` solo puede pasar de `draft` → `sent` → `sale`, o a `cancel`.
- **RN-VEN-002**: El campo `name` se genera automáticamente por la secuencia configurada en la compañía.
- **RN-VEN-003**: Descuentos mayores al 10% (configurable) pueden requerir aprobación.

## Datos de entrada

- Cliente (`partner_id`).
- Compañía (`company_id`).
- Moneda (`currency_id`).
- Lista de precios (`pricelist_id`, opcional).
- Líneas (`order_line` con productos).

## Datos de salida

- Registro `sale.order` persistido.
- Líneas `sale.order.line` relacionadas.
- Correo enviado (opcional).

## Estados involucrados

- `draft` (Quotation) — estado inicial.
- `sent` (Quotation Sent) — al enviar por email.
- `sale` (Sales Order) — al confirmar.
- `cancel` (Cancelled) — al cancelar.

## Pantallas involucradas

- `view_sale_order_form` — form principal (ver `addons/sale/views/sale_order_view.xml`).
- `view_sale_order_kanban` — vista kanban (ver mismo archivo).
- `view_sale_order_tree` — vista tree (listado).

## Modelos de Odoo relacionados

- `sale.order` (principal, `_name = 'sale.order'`).
- `sale.order.line` (líneas).
- `res.partner` (cliente).
- `product.product` (productos).
- `account.tax` (impuestos).
- `product.pricelist` (lista de precios).

## Métodos de Odoo relacionados

- `action_quotation_send()` — abre wizard de email (ver `addons/sale/models/sale_order.py:1067`).
- `action_confirm()` — confirma el pedido (ver `addons/sale/models/sale_order.py:1166`).
- `action_cancel()` — cancela el pedido (ver `addons/sale/models/sale_order.py:1324`).
- `_compute_amounts()` — calcula totales (ver `addons/sale/models/sale_order.py:513`).

## Permisos requeridos

- `sales_team.group_sale_salesman` — para crear y editar presupuestos.
- `sales_team.group_sale_manager` — para aprobar descuentos y confirmar pedidos.

## Configuraciones relevantes

- Política de facturación en `res.company` (`sale_order_template_id`).
- Secuencia de presupuestos en `ir.sequence` (`sale.order.template` o equivalente según versión).
- Configuración de descuentos máximos.

## Casos de uso relacionados

- CU-VEN-002 Modificar presupuesto.
- CU-VEN-003 Enviar presupuesto al cliente.
- CU-VEN-004 Confirmar pedido de venta.

## Criterios de aceptación

- [ ] El vendedor puede crear un presupuesto en menos de 5 clicks.
- [ ] El sistema valida la dirección de entrega antes de confirmar.
- [ ] El correo al cliente incluye el PDF del presupuesto.
- [ ] Los totales se calculan automáticamente.

## Evidencias de ingeniería inversa

- **EV-COD-001**: `addons/sale/models/sale_order.py:34-36` — definición de la clase `SaleOrder` con `_name = 'sale.order'`.
  ```python
  class SaleOrder(models.Model):
      _name = 'sale.order'
      _inherit = ['portal.mixin', 'product.catalog.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin', 'account.document.import.mixin']
      _description = "Sales Order"
  ```
- **EV-COD-002**: `addons/sale/models/sale_order.py:26-31` — definición de `SALE_ORDER_STATE`.
  ```python
  SALE_ORDER_STATE = [
      ('draft', "Quotation"),
      ('sent', "Quotation Sent"),
      ('sale', "Sales Order"),
      ('cancel', "Cancelled"),
  ]
  ```
- **EV-COD-003**: `addons/sale/models/sale_order.py:1067` — método `action_quotation_send`.
- **EV-COD-004**: `addons/sale/models/sale_order.py:1166` — método `action_confirm`.
- **EV-COD-005**: `addons/sale/models/sale_order.py:54-58` — campo `name` con default `_("New")`.

## Supuestos y aspectos pendientes de validación

- **EV-INF-001**: El wizard de email usa `mail.compose.message` (verificado por contexto en `action_quotation_send`).
- **EV-INF-002**: La secuencia `sale.order` puede variar según configuración de la compañía.
- **EV-INF-003**: La validación de descuento máximo depende de configuración que requiere verificación.