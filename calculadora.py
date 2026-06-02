from calculadora import somar, multiplicar
from config import FEATURE_MULTIPLICACAO

print("Soma:", somar(2, 3))

if FEATURE_MULTIPLICACAO:
    print("Multiplicação:", multiplicar(2, 3))
else:
    print("Multiplicação indisponível")
