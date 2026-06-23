# Cómo leer los Casos de Uso

## Estructura de un CU

Cada archivo `cu_xxx_nnn_nombre.md` tiene **20 secciones fijas**. Vamos a recorrerlas una por una con un ejemplo real.

## Ejemplo: CU-VEN-001 Crear Presupuesto

Vamos a leer el archivo [`cu_ven_001_crear_presupuesto.md`](../../02_casos_uso/cu_ven_001_crear_presupuesto.md) sección por sección.

### 1. Objetivo

> *"Crear un presupuesto de venta (sales quotation) para un cliente en estado `draft`."*

**Qué te dice**: en una frase, qué hace el CU. Si no podés resumir el CU en una oración, probablemente está mal definido.

### 2. Alcance

> *"Módulo `sale` de Odoo 19.0. Aplica al modelo `sale.order`."*

**Qué te dice**: en qué parte del sistema aplica. El módulo y el modelo principal.

### 3. Nivel

> *"Primario (esencial para el proceso de ventas)."*

**Tres valores posibles**:
- **Primario**: esencial, no se puede eliminar.
- **Secundario**: importante pero no esencial.
- **Opcional**: nice-to-have.

### 4. Actor principal

> *"Vendedor (usuario con permisos `sales_team.group_sale_salesman`)."*

**Qué te dice**: quién inicia el CU. Siempre con el permiso técnico necesario.

### 5. Actores secundarios

> *"Cliente (consulta estado), Servicio de correo (envía presupuesto)."*

**Qué te dice**: otros actores involucrados pero que no inician el CU.

### 6. Interesados (stakeholders)

> *"Responsable de ventas (aprueba descuentos), Administración (visualiza pipeline)."*

**Qué te dice**: personas o sistemas afectados por el CU, aunque no participen directamente.

### 7. Disparador

> *"El vendedor hace clic en 'Nuevo' desde la vista kanban o tree de `sale.order`."*

**Qué te dice**: qué evento inicia el CU.

### 8. Precondiciones

> *"El usuario tiene acceso al módulo `sale`. Existe al menos un cliente activo en `res.partner`. El catálogo de productos contiene productos publicables."*

**Qué te dice**: qué condiciones deben cumplirse ANTES de que el CU pueda ejecutarse.

### 9. Garantías mínimas

> *"El sistema crea un registro `sale.order` en estado `draft` sin errores."*

**Qué te dice**: qué pasa **incluso si algo falla**. Por ejemplo, "se crea el registro aunque después falle otro paso".

### 10. Garantías de éxito

> *"El presupuesto tiene un `name` único asignado por la secuencia `sale.order`. Los totales se calculan automáticamente con impuestos."*

**Qué te dice**: qué pasa **cuando todo sale bien**.

### 11. Flujo principal (paso a paso)

> 1. Vendedor hace clic en "Nuevo" → sistema crea `sale.order` en estado `draft`.
> 2. Sistema asigna `name` con valor por defecto...
> 3. Vendedor selecciona `partner_id`...

**Qué te dice**: la secuencia de pasos **felices**. Cada paso debe ser verificable.

### 12. Flujos alternativos

> FA-01 — Aplicar descuento
> 1. Vendedor edita `discount` en una línea...

**Qué te dice**: variaciones del flujo principal. Se numeran como FA-NN.

### 13. Excepciones

> EX-01 — Cliente sin dirección de entrega
> 1. Al intentar confirmar (estado `sale`), sistema valida...

**Qué te dice**: qué pasa cuando algo falla. Se numeran como EX-NN.

### 14. Reglas de negocio

> - **RN-VEN-001**: `state` solo puede pasar de `draft` → `sent` → `sale`, o a `cancel`.

**Qué te dice**: reglas que el sistema debe enforzar. Se numeran como RN-{AREA}-{NNN}.

### 15. Datos de entrada / salida

**Entrada**: cliente, compañía, moneda, lista de precios, líneas.
**Salida**: registro `sale.order` persistido, líneas, correo.

**Qué te dice**: qué información fluye hacia adentro y hacia afuera.

### 16. Estados involucrados

> `draft` → `sent` → `sale` (o `cancel`).

**Qué te dice**: las transiciones de estado del modelo.

### 17. Pantallas involucradas

> - `view_sale_order_form`
> - `view_sale_order_kanban`
> - `view_sale_order_tree`

**Qué te dice**: las vistas que el usuario ve durante el CU.

### 18. Modelos y métodos de Odoo

> **Modelos**: `sale.order`, `sale.order.line`, `res.partner`, `product.product`...
> **Métodos**: `action_quotation_send()`, `action_confirm()`, `_compute_amounts()`...

**Qué te dice**: las clases técnicas de Odoo y sus métodos. Acá empieza el modelo técnico.

### 19. Permisos y configuraciones

> - `sales_team.group_sale_salesman` (vendedor)
> - `sales_team.group_sale_manager` (responsable)

**Qué te dice**: permisos requeridos y configuraciones que afectan el CU.

### 20. Evidencias de ingeniería inversa

> **EV-COD-001**: `addons/sale/models/sale_order.py:34-36` — definición de la clase `SaleOrder` con `_name = 'sale.order'`.

**Qué te dice**: **la fuente exacta** que respalda cada afirmación. **Esta es la sección más importante** del CU.

## Cómo navegar un CU para entender un proceso

1. **Empezá por el Objetivo y el Disparador** (sección 1 y 7).
2. **Leé el Flujo principal** (sección 11) para entender el camino feliz.
3. **Revisá las Reglas de negocio** (sección 14) para entender las restricciones.
4. **Leé las Evidencias** (sección 20) para validar que lo que dice el CU coincide con el código real.
5. Si necesitás detalle técnico, mirá las secciones 17-19 (pantallas, modelos, métodos).

## Diferencia entre CU y método técnico

Un **CU** describe **qué** hace el sistema desde la perspectiva del usuario. Un **método técnico** describe **cómo** lo hace.

Por ejemplo:

| CU | Método |
|----|--------|
| *"Vendedor confirma el pedido"* | `sale.order.action_confirm()` |
| *"El sistema valida que las líneas tengan producto"* | `_confirmation_error_message()` retorna string si hay error |
| *"Se envía email al cliente"* | `action_quotation_send()` abre wizard de email |

Cuando leas un CU, **no te pierdas en los métodos**. Lee primero el flujo, después mirá los métodos para entender la implementación.

## Próxima sección

→ [Ejercicios prácticos](04_ejercicios_practicos.md) — para fijar los conceptos.