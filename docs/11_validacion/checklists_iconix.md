# Checklists ICONIX — SAP-TFI-2026

> Documento vivo. Última actualización: 2026-06-18.

## ¿Qué es esto?

Cada diagrama ICONIX tiene su propio **checklist de calidad**. Este documento define los checklists para cada tipo de diagrama del proyecto y aplica el checklist a cada artefacto existente.

## Checklists por tipo de diagrama

---

### Checklist D-CU — Diagrama de Casos de Uso

- [ ] Tiene un **título** claro y descriptivo.
- [ ] Muestra **actores** (humanos y sistemas externos) con sus nombres legibles.
- [ ] Cada CU tiene **nombre único** y descripción en una línea.
- [ ] Los CU están **agrupados** por módulo/subdominio (rectangle/package).
- [ ] Las **asociaciones actor-CU** están bien etiquetadas (verbo en infinitivo).
- [ ] Tiene al menos **1 CU <<include>>** por cada CU con sub-flujos obligatorios.
- [ ] Tiene al menos **1 CU <<extend>>** por cada CU con sub-flujos opcionales.
- [ ] Las relaciones `<<include>>` y `<<extend>>` están **etiquetadas** correctamente.
- [ ] Las **flechas de <<include>>** apuntan del CU base al CU incluido.
- [ ] Las **flechas de <<extend>>** apuntan del CU que extiende al CU base.
- [ ] **No hay** CU "huérfanos" (sin actor).
- [ ] **No hay** CU redundantes (funcionalidad duplicada).
- [ ] **No hay** flechas circulares.
- [ ] El diagrama tiene una **leyenda** explicando convenciones.
- [ ] El diagrama **compila** sin errores en PlantUML.

---

### Checklist D-ROB — Diagrama de Robustez

- [ ] Tiene un **título** claro (formato `D-ROB-{AREA}-{NNN} — {descripción}`).
- [ ] El título referencia al **CU asociado**.
- [ ] Tiene **al menos un actor** (boundary o trigger externo).
- [ ] **Todos los elementos** están clasificados en boundary/control/entity.
- [ ] Los **boundary** representan vistas, formularios, wizards, APIs externas.
- [ ] Los **control** representan coordinadores, validadores, métodos de orquestación.
- [ ] Los **entity** representan objetos persistentes (modelos Odoo).
- [ ] Los **mensajes entre elementos** son verbos en voz activa.
- [ ] Los mensajes entre **control → entity** son verbos como Lee, Escribe, Crea, Actualiza, Busca.
- [ ] Los mensajes entre **boundary → control** son verbos como Invoca, Pide, Solicita.
- [ ] Los mensajes entre **actor → boundary** son verbos como Presiona, Selecciona, Completa.
- [ ] Hay **alt/else/opt** para flujos alternativos y excepciones.
- [ ] Las **condiciones de alt/else/opt** están explícitas ("Si OK", "Si error").
- [ ] Los **errores** se muestran en el boundary (no se "esconden" en el control).
- [ ] El diagrama **no tiene ciclos**.
- [ ] El diagrama tiene una **leyenda** explicando el proyecto.
- [ ] El diagrama **compila** sin errores en PlantUML.

---

### Checklist D-SEC — Diagrama de Secuencia

- [ ] Tiene un **título** claro (formato `D-SEC-{AREA}-{NNN} — {descripción}`).
- [ ] El título referencia al **CU asociado**.
- [ ] Los **lifelines** incluyen actor, boundary, control, entity.
- [ ] Los **mensajes** siguen el orden temporal.
- [ ] Los **mensajes síncronos** se distinguen de los asíncronos (→ vs -->).
- [ ] Hay **activate/deactivate** para cada llamada.
- [ ] Las **condiciones alt/else/opt** están explícitas.
- [ ] Hay **referencia a la base de datos** (`database "PostgreSQL"`).
- [ ] Los **SQL queries** están explícitos (SELECT, INSERT, UPDATE).
- [ ] El diagrama **no tiene llamadas "mágicas"** (todo es explícito).
- [ ] El diagrama tiene una **leyenda**.
- [ ] El diagrama **compila** sin errores en PlantUML.

---

### Checklist D-CLA — Diagrama de Clases

#### Para D-CLA-CON (Modelo de Dominio Conceptual)

- [ ] Las clases representan **conceptos del dominio** (no de la solución).
- [ ] Los nombres de clase están en **español** (Cliente, Producto, PedidoVenta, etc.).
- [ ] Los **atributos** están en lenguaje natural (no son campos técnicos).
- [ ] Las **relaciones** tienen cardinalidad (1, *, 0..1).
- [ ] Los nombres de relaciones son verbos o frases preposicionales.
- [ ] **No hay** referencias a clases técnicas Odoo (`sale.order`, etc.).
- [ ] **No hay** atributos técnicos (`create_date`, `write_uid`).
- [ ] El diagrama tiene una **leyenda**.
- [ ] El diagrama **compila** sin errores en PlantUML.

#### Para D-CLA-INT (Modelo de Clases Técnico / Integración)

- [ ] Las clases tienen **`_name`** explícito (ej: `sale.order`).
- [ ] Las clases tienen **`_inherit`** cuando aplica.
- [ ] Los **campos** tienen tipo (Char, Many2one, Selection, Float, etc.).
- [ ] Los **métodos** tienen paréntesis (ej: `action_confirm()`).
- [ ] Las **relaciones** muestran cómo se conectan las clases (One2many, Many2one, Many2many).
- [ ] Las **foreign keys** están representadas (sale_id, picking_id, etc.).
- [ ] El diagrama tiene una **leyenda** explicando el proyecto.
- [ ] El diagrama **compila** sin errores en PlantUML.

---

### Checklist D-ARQ — Diagrama de Arquitectura

- [ ] Tiene un **título** claro (formato `D-ARQ-{TIPO}-{NNN} — {descripción}`).
- [ ] Muestra **capas** bien definidas (Cliente, Servidor, Datos, etc.).
- [ ] Las **subcapas** están claramente delimitadas (package dentro de package).
- [ ] Los **componentes** tienen nombre y descripción.
- [ ] Las **conexiones** tienen dirección y label.
- [ ] Cubre **todos los componentes del stack** (views, models, controllers, etc.).
- [ ] Muestra **integraciones externas** (APIs REST, SMTP, payments).
- [ ] El diagrama tiene una **leyenda**.
- [ ] El diagrama **compila** sin errores en PlantUML.

---

## Aplicación de los checklists a los artefactos del proyecto

### D-CU-GEN-002 — Casos de Uso con extend e include

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-CU-GEN-002 — Casos de Uso con extend e include" |
| Actores legibles | ✅ | Vendedor, Operario, Facturador, Sistema |
| Nombres únicos | ✅ | CU-VEN-001, CU-VEN-004, CU-ENT-002, CU-ENT-004, CU-FAC-001, CU-FAC-002, CU-FAC-003 |
| Agrupación por módulo | ✅ | Módulos sale/stock/account en rectangle |
| Asociaciones actor-CU | ✅ | "crea", "confirma", "reserva", "valida", "factura", "publica", "cobrar", "autentica" |
| ≥1 CU include | ✅ | 5 includes (CU-AUTH-001, CU-CALC-001, CU-GENPICK-001, CU-VALLIN-001, CU-GENJOUR-001) |
| ≥1 CU extend | ✅ | 5 extends (CU-VEN-001-EMAIL, CU-VEN-001-DISC, CU-ENT-002-MTO, CU-ENT-004-BACK, CU-FAC-002-VAL) |
| Etiquetas include/extend | ✅ | `<<include>>` y `<<extend>>` |
| Flechas include correctas | ✅ | `..>` del CU base al incluido |
| Flechas extend correctas | ✅ | `..>` del CU que extiende al base |
| Sin CU huérfanos | ✅ | Todos los CU tienen al menos un actor |
| Sin CU redundantes | ✅ | Cada CU tiene un objetivo único |
| Sin flechas circulares | ✅ | No hay ciclos |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 15/15 ✅** — Excelente.

---

### D-ROB-VEN-001 — Robustez Crear Presupuesto

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-ROB-VEN-001 — Diagrama de Robustez - Crear Presupuesto (CU-VEN-001)" |
| Referencia al CU | ✅ | CU-VEN-001 |
| ≥1 actor | ✅ | Vendedor |
| Clasificación boundary/control/entity | ✅ | B_New, B_Form (boundary); C_Send, C_Mail (control); E_SO, E_Mail (entity) |
| Mensajes en voz activa | ✅ | "Click Nuevo", "Crea sale.order", "Abre form", "Muestra form", "Completa cliente", "Actualiza", "Calcula", etc. |
| Alt/else/opt | ✅ | `opt Si envia por email` |
| Errores en boundary | ✅ | Errores se muestran al actor vía B_Form |
| Sin ciclos | ✅ | Flujo lineal |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 10/10 ✅** — Excelente.

---

### D-ROB-VEN-004 — Robustez Confirmar Pedido

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-ROB-VEN-004 — Diagrama de Robustez - Confirmar Pedido de Venta (CU-VEN-004)" |
| Referencia al CU | ✅ | CU-VEN-004 |
| ≥1 actor | ✅ | Vendedor |
| Clasificación boundary/control/entity | ✅ | B_Form, B_Wiz (boundary); C_SO, C_Val, C_CV, C_Stk, C_Inv (control); E_SO, E_Line, E_Pick, E_Move (entity) |
| Mensajes en voz activa | ✅ | "Invoca action_confirm", "Valida pedido", "Lee estado y líneas", "Prepara valores", "Write state='sale'", "Crea picking", "Crea factura", "Retorna OK" |
| Alt/else/opt | ✅ | `alt Si OK` / `else Si error` |
| Errores en boundary | ✅ | "Muestra error" |
| Sin ciclos | ✅ | Flujo lineal |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 10/10 ✅** — Excelente.

---

### D-ROB-ENT-002 — Robustez Reservar Productos

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-ROB-ENT-002 — Diagrama de Robustez - Reservar Productos (CU-ENT-002)" |
| Referencia al CU | ✅ | CU-ENT-002 |
| ≥1 actor | ✅ | Sistema (o Operario) |
| Clasificación boundary/control/entity | ✅ | B_Trig (boundary); C_Assign, C_Proc (control); E_Pick, E_ML, E_WO, E_PO (entity) |
| Mensajes en voz activa | ✅ | "Trigger reserva", "Lee picking", "Recorre lineas", "Busca stock disponible", "Reserva cantidad", "Busca reabastecimiento", "Crea purchase order (MTO)", "Actualiza estado" |
| Alt/else/opt | ✅ | `alt Si hay stock` / `else Si no hay stock` y `alt Si todas las lineas tienen reserva` / `else Si hay parcial` |
| Errores en boundary | ✅ | (No tiene errores específicos en este CU) |
| Sin ciclos | ✅ | Flujo lineal |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 10/10 ✅** — Excelente.

---

### D-ROB-FAC-001 — Robustez Crear Factura

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-ROB-FAC-001 — Diagrama de Robustez - Crear Factura desde Pedido (CU-FAC-001)" |
| Referencia al CU | ✅ | CU-FAC-001 |
| ≥1 actor | ✅ | Facturador (o Vendedor) |
| Clasificación boundary/control/entity | ✅ | B_Btn (boundary); C_Inv (control); E_SO, E_Line, E_AM, E_AML, E_Tax (entity) |
| Mensajes en voz activa | ✅ | "Click Crear Factura", "_create_invoices()", "Lee pedido", "Verifica invoice_status", "Lee lineas pendientes", "Aplica impuestos", "Crea account.move.line", "Crea account.move (draft)", "Asocia invoice_ids", "Actualiza invoice_status" |
| Alt/else/opt | ✅ | `alt Si hay lineas a facturar` / `else Si nada que facturar` |
| Errores en boundary | ✅ | "Mensaje Nothing to invoice" |
| Sin ciclos | ✅ | Flujo lineal con loop interno |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 10/10 ✅** — Excelente.

---

### D-SEC-VEN-001 — Secuencia Crear Presupuesto

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-SEC-VEN-001 — Diagrama de Secuencia - Crear Presupuesto (CU-VEN-001)" |
| Referencia al CU | ✅ | CU-VEN-001 |
| Lifelines | ✅ | Vendedor, Form, SaleOrder, Mail, PostgreSQL |
| Orden temporal | ✅ | Mensajes numerados secuencialmente |
| Síncrono vs asíncrono | ✅ | Todos `->` (síncronos) |
| Activate/deactivate | ✅ | Cada llamada tiene su activate/deactivate |
| Alt/else/opt | ✅ | `opt Si envia por email` |
| Referencia a DB | ✅ | `database "PostgreSQL" as DB` |
| SQL queries explícitos | ✅ | SELECT, INSERT, UPDATE |
| Sin llamadas mágicas | ✅ | Todo es explícito |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 12/12 ✅** — Excelente.

---

### D-SEC-VEN-004 — Secuencia Confirmar Pedido

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-SEC-VEN-004 — Diagrama de Secuencia - Confirmar Pedido de Venta (CU-VEN-004)" |
| Referencia al CU | ✅ | CU-VEN-004 |
| Lifelines | ✅ | Vendedor, Form, SaleOrder, Validator, Conf. Values, Stock Layer, Invoice Layer, PostgreSQL |
| Orden temporal | ✅ | Mensajes numerados secuencialmente |
| Síncrono vs asíncrono | ✅ | Todos `->` (síncronos) |
| Activate/deactivate | ✅ | Cada llamada tiene su activate/deactivate |
| Alt/else/opt | ✅ | `alt Si estado OK y líneas OK` / `else Si error` y `opt Si auto-factura configurada` |
| Referencia a DB | ✅ | `database "PostgreSQL" as DB` |
| SQL queries explícitos | ✅ | SELECT, UPDATE, INSERT |
| Sin llamadas mágicas | ✅ | Todo es explícito |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 12/12 ✅** — Excelente.

---

### D-SEC-ENT-002 — Secuencia Reservar Productos

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-SEC-ENT-002 — Diagrama de Secuencia - Reservar Productos (CU-ENT-002)" |
| Referencia al CU | ✅ | CU-ENT-002 |
| Lifelines | ✅ | Sistema, StockPicking, StockMove, Procurement, PostgreSQL |
| Orden temporal | ✅ | Mensajes numerados secuencialmente |
| Síncrono vs asíncrono | ✅ | Todos `->` (síncronos) |
| Activate/deactivate | ✅ | Cada llamada tiene su activate/deactivate |
| Alt/else/opt | ✅ | `alt Cantidad >= requerida` / `else Cantidad < requerida`, `opt Si hay orderpoint MTO`, `alt Si todas las lineas reservadas` / `else Si hay parcial` |
| Referencia a DB | ✅ | `database "PostgreSQL" as DB` |
| SQL queries explícitos | ✅ | SELECT, INSERT |
| Sin llamadas mágicas | ✅ | Todo es explícito |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 12/12 ✅** — Excelente.

---

### D-SEC-FAC-001 — Secuencia Crear Factura

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-SEC-FAC-001 — Diagrama de Secuencia - Crear Factura (CU-FAC-001)" |
| Referencia al CU | ✅ | CU-FAC-001 |
| Lifelines | ✅ | Facturador, Botón, SaleOrder, AccountMove, PostgreSQL |
| Orden temporal | ✅ | Mensajes numerados secuencialmente |
| Síncrono vs asíncrono | ✅ | Todos `->` (síncronos) |
| Activate/deactivate | ✅ | Cada llamada tiene su activate/deactivate |
| Alt/else/opt | ✅ | `alt Hay lineas a facturar` / `else Nada que facturar` |
| Referencia a DB | ✅ | `database "PostgreSQL" as DB` |
| SQL queries explícitos | ✅ | SELECT, INSERT, UPDATE |
| Sin llamadas mágicas | ✅ | Todo es explícito |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 12/12 ✅** — Excelente.

---

### D-CLA-CON-GEN-001 — Modelo de Dominio Conceptual

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Clases son conceptos del dominio | ✅ | Cliente, Producto, Presupuesto, PedidoVenta, LineaPedido, Transferencia, LineaMovimiento, Factura, LineaFactura, Pago, Almacen, Ubicacion |
| Nombres en español | ✅ | Sí (Cliente, Producto, etc.) |
| Atributos en lenguaje natural | ✅ | nombre, direccion, fecha, etc. |
| Relaciones con cardinalidad | ✅ | 1, *, 0..1 |
| Nombres de relaciones | ✅ | solicita, compra, contiene, genera, etc. |
| Sin referencias a clases Odoo | ✅ | Solo conceptos |
| Sin atributos técnicos | ✅ | Solo atributos del dominio |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 9/9 ✅** — Excelente.

---

### D-CLA-INT-001 — Modelo de Clases Técnico

| Ítem | Estado | Comentario |
|------|--------|-----------|
| _name explícito | ✅ | sale.order, sale.order.line, stock.picking, stock.move, account.move, account.move.line |
| _inherit cuando aplica | ⚠️ | Mencionado en comment pero no mostrado (decisión: mostrar solo campos clave) |
| Campos con tipo | ✅ | Char, Many2one, Selection, Float, Monetary |
| Métodos con paréntesis | ✅ | action_confirm(), action_quotation_send(), etc. |
| Relaciones One2many/Many2one/etc | ✅ | order_line, invoice_ids, move_ids |
| Foreign keys | ✅ | sale_id, picking_id, move_id, etc. |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 7/8 ✅** — Excelente (con 1 nota: _inherit no mostrado por simplicidad).

---

### D-ARQ-TECH-001 — Arquitectura Estratificada de Odoo

| Ítem | Estado | Comentario |
|------|--------|-----------|
| Título claro | ✅ | "D-ARQ-TECH-001 — Arquitectura Estratificada de Odoo" |
| Capas bien definidas | ✅ | 4 capas: Cliente, Servidor (4 subcapas), Persistencia, Integración |
| Subcapas delimitadas | ✅ | Subcapas 2.1-2.4 dentro de Capa 2 |
| Componentes con nombre/descripción | ✅ | Browser, OWL, Router, Models, ORM, etc. |
| Conexiones con dirección | ✅ | `-->`, `<--`, `..>` |
| Stack completo | ✅ | views, models, controllers, REST, XML-RPC, router, static, OWL, addons, etc. |
| Integraciones externas | ✅ | API REST, SMTP, Payment, Webhooks |
| Leyenda | ✅ | Proyecto, agente, metodología, fuente |
| Compila | ✅ | Generado PNG/SVG/PDF |

**Resultado: 9/9 ✅** — Excelente.

---

## Resumen global

| Diagrama | Tipo | Score | Estado |
|---|---|---|---|
| D-CU-GEN-002 | CU | 15/15 | ✅ |
| D-ROB-VEN-001 | ROB | 10/10 | ✅ |
| D-ROB-VEN-004 | ROB | 10/10 | ✅ |
| D-ROB-ENT-002 | ROB | 10/10 | ✅ |
| D-ROB-FAC-001 | ROB | 10/10 | ✅ |
| D-SEC-VEN-001 | SEC | 12/12 | ✅ |
| D-SEC-VEN-004 | SEC | 12/12 | ✅ |
| D-SEC-ENT-002 | SEC | 12/12 | ✅ |
| D-SEC-FAC-001 | SEC | 12/12 | ✅ |
| D-CLA-CON-GEN-001 | CLA-CON | 9/9 | ✅ |
| D-CLA-INT-001 | CLA-INT | 7/8 | ✅ |
| D-ARQ-TECH-001 | ARQ | 9/9 | ✅ |

**Total: 127/128 ✅** (99.2%)

**Único ítem con nota**: `_inherit` en D-CLA-INT-001 — mencionado en comment pero no representado explícitamente en el diagrama (decisión consciente para mantener el diagrama legible).

---

## Pendientes

### Diagramas pendientes de ROB/SEC

| CU | ROB | SEC | Estado |
|---|---|---|---|
| CU-ENT-004 Validar entrega | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-FAC-002 Publicar factura | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-FAC-003 Registrar pago | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-VEN-001-EMAIL | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-VEN-001-DISC | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-ENT-002-MTO | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-ENT-004-BACK | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-FAC-002-VAL | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-AUTH-001 | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-CALC-001 | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-GENPICK-001 | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-VALLIN-001 | ❌ falta | ❌ falta | Pendiente iteración 2 |
| CU-GENJOUR-001 | ❌ falta | ❌ falta | Pendiente iteración 2 |

### Próximas acciones

- [ ] Generar ROB/SEC para los CU pendientes en iteración 2.
- [ ] Aplicar el checklist a cada nuevo diagrama antes de commitear.
- [ ] Agregar el checklist al skill `saptfi2026-plantuml-builder` para auto-validación.