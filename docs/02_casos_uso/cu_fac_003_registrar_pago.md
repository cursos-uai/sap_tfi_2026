# CU-FAC-003 — Registrar pago

## Objetivo

Registrar el pago de una factura, marcando el saldo como cobrado y actualizando el estado de pago del cliente.

## Alcance

Módulo `account` de Odoo 19.0. Aplica al modelo `account.move`.

## Nivel

Primario (cierra el circuito de venta).

## Actor principal

Responsable de facturación o Contador (usuario con permisos `account.group_account_invoice` o `account.group_account_user`).

## Actores secundarios

- Sistema bancario (si hay integración).
- Cliente (origen del pago).

## Interesados

- Contador (visualiza estado de pagos).
- Cliente (ve su saldo actualizado).

## Disparador

El usuario hace clic en "Registrar pago" en la factura.

## Precondiciones

- La factura está en estado `posted`.
- La factura no está completamente pagada (o se requiere un pago parcial).

## Garantías mínimas

El sistema crea un `account.payment` o equivalente y actualiza el estado de pago.

## Garantías de éxito

- Pago registrado en el sistema.
- Estado de pago de la factura: `paid` (si es pago completo) o `partial` (si parcial).
- Asiento contable de pago generado.

## Flujo principal

1. Usuario hace clic en "Registrar pago" → sistema invoca `action_register_payment()` (ver `addons/account/models/account_move.py:6022`).
2. Sistema abre wizard de registro de pago (`account.payment.register`).
3. Usuario completa:
   - Fecha del pago.
   - Diario de banco/caja.
   - Método de pago.
   - Monto (por defecto, saldo pendiente).
4. Usuario confirma.
5. Sistema crea `account.payment` con el monto y método.
6. Sistema genera el asiento contable del pago (débito a banco, crédito a cuenta del cliente).
7. Sistema reconcilia el pago con la factura.
8. Sistema actualiza `payment_state` de la factura:
   - `paid` si el pago completa el saldo.
   - `partial` si es parcial.
   - `in_payment` si está en proceso (cheques, etc.).

## Flujos alternativos

### FA-01 — Pago parcial

1. Usuario registra un pago menor al saldo.
2. Sistema crea el pago parcial.
3. `payment_state` queda en `partial`.
4. Queda saldo pendiente para pagos futuros.

### FA-02 — Pago múltiple

1. Usuario registra varios pagos para la misma factura.
2. Cada pago genera un `account.payment` separado.
3. Cuando se completa el saldo, `payment_state` pasa a `paid`.

## Excepciones

### EX-01 — Factura no posted

1. Factura en estado `draft` o `cancel`.
2. Sistema no permite registrar pago.

### EX-02 — Pago mayor al saldo

1. Usuario intenta pagar más de lo adeudado.
2. Sistema advierte o rechaza según configuración.

## Reglas de negocio

- **RN-FAC-005**: Una factura pagada no puede recibir más pagos (saldo = 0).
- **RN-FAC-006**: El estado `payment_state` se calcula automáticamente en función de los pagos.

## Datos de entrada

- Factura en estado `posted`.
- Datos del pago (fecha, diario, método, monto).

## Datos de salida

- `account.payment` creado.
- Asiento contable de pago.
- `payment_state` actualizado.

## Estados involucrados

- Factura: `posted` → `payment_state=in_payment` → `payment_state=paid`.
- O `posted` → `payment_state=partial` → `payment_state=paid` (pagos múltiples).

## Pantallas involucradas

- `account.view_move_form` — botón "Registrar pago".
- `account.view_account_payment_form` — wizard.

## Modelos de Odoo relacionados

- `account.move` (factura).
- `account.payment` (pago).
- `account.payment.register` (wizard).
- `account.journal` (diario de banco).
- `account.account` (cuentas contables).

## Métodos de Odoo relacionados

- `action_register_payment()` — entry point (ver `addons/account/models/account_move.py:6022`).

## Permisos requeridos

- `account.group_account_invoice` o `account.group_account_user`.

## Configuraciones relevantes

- Diarios de banco/caja.
- Métodos de pago disponibles.
- Configuración de reconciliación.

## Casos de uso relacionados

- CU-FAC-002 Publicar factura (precondición).

## Criterios de aceptación

- [ ] Una factura posted puede recibir un pago.
- [ ] Al pagar el saldo completo, `payment_state` cambia a `paid`.
- [ ] Los pagos parciales dejan `payment_state=partial`.

## Evidencias de ingeniería inversa

- **EV-COD-019**: `addons/account/models/account_move.py:6022` — método `action_register_payment`.
- **EV-COD-020**: `addons/account/models/account_move.py:600` — campo `payment_state = fields.Selection(...)` (probablemente con valores como `not_paid`, `in_payment`, `paid`, `partial`, `reversed`).

## Supuestos y aspectos pendientes de validación

- **EV-INF-014**: Los valores exactos de `payment_state` requieren verificación leyendo las opciones del campo.
- **EV-INF-015**: La lógica de reconciliación requiere lectura adicional.
- **EV-INF-016**: El método `action_register_payment` puede haber cambiado entre versiones.