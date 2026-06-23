# Prototipo: Formulario de Presupuesto

> Documento vivo. Última actualización: 2026-06-18.

## Pantalla

- **Nombre interno**: `view_sale_order_form`
- **XML ID**: `sale.view_sale_order_form`
- **Modelo**: `sale.order`
- **Tipo**: form (edición)
- **Actor principal**: Vendedor

## Objetivo

Permitir al vendedor crear y editar un presupuesto de venta.

## Campos visibles

### Header

- **Order Reference** (`name`): Char, requerido, readonly después de guardar.
- **Customer** (`partner_id`): Many2one a `res.partner`, requerido.
- **Salesperson** (`user_id`): Many2one a `res.users`, default = usuario actual.
- **Sales Team** (`team_id`): Many2one a `crm.team`.
- **Currency** (`currency_id`): Many2one a `res.currency`.
- **Pricelist** (`pricelist_id`): Many2one a `product.pricelist`.
- **Status** (`state`): Selection (`draft`, `sent`, `sale`, `cancel`), readonly.

### Tabs

#### Tab "Order Lines"

- **Order Lines** (`order_line`): One2many a `sale.order.line`.
  - **Product** (`product_id`): Many2one a `product.product`, requerido.
  - **Description** (`name`): Text.
  - **Quantity** (`product_uom_qty`): Float, default=1.
  - **Unit of Measure** (`product_uom`): Many2one a `uom.uom`.
  - **Unit Price** (`price_unit`): Float.
  - **Discount (%)** (`discount`): Float.
  - **Taxes** (`tax_id`): Many2many a `account.tax`.
  - **Subtotal** (`price_subtotal`): Monetary, readonly.

#### Tab "Other Information"

- **Sales Order Date** (`date_order`): Datetime.
- **Expiration Date** (`validity_date`): Date.
- **Quotation Template** (`sale_order_template_id`): Many2one a `sale.order.template`.
- **Source Document** (`origin`): Char.

### Totales (al pie del form)

- **Untaxed Amount** (`amount_untaxed`): Monetary, readonly.
- **Taxes** (`amount_tax`): Monetary, readonly.
- **Total** (`amount_total`): Monetary, readonly.

## Botones y acciones

- **Confirmar** (`action_confirm`): Solo visible si `state IN ('draft', 'sent')`. Cambia estado a `sale`.
- **Send by Email** (`action_quotation_send`): Abre wizard de email.
- **Cancel** (`action_cancel`): Solo visible si `state != 'cancel'`. Cambia estado a `cancel`.
- **Create Invoice** (`action_create_invoice` o `_create_invoices`): Solo visible si `state='sale'`.
- **Lock** (`action_lock`): Solo si `sale.group_auto_done_setting` activo.

## Estados que muestran/ocultan

| Estado | Botones visibles |
|--------|------------------|
| `draft` | Confirmar, Send, Cancel |
| `sent` | Confirmar, Send, Cancel |
| `sale` | Create Invoice, Cancel, Lock (si aplica) |
| `cancel` | (ninguno, solo lectura) |

## Reglas de visibilidad

- **Locked**: Si `locked=True`, todos los campos son readonly.
- **Cancelled**: Si `state='cancel'`, todos los campos son readonly.

## Modelo y vista relacionados

- **Modelo**: `sale.order` (ver `addons/sale/models/sale_order.py:34-36`).
- **Vista XML**: `addons/sale/views/sale_order_view.xml` (referencia al XML ID `sale.view_sale_order_form`).
- **Herencia de vista**: módulos como `sale_stock` agregan campos y pestañas adicionales.

## Prototipo visual (wireframe)

```
┌────────────────────────────────────────────────────────────────┐
│  Pedido de venta: SO001            Estado: [Borrador ▾]        │
├────────────────────────────────────────────────────────────────┤
│  Cliente: [ACME Corp ▾]    Vendedor: [Juan ▾]                  │
│  Equipo:  [Ventas ▾]       Moneda:  [USD ▾]                    │
├────────────────────────────────────────────────────────────────┤
│  [Líneas] [Otra información]                                       │
├────────────────────────────────────────────────────────────────┤
│  Producto       | Cant | UoM | Precio | Dto% | Impuestos | Sub  │
│  [Widget]       | 1.0  | u   | 100.00 | 0.0  | IVA 21%    | 100  │
│  [Widget]       | 2.0  | u   | 50.00  | 10.0 | IVA 21%    | 90.00│
│  + Agregar línea                                                     │
├────────────────────────────────────────────────────────────────┤
│  Subtotal:  $190.00                                                │
│  Impuestos: $39.90                                                 │
│  Total:     $229.90                                                │
├────────────────────────────────────────────────────────────────┤
│  [Confirmar]  [Enviar por email]  [Cancelar]                     │
└────────────────────────────────────────────────────────────────┘
```

## Diagrama PlantUML (Salt)

Ver `diagrams/plantuml/d_pro_ven_001_prototipo_presupuesto.puml`.

## Pendientes de validación

- **EV-INF-021**: Los campos exactos del form pueden variar según versión de Odoo y módulos instalados.
- **EV-INF-022**: Los botones visibles dependen de permisos del usuario.