import tensorflow as tf
import numpy as np
#import matplotlib as plt

entrada = np.array([-40, -10, 0, 15, 30, 100], dtype=float)
salida = np.array([-40, 14, 32, 59, 86, 212], dtype=float)

capa = tf.keras.layers.Dense(unidades=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Entrenando...")
historial = modelo.fit(entrada, salida, epochs=1000, verbose= False)
print("Modelo entrenado")

"""
plt.xlabel("# Epocas")
plt.ylabel("# Perdidas")
plt.show()

prediccion = modelo.prediction()
"""