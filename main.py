#
# autor: Michel
# data: 04-09-2024
#

# importação das classes
from calculadora import Calculadora as C

# criar instancias 
val1 = int(input("informe o valor1: "))
val2 = int(input("informe o valor2: "))
#c1 = C(3, 5)
c1 = C(val1, val2)
print(c1.somar())
print(c1.multiplicar())
print(c1.potencia())
print(c1.dividir())