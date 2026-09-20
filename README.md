<div style="text-align: left;">
  <img width="200" src="https://www.fciencias.unam.mx/sites/default/files/logoFC_2.png" alt="Logo FC">
</div>

# Proyecto ENDIREH 2021: Violencia contra las Mujeres

## 1. Objetivo del proyecto

Estructurar un proyecto de minería de datos con una arquitectura de carpetas estándar,
seleccionar y justificar un framework de análisis de datos (**polars**), aplicar un
preprocesamiento riguroso (normalización, duplicados, tipos de dato e imputación) y
calcular e interpretar medidas de localización y variabilidad como parte del análisis
exploratorio, previo a cualquier modelado.

## 2. Fuente de los datos

- **Archivo utilizado:** el CSV proporcionado por classroom, eliminando el prefijo del nombre:
  `endireh_ml_dataset_texto_fecha.csv`
- **Se tiene que agregar manualmente a la carpeta `data/data_raw/` quitando el nombre propio y apellidos

## 3. Estructura del proyecto

```
proyecto-endireh-violencia/
   config/
      rutas.py             # Rutas de archivos estaticos
   data/
      data-raw/            # Datos originales, tal como se descargaron (nunca se editan)
      data-processed/      # Datos ya limpios: sin duplicados, tipos corregidos, imputados
      data-input-model/    # Datos ya transformados y listos como entrada de un modelo
      data-model/          # Salidas del modelo: predicciones, clusters, reglas obtenidas
   src/
      cleaning/            # Scripts de limpieza y preprocesamiento
      visualization/       # Scripts de graficas y EDA
      models/              # Scripts de entrenamiento y evaluacion de modelos
   notebooks/              # Notebooks exploratorios (no productivos)
   README.md               # Documentacion del proyecto
   requirements.txt        # Dependencias exactas del proyecto
```


## 4. Instalación del entorno

### 4.1 Requisitos previos

| Herramienta | Versión | Para qué se usa |
|---|---|---|
| Python | 3.10 o superior | Lenguaje base del proyecto |
| pip | Incluido con Python | Instalación de dependencias |
| Git | Cualquier versión reciente | Control de versiones |
| VS Code o Jupyter | Cualquiera | Ejecutar el notebook |

### 4.2 Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd proyecto-endireh-violencia
```

### 4.3 Crear y activar el entorno virtual

Crea el entorno, en la raíz del proyecto:

```bash
python3 -m venv .venv
```

Activalo (cada vez que se abra una terminal nueva):

```bash
source .venv/bin/activate
```

### 4.4 Instalar las dependencias

Con el entorno activado:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Colocar los datos

1. Descarga el CSV de la práctica desde **Classroom**.
2. **Renómbralo** quitando solo el nombre propio del prefijo, de modo que el archivo se
   llame exactamente:

   ```
   endireh_ml_dataset_texto_fecha.csv
   ```
3. Colócalo dentro de `data/data-raw/`.

Esto asegura que todo el equipo use el mismo nombre de archivo, definido en
`config/rutas.py`:

```python
RUTA_ENDIREH_CSV = RUTA_DATA_RAW / "endireh_ml_dataset_texto_fecha.csv"
```

