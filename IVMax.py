import numpy as np
import random

def Pair(N):
    # Retorna una lista en orden aleatoria de la segunda mitad de los individuos
    # ej: N=8 -> [7, 6, 5, 4]
    randomN=random.sample(range(int(N/2), N), int(N/2))
    pair={}
    # Puebla el diccionario con los pares
    # ej: {0: 7, 7: 0, 1: 6, 6: 1...}
    for i in range(int(N/2)):
        pair[i]=randomN[i]
        pair[randomN[i]]=i
    return pair