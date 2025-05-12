import pandas as pd
from itertools import product

# Definir los factores y niveles
factores = {
    "SECTOR": ["PRI", "PUB"],
    "NIVEL_DOCENTE": ["PROF", "LIC"],
    "ESPECIALIDAD": ["MAT", "OTRO"],
    "USO_LIBROTXT": ["NO", "SI"]
    }

# Generar todas las combinaciones posibles
combinaciones = list(product(*factores.values()))

# Crear el DataFrame con numeración correlativa
df = pd.DataFrame(combinaciones, columns=factores.keys())
df.insert(0, "Correlativo", range(1, len(df) + 1))

# Guardar la matriz en un archivo Excel (opcional)
df.to_excel("Matriz_Tratamientos.xlsx", index=False)

# Mostrar los primeros registros
print(df.head())

# Si quieres abrir el archivo Excel directamente desde Python (opcional en Windows)
import os
os.system("start Matriz_Tratamientos.xlsx")
