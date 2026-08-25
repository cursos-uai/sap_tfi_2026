# Prototipo de fronteras ICONIX

Prototipo navegable que representa las pantallas asociadas a los diagramas de
robustez del flujo comercial. Su objetivo es mostrar, con fines didácticos, la
trazabilidad entre:

- **Boundary**: pantalla, formulario, botón, enlace, tabla o mensaje visible.
- **Control**: acción disparada por una interacción.
- **Entity**: modelo y datos consultados o modificados.

## Abrir

No requiere instalación ni servidor. Abrir `index.html` en un navegador.

La versión publicada está disponible en:
<https://cursos-uai.github.io/sap_tfi_2026/>.

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

## Ejercicios interactivos

Abrir `ejercicios.html` para recorrer seis estaciones de aprendizaje:

1. fundamentos de diseño para el cambio y ocultamiento de información;
2. modelo de dominio;
3. casos de uso;
4. diagramas de robustez;
5. diagramas de secuencia;
6. diagramas de clases.

Los ejercicios ofrecen corrección inmediata, explicación de la respuesta y
progreso persistente en el navegador. La base teórica se encuentra citada al
pie de cada estación.

## Guías paso a paso

Abrir `guias.html` para resolver seis casos progresivos con una hoja de ruta:
comprender el problema, anticipar cambios, descomponer, diseñar interfaces,
establecer relaciones y validar el diseño. Cada paso permite registrar el
razonamiento, solicitar una pista y comparar al final con una solución modelo.

## Alcance

Es un prototipo educativo, no una reproducción exacta ni conectada a Odoo. Los
datos son ficticios y las acciones se ejecutan en memoria. Las correspondencias
se basan en las fuentes PlantUML existentes en `diagrams/plantuml/`.
