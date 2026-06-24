# Arquitectura General del Proyecto SAP-TFI-2026

## Nivel C4: Contexto

```
[Usuario] ───usa───> [Sistema Odoo 19]
                        │
                        │──consulta──> [PostgreSQL]
                        │
                        │──envía──> [Servicio de Email]
                        │
                        │──integra──> [Servicio de Pago]
```

### Actores externos

- **Usuario**: persona que opera Odoo (vendedor, operador de almacén, facturador).
- **Servicio de Email**: SMTP relay para envío de correos de presupuestos y confirmaciones.
- **Servicio de Pago**: pasarela de pago externa (integrable vía módulos).
- **PostgreSQL**: base de datos relacional que persiste todos los datos.

## Nivel C4: Contenedores

```
[Cliente Web (navegador)]
       │
       │ HTTPS
       ↓
[Servidor Odoo]
├── [Módulo sale] (Python)
├── [Módulo account] (Python)
├── [Módulo stock] (Python)
├── [Módulo product] (Python)
├── [Módulo mail] (Python)
├── [Módulo delivery] (Python)
└── [ORM Odoo]
       │
       │ conexión nativa
       ↓
[PostgreSQL]
```

### Componentes principales

| Componente | Descripción | Tecnología |
|------------|-------------|------------|
| Cliente Web | Interfaz de usuario | HTML/CSS/JS (servido por Odoo) |
| Servidor Odoo | Aplicación principal | Python + Odoo Framework |
| Módulo sale | Lógica de ventas | Python |
| Módulo account | Lógica contable | Python |
| Módulo stock | Lógica de inventario | Python |
| Módulo product | Lógica de productos | Python |
| Módulo mail | Comunicación (correos) | Python |
| Módulo delivery | Logística de entrega | Python |
| ORM Odoo | Capa de abstracción de datos | Python |
| PostgreSQL | Almacenamiento persistente | C |

## Diagrama PlantUML

Ver `diagrams/plantuml/d_arq_gen_001_arquitectura_general.puml`.

## Reglas arquitectónicas

- **RN-ARQ-001**: El servidor Odoo es el único punto de entrada al sistema.
- **RN-ARQ-002**: Toda la persistencia se realiza vía ORM Odoo (no acceso directo a DB).
- **RN-ARQ-003**: Los módulos extienden funcionalidad vía `_inherit` (ver `addons/sale/models/sale_order.py:36`).

## Pendientes de validación

- **EV-INF-019**: La arquitectura refleja la versión Community. Enterprise tendría módulos adicionales (`sale_subscription`, `sale_timesheet`, etc.).
- **EV-INF-020**: La integración con pasarela de pago no fue verificada en detalle.