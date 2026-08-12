"""Calcula el tiempo promedio por estación a partir de datos/tiempos.csv."""

import csv
from collections import defaultdict
from pathlib import Path


def cargar_tiempos(archivo: Path) -> dict[str, list[float]]:
    tiempos_por_estacion: dict[str, list[float]] = defaultdict(list)

    with archivo.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            fila = {clave.strip(): valor.strip() for clave, valor in fila.items()}
            estacion = fila["estacion"]
            tiempo = float(fila["tiempo_seg"])
            tiempos_por_estacion[estacion].append(tiempo)

    return tiempos_por_estacion


def main() -> None:
    archivo = Path(__file__).parent / "datos" / "tiempos.csv"
    tiempos_por_estacion = cargar_tiempos(archivo)

    print("Tiempo promedio por estación (segundos):")
    for estacion in sorted(tiempos_por_estacion, key=lambda e: int(e)):
        tiempos = tiempos_por_estacion[estacion]
        promedio = sum(tiempos) / len(tiempos)
        print(f"  Estación {estacion}: {promedio:.2f} s")


if __name__ == "__main__":
    main()
