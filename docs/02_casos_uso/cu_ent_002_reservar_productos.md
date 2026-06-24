# CU-ENT-002 — Reservar Productos

## Nombre

**Reservar Productos en Almacén**

## Objetivo

El sistema (o el operario de almacén) reserva las cantidades pedidas de cada producto, asegurando disponibilidad antes de la entrega.

## Pre-condición

- El picking está en estado `draft`, `waiting` o `confirmed`.
- Los productos tienen stock disponible o reglas de reabastecimiento aplicables.

## Post-condición

- Las cantidades reservadas quedan en `stock.move.line` con `reserved_availability`.
- El estado del picking cambia a `assigned` (si todas las líneas tienen reserva) o `partially_available` (si hay parcial).

## Pasos trascendentes (camino feliz, en voz activa)

1. El sistema (o el operario) **dispara** el trigger de reserva (confirmación de pedido o botón manual).
2. El sistema **lee** el picking y sus líneas.
3. El sistema **invoca** `action_assign()` sobre el picking.
4. El sistema **recorre** cada línea del picking.
5. Para cada línea, el sistema **busca** stock disponible en `stock.quant`.
6. El sistema **encuentra** cantidad suficiente.
7. El sistema **reserva** la cantidad creando `stock.move.line`.
8. El sistema **actualiza** `reserved_availability` en la línea.
9. El sistema **actualiza** el estado del picking.
10. El sistema **asigna** el estado `assigned` cuando todas las líneas tienen reserva.

## Caminos alternativos (en voz activa)

### FA-01 — El sistema no encuentra stock suficiente

1. El sistema **busca** stock disponible y **encuentra** cantidad insuficiente.
2. El sistema **consulta** las reglas de reabastecimiento (`stock.warehouse.orderpoint`).
3. Si hay reglas MTO, el sistema **extiende** con `CU-ENT-002-MTO` para generar orden de compra.
4. El sistema **crea** una `purchase.order` para reabastecer.
5. El sistema **programa** la recepción del producto.
6. El sistema **marca** la línea como `partially_available`.

### FA-02 — El sistema hace reserva parcial

1. El sistema **reserva** parte de las cantidades.
2. El sistema **marca** las líneas con reserva como `assigned`.
3. El sistema **deja** las líneas sin reserva como `partially_available`.
4. El sistema **no cambia** el estado global del picking a `assigned`.

### FA-03 — El operario fuerza la reserva manualmente

1. El operario **presiona** "Reservar" en el form del picking.
2. El sistema **invoca** `action_assign()`.
3. El sistema **ejecuta** los pasos trascendentes.

## Excepciones (en voz activa)

### EX-01 — El picking no tiene movimientos

1. El sistema **detecta** que no hay movimientos para reservar.
2. El sistema **muestra** el error "Nothing to check the availability for".

### EX-02 — No hay stock ni reglas aplicables

1. El sistema **busca** stock y **no encuentra** cantidad.
2. El sistema **consulta** reglas de reabastecimiento y **no encuentra** aplicables.
3. El sistema **deja** el picking en estado `partially_available`.
4. El operario **debe** decidir acción manual.

## Reglas de negocio

- **RN-ENT-002**: La reserva no afecta disponibilidad para otros pedidos hasta que se confirme el picking.
- **RN-ENT-003**: Las reservas se liberan automáticamente al cancelar el pedido o el picking.

## Relaciones con otros CU

- **<<extend>> CU-ENT-002-MTO**: Genera orden de compra (MTO) cuando no hay stock (opcional).

## Diagrama de robustez asociado

`diagrams/plantuml/d_rob_ent_002_reservar_productos.puml`

## Verbos clave (para validar la voz activa)

| Verbo | Actor | Acción sobre |
|-------|-------|--------------|
| **dispara** | Sistema/Operario | Trigger de reserva |
| **lee** | Sistema | Picking y líneas |
| **invoca** | Sistema | `action_assign()` |
| **recorre** | Sistema | Líneas del picking |
| **busca** | Sistema | Stock en `stock.quant` |
| **encuentra** | Sistema | Cantidad disponible |
| **reserva** | Sistema | `stock.move.line` |
| **actualiza** | Sistema | `reserved_availability`, estado |
| **asigna** | Sistema | Estado `assigned` |
| **consulta** | Sistema | `stock.warehouse.orderpoint` |
| **extiende** | Sistema | `CU-ENT-002-MTO` |
| **crea** | Sistema | `purchase.order` |
| **programa** | Sistema | Recepción |
| **marca** | Sistema | `partially_available` |
| **deja** | Sistema | Estado sin cambio |
| **presiona** | Operario | Botón "Reservar" |
| **ejecuta** | Sistema | Pasos trascendentes |
| **detecta** | Sistema | Movimientos / reglas |
| **muestra** | Sistema | Error |
| **libera** | Sistema | Reservas (al cancelar) |