#
# autor: Michel
# data: 04-09-2024
#

# Crie a classe carro conforme os atributos e métodos abaixo:
# Atributos: marca, modelo, cor e combustível

# Métodos: ligar, acelera, frear, desligar

class Carro:
  def __init__(self, marca, modelo, cor, combustivel):
    self.marca = marca
    self.modelo = modelo
    self.cor = cor
    self.combustivel = combustivel
    
  def ligar(self):
    return "Carro ligado"
  
  def acelerar(self):
    return "Carro acelerando"
  
  def frear(self):
    return "Carro freando"
  
  def desligar(self):
    return "Carro desligado"
  
# Teste a classe Carro
carro1 = Carro("Ford", "Fiesta", "Branco", "Gasolina")
print(carro1.ligar())
print(carro1.acelerar())
print(carro1.frear())
print(carro1.desligar())
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
print(carro1.combustivel)
