# Patrón Composite aplicado a Lista de Materiales (BoM) en Odoo 19.0

> Documento vivo. Última actualización: 2026-06-18.
> Formato: Estándar de la FCEIA-UNR para documentación de patrones de diseño (Cristia, 2015).

---

## Diagrama

Ver `diagrams/plantuml/d_pat_composite_001_bom.puml`.

---

## Documentación del Patrón

```
Pattern EstructuraProducto based on Composite because

Cambios previstos: i) un producto está compuesto por uno o más componentes
(sub-productos o materia prima); ii) los componentes son a su vez productos
que pueden estar compuestos por otros componentes (recursión); iii) es
necesario calcular el costo total y la lista plana de materiales de un
producto recorriendo la jerarquía completa; iv) la jerarquía debe
validarse para detectar ciclos; v) el cliente (interfaz, motor de
manufactura, reportes) debe tratar uniformemente productos simples y
compuestos.

Estos cambios son los admitidos por el patrón Composite según Gamma et
al. (2003): representación uniforme de objetos individuales y compuestos,
composición recursiva, y delegación de operaciones.

where
    Component             is BomComponent
    Component             is BomComponent (repetido por cada participante que comparte la interfaz)
    Leaf                  is ProductProduct (producto simple sin BoM)
    Composite             is MrpBom (producto con BoM)
    Composite             is MrpBom (repetido: cada BoM de Odoo es un Composite)
    children              is bom_line_ids (campo One2many de MrpBom)
    Operation()           is explode(product, quantity) (método recursivo de MrpBom)
    Operation()           is get_cost() (método polimórfico)
    Operation()           is get_quantity() (método polimórfico)
    add(Component)        is _onchange_product_id() (en MrpBomLine, agrega un componente)
    remove(Component)     is _onchange_product_id() (en MrpBomLine, elimina un componente)
    getChild(int)         is _compute_child_bom_id() (en MrpBomLine, obtiene el BoM hijo)

comments
La interfaz BomComponent define las operaciones que cualquier participante
del patrón (sea Leaf o Composite) debe soportar: get_product_id(),
get_quantity(), get_uom(), get_cost(), explode(). En Python no existe
interfaz formal, pero los modelos MrpBom y MrpBomLine exponen estos métodos
como un contrato implícito.

Leaf (product.product sin BoM asociado): un producto simple que no se
descompone. Responde a get_cost() con su propio standard_price. El método
explode() retorna una lista vacía o con el único componente (él mismo).

Composite (mrp.bom): representa un producto que se descompone en otros
productos. Mantiene una colección de hijos (bom_line_ids) y delega el
trabajo recursivo en su método explode(). Cuando explode() procesa una
línea, si esa línea tiene un child_bom_id (computed field que apunta al
BoM del producto hijo), se invoca recursivamente explode() sobre ese
BoM hijo.

La relación "children" del Composite se modela en Odoo como un One2many
(bom_line_ids) desde MrpBom hacia MrpBomLine. La relación inversa es un
Many2one (bom_id) en MrpBomLine. El campo computado child_bom_id en
MrpBomLine permite la navegación automática hacia el BoM del producto
hijo (si existe), facilitando la recursión sin necesidad de lookups
adicionales.

La validación de ciclos (_check_bom_cycle) es crítica en este patrón:
sin ella, una estructura mal configurada podría generar recursión
infinita. El método recorre recursivamente la jerarquía detectando si
un producto aparece como descendiente de sí mismo.

Verificacion de completitud: todos los elementos estructurales del patrón
Composite (Component, Leaf, Composite, children, Operation, add, remove,
getChild) están mapeados a elementos concretos del diseño. La repetición
intencional de Composite y Component en múltiples cláusulas `is` cumple
con la regla 1 del estándar (Gamma et al. y Cristia).
```

---

## Estructura del Patrón

### Participants (GoF)

| Participant | Rol en el patrón |
|-------------|------------------|
| **Component** | Declara la interfaz común para todos los objetos de la composición. Implementa el comportamiento por defecto. Declara la interfaz para acceder y gestionar los hijos. |
| **Leaf** | Representa objetos hoja (sin hijos) en la composición. Define el comportamiento para objetos primitivos. |
| **Composite** | Define el comportamiento para componentes que tienen hijos. Almacena los componentes hijos. Implementa las operaciones de la interfaz Component delegando en los hijos. |
| **Client** | Manipula los objetos de la composición a través de la interfaz Component. |

### Elementos del Patrón Mapeados al Diseño de Odoo

| Elemento Patrón | Elemento Diseño | Tipo | Ubicación |
|-----------------|-----------------|------|-----------|
| `Component` | `BomComponent` | interfaz abstracta (Python) | Contrato implícito |
| `Component` | `BomComponent` (repetido) | | (clientes múltiples) |
| `Leaf` | `product.product` | clase concreta | `addons/product/models/product_product.py` |
| `Composite` | `mrp.bom` | clase concreta | `addons/mrp/models/mrp_bom.py:12` |
| `Composite` | `mrp.bom` (repetido) | | (cada BoM es un Composite) |
| `children` | `bom_line_ids` | atributo (One2many) | `mrp_bom.py:40` |
| `Operation()` | `explode(product, quantity)` | método | `mrp_bom.py:419` |
| `Operation()` | `get_cost()` | método polimórfico | contrato implícito |
| `Operation()` | `get_quantity()` | método polimórfico | contrato implícito |
| `add(Component)` | `_onchange_product_id()` | método | `mrp_bom.py:114` |
| `remove(Component)` | `unlink()` (CRUD Odoo) | método | ORM estándar |
| `getChild(int)` | `_compute_child_bom_id()` | método (computed) | `mrp_bom.py:734` |

---

## Análisis de Cambios

### Cambios que el Patrón Admite

| Cambio | Soporte del Patrón | Aplicación en Odoo |
|--------|---------------------|---------------------|
| Agregar un nuevo tipo de componente | Sí (crear nueva subclase de Component) | Heredar de `mrp.bom` o `mrp.bom.line` |
| Agregar un nuevo tipo de hoja | Sí (crear nueva subclase de Leaf) | Heredar de `product.product` |
| Cambiar la estructura de la composición | Sí (modificar Composite) | Heredar `mrp.bom` para casos especiales |
| Añadir nuevas operaciones | Sí (añadir a Component) | Heredar `mrp.bom` con nuevos métodos |

### Cambios Anticipados en el Diseño

1. **Cálculo de costo multi-nivel**: hoy el costo se calcula para un solo nivel; podría requerir recursión profunda para obtener el costo "rolled-up" completo.
2. **Visualización del árbol de BoM**: actualmente se muestra aplanado; podría requerir una vista jerárquica tipo árbol.
3. **Variantes del producto**: hoy cada variante tiene su propio BoM; podría simplificarse parametrizando.
4. **Manufactura fantasma (phantom BoMs)**: ya soportado vía `bom_type='phantom'`; podría ampliarse a otros tipos.
5. **Operaciones (work orders)**: la lista de operaciones ya está en `mrp.routing.workcenter`; podría agregarse navegación desde Composite.

### Restricciones de Diseño Impuestas

- **Sin ciclos**: la jerarquía debe ser un DAG (Directed Acyclic Graph). Validado por `_check_bom_cycle()`.
- **Composición finita**: todos los `children` deben ser finitos (no se admite referencia infinita).
- **Interfaz uniforme**: `Leaf` y `Composite` deben responder al menos a `explode()`, `get_cost()`, `get_quantity()`.

---

## Variantes y Consideraciones

### Variante 1: Composite con Interfaz Diferenciada

En esta implementación, `mrp.bom.line` también es un participante del
patrón (es un Component de sí mismo, ya que referencia un `product_id`
que puede tener su propio BoM). Esto da una estructura de "doble nivel"
donde cada línea puede ser Leaf o Composite según el producto.

### Variante 2: Composite con Composición Compartida

Odoo permite que múltiples productos compartan el mismo BoM como sub-componente
(composite shared). Esto se logra haciendo que `child_bom_id` de varias
`mrp.bom.line` apunte al mismo `mrp.bom`. No es el caso típico de Composite,
pero es soportado por la implementación.

### Variante 3: Composición Recursiva con Ciclo Potencial

Si un producto A tiene un BoM que incluye el producto B, y B tiene un BoM
que incluye A, el patrón Composite entraría en recursión infinita. Por
eso Odoo implementa `_check_bom_cycle()` que se ejecuta en el constraint
`_check_bom_lines`. Esta validación es esencial y debe ejecutarse cada vez
que se modifica un BoM.

---

## Justificación Detallada (en términos del estándar UNR)

### Decisión de Aplicar el Patrón

Se eligió Composite porque el problema tiene las tres características
que lo justifican según Gamma et al. (2003, p. 151):

1. **Representar jerarquías parte-todo**: los productos se componen de
   sub-productos que a su vez pueden componerse de otros sub-productos.

2. **Tratamiento uniforme de objetos simples y compuestos**: el cliente
   (motor de manufactura, reportes, etc.) no debe distinguir si un
   producto es simple (Leaf) o compuesto (Composite); ambos responden
   a las mismas operaciones.

3. **Estructura recursiva**: cualquier nivel de anidamiento debe ser
   soportado, no solo dos niveles.

### Análisis de Alternativas

| Alternativa | Razón para descartarla |
|-------------|------------------------|
| Lista simple de componentes (sin recursión) | No soporta productos con sub-productos |
| Clase separada para cada nivel | Explosión combinatoria de clases |
| Tabla única sin relación padre-hijo | Difícil de navegar y mantener |

---

## Verificación con Código Real (EV-COD)

- **EV-COD-031**: `addons/mrp/models/mrp_bom.py:12-17` — definición de `MrpBom` con `_name='mrp.bom'`, `_inherit=['mail.thread', 'product.catalog.mixin']`.
- **EV-COD-032**: `addons/mrp/models/mrp_bom.py:683-685` — definición de `MrpBomLine` con `_name='mrp.bom.line'`.
- **EV-COD-033**: `addons/mrp/models/mrp_bom.py:40` — campo `bom_line_ids = fields.One2many('mrp.bom.line', 'bom_id', 'BoM Lines', copy=True)`.
- **EV-COD-034**: `addons/mrp/models/mrp_bom.py:706` — campo `bom_id = fields.Many2one(...)` en MrpBomLine.
- **EV-COD-035**: `addons/mrp/models/mrp_bom.py:720-722` — campo computado `child_bom_id = fields.Many2one('mrp.bom', ...)` en MrpBomLine.
- **EV-COD-036**: `addons/mrp/models/mrp_bom.py:419-474` — método `explode(self, product, quantity, picking_type=False, never_attribute_values=False)`.
- **EV-COD-037**: `addons/mrp/models/mrp_bom.py:133-183` — método `_check_bom_cycle(self)` con detección recursiva de ciclos.
- **EV-COD-038**: `addons/mrp/models/mrp_bom.py:114` — método `_onchange_product_id(self)`.

## Referencias

- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (2003). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley. Composite: pp. 151-164.
- Cristia, M. (2015). *Standard for Documenting Design Patterns in Software Design*. FCEIA, Universidad Nacional de Rosario. Disponible en: https://www.fceia.unr.edu.ar/ingsoft/patrones-doc.pdf
- Odoo S.A. (2024). *Odoo 19.0 MRP Module - Bills of Materials*. Disponible en: https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/manufacturing.html