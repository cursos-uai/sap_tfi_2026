# SAP-TFI-2026 — Apunte de Clase

> Material de apoyo para la resolución del Trabajo Práctico de la sección técnica del curso SAP-TFI-2026.
> Facultad de Ciencias Exactas, Ingeniería y Agrimensura — Universidad Nacional de Rosario (o la institución que corresponda).
> Última actualización: 2026-06-18.

---

## ¿Qué es este repositorio?

Este repositorio es **material de apoyo** para que los alumnos del curso SAP-TFI-2026 puedan resolver el Trabajo Práctico (TP) de la sección técnica. Contiene:

- **Diagramas ICONIX** (PlantUML) de los casos de uso core del dominio ERP (Ventas, Facturación, Entregas, Inventario).
- **Documentación explicativa** de cada artefacto siguiendo la metodología ICONIX.
- **Casos de uso modelo** (CU-VEN-001, CU-VEN-004, CU-ENT-002, CU-ENT-004, CU-FAC-001, CU-FAC-002, CU-FAC-003) que sirven como referencia para el TP.
- **Material pedagógico** en `docs/10_material_estudio/` con guías paso a paso.
- **Checklists de calidad** en `docs/11_validacion/` para auto-evaluación de los diagramas.

### ¿Qué NO es este repositorio?

- **No es la solución del TP**. Cada alumno debe producir su propia versión.
- **No es código fuente** que el alumno deba ejecutar. Es documentación.
- **No es opcional**. El alumno debe usar este repositorio como punto de partida para entender la metodología ICONIX aplicada al dominio ERP.

---

## ¿Cómo está organizado?

```
sap_tfi_2026/
├── README.md                                  ← este archivo
├── docs/
│   ├── 00_plan/                               ← plan del proyecto
│   ├── 01_contexto/                           ← contexto de Odoo 19.0
│   ├── 02_casos_uso/                          ← 7 CU modelo (referencia para el TP)
│   ├── 03_dominio/                            ← modelo de dominio
│   ├── 04_arquitectura/                       ← arquitectura general
│   ├── 05_prototipos/                         ← prototipos de UI
│   ├── 09_trazabilidad/                       ← matriz de trazabilidad
│   ├── 10_material_estudio/                   ← material pedagógico
│   ├── 11_validacion/                         ← checklists ICONIX
│   └── 12_patrones_diseno/                    ← patrones de diseño aplicados
├── diagrams/
│   ├── plantuml/                              ← código fuente .puml
│   ├── png/                                   ← versiones PNG
│   ├── svg/                                   ← versiones SVG
│   └── pdf/                                   ← versiones PDF
├── evidence/
│   └── index.md                               ← catálogo de evidencias
└── .gitignore
```

---

## Cómo usar este repositorio para el TP

### Paso 1: Entender la metodología ICONIX

Antes de hacer cualquier diagrama, leé:

- **`docs/10_material_estudio/01_que_es_iconix.md`** — qué es ICONIX.
- **`docs/10_material_estudio/02_aplicacion_a_odoo.md`** — cómo se adaptó a Odoo.

### Paso 2: Estudiar los casos de uso modelo

Los 7 CU modelo están en **`docs/02_casos_uso/`**. Cada uno tiene la estructura completa:

- Nombre, objetivo, pre/post-condición
- Pasos trascendentes (en voz activa)
- Caminos alternativos
- Excepciones, reglas de negocio
- Diagramas asociados (robustez, secuencia, clases)

**Sugerencia**: empezá por `cu_ven_001_crear_presupuesto.md` (es el más simple) y avanzá progresivamente.

### Paso 3: Estudiar los diagramas

Los diagramas están en **`diagrams/plantuml/`** (código fuente) y **`diagrams/pdf/`** (versión renderizada).

Para visualizar:
- Abrí los PDFs directamente.
- Para regenerar: instalá PlantUML (`apt-get install plantuml` o descargá el jar).
- Para modificar: editá los `.puml` y regenerá.

### Paso 4: Aplicar ICONIX a tu TP

Para cada CU que debas documentar:

1. Identificá los actores.
2. Escribí la especificación del CU (usá `docs/02_casos_uso/cu_ven_001_crear_presupuesto.md` como plantilla).
3. Generá el diagrama de robustez (`diagrams/plantuml/d_rob_*.puml` como plantilla).
4. Generá el diagrama de secuencia (`diagrams/plantuml/d_sec_*.puml` como plantilla).
5. Generá el diagrama de clases técnico (`diagrams/plantuml/d_cla_int_*.puml` como plantilla).
6. Aplicá el checklist (`docs/11_validacion/checklists_iconix.md`).

### Paso 5: Validar

Antes de entregar tu TP:

- Aplicá los checklists de `docs/11_validacion/checklists_iconix.md`.
- Verificá que cada CU tenga su diagrama de robustez, secuencia y clases.
- Verificá que la matriz de trazabilidad esté completa.

---

## Ejemplos de diagramas ICONIX para casos de uso core de ERP

A continuación se muestran los diagramas principales del repositorio. Cada uno corresponde a un caso de uso core del dominio ERP.

### Ejemplo 1: Diagrama de Casos de Uso (D-CU-GEN-002)

El diagrama de CU muestra los casos de uso principales del flujo comercial, con relaciones `<<include>>` (sub-flujos obligatorios) y `<<extend>>` (sub-flujos opcionales).

**Actores**:
- Vendedor (crea presupuestos, confirma pedidos)
- Operario de Almacén (reserva productos, valida entregas)
- Facturador (crea, publica y registra pagos de facturas)
- Sistema (autentica)

**Casos de uso principales**:
- `CU-VEN-001` Crear presupuesto
- `CU-VEN-004` Confirmar pedido de venta
- `CU-ENT-002` Reservar productos en almacén
- `CU-ENT-004` Validar entrega de productos
- `CU-FAC-001` Crear factura desde pedido
- `CU-FAC-002` Publicar factura
- `CU-FAC-003` Registrar pago

**5 relaciones <<include>>** (sub-flujos obligatorios):
- `CU-AUTH-001` Validar sesión de usuario (incluido por CU-VEN-001 y CU-VEN-004)
- `CU-CALC-001` Calcular totales con impuestos (incluido por CU-VEN-001)
- `CU-GENPICK-001` Generar picking de entrega (incluido por CU-VEN-004)
- `CU-VALLIN-001` Validar líneas pendientes (incluido por CU-FAC-001)
- `CU-GENJOUR-001` Crear asiento contable (incluido por CU-FAC-002)

**5 relaciones <<extend>>** (sub-flujos opcionales/condicionales):
- `CU-VEN-001-EMAIL` Enviar presupuesto por email (opcional)
- `CU-VEN-001-DISC` Aplicar descuento (opcional)
- `CU-ENT-002-MTO` Generar orden de compra (MTO) (opcional)
- `CU-ENT-004-BACK` Crear backorder de entrega parcial (opcional)
- `CU-FAC-002-VAL` Validar asiento anormal (opcional)

**Diagrama**: `diagrams/plantuml/d_cu_gen_002_casos_uso_extend_include.puml`

**Lección para el alumno**: en ICONIX, las relaciones `<<include>>` se usan para sub-flujos obligatorios (siempre se ejecutan), mientras que `<<extend>>` se usa para sub-flujos opcionales (solo se ejecutan bajo ciertas condiciones). El diagrama de CU debe mostrar ambos tipos cuando apliquen.

---

### Ejemplo 2: Diagrama de Robustez (D-ROB-VEN-001)

El diagrama de robustez muestra qué objetos intervienen en un CU, clasificándolos en boundary (vista), control (coordinador) y entity (objeto persistente).

Para el CU-VEN-001 (Crear Presupuesto):

- **Actor**: Vendedor
- **Boundary**: `Boton Nuevo`, `Form (view_sale_order_form)`
- **Control**: `SaleOrder (action_quotation_send)`, `Mail Compose (mail.compose.message)`
- **Entity**: `sale.order (draft)`, `mail.mail`

**Flujo principal** (pasos en voz activa):

1. Vendedor **presiona** "Nuevo" → Botón Nuevo **crea** sale.order en draft → abre form.
2. Vendedor **completa** cliente y líneas → form **actualiza** sale.order → recalcula totales.
3. (Opcional) Vendedor **presiona** "Enviar" → action_quotation_send **invoca** → marca enviado → Mail Compose **crea** mail.mail → **envía** email.

**Lección para el alumno**: el diagrama de robustez usa exactamente 3 tipos de elementos (boundary/control/entity). Los mensajes entre elementos son verbos en voz activa que después se traducen 1:1 a los pasos del CU. Si un verbo no aparece en el diagrama de robustez, no puede aparecer en la especificación del CU.

---

### Ejemplo 3: Diagrama de Secuencia (D-SEC-VEN-004)

El diagrama de secuencia muestra las interacciones en el tiempo entre los lifelines (actor, vistas, controles, entidades, base de datos).

Para el CU-VEN-004 (Confirmar Pedido):

- **Lifelines**: Vendedor, Form, SaleOrder, Validator, Conf. Values, Stock Layer, Invoice Layer, PostgreSQL
- **Mensajes numerados** (orden temporal estricto)
- **Activate/deactivate** para cada llamada
- **Alt/else/opt** para flujos alternativos
- **SQL queries explícitos** (SELECT, INSERT, UPDATE)

**Lección para el alumno**: el diagrama de secuencia debe mostrar la base de datos explícitamente y los SQL queries como mensajes. Esto permite que un DBA o un desarrollador verifiquen la implementación sin tener que leer código.

---

### Ejemplo 4: Diagrama de Clases Técnico (D-CLA-INT-001)

El diagrama de clases técnico muestra las clases reales de Odoo con sus `_name`, `_inherit`, campos y métodos.

Para la integración venta/stock/contabilidad:

- `<sale.order>` (modelo `_name = 'sale.order'`, `_inherit = ['mail.thread', ...]`)
- `<sale.order.line>` (líneas de pedido)
- `<stock.picking>` (entregas)
- `<stock.move>` (movimientos)
- `<account.move>` (facturas)
- `<account.move.line>` (líneas de factura)

**Relaciones**:
- SO "1" *-- "*" SOL : order_line (One2many)
- SO "1" *-- "*" AM : invoice_ids
- SP "*" --> "1" SO : sale_id
- AM "*" --> "1" SOL : invoice_line_ids

**Lección para el alumno**: el diagrama de clases técnico refleja el código real de Odoo, no el modelo conceptual. Cada clase tiene `_name` (nombre técnico) y los campos tienen tipo (Many2one, One2many, Float, etc.). Las relaciones muestran cómo se conectan los modelos vía foreign keys.

---

### Ejemplo 5: Diagrama de Arquitectura Estratificada (D-ARQ-TECH-001)

El diagrama de arquitectura muestra las capas del stack tecnológico de Odoo:

- **Capa 1**: Cliente (navegador, JS runtime)
- **Capa 2**: Servidor de aplicación (4 subcapas: Presentación, Web, Logic, Addons)
- **Capa 3**: Persistencia (PostgreSQL, Filestore)
- **Capa 4**: Integración externa (REST API, SMTP, Payment, Webhooks)

**Lección para el alumno**: el diagrama de arquitectura debe mostrar TODAS las capas relevantes del stack, no solo la capa de aplicación. Esto permite entender dónde corre cada componente y cómo se comunican entre capas.

---

### Ejemplo 6: Patrón Composite aplicado a BoM (D-PAT-COMPOSITE-001)

El diagrama del patrón Composite muestra cómo Odoo implementa la Lista de Materiales (Bill of Materials) usando el patrón Composite de GoF:

- **Component** (interfaz abstracta) → `BomComponent`
- **Leaf** (producto simple) → `product.product`
- **Composite** (producto con BoM) → `mrp.bom`
- **children** (lista de hijos) → campo `bom_line_ids` (One2many)
- **Operation** → método `explode(product, quantity)`

**Lección para el alumno**: Odoo usa patrones de diseño estándar (GoF). Identificar el patrón aplicado a cada subsistema es clave para entender cómo está estructurado el código. La documentación del patrón debe seguir el estándar de la FCEIA-UNR (Cristia, 2015).

---

## Recursos adicionales

### Material pedagógico

- **`docs/10_material_estudio/README.md`** — índice del material de estudio.
- **`docs/10_material_estudio/01_que_es_iconix.md`** — qué es ICONIX.
- **`docs/10_material_estudio/02_aplicacion_a_odoo.md`** — cómo se aplicó a Odoo.
- **`docs/10_material_estudio/03_como_leer_los_cu.md`** — cómo leer las CU.
- **`docs/10_material_estudio/04_ejercicios_practicos.md`** — ejercicios prácticos.

### Validación

- **`docs/11_validacion/checklists_iconix.md`** — checklists por tipo de diagrama, con aplicación a los 12 diagramas existentes.

### Patrones de diseño

- **`docs/12_patrones_diseno/composite_bom.md`** — patrón Composite aplicado a BoM, con documentación siguiendo estándar UNR.

### Evidencias

- **`evidence/index.md`** — catálogo de 30 EV-COD y 8 EV-INF verificables contra código real de Odoo 19.0.

---

## Recomendaciones para el TP

1. **No copies directamente**. Los CU modelo son para entender la metodología, no para copiar. Cada alumno debe producir su propia versión adaptada a su contexto.

2. **Verificá contra código real**. Cada afirmación sobre Odoo debe tener una evidencia EV-COD con ruta exacta del archivo y línea. Esto distingue la ingeniería inversa seria de la invención.

3. **Usá los checklists antes de entregar**. Aplicá los checklists de `docs/11_validacion/checklists_iconix.md` antes de entregar el TP. Un diagrama que no pasa el checklist no debe ser entregado.

4. **Compilá los .puml**. Un .puml que no compila no sirve. Antes de entregar, regenerá todos los PDFs y verificá que se ven bien.

5. **Mantené la trazabilidad**. Cada CU debe tener su diagrama de robustez, secuencia y clases. La matriz de trazabilidad debe estar completa.

---

## Contacto y soporte

- **Operador del repositorio**: Ale Sartorio
- **Issues**: usar el sistema de issues del repositorio en GitHub
- **Email**: (según corresponda al curso)

---

## Licencia

Este material se distribuye bajo la licencia Creative Commons BY-SA 4.0. Podés usarlo, modificarlo y redistribuirlo libremente, citando la fuente.