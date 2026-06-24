# Matriz de Trazabilidad — SAP-TFI-2026

> Documento vivo. Última actualización: 2026-06-18.

## Diagrama de CU principal

`D-CU-GEN-002` — Casos de Uso con extend/include
- **5 includes**: CU-AUTH-001, CU-CALC-001, CU-GENPICK-001, CU-VALLIN-001, CU-GENJOUR-001
- **5 extends**: CU-VEN-001-EMAIL, CU-VEN-001-DISC, CU-ENT-002-MTO, CU-ENT-004-BACK, CU-FAC-002-VAL

## Versión Odoo analizada

- **19.0 Community**
- **Rama**: `19.0`
- **Path local código fuente**: `~/proyectos/odoo_src/odoo`
- **Path local repo proyecto**: `~/proyectos/sap_tfi_2026`

## Matriz principal

| Requisito | Caso de uso | Reglas | Diagrama de robustez | Diagrama de secuencia | Clases | Modelo Odoo | Evidencia |
|-----------|-------------|--------|---------------------|----------------------|--------|-------------|-----------|
| REQ-VEN-001 | CU-VEN-001 | RN-VEN-001, RN-VEN-002, RN-VEN-003 | D-ROB-VEN-001 | D-SEC-VEN-001 | D-CLA-INT-001 | sale.order | EV-COD-001..005 |
| REQ-VEN-004 | CU-VEN-004 | RN-VEN-004, RN-VEN-005, RN-VEN-006 | D-ROB-VEN-004 | D-SEC-VEN-004 | D-CLA-INT-001 | sale.order | EV-COD-006..009, EV-COD-021, EV-COD-027, EV-COD-028, EV-COD-030 |
| REQ-ENT-002 | CU-ENT-002 | RN-ENT-002, RN-ENT-003 | D-ROB-ENT-002 | D-SEC-ENT-002 | D-CLA-INT-001 | stock.picking | EV-COD-010, EV-COD-011, EV-COD-022 |
| REQ-ENT-004 | CU-ENT-004 | RN-ENT-004, RN-ENT-005 | (no ROB) | (no SEC) | D-CLA-INT-001 | stock.picking | EV-COD-012, EV-COD-029 |
| REQ-FAC-001 | CU-FAC-001 | RN-FAC-001, RN-FAC-002 | D-ROB-FAC-001 | D-SEC-FAC-001 | D-CLA-INT-001 | sale.order, account.move | EV-COD-013, EV-COD-014, EV-COD-023 |
| REQ-FAC-002 | CU-FAC-002 | RN-FAC-003, RN-FAC-004 | (no ROB) | (no SEC) | D-CLA-INT-001 | account.move | EV-COD-016, EV-COD-017, EV-COD-018, EV-COD-026 |
| REQ-FAC-003 | CU-FAC-003 | RN-FAC-005, RN-FAC-006 | (no ROB) | (no SEC) | D-CLA-INT-001 | account.move | EV-COD-019, EV-COD-020, EV-COD-024, EV-COD-025 |

## Tabla de CU includes y extends

| CU Base | Relación | CU Relacionado | Tipo |
|---------|----------|----------------|------|
| CU-VEN-001 | <<include>> | CU-AUTH-001 | Validación de sesión |
| CU-VEN-001 | <<include>> | CU-CALC-001 | Cálculo de totales |
| CU-VEN-004 | <<include>> | CU-AUTH-001 | Validación de sesión |
| CU-VEN-004 | <<include>> | CU-GENPICK-001 | Generación de picking |
| CU-FAC-001 | <<include>> | CU-VALLIN-001 | Validación de líneas |
| CU-FAC-002 | <<include>> | CU-GENJOUR-001 | Generación de asiento |
| CU-VEN-001 | <<extend>> | CU-VEN-001-EMAIL | Envío de email (opcional) |
| CU-VEN-001 | <<extend>> | CU-VEN-001-DISC | Aplicar descuento (opcional) |
| CU-ENT-002 | <<extend>> | CU-ENT-002-MTO | Generar PO (MTO) (opcional) |
| CU-ENT-004 | <<extend>> | CU-ENT-004-BACK | Crear backorder (opcional) |
| CU-FAC-002 | <<extend>> | CU-FAC-002-VAL | Validar asiento anormal (opcional) |

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

## Próximas acciones

- [ ] Validar las 8 EV-INF en iteraciones siguientes.
- [ ] Agregar diagramas de robustez/secuencia para CU-FAC-002, CU-FAC-003, CU-ENT-004.
- [ ] Documentar los 10 CU secundarios (5 includes + 5 extends).
- [ ] Generar diagramas de robustez y secuencia para cada uno.