"""
Seminario de Inteligencia Artificial 2
Ejemplo clase 23.08.2023
Ejemplo de Neurona Artificial
"""

import numpy as np

w = np.array([-1.5, 1, 1])
x = np.array([(0, 0), (0, 1), (1, 0), (1, 1)])

x_m = np.hstack((np.ones((4, 1)), x))


#print(np.dot(w, x_m[0]) >= 0)
#print(np.dot(w, x_m[1]) >= 0)
#print(np.dot(w, x_m[2]) >= 0)
#print(np.dot(w, x_m[3]) >= 0)

print(np.dot(w, x_m.T) >= 0)