# CU-VEN-001 — Crear Presupuesto

## Nombre

**Crear Presupuesto de Venta**

## Objetivo

El vendedor registra un presupuesto de venta en estado `draft` para un cliente, con sus líneas de productos, precios y totales calculados.

## Pre-condición

- El vendedor tiene sesión iniciada (`CU-AUTH-001`).
- Existe al menos un cliente activo en `res.partner`.
- El catálogo contiene productos publicables en `product.product`.
- La compañía tiene configurada la secuencia de presupuestos en `ir.sequence`.

## Post-condición

- Existe un registro `sale.order` en estado `draft` con `name` único.
- Las líneas tienen productos, cantidades, precios unitarios, impuestos y descuentos.
- Los totales (`amount_untaxed`, `amount_tax`, `amount_total`) están calculados.
- El cliente tiene una lista de precios asociada por defecto.

## Pasos trascendentes (camino feliz, en voz activa)

1. El vendedor **presiona** "Nuevo" desde el menú Ventas → Presupuestos.
2. El sistema **crea** un `sale.order` en estado `draft` con `name` provisional.
3. El sistema **abre** el form `view_sale_order_form`.
4. El vendedor **selecciona** el cliente.
5. El sistema **carga** la lista de precios por defecto del cliente.
6. El vendedor **agrega** líneas con productos y cantidades.
7. El sistema **actualiza** `partner_id` y `order_line` en `sale.order`.
8. El sistema **calcula** los totales con `_compute_amounts()`.
9. El sistema **muestra** los totales en el form.
10. El vendedor **guarda** el presupuesto.

## Caminos alternativos (en voz activa)

### FA-01 — El vendedor envía el presupuesto por email

1. El vendedor **presiona** "Enviar por email".
2. El sistema **invoca** `action_quotation_send()`.
3. El sistema **valida** la distribución analítica.
4. El sistema **marca** el presupuesto como enviado.
5. El sistema **cambia** el estado de `draft` a `sent`.
6. El sistema **crea** un `mail.compose.message`.
7. El sistema **genera** el `mail.mail`.
8. El sistema **envía** el email al cliente.

### FA-02 — El vendedor aplica un descuento (incluye CU-VEN-001-DISC)

1. El vendedor **edita** el campo `discount` en una línea.
2. El sistema **recalcula** el subtotal de la línea.
3. Si el descuento supera el máximo permitido, el sistema **bloquea** o **notifica**.

### FA-03 — El vendedor duplica el presupuesto

1. El vendedor **selecciona** un presupuesto existente.
2. El vendedor **presiona** "Duplicar".
3. El sistema **crea** un nuevo `sale.order` copiando las líneas.
4. El sistema **asigna** estado `draft` al nuevo presupuesto.

## Reglas de negocio

- **RN-VEN-001**: El estado `state` solo puede pasar de `draft` → `sent` → `sale`, o a `cancel`.
- **RN-VEN-002**: El campo `name` se genera por la secuencia configurada en la compañía.
- **RN-VEN-003**: Los descuentos mayores al 10% pueden requerir aprobación.

## Relaciones con otros CU

- **<<include>> CU-AUTH-001**: Valida la sesión antes de crear el presupuesto.
- **<<include>> CU-CALC-001**: Calcula los totales con impuestos.
- **<<extend>> CU-VEN-001-EMAIL**: Envía el presupuesto por email (opcional).
- **<<extend>> CU-VEN-001-DISC**: Aplica descuento (opcional).

## Diagrama de robustez asociado

`diagrams/plantuml/d_rob_ven_001_crear_presupuesto.puml`

## Verbos clave (para validar la voz activa)

| Verbo | Actor | Acción sobre |
|-------|-------|--------------|
| **presiona** | Vendedor | Botón "Nuevo" |
| **crea** | Sistema | `sale.order` (draft) |
| **abre** | Sistema | `view_sale_order_form` |
| **selecciona** | Vendedor | Cliente |
| **carga** | Sistema | Lista de precios |
| **agrega** | Vendedor | Líneas |
| **actualiza** | Sistema | `partner_id`, `order_line` |
| **calcula** | Sistema | `_compute_amounts()` |
| **muestra** | Sistema | Totales en form |
| **guarda** | Vendedor | Presupuesto |
| **invoca** | Sistema | `action_quotation_send()` |
| **valida** | Sistema | Distribución analítica |
| **marca** | Sistema | `mark_so_as_sent` |
| **cambia** | Sistema | Estado `draft` → `sent` |
| **genera** | Sistema | `mail.mail` |
| **envía** | Sistema | Email al cliente |