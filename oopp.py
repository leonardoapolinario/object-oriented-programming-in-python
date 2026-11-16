class Carro():
    def __init__(self,marca,modelo, ano,preco,portas):
        #print("O objeto {} foi construído!".format(self))
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.portas = portas
        self.__preco = preco

    def aumentar_preco(self,preco):
        self.__preco += preco

    def __metod_privado(self):
        return 'método privado'

    def set_modelo(self, modelo):
        self.modelo = modelo.title()

    def get_modelo(self):
        return self.modelo

c1 = Carro('Fiat', 'Marea Turbo', 2026, 50000, 4)

car = Carro('Fiat', 'Marea Turbo', 2026, 50000, 4)

print(car._Carro__preco) #Acessando atributos privados

car.set_modelo('marea turbo plus')

print(car.get_modelo())




