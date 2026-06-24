# Estilos Arquitectónicos aplicados a Odoo 19.0

> Documento vivo. Última actualización: 2026-06-18.
> Basado en el apunte de la materia sobre estilos arquitectónicos.

## Diagrama

Ver `diagrams/plantuml/d_arq_tech_002_estilos_arquitectonicos.puml`.

## ¿Qué son los estilos arquitectónicos?

Un **estilo arquitectónico** es un conjunto de principios y patrones que define cómo se organizan los componentes de un sistema, cómo interactúan entre sí y qué restricciones se imponen. Diferentes estilos son apropiados para diferentes tipos de sistemas.

En la práctica, los sistemas complejos como Odoo **combinan varios estilos arquitectónicos** en distintas partes. A continuación se describen los estilos identificados en la arquitectura de Odoo 19.0.

---

## Estilos identificados en Odoo 19.0

### 1. Cliente-Servidor (Client-Server)

**Descripción**: el sistema se divide en dos partes: un cliente que solicita servicios y un servidor que los provee. La comunicación es típicamente request-response.

**Aplicación en Odoo**:
- El navegador web (cliente) hace HTTP requests al servidor Odoo.
- El servidor Odoo procesa cada request y devuelve la respuesta (HTML, JSON, PDF, etc.).
- El servidor no inicia la comunicación; siempre es el cliente quien lo hace.

**Evidencia**:
- **EV-ARQ-001**: Toda la comunicación se realiza vía HTTP/HTTPS (ver `addons/web/http.py`).

### 2. 3-Tier / N-Tier

**Descripción**: el sistema se divide en tres o más capas lógicas separadas: presentación, lógica de negocio y datos. Cada capa se comunica solo con la capa adyacente.

**Aplicación en Odoo** (N-Tier con 4 capas):
- **Capa 1**: Cliente (navegador).
- **Capa 2**: Servidor de aplicación Odoo (con 4 subcapas: Presentación, Web, Logic, Addons).
- **Capa 3**: Persistencia (PostgreSQL, Filestore).
- **Capa 4**: Integración externa (servicios de terceros).

**Beneficio**: cada capa puede escalarse, modificarse o reemplazarse independientemente.

### 3. MVC (Modelo-Vista-Controlador)

**Descripción**: patrón arquitectónico que separa la lógica de negocio (Modelo), la presentación (Vista) y el manejo de requests (Controlador).

**Aplicación en Odoo** (MVC extendido):

| Componente MVC | Implementación en Odoo |
|----------------|--------------------------|
| **Modelo** | `models/*.py` (clases Python que heredan de `models.Model`). Encapsula datos y lógica de negocio. |
| **Vista** | `views/*.xml` (form, tree, kanban, search). Define cómo se presentan los datos. |
| **Controlador** | `controllers/*.py` (clases Python que heredan de `http.Controller`). Manejan HTTP requests. |

**Diferencia con MVC clásico**: en Odoo, los controllers son opcionales. La mayoría de las vistas se generan automáticamente a partir del modelo. Solo se usan controllers cuando se necesita lógica HTTP custom (ej: endpoints REST, webhooks).

**Evidencia**:
- **EV-ARQ-002**: `addons/web/controllers/main.py` — controllers principales de Odoo.
- **EV-ARQ-003**: `addons/sale/views/sale_order_views.xml` — vistas del modelo `sale.order`.

### 4. Capas (Layered Architecture)

**Descripción**: cada capa provee servicios a la capa superior y consume servicios de la capa inferior. Las capas están estrictamente separadas.

**Aplicación en Odoo** (4 subcapas dentro de Capa 2):
- **Capa 2.1: Presentación**: OWL, Views (XML), Static.
- **Capa 2.2: Web Layer**: Router, Controllers, JSON-RPC, XML-RPC.
- **Capa 2.3: Business Logic**: Models, ORM, Computed.
- **Capa 2.4: Addons**: sale, account, stock, product (extensiones modulares).

**Beneficio**: cada capa tiene responsabilidades claras y límites bien definidos.

### 5. Pipe-and-Filter

**Descripción**: el procesamiento de datos se organiza como una cadena de filtros (procesadores) conectados por pipes (conductos). Cada filtro transforma los datos y los pasa al siguiente.

**Aplicación en Odoo**:
- El pipeline de HTTP requests pasa por varios filtros antes de llegar al controller:
  1. **Autenticación** (validación de sesión).
  2. **Routing** (resolución de URL a controller).
  3. **CSRF check** (validación de token).
  4. **Controller** (procesamiento del request).
  5. **Response** (renderizado a JSON/HTML).

**Evidencia**:
- **EV-ARQ-004**: `addons/web/http.py` — pipeline de middlewares de Odoo.

### 6. Microkernel (Plugin-Based)

**Descripción**: el sistema tiene un núcleo mínimo que provee funcionalidades básicas, y las funcionalidades adicionales se agregan como plugins (módulos).

**Aplicación en Odoo**:
- El núcleo de Odoo provee el ORM, el framework HTTP y los modelos base (`res.partner`, `res.company`).
- Los addons extienden el núcleo vía `_inherit`:
  - `sale` extiende `mail.thread` y agrega `sale.order`.
  - `account` extiende el modelo base y agrega `account.move`.
  - `stock` agrega `stock.picking`, `stock.move`, etc.

**Beneficio**: el sistema puede extenderse sin modificar el código del núcleo.

**Evidencia**:
- **EV-ARQ-005**: `addons/sale/models/sale_order.py:36` — `_inherit = ['portal.mixin', 'product.catalog.mixin', 'mail.thread', ...]`.

### 7. Repository

**Descripción**: encapsula el acceso a datos detrás de una interfaz orientada a objetos. El cliente no interactúa directamente con la base de datos.

**Aplicación en Odoo**:
- El ORM de Odoo encapsula el acceso a PostgreSQL.
- Los modelos definen sus campos en Python y el ORM se encarga de crear las tablas, hacer queries, gestionar transacciones, etc.
- El cliente (controller o vista) nunca hace SQL directamente; siempre interactúa con el ORM.

**Beneficio**: cambios en el esquema de BD no afectan la lógica de negocio.

**Evidencia**:
- **EV-ARQ-006**: `odoo/orm/` — implementación del ORM de Odoo.

### 8. Event-Driven

**Descripción**: el sistema reacciona a eventos publicados por otros componentes. Los componentes no se llaman entre sí directamente; se comunican vía eventos.

**Aplicación en Odoo**:
- **`mail.thread`**: registra todos los cambios al modelo como mensajes (eventos).
- **`onchange`**: dispara lógica cuando un campo cambia en el form.
- **`@api.depends`**: recalcula campos cuando otros campos cambian.
- **Cron jobs**: ejecutan tareas programadas periódicamente.
- **Webhooks**: notifican a sistemas externos cuando ocurren eventos.

**Beneficio**: bajo acoplamiento entre componentes.

---

## Combinación de estilos

Odoo **no usa un solo estilo**, sino una combinación de ellos. Esta es la práctica común en sistemas complejos.

| Estilo | Dónde se aplica | Por qué |
|--------|-----------------|---------|
| Cliente-Servidor | Toda la comunicación | Separación clara entre UI y lógica |
| 3-Tier | Capas 1, 2, 3 | Aislamiento entre cliente, lógica y datos |
| MVC | Capa 2 | Separación entre modelo, vista y controlador |
| Capas | Capa 2 (subcapas 2.1-2.4) | Organización modular interna |
| Pipe-and-Filter | Pipeline HTTP | Procesamiento ordenado de requests |
| Microkernel | Addons | Extensibilidad sin modificar núcleo |
| Repository | Capa 2.3 → Capa 3 | Abstracción de persistencia |
| Event-Driven | mail.thread, onchange, cron | Reactividad y desacoplamiento |

---

## Consecuencias arquitectónicas

### Beneficios

- **Extensibilidad**: nuevos addons pueden agregarse sin modificar el núcleo (Microkernel).
- **Mantenibilidad**: separación clara entre capas, MVC, lógica (Repository).
- **Escalabilidad**: cada capa puede escalarse independientemente (3-Tier).
- **Reusabilidad**: los addons pueden reutilizar funcionalidad de otros addons (Microkernel + MVC).
- **Interoperabilidad**: el sistema expone APIs estándar (JSON-RPC, XML-RPC) para integraciones externas (Cliente-Servidor).

### Trade-offs

- **Complejidad**: la combinación de 8 estilos puede ser difícil de entender para nuevos desarrolladores.
- **Performance**: el pipeline HTTP (Pipe-and-Filter) agrega latencia.
- **Acoplamiento entre addons**: si dos addons se acoplan fuertemente vía `_inherit`, pueden romperse mutuamente al actualizarse.
- **Curva de aprendizaje**: el ORM de Odoo (Repository) tiene una API específica que requiere tiempo para dominar.

---

## Relación con el apunte de la materia

Este documento aplica los conceptos del **apunte de la materia sobre estilos arquitectónicos** al caso concreto de Odoo 19.0. Los estudiantes deben:

1. Leer el apunte de la materia para entender los estilos teóricos.
2. Leer este documento para ver cómo se aplican a un sistema real.
3. Identificar los estilos en otros sistemas que conozcan (ej: otros ERPs, e-commerce, etc.).

---

## Referencias

- **Apunte de la materia sobre estilos arquitectónicos**: https://drive.google.com/file/d/0B8MI0532KYVjTzJTWGJMTXcxRUU/view?usp=sharing&resourcekey=0-KFIUox1cee5ulFXDP7MZVg
- Gamma et al. (2003). *Design Patterns*. — patrones GoF.
- Odoo S.A. (2024). *Odoo 19.0 Documentation*. https://www.odoo.com/documentation/19.0/
- Repositorio oficial de Odoo: https://github.com/odoo/odoo (rama `19.0`)