# Prototipo de fronteras ICONIX

Prototipo navegable que representa las pantallas asociadas a los diagramas de
robustez del flujo comercial. Su objetivo es mostrar, con fines didácticos, la
trazabilidad entre:

- **Boundary**: pantalla, formulario, botón, enlace, tabla o mensaje visible.
- **Control**: acción disparada por una interacción.
- **Entity**: modelo y datos consultados o modificados.

## Abrir

No requiere instalación ni servidor. Abrir `index.html` en un navegador.

Para servirlo localmente (opcional):

```bash
python3 -m http.server 8000 --directory prototipo
```

Luego visitar <http://localhost:8000>.

## Escenarios incluidos

| Pantalla | Caso de uso | Diagrama de robustez |
|---|---|---|
| Presupuesto | CU-VEN-001 | D-ROB-VEN-001 |
| Confirmación | CU-VEN-004 | D-ROB-VEN-004 |
| Reserva | CU-ENT-002 | D-ROB-ENT-002 |
| Facturación | CU-FAC-001 | D-ROB-FAC-001 |

## Alcance

Es un prototipo educativo, no una reproducción exacta ni conectada a Odoo. Los
datos son ficticios y las acciones se ejecutan en memoria. Las correspondencias
se basan en las fuentes PlantUML existentes en `diagrams/plantuml/`.
