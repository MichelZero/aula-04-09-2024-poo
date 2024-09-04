#
# autor: Michel
# data: 04-09-2024

#Crie uma classe para somar 2 valores.

##### 3 teste ###########
class Calculadora: 
  def __init__(self, valor1, valor2):
    self.valor1 = valor1
    self.valor2 =  valor2
    
  def somar(self): # método da classe Calculadora
    return self.valor1 + self.valor2
  
  def subtrair(self):
    return self.valor1 - self.valor2
  
  def multiplicar(self):
    return self.valor1 * self.valor2
  
  def potencia(self):
    return self.valor1 ** self.valor2
  
  def dividir(self):
    if self.valor2 == 0:
      return f"{self.valor1} não pode dividir por {self.valor2}"
    else:
      return self.valor1 / self.valor2