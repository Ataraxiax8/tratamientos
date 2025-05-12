# Crear archivo README.md con el contenido proporcionado

readme_content = """
# Generador de Matriz de Tratamientos para Experimentos Estadísticos

Este repositorio contiene un script en Python que genera automáticamente la matriz de tratamientos (combinaciones de factores y niveles) para el diseño de experimentos utilizados en análisis estadístico. La salida se exporta en formato Excel y puede ser usada como base para el diseño de pruebas o análisis factoriales.

## 🧪 Descripción

El script permite:

- Definir factores categóricos y sus respectivos niveles.
- Generar todas las combinaciones posibles entre los factores (tratamientos).
- Numerar correlativamente cada tratamiento.
- Exportar la matriz a un archivo Excel (`Matriz_Tratamientos.xlsx`).
- (Opcional) Abrir el archivo Excel automáticamente en sistemas Windows.

## ⚙️ Factores utilizados (ejemplo incluido)

El ejemplo incluido utiliza los siguientes factores:

| Factor          | Niveles          |
|-----------------|------------------|
| SECTOR          | PRI, PUB         |
| NIVEL_DOCENTE   | PROF, LIC        |
| ESPECIALIDAD    | MAT, OTRO        |
| USO_LIBROTXT    | NO, SI           |

Esto genera una matriz de 16 tratamientos distintos (2x2x2x2).

## 📁 Requisitos

- Python 3.x
- Librerías:
  - `pandas`
  - `itertools` (incluida en la biblioteca estándar)

Para instalar `pandas`:

```bash
pip install pandas
