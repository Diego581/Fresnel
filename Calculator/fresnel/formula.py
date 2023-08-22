import math
def fresnel(distancia, frecuencia):
    division = float(distancia)/float(frecuencia)
    resultado = 8.656 * (math.sqrt(division))
    return resultado

    
fresnel(24,5.8)
