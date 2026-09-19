from pathlib import Path

# Carpeta raíz del proyecto
RUTA_PROYECTO = Path(__file__).resolve().parent.parent

# Carpetas de datos
RUTA_DATA = RUTA_PROYECTO / "data"

RUTA_DATA_RAW = RUTA_DATA / "data-raw"
RUTA_DATA_PROCESSED = RUTA_DATA / "data-processed"
RUTA_DATA_INPUT_MODEL = RUTA_DATA / "data-input-model"
RUTA_DATA_MODEL = RUTA_DATA / "data-model"


# Se tiene que renombrar el nombre del archivo a este (Que es quitando solo el nombre propio) para
# para manejar un mismo nombre de archivo todos
RUTA_ENDIREH_CSV = RUTA_DATA_RAW / "endireh_ml_dataset_texto_fecha.csv"