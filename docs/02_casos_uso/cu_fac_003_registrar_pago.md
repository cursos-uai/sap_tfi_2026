# CU-FAC-003 — Registrar Pago

## Nombre

**Registrar Pago de Factura**

## Objetivo

El facturador (o el contador) registra el pago de una factura, marcando el saldo como cobrado y actualizando el estado de pago del cliente.

## Pre-condición

- La factura está en estado `posted`.
- La factura no está completamente pagada.
- El diario de banco/caja está configurado.

## Post-condición

- Existe un `account.payment` registrado.
- El asiento contable del pago queda generado.
- El `payment_state` de la factura se actualiza (`paid`, `partial`, o `in_payment`).

## Pasos trascendentes (camino feliz, en voz activa)

1. El facturador **presiona** "Registrar pago" en el form de la factura.
2. El sistema **invoca** `action_register_payment()`.
3. El sistema **abre** el wizard `account.payment.register`.
4. El facturador **completa** los datos del pago (fecha, diario, método, monto).
5. El facturador **confirma** el wizard.
6. El sistema **crea** un `account.payment` con los datos ingresados.
7. El sistema **genera** el asiento contable del pago (débito banco, crédito cliente).
8. El sistema **reconcilia** el pago con la factura.
9. El sistema **actualiza** `payment_state` de la factura a `paid`.
10. El sistema **muestra** el pago registrado.

## Caminos alternativos (en voz activa)

### FA-01 — El facturador hace pago parcial

1. El facturador **ingresa** un monto menor al saldo pendiente.
2. El sistema **crea** el pago parcial.
3. El sistema **actualiza** `payment_state` a `partial`.
4. El sistema **deja** saldo pendiente para pagos futuros.
5. El facturador **registra** más pagos hasta completar el saldo.

### FA-02 — El facturador hace pago múltiple

1. El facturador **registra** varios pagos para la misma factura.
2. Para cada pago, el sistema **ejecuta** los pasos trascendentes.
3. El sistema **acumula** los pagos.
4. Cuando se completa el saldo, el sistema **actualiza** `payment_state` a `paid`.

### FA-03 — El sistema integra con pasarela de pago

1. El sistema **detecta** que hay una pasarela configurada.
2. El sistema **redirige** al cliente a la pasarela.
3. El sistema **recibe** la confirmación de pago.
4. El sistema **crea** el `account.payment` automáticamente.

## Excepciones (en voz activa)

### EX-01 — La factura no está posted

1. La factura está en estado `draft` o `cancel`.
2. El sistema **detecta** el estado inválido.
3. El sistema **impide** el registro del pago.

### EX-02 — El pago excede el saldo

1. El facturador **intenta** pagar más de lo adeudado.
2. El sistema **advierte** o **rechaza** según configuración.
3. El sistema **muestra** el mensaje de error.

## Reglas de negocio

- **RN-FAC-005**: Una factura pagada no puede recibir más pagos (saldo = 0).
- **RN-FAC-006**: El estado `payment_state` se calcula automáticamente.

## Relaciones con otros CU

(No tiene relaciones `<<include>>` o `<<extend>>` explícitas en este CU; es terminal del flujo)

## Diagrama de robustez asociado

(No tiene ROB dedicado en la primera iteración)

## Verbos clave (para validar la voz activa)

| Verbo | Actor | Acción sobre |
|-------|-------|--------------|
| **presiona** | Facturador | Botón "Registrar pago" |
| **invoca** | Sistema | `action_register_payment()` |
| **abre** | Sistema | Wizard de pago |
| **completa** | Facturador | Datos del pago |
| **confirma** | Facturador | Wizard |
| **crea** | Sistema | `account.payment` |
| **genera** | Sistema | Asiento contable |
| **reconcilia** | Sistema | Pago con factura |
| **actualiza** | Sistema | `payment_state` |
| **muestra** | Sistema | Pago registrado |
| **ingresa** | Facturador | Monto parcial |
| **deja** | Sistema | Saldo pendiente |
| **registra** | Facturador | Más pagos |
| **ejecuta** | Sistema | Pasos trascendentes |
| **acumula** | Sistema | Pagos |
| **detecta** | Sistema | Pasarela / estado |
| **redirige** | Sistema | Cliente a pasarela |
| **recibe** | Sistema | Confirmación de pago |
| **impide** | Sistema | Registro de pago |
| **intenta** | Facturador | Pagar de más |
| **advierte** | Sistema | Pago excedido |
| **rechaza** | Sistema | Pago excedido |