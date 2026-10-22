# Proyecto de mejora - Planta XYZ

Registro de tiempos de operación en la planta y cálculo del promedio por estación, para detectar el cuello de botella y priorizar mejoras con datos.

## Contenido

| Archivo | Para qué sirve |
| --- | --- |
| `analisis.py` | Lee `datos/tiempos.csv` e imprime el tiempo promedio por estación |
| `datos/tiempos.csv` | Mediciones: estación, operación y tiempo en segundos |
| `informe.md` | Avance de la semana 1, conclusiones y recomendaciones |

## Cómo ejecutarlo

Se necesita Python 3.

```powershell
python analisis.py
```

La salida es el tiempo promedio, en segundos, de cada estación que tenga filas en el CSV.

## Formato de los datos

El CSV usa estas columnas:

- `estacion`
- `operacion`
- `tiempo_seg`

`tiempo_seg` es un número en segundos. Cada fila es una medición.

## Estado

El informe de la semana 1 dice que se midieron 5 operaciones y recuerda un único dato (estación 1, operación *llenar*, 20 s). El CSV todavía no trae esas filas, así que el script no puede señalar el cuello de botella real hasta completar el registro. Las recomendaciones están en `informe.md`.
