# ACTIVIDAD 5: Procesamiento de conjuntos de datos en Python
# Nombre - Matrícula: Jorge Alberto Castillo Ramírez-2095681, Carlos Alejandro Ochoa Garma-2042592,
# Isaac Romero Méndez-2094864, César Eduardo Cossio Colunga-2069336,
# Bryant Alberto Martinez Montero-1727324
# Ejercicio 1.- Análisis y normalización de datos de sensores en un robot móvil.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 1. Cargar el datasheet con pandas
url = "https://raw.githubusercontent.com/dilp90/InteligenciaArtificial_y_RedesNeuronales_UANL_FIME/main/MachineLearning/Datasets/robot_sensors.csv"
df = pd.read_csv(url)
