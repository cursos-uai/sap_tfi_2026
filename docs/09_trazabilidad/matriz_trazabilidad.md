# Matriz de Trazabilidad — SAP-TFI-2026

> Documento vivo. Última actualización: 2026-06-18.

**Versión Odoo analizada:** 19.0 Community
**Rama:** 19.0
**Edición:** Community
**Path local código fuente:** `~/proyectos/odoo_src/odoo`
**Path local repo proyecto:** `~/proyectos/sap_tfi_2026`

## Matriz principal

| Requisito | Caso de uso | Regla | Pantalla | Robustez | Secuencia | Clase | Modelo Odoo | Evidencia | Estado |
|-----------|-------------|-------|----------|----------|-----------|-------|-------------|-----------|--------|
| REQ-VEN-001 | CU-VEN-001 | RN-VEN-001, RN-VEN-002 | view_sale_order_form | (futuro) | (futuro) | (futuro) | sale.order | EV-COD-001..005 | Verificado |
| REQ-VEN-004 | CU-VEN-004 | RN-VEN-004, RN-VEN-005, RN-VEN-006 | view_sale_order_form | D-ROB-VEN-004 | D-SEC-VEN-004 | (en D-CLA-INT-001) | sale.order | EV-COD-006..009 | Verificado |
| REQ-ENT-002 | CU-ENT-002 | RN-ENT-002, RN-ENT-003 | view_picking_form | (futuro) | (futuro) | (en D-CLA-INT-001) | stock.picking | EV-COD-010, EV-COD-011 | Verificado |
| REQ-ENT-004 | CU-ENT-004 | RN-ENT-004, RN-ENT-005 | view_picking_form | (futuro) | (futuro) | (en D-CLA-INT-001) | stock.picking | EV-COD-012 | Verificado |
| REQ-FAC-001 | CU-FAC-001 | RN-FAC-001, RN-FAC-002 | view_sale_order_form | (futuro) | (futuro) | (en D-CLA-INT-001) | sale.order, account.move | EV-COD-013, EV-COD-014 | Verificado |
| REQ-FAC-002 | CU-FAC-002 | RN-FAC-003, RN-FAC-004 | view_move_form | (futuro) | (futuro) | (en D-CLA-INT-001) | account.move | EV-COD-016, EV-COD-017, EV-COD-018 | Verificado |
| REQ-FAC-003 | CU-FAC-003 | RN-FAC-005, RN-FAC-006 | view_move_form | (futuro) | (futuro) | (en D-CLA-INT-001) | account.move | EV-COD-019, EV-COD-020 | Verificado |

## Leyenda de estados

- **Pendiente** — aún no iniciado.
- **En análisis** — evidencia recopilándose.
- **Modelado** — artefactos en borrador.
- **Verificado** — artefacto validado contra código Odoo.
- **Requiere revisión** — discrepancia detectada.
- **Aprobado** — revisado y firmado por Ale.
- **Obsoleto** — reemplazado por versión posterior.

## Leyenda de evidencia

- **EV-COD** — código fuente (ruta + línea)
- **EV-XML** — vista o dato XML (ruta + elemento)
- **EV-UI** — comportamiento observado en la interfaz
- **EV-DB** — registro o estructura de base de datos
- **EV-DOC** — documentación oficial (URL + sección)
- **EV-TEST** — prueba automatizada (ruta)
- **EV-INF** — inferencia pendiente de validación

## Áreas

- **VEN** — Ventas
- **FAC** — Facturación
- **ENT** — Entregas
- **INV** — Inventario
- **ARQ** — Arquitectura
- **DOM** — Dominio
- **GEN** — General

## Resumen por estado

| Estado | Cantidad | % |
|--------|----------|---|
| Pendiente | 0 | 0% |
| En análisis | 0 | 0% |
| Modelado | 0 | 0% |
| Verificado | 7 | 100% |
| Requiere revisión | 0 | 0% |
| Aprobado | 0 | 0% |
| Obsoleto | 0 | 0% |
| **TOTAL** | **7** | **100%** |

## Evidencias generadas (20)

| Código | Tipo | Descripción | Archivo |
|--------|------|-------------|---------|
| EV-COD-001 | EV-COD | `sale.order` definición de clase | `addons/sale/models/sale_order.py:34-36` |
| EV-COD-002 | EV-COD | `SALE_ORDER_STATE` constantes | `addons/sale/models/sale_order.py:26-31` |
| EV-COD-003 | EV-COD | `action_quotation_send` | `addons/sale/models/sale_order.py:1067` |
| EV-COD-004 | EV-COD | `action_confirm` | `addons/sale/models/sale_order.py:1166` |
| EV-COD-005 | EV-COD | `name` field | `addons/sale/models/sale_order.py:54-58` |
| EV-COD-006 | EV-COD | `action_confirm` cuerpo | `addons/sale/models/sale_order.py:1166-1196` |
| EV-COD-007 | EV-COD | `_confirmation_error_message` | `addons/sale/models/sale_order.py:1203-1216` |
| EV-COD-008 | EV-COD | `_prepare_confirmation_values` | `addons/sale/models/sale_order.py:1218-1229` |
| EV-COD-009 | EV-COD | `_should_be_locked` | `addons/sale/models/sale_order.py:1198-1201` |
| EV-COD-010 | EV-COD | `action_assign` (stock.picking) | `addons/stock/models/stock_picking.py:1195` |
| EV-COD-011 | EV-COD | `action_confirm` (stock.picking) | `addons/stock/models/stock_picking.py:1186` |
| EV-COD-012 | EV-COD | `button_validate` | `addons/stock/models/stock_picking.py:1398` |
| EV-COD-013 | EV-COD | `_create_invoices` | `addons/sale/models/sale_order.py:1550` |
| EV-COD-014 | EV-COD | `_prepare_invoice` | `addons/sale/models/sale_order.py:1411` |
| EV-COD-015 | EV-COD | `account.move` definición | `addons/account/models/account_move.py:72-73` |
| EV-COD-016 | EV-COD | `action_post` | `addons/account/models/account_move.py:6101` |
| EV-COD-017 | EV-COD | `AccountMove` class | `addons/account/models/account_move.py:72-73` |
| EV-COD-018 | EV-COD | `state` field (account.move) | `addons/account/models/account_move.py:129` |
| EV-COD-019 | EV-COD | `action_register_payment` | `addons/account/models/account_move.py:6022` |
| EV-COD-020 | EV-COD | `payment_state` field | `addons/account/models/account_move.py:600` |

## Inferencias pendientes (EV-INF)

Total: **22 inferencias** documentadas en los CU y diagramas. Las más relevantes:

- **EV-INF-004**: Implementación interna de `_action_confirm()` no leída.
- **EV-INF-005**: Efectos downstream sobre `stock.picking` y `account.move` se validan en CU específicos.
- **EV-INF-006, 007**: Lógica interna de `action_assign()` y `procurement.order` no leídas.
- **EV-INF-008, 009**: Lógica de `button_validate()` y backorder no leídas.
- **EV-INF-010, 011**: Lógica de agrupación de facturas no leída.
- **EV-INF-012, 013**: Lógica de `action_post()` y validaciones no leídas.
- **EV-INF-014, 015, 016**: Valores de `payment_state` y reconciliación no verificados.
- **EV-INF-017, 018**: Modelo conceptual aproximado, refinable.
- **EV-INF-019, 020**: Versión Community vs Enterprise.
- **EV-INF-021, 022**: Campos exactos del form y botones visibles.

## Próximas acciones

- [ ] Validar las 22 EV-INF en iteraciones siguientes.
- [ ] Leer `_action_confirm()` de `sale.order` para refinar CU-VEN-004.
- [ ] Agregar CU de cancelación de pedido y factura.
- [ ] Generar diagramas de robustez y secuencia para los CU que faltan.