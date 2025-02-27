import numpy as np
import matplotlib.pyplot as plot
import random

pontos = {
    "a" : (-8, 9),
    "b" : (10, -9),
    "c" : (3, 8),
    "d" : (7, 12),
    "e" : (4, -3)
}

ligacoes = [("c", "e"), ("a", "b"), ("b", "c"), ("d", "a")]

# DEfinir limite x, y
plot.xlim(-50, 50)
plot.ylim(-50, 50)

plot.grid('on')

# Colocar os pontos
cores = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

for key, value in pontos.items():
    plot.plot(value[0], value[1], random.choice(cores)+"o", label=key)

# Ligar os pontos
for lig in ligacoes:
    pontoA = pontos[lig[0]]
    pontoB = pontos[lig[1]]

    distancia = np.sqrt((pontoA[0] - pontoB[0])**2 + (pontoA[1] - pontoB[1])**2)

    plot.plot([pontoA[0], pontoB[0]], [pontoA[1], pontoB[1]], 'k-', label=f"Distancia ({lig[0]}, {lig[1]}): {distancia:.2f}")

plot.legend(loc='upper right')
plot.show()
