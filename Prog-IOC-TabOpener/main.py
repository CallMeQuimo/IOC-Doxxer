#Importo funciones de function
from backend.functions import *

# Entrada por consola (TEMPORAL)
if __name__ == "__main__":
    cuant = int(input("¿Cuántos IOC quieres analizar?"))
    for i in range(cuant):
        ioc = validIOC(input("Ingrese IP o URL a analizar:").strip().lower())
        #No pregunta qué herramientas usar(eso será en la GUI)
        opVT(ioc)
        opIPBD(ioc)