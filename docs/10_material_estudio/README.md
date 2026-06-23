# Material Educativo — SAP-TFI-2026

> Material pedagógico para estudiantes del curso SAP-TFI-2026 y revisores técnicos.

## ¿Qué encontrarás aquí?

Este material explica **cómo se aplicó la metodología ICONIX** para hacer ingeniería inversa de los módulos nativos de Odoo 19.0 (Ventas, Facturación, Entregas, Inventario). Está pensado para que cualquier estudiante o analista pueda entender el proceso y replicarlo.

## Secciones

| # | Sección | Descripción |
|---|---------|-------------|
| 1 | [¿Qué es ICONIX?](01_que_es_iconix.md) | Introducción a la metodología ICONIX |
| 2 | [Aplicación a Odoo](02_aplicacion_a_odoo.md) | Cómo se adaptó ICONIX a Odoo |
| 3 | [Cómo leer los CU](03_como_leer_los_cu.md) | Guía para leer las especificaciones de casos de uso |
| 4 | [Ejercicios prácticos](04_ejercicios_practicos.md) | Ejercicios para fijar los conceptos |

## Audiencia

- **Estudiantes** del curso SAP-TFI-2026 que están aprendiendo ICONIX.
- **Analistas funcionales** que necesitan entender Odoo antes de implementarlo.
- **Desarrolladores** que quieren entender cómo está estructurado Odoo por dentro.
- **Revisores técnicos** que validan que la documentación refleja el código real.

## Cómo usar este material

1. **Empezá por la sección 1** para entender qué es ICONIX.
2. **Leé la sección 2** para ver cómo se aplicó específicamente a Odoo.
3. **Usá la sección 3 como referencia** cada vez que leas un CU.
4. **Hacé los ejercicios de la sección 4** para fijar los conceptos.

## Regla de oro del material

> **Cada afirmación sobre Odoo tiene una fuente de evidencia.** Si no podés verificar una afirmación contra código, está marcada como `EV-INF` (inferencia pendiente). Si la podés verificar contra código real, está marcada como `EV-COD` (código verificado) con la ruta exacta del archivo y la línea.

## Cómo se generó

Este material fue generado por el agente `saptfi2026` (parte del swarm Hermano de Ale Sartorio) aplicando la metodología ICONIX de manera rigurosa, con verificación contra el código fuente oficial de Odoo 19.0 (rama `19.0` del repositorio `https://github.com/odoo/odoo`).