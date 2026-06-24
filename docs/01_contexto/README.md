# Contexto del Proyecto SAP-TFI-2026

## Stack tecnológico

- **Odoo 19.0 Community** (rama `19.0` del repo oficial `https://github.com/odoo/odoo`)
- **Base de datos:** PostgreSQL
- **Servidor:** Odoo (Python 3.11+)
- **Frontend:** Odoo Web Client (HTML/CSS/JS)

## Módulos Odoo relevantes (versión 19.0)

Verificado contra código fuente:

| Módulo | Versión | Path |
|--------|---------|------|
| sale | 1.2 | `addons/sale/` |
| sale_management | 1.0 | `addons/sale_management/` |
| sale_stock | 1.0 | `addons/sale_stock/` |
| account | 1.4 | `addons/account/` |
| stock | 1.1 | `addons/stock/` |
| product | 1.2 | `addons/product/` |
| purchase | 1.2 | `addons/purchase/` |
| delivery | 1.0 | `addons/delivery/` |
| mail | 1.19 | `addons/mail/` |
| contacts | (en repo) | `addons/contacts/` |
| uom | 1.0 | `addons/uom/` |

> **EV-DOC-001**: Versiones extraídas de `__manifest__.py` de cada módulo en la rama `19.0` de `https://github.com/odoo/odoo`. Verificables con `grep '"version"' addons/<módulo>/__manifest__.py`.

## Versión analizada

- **Odoo:** 19.0 (rama `19.0`)
- **Edición:** Community
- **Último commit en la rama:** `aa417106 [IMP] payment_redsys: add error code message mapping`
- **Path local:** `~/proyectos/odoo_src/odoo`

## Arquitectura general

```
Usuario (navegador)
  │
  ↓ HTTPS
  │
Odoo Server (Python + PostgreSQL)
  │
  ├── sale (sale.order, sale.order.line)
  ├── account (account.move, account.move.line)
  ├── stock (stock.picking, stock.move)
  ├── product (product.product, product.template)
  ├── delivery (delivery.carrier)
  └── mail (mail.thread, mail.activity)
```

## Contexto del dominio

El proyecto analiza cómo Odoo implementa el flujo completo de ventas
desde la creación de un presupuesto hasta el registro del pago, pasando
por la confirmación, reserva de stock, entrega y facturación.