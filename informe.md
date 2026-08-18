## Avance semana 1: se midieron 5 operaciones

## Conclusiones

### Recomendaciones de mejora

1. **Completar el registro de tiempos en todas las estaciones.** El CSV solo tiene un dato (estación 1, operación *llenar*, 20 s), pero el informe indica que se midieron 5 operaciones. Sin mediciones de las demás estaciones no se puede identificar el cuello de botella real ni priorizar mejoras con datos.
2. **Analizar la operación *llenar* como posible punto de atención.** Con 20 s por ciclo en la estación 1, conviene comparar ese tiempo con el estándar de la planta y evaluar si reducir variabilidad o automatizar pasos del llenado puede bajar el tiempo promedio por estación.

### Reflexión

- **¿Qué fue más rápido con IA?** Redactar el script `analisis.py`, la descripción del Pull Request y explicar conceptos como el *fast-forward* de `git pull`; la IA aceleró tareas de escritura y análisis que habrían tomado más tiempo hacer a mano.
- **¿Cuándo sirvió saber los comandos?** Al cambiar de rama, traer cambios del remoto y revisar el historial de commits; tener el control directo con Git permitió verificar cada paso del flujo cuando herramientas como `gh` o Python no estaban disponibles en el entorno.
