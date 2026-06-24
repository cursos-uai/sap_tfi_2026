# CU-FAC-002 — Publicar factura

## Objetivo

Publicar (confirmar) una factura en estado `draft`, generando el asiento contable y haciendo la factura oficial.

## Alcance

Módulo `account` de Odoo 19.0. Aplica al modelo `account.move`.

## Nivel

Primario (esencial — la factura no tiene valor contable hasta publicarse).

## Actor principal

Responsable de facturación o Contador (usuario con permisos `account.group_account_invoice`).

## Actores secundarios

- Sistema contable (genera asiento).

## Interesados

- Contador (visualiza asientos).
- Cliente (recibe factura oficial).
- Administración (reportes contables).

## Disparador

El usuario hace clic en "Confirmar" en la vista form de la factura.

## Precondiciones

- La factura está en estado `draft`.
- Las líneas tienen impuestos y cuentas contables válidas.
- El diario contable está configurado.

## Garantías mínimas

El sistema cambia el estado de la factura o muestra un error explicativo.

## Garantías de éxito

- Estado de la factura: `posted`.
- Asiento contable generado (`account.move` con `state='posted'`).
- `invoice_date` con la fecha de publicación.
- Número de factura asignado por secuencia.

## Flujo principal

1. Usuario hace clic en "Confirmar" → sistema invoca `action_post()` (ver `addons/account/models/account_move.py:6101`).
2. Sistema valida la factura:
   - Líneas con productos y precios válidos.
   - Impuestos aplicados correctamente.
   - Cuentas contables válidas.
3. Si pasa validación, sistema genera el asiento contable (una línea por cada movimiento).
4. Sistema asigna número de factura por secuencia del diario.
5. Sistema actualiza `state` a `posted`.
6. Sistema actualiza `invoice_date` a la fecha actual.

## Flujos alternativos

### FA-01 — Publicación masiva

1. Usuario selecciona múltiples facturas draft.
2. Sistema itera y publica cada una.
3. Si alguna falla, sistema muestra error y detiene.

### FA-02 — Reversión a draft

1. Si la factura necesita corrección, usuario con permisos puede invocar `action_post_draft()`.
2. Sistema revierte a `draft`, permite edición.
3. Vuelve a publicar cuando esté listo.

## Excepciones

### EX-01 — Líneas sin cuenta contable

1. Alguna línea no tiene cuenta contable asignada.
2. Sistema muestra error "Cuenta contable requerida".

### EX-02 — Factura con totales en cero

1. Factura con líneas pero totales son 0.
2. Sistema puede advertir o bloquear según configuración.

## Reglas de negocio

- **RN-FAC-003**: Una factura publicada no se puede borrar, solo revertir a draft.
- **RN-FAC-004**: Al publicar, se crea un asiento contable con la fecha del día.

## Datos de entrada

- Factura en estado `draft`.

## Datos de salida

- Factura en estado `posted`.
- Asiento contable generado.
- Número de factura asignado.

## Estados involucrados

- `draft` → `posted` (transición principal).
- `posted` → `draft` (reversión, vía `action_post_draft()`).

## Pantallas involucradas

- `account.view_move_form` — botón "Confirmar".

## Modelos de Odoo relacionados

- `account.move` (factura + asiento).
- `account.move.line` (líneas, ahora con cuenta contable).
- `account.journal` (diario contable).

## Métodos de Odoo relacionados

- `action_post()` — entry point (ver `addons/account/models/account_move.py:6101`).
- `action_post_draft()` — reversión.

## Permisos requeridos

- `account.group_account_invoice` — para publicar.

## Configuraciones relevantes

- Secuencia de facturas en el diario (`account.journal.sequence_id`).
- Configuración de impuestos y cuentas.

## Casos de uso relacionados

- CU-FAC-001 Crear factura (precondición).
- CU-FAC-003 Registrar pago (siguiente paso).

## Criterios de aceptación

- [ ] Una factura en `draft` puede publicarse si pasa las validaciones.
- [ ] Al publicar, se genera el asiento contable.
- [ ] El número de factura es único y secuencial.

## Evidencias de ingeniería inversa

- **EV-COD-016**: `addons/account/models/account_move.py:6101` — método `action_post`.
- **EV-COD-017**: `addons/account/models/account_move.py:72-73` — definición de `AccountMove` con `_name = 'account.move'`.
- **EV-COD-018**: `addons/account/models/account_move.py:129` — campo `state = fields.Selection(...)`.

## Supuestos y aspectos pendientes de validación

- **EV-INF-012**: La lógica interna de `action_post()` (cómo genera el asiento, cómo asigna cuentas) no fue leída en detalle.
- **EV-INF-013**: Las validaciones específicas (impuestos, cuentas, totales) requieren lectura adicional.