# CU-FAC-002 — Publicar Factura

## Nombre

**Publicar Factura (Confirmar y Generar Asiento Contable)**

## Objetivo

El facturador publica una factura en estado `draft`, generando el asiento contable y haciendo la factura oficial.

## Pre-condición

- La factura está en estado `draft`.
- Las líneas tienen impuestos y cuentas contables válidas.
- El diario contable está configurado.
- La factura pasó las validaciones (`CU-VALLIN-001`).

## Post-condición

- El estado de la factura cambia a `posted`.
- El asiento contable queda generado.
- `invoice_date` tiene la fecha de publicación.
- El número de factura queda asignado por la secuencia del diario.

## Pasos trascendentes (camino feliz, en voz activa)

1. El facturador **presiona** "Confirmar" en el form de la factura.
2. El sistema **invoca** `action_post()` sobre la factura.
3. El sistema **valida** la factura (líneas, impuestos, cuentas).
4. El sistema **verifica** que las líneas tengan cuentas contables asignadas.
5. El sistema **verifica** que los totales sean correctos.
6. El sistema **genera** el asiento contable (una línea por cada movimiento).
7. El sistema **asigna** el número de factura por la secuencia del diario.
8. El sistema **actualiza** `state` a `posted`.
9. El sistema **actualiza** `invoice_date` a la fecha actual.
10. El sistema **publica** la factura oficialmente.

## Caminos alternativos (en voz activa)

### FA-01 — El facturador hace publicación masiva

1. El facturador **selecciona** múltiples facturas en estado `draft`.
2. El facturador **presiona** "Confirmar" (acción masiva).
3. El sistema **itera** sobre cada factura.
4. Para cada factura, el sistema **ejecuta** los pasos trascendentes.
5. Si alguna falla, el sistema **muestra** el error y **detiene** el proceso.

### FA-02 — El facturador revierte a draft

1. El facturador **detecta** un error en la factura publicada.
2. El facturador **presiona** "Restablecer a borrador".
3. El sistema **invoca** `action_post_draft()`.
4. El sistema **revierte** el estado a `draft`.
5. El sistema **permite** la edición de la factura.
6. El facturador **corrige** los datos.
7. El facturador **vuelve** a publicar.

### FA-03 — El sistema valida asientos anormales (extiende CU-FAC-002-VAL)

1. El sistema **detecta** montos o fechas anormales.
2. El sistema **invoca** el wizard `validate.account.move`.
3. El sistema **abre** el wizard de validación.
4. El facturador **confirma** la validación.
5. El sistema **publica** la factura.

## Excepciones (en voz activa)

### EX-01 — Alguna línea no tiene cuenta contable

1. El sistema **detecta** que alguna línea no tiene cuenta asignada.
2. El sistema **muestra** el error "Cuenta contable requerida".

### EX-02 — La factura tiene totales en cero

1. El sistema **detecta** que los totales son 0.
2. El sistema **advierte** o **bloquea** según configuración.

## Reglas de negocio

- **RN-FAC-003**: Una factura publicada no se puede borrar, solo revertir a draft.
- **RN-FAC-004**: Al publicar, se crea un asiento contable con la fecha del día.

## Relaciones con otros CU

- **<<include>> CU-GENJOUR-001**: Crea el asiento contable al publicar.
- **<<extend>> CU-FAC-002-VAL**: Valida asientos anormales (opcional).

## Diagrama de robustez asociado

(No tiene ROB dedicado en la primera iteración; consultar `d_rob_fac_001_crear_factura.puml` como referencia conceptual)

## Verbos clave (para validar la voz activa)

| Verbo | Actor | Acción sobre |
|-------|-------|--------------|
| **presiona** | Facturador | Botón "Confirmar" |
| **invoca** | Sistema | `action_post()` |
| **valida** | Sistema | Líneas, impuestos, cuentas |
| **verifica** | Sistema | Cuentas contables, totales |
| **genera** | Sistema | Asiento contable |
| **asigna** | Sistema | Número de factura |
| **actualiza** | Sistema | `state`, `invoice_date` |
| **publica** | Sistema | Factura |
| **selecciona** | Facturador | Múltiples facturas |
| **iterar** | Sistema | Lista de facturas |
| **ejecuta** | Sistema | Pasos trascendentes |
| **muestra** | Sistema | Error |
| **detiene** | Sistema | Proceso |
| **detecta** | Facturador/Sistema | Error / monto anormal |
| **revierte** | Sistema | Estado a `draft` |
| **permite** | Sistema | Edición |
| **corrige** | Facturador | Datos |
| **vuelve** | Facturador | Publicar |
| **abre** | Sistema | Wizard de validación |
| **confirma** | Facturador | Validación |
| **advierte** | Sistema | Totales en 0 |
| **bloquea** | Sistema | Publicación |