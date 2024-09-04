#
# autor: Michel
# data: 04-09-2024

# crie uma classe pessoa com os seguintes atributos: nome, idade, sexo, altura e peso
# crie um método para calcular o IMC da pessoa
# crie um método para calcular a idade da pessoa em dias

class Pessoa:
  def __init__(self, nome, idade, sexo, altura, peso):
    self.nome = nome
    self.idade = idade
    self.sexo = sexo
    self.altura = altura
    self.peso = peso

  def imc(self):
    return self.peso / (self.altura ** 2)

  def idade_dias(self):
    return self.idade * 365
  
# Teste a classe Pessoa
p1 = Pessoa("Michel", 30, "M", 1.75, 75)
print(p1.imc())
print(p1.idade_dias())
print(p1.nome)
print(p1.idade)
print(p1.sexo)
print(p1.altura)
print(p1.peso)
