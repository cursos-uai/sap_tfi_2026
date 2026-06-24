# CU-FAC-001 — Crear Factura desde Pedido

## Nombre

**Crear Factura desde Pedido de Venta**

## Objetivo

El facturador (o el vendedor) genera una factura (`account.move`) basada en un pedido de venta confirmado, para registrar la venta en el sistema contable.

## Pre-condición

- El pedido está en estado `sale`.
- Hay productos a facturar (`invoice_status != 'invoiced'`).
- El cliente y la compañía tienen configurados los diarios contables.
- El sistema validó las líneas pendientes (`CU-VALLIN-001`).

## Post-condición

- Existe un `account.move` en estado `draft` con tipo `out_invoice`.
- Las líneas tienen `quantity`, `price_unit`, `tax_ids` correctos.
- `invoice_origin` apunta al pedido original.
- El pedido referencia la factura vía `invoice_ids`.

## Pasos trascendentes (camino feliz, en voz activa)

1. El facturador **presiona** "Crear Factura" en el form del pedido.
2. El sistema **invoca** `_create_invoices()` sobre el pedido.
3. El sistema **lee** el pedido (`sale.order` en estado `sale`).
4. El sistema **verifica** el `invoice_status` del pedido.
5. El sistema **lee** las líneas pendientes (`sale.order.line`).
6. El sistema **aplica** los impuestos (`account.tax`) a cada línea.
7. Para cada línea, el sistema **crea** un `account.move.line`.
8. El sistema **construye** los valores del invoice con `_prepare_invoice()`.
9. El sistema **crea** un `account.move` en estado `draft`.
10. El sistema **asocia** la factura al pedido vía `invoice_ids`.
11. El sistema **actualiza** `invoice_status` del pedido.
12. El sistema **muestra** la factura creada al facturador.

## Caminos alternativos (en voz activa)

### FA-01 — El facturador hace facturación agrupada

1. El facturador **selecciona** múltiples pedidos.
2. El facturador **presiona** "Crear Factura" con `grouped=True`.
3. El sistema **agrupa** las líneas de todos los pedidos.
4. El sistema **crea** una sola factura con todas las líneas.
5. El sistema **asocia** la factura a cada pedido.

### FA-02 — El facturador hace facturación parcial

1. El facturador **selecciona** las líneas específicas a facturar.
2. El sistema **factura** solo esas líneas.
3. El sistema **deja** las demás líneas pendientes.
4. El sistema **actualiza** `invoice_status` a `to invoice` parcial.

### FA-03 — El sistema crea factura automáticamente al validar entrega

1. El sistema **detecta** que la entrega fue validada.
2. El sistema **invoca** `_create_invoices()` automáticamente.
3. El sistema **ejecuta** los pasos trascendentes.

## Excepciones (en voz activa)

### EX-01 — No hay nada que facturar

1. El sistema **verifica** que `invoice_status` es `invoiced`.
2. El sistema **muestra** el mensaje "Nothing to invoice".

### EX-02 — La compañía no tiene diario configurado

1. El sistema **detecta** que `journal_id` está vacío.
2. El sistema **muestra** el error de configuración.

## Reglas de negocio

- **RN-FAC-001**: Solo se puede facturar un pedido en estado `sale`.
- **RN-FAC-002**: Una factura no se puede modificar después de publicarse.

## Relaciones con otros CU

- **<<include>> CU-VALLIN-001**: Valida líneas pendientes antes de facturar.

## Diagrama de robustez asociado

`diagrams/plantuml/d_rob_fac_001_crear_factura.puml`

## Verbos clave (para validar la voz activa)

| Verbo | Actor | Acción sobre |
|-------|-------|--------------|
| **presiona** | Facturador | Botón "Crear Factura" |
| **invoca** | Sistema | `_create_invoices()` |
| **lee** | Sistema | Pedido, líneas, taxes |
| **verifica** | Sistema | `invoice_status` |
| **aplica** | Sistema | Impuestos a líneas |
| **crea** | Sistema | `account.move`, `account.move.line` |
| **construye** | Sistema | `_prepare_invoice()` |
| **asocia** | Sistema | `invoice_ids` |
| **actualiza** | Sistema | `invoice_status` |
| **muestra** | Sistema | Factura al facturador |
| **selecciona** | Facturador | Múltiples pedidos |
| **agrupa** | Sistema | Líneas agrupadas |
| **factura** | Sistema | Líneas específicas |
| **deja** | Sistema | Líneas pendientes |
| **detecta** | Sistema | Validación de entrega / config |
| **ejecuta** | Sistema | Pasos trascendentes |
| **muestra** | Sistema | Mensaje de error |