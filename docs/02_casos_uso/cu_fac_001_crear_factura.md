# CU-FAC-001 — Crear factura desde pedido

## Objetivo

Generar una factura (`account.move`) basada en un pedido de venta confirmado, para registrar la venta en el sistema contable.

## Alcance

Módulo `sale` (Odoo 19.0) que invoca a `account` para crear la factura. Aplica al modelo `sale.order`.

## Nivel

Primario (esencial para el circuito contable).

## Actor principal

Responsable de facturación o sistema (acción automática configurable).

## Actores secundarios

- Vendedor (solicita facturación).
- Sistema contable (registra el asiento).

## Interesados

- Responsable de facturación.
- Contador (visualiza asientos).
- Cliente (recibe factura).

## Disparador

- Manual: vendedor o facturador hace clic en "Crear factura" en el pedido.
- Automático: al validar la entrega (CU-ENT-004), si está configurado.
- Automático: al alcanzar la política de facturación del pedido (`invoice_status`).

## Precondiciones

- El pedido está en estado `sale`.
- Hay productos a facturar (no todo está ya facturado).
- El cliente y la compañía tienen configurados los diarios contables.

## Garantías mínimas

El sistema crea un `account.move` en estado `draft` o muestra un error.

## Garantías de éxito

- Factura creada en estado `draft`.
- Línea de factura con `quantity`, `price_unit`, `tax_ids` correctos.
- `invoice_origin` apunta al pedido original.

## Flujo principal

1. Usuario hace clic en "Crear factura" → sistema invoca `_create_invoices()` (ver `addons/sale/models/sale_order.py:1550`).
2. Sistema prepara las líneas de factura con `_prepare_invoice()` (ver `addons/sale/models/sale_order.py:1411`).
3. Sistema crea un nuevo `account.move` con tipo `out_invoice` (factura de cliente).
4. Sistema crea las `account.move.line` correspondientes.
5. Sistema vincula el pedido con la factura vía `invoice_ids` (Many2many).
6. Sistema actualiza `invoice_status` del pedido según corresponda.
7. Factura queda en estado `draft`.

## Flujos alternativos

### FA-01 — Facturación agrupada

1. Sistema agrupa múltiples pedidos en una sola factura (cuando `grouped=True`).
2. Sistema crea una factura con líneas de todos los pedidos.
3. Cada pedido referencia la factura agrupada.

### FA-02 — Facturación parcial

1. Sistema factura solo una parte de las cantidades (parcial o downpayment).
2. Resto queda pendiente para futuras facturas.

## Excepciones

### EX-01 — Todo ya facturado

1. Sistema detecta que `invoice_status` es `invoiced`.
2. Sistema retorna mensaje "Nothing to invoice".

### EX-02 — Compañía sin diario configurado

1. Compañía no tiene `currency_id` o `journal_id` configurado.
2. Sistema retorna error de configuración.

## Reglas de negocio

- **RN-FAC-001**: Solo se puede facturar un pedido en estado `sale`.
- **RN-FAC-002**: Una factura no se puede modificar después de publicarse (CU-FAC-002), solo cancelar.

## Datos de entrada

- Pedido en estado `sale`.
- Cantidades a facturar (pueden ser parciales).

## Datos de salida

- `account.move` (factura) en estado `draft`.
- `account.move.line` (líneas de factura).

## Estados involucrados

- Factura: `draft` → `posted` (después de CU-FAC-002).

## Pantallas involucradas

- `view_sale_order_form` — botón "Crear factura".
- `account.view_move_form` — form de la factura creada.

## Modelos de Odoo relacionados

- `sale.order` (origen).
- `sale.order.line` (líneas a facturar).
- `account.move` (factura creada).
- `account.move.line` (líneas de factura).
- `account.tax` (impuestos aplicados).

## Métodos de Odoo relacionados

- `_create_invoices()` — entry point (ver `addons/sale/models/sale_order.py:1550`).
- `_prepare_invoice()` — prepara valores (ver `addons/sale/models/sale_order.py:1411`).

## Permisos requeridos

- `sales_team.group_sale_salesman_all` o `account.group_account_invoice` — para crear facturas.

## Configuraciones relevantes

- Política de facturación del pedido (`invoice_policy`).
- Diarios contables en `res.company`.

## Casos de uso relacionados

- CU-VEN-004 Confirmar pedido de venta (precondición).
- CU-ENT-004 Validar entrega (puede disparar).
- CU-FAC-002 Publicar factura (siguiente paso).

## Criterios de aceptación

- [ ] Al facturar un pedido confirmado, se crea una factura en estado `draft`.
- [ ] La factura referencia correctamente al pedido origen.
- [ ] Los totales coinciden con las líneas facturadas.

## Evidencias de ingeniería inversa

- **EV-COD-013**: `addons/sale/models/sale_order.py:1550` — método `_create_invoices`.
- **EV-COD-014**: `addons/sale/models/sale_order.py:1411` — método `_prepare_invoice`.
- **EV-COD-015**: `addons/account/models/account_move.py:72-73` — definición de `AccountMove` con `_name = 'account.move'`.

## Supuestos y aspectos pendientes de validación

- **EV-INF-010**: La lógica de agrupación de facturas (`grouped=True`) no fue leída en detalle.
- **EV-INF-011**: La integración con `_action_invoice_create` (versión legacy) requiere verificación.