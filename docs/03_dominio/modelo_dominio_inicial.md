# Modelo de Dominio Inicial

> Documento vivo. Última actualización: 2026-06-18.

## Conceptos del dominio

Estos son los conceptos funcionales identificados a partir del análisis de Odoo 19.0. Se mantienen separados de las clases técnicas de Odoo.

### Cliente (`Customer`)

- **Definición**: Persona o empresa que compra productos o servicios.
- **Correspondencia técnica**: `res.partner` (con `is_company=True` para empresas).
- **Atributos clave**: nombre, dirección, contacto, lista de precios, condición de pago.
- **Evidencia**: módulo `contacts` en `addons/contacts/`.

### Producto (`Product`)

- **Definición**: Bien o servicio que se vende.
- **Correspondencia técnica**: `product.template` + `product.product`.
- **Atributos clave**: nombre, descripción, precio, costo, impuestos, categoría.
- **Evidencia**: módulo `product` en `addons/product/`.

### Lista de precios (`Price List`)

- **Definición**: Conjunto de precios para productos en función de la moneda, el país y el período.
- **Correspondencia técnica**: `product.pricelist`.
- **Evidencia**: ver `addons/product/models/product_pricelist.py`.

### Impuesto (`Tax`)

- **Definición**: Regla fiscal aplicada a las ventas.
- **Correspondencia técnica**: `account.tax`.
- **Evidencia**: ver `addons/account/models/account_tax.py`.

### Presupuesto (`Quotation`)

- **Definición**: Oferta de venta en estado `draft` o `sent`, previa al pedido confirmado.
- **Correspondencia técnica**: `sale.order` con `state IN ('draft', 'sent')`.
- **Atributos clave**: nombre, cliente, líneas, totales, fechas.
- **Estado actual**: `draft` (Quotation), `sent` (Quotation Sent).
- **Evidencia**: `addons/sale/models/sale_order.py:26-31` (definición de `SALE_ORDER_STATE`).

### Pedido de venta (`Sales Order`)

- **Definición**: Pedido confirmado (`state='sale'`) que activa el flujo operativo.
- **Correspondencia técnica**: `sale.order` con `state='sale'`.
- **Atributos clave**: idem presupuesto + fecha de confirmación + estado de facturación + estado de entrega.
- **Evidencia**: `addons/sale/models/sale_order.py:34-36` (clase `SaleOrder`).

### Línea de pedido (`Order Line`)

- **Definición**: Línea de producto dentro de un presupuesto o pedido.
- **Correspondencia técnica**: `sale.order.line`.
- **Atributos clave**: producto, cantidad, precio unitario, descuento, subtotal, impuesto.
- **Evidencia**: ver `addons/sale/models/sale_order_line.py`.

### Transferencia (`Delivery`)

- **Definición**: Movimiento físico de productos del almacén al cliente.
- **Correspondencia técnica**: `stock.picking`.
- **Atributos clave**: líneas de movimiento, estado, cantidad reservada/entregada.
- **Evidencia**: ver `addons/stock/models/stock_picking.py`.

### Línea de transferencia (`Move Line`)

- **Definición**: Línea de producto dentro de una transferencia, con cantidad reservada y entregada.
- **Correspondencia técnica**: `stock.move` (movimiento) y `stock.move.line` (reservas).
- **Evidencia**: ver `addons/stock/models/stock_move.py` y `addons/stock/models/stock_move_line.py`.

### Factura (`Invoice`)

- **Definición**: Documento contable que registra una venta.
- **Correspondencia técnica**: `account.move` con `move_type='out_invoice'`.
- **Atributos clave**: número, fecha, cliente, líneas, totales, impuestos, estado de pago.
- **Estado actual**: `draft`, `posted`, `cancel`.
- **Evidencia**: `addons/account/models/account_move.py:72-73` (clase `AccountMove`).

### Línea de factura (`Invoice Line`)

- **Definición**: Línea de producto dentro de una factura.
- **Correspondencia técnica**: `account.move.line`.
- **Atributos clave**: producto, cantidad, precio, impuestos, cuenta contable.
- **Evidencia**: ver `addons/account/models/account_move_line.py`.

### Pago (`Payment`)

- **Definición**: Registro de un cobro aplicado a una factura.
- **Correspondencia técnica**: `account.payment`.
- **Atributos clave**: fecha, monto, diario, método de pago, factura relacionada.
- **Evidencia**: ver `addons/account/models/account_payment.py`.

### Almacén (`Warehouse`)

- **Definición**: Lugar físico donde se almacenan productos.
- **Correspondencia técnica**: `stock.warehouse`.
- **Evidencia**: ver `addons/stock/models/stock_warehouse.py`.

### Ubicación (`Location`)

- **Definición**: Posición específica dentro de un almacén.
- **Correspondencia técnica**: `stock.location`.
- **Evidencia**: ver `addons/stock/models/stock_location.py`.

## Diagrama del modelo de dominio

Ver `diagrams/plantuml/d_cla_con_gen_001_modelo_dominio.puml`.

## Reglas de negocio del dominio

- **RN-DOM-001**: Un Cliente puede tener muchos Pedidos de venta.
- **RN-DOM-002**: Un Pedido de venta tiene muchas Líneas de pedido.
- **RN-DOM-003**: Un Pedido de venta confirmado genera una o más Transferencias.
- **RN-DOM-004**: Una Transferencia genera cero o más Reservas (Líneas de transferencia).
- **RN-DOM-005**: Un Pedido de venta genera una o más Facturas.
- **RN-DOM-006**: Una Factura tiene muchas Líneas de factura.
- **RN-DOM-007**: Una Factura puede tener muchos Pagos (pagos parciales).
- **RN-DOM-008**: Un Producto pertenece a una o más Categorías.
- **RN-DOM-009**: Una Línea de pedido referencia un Producto y aplica Impuestos.

## Pendientes de validación

- **EV-INF-017**: Las correspondencias técnicas son aproximadas; algunas relaciones pueden ser más complejas (campos calculados, herencia, etc.).
- **EV-INF-018**: El modelo conceptual debe refinarse a medida que se descubran nuevos conceptos en iteraciones siguientes.