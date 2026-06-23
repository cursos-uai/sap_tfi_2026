# Plan del Proyecto SAP-TFI-2026

> Documento vivo. Última actualización: 2026-06-18.

## Objetivo

Realizar la ingeniería inversa de los módulos nativos de Odoo relacionados
con Ventas, Facturación, Entregas e Inventario, y producir documentación
técnica completa aplicando la metodología ICONIX.

## Alcance de la primera iteración

- **Versión analizada:** Odoo 19.0 (Community)
- **Rama del repo de código fuente:** `19.0`
- **Path local del código fuente:** `~/proyectos/odoo_src/odoo`
- **Repo del proyecto:** `https://github.com/cursos-uai/sap_tfi_2026`
- **Rama de trabajo:** `feature/initial-iteration`

## Flujo analizado

```
Crear presupuesto (CU-VEN-001)
    ↓
Confirmar pedido de venta (CU-VEN-004)
    ↓
Reservar productos (CU-ENT-002)
    ↓
Validar entrega (CU-ENT-004)
    ↓
Crear factura (CU-FAC-001)
    ↓
Publicar factura (CU-FAC-002)
    ↓
Registrar pago (CU-FAC-003)
```

## Artefactos a generar (14)

1. Diagrama general de casos de uso (C1)
2-8. Siete especificaciones de CU (uno por cada paso del flujo)
9. Modelo de dominio inicial
10. Diagrama de arquitectura general (C4 nivel contexto)
11. Prototipo del formulario de presupuesto
12. Diagrama de robustez de confirmación de pedido
13. Diagrama de secuencia de confirmación de pedido
14. Diagrama de clases de integración venta/stock/contabilidad

## Convenciones

- Ver `AGENTS.md` del perfil `saptfi2026`.
- Evidencia: `EV-COD` (código), `EV-XML` (vista), `EV-UI` (UI), `EV-DB` (BD),
  `EV-DOC` (docs), `EV-TEST` (pruebas), `EV-INF` (inferencia).

## Estado

| Artefacto | Estado |
|-----------|--------|
| Estructura del repo | ✅ |
| Código fuente Odoo 19 clonado | ✅ |
| Artefactos 1-14 | ⏳ (en esta iteración) |
| Matriz de trazabilidad | ⏳ (al final de la iteración) |
| Validación con Ale | ⏳ (después del commit) |
| Push a GitHub | ⏳ (Ale ejecuta manualmente) |