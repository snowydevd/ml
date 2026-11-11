# %% Carga de datos
import numpy as np

# %% Constantes
mat = [
    [25.0, 20.5, 19.6],
    [29.5, 22.2, 16.6],
    [22.0, 27.0, 14.1],
    [24.3, 25.6, 18.2],
    [21.1, 22.6, 19.7],
]
arr = np.array(mat)

# %% impresion
print(arr)
print(arr.dtype)
print(arr.shape)

# %% Valores independientes
print(arr[2, 1]) # Dia 3, sensor 2
print(arr[1]) # Todas las lecturas del dia 2
column = arr[:, 2]
print(column) # Una columna entera en este caso todos los terceros sensores
print(arr[0:3]) # Los primeros 3 dias

# %% Fahrenheit
FAHRENHEIT_MAT = (arr * 9/5) + 32
print(FAHRENHEIT_MAT)

# %% Supera los 25C
supera = arr > 25.0
print(supera)

# %% Summarizing
# media de cada columna (por sensor)
# for i in range(3):
#     print("Minimo por sensor: ", arr[:, i].min())
#     print("Maximo por sensor: ", arr[:, i].max())
#     print("Desviacion standard: ", arr[:, i].std())
#     print(arr[:, i].mean())

# # media por dia (filas)
# for i in range(5):
#     print("Minimo por dia: ", arr[i].min())
#     print("Maximo por dia: ", arr[i].max())

#     print(arr[i].mean())

# con axis
col_mean = arr.mean(axis = 0)
row_mean = arr.mean(axis = 1)

col_min = arr.min(axis = 0)
row_min = arr.min(axis = 1)

col_max = arr.max(axis=0)
row_max = arr.max(axis=1)

col_std = arr.std(axis=0)

print(arr.mean())
print(col_mean)
print(row_mean)

print(col_min)
print(row_min)

print(col_max)
print(row_max)

print(col_std)
print(arr.min())





