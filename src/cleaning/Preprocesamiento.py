from pathlib import Path
import sys

import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# RUTA DEL PROYECTO
# ============================================================

# Este archivo está en:
# proyecto-endireh-violencia/src/cleaning/Preprocesamiento.py
#
# parents[2] nos lleva hasta:
# proyecto-endireh-violencia/

RUTA_PROYECTO = Path(__file__).resolve().parents[2]

# Agregamos la raiz del proyecto para poder importar config
sys.path.insert(0, str(RUTA_PROYECTO))


# ============================================================
# IMPORTAR RUTAS
# ============================================================
from config.rutas import (
    RUTA_PROYECTO,
    RUTA_DATA_RAW,
    RUTA_DATA_PROCESSED,
    RUTA_ENDIREH_CSV,
)


# ============================================================
# CARGA DE DATOS
# ============================================================
def cargar_datos():
    print("Cargando dataset...")

    df_crudo = pl.read_csv(RUTA_ENDIREH_CSV)

    print(f"Dimensiones: {df_crudo.shape}")
    print(df_crudo.head())

    return df_crudo


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    df_crudo = cargar_datos()


if __name__ == "__main__":
    main()