class Carro():
    def __init__(self,marca,modelo,ano,preco,portas):
        #print("O objeto {} foi construído!".format(self))
        self.marca = marca
        self.__modelo = modelo
        self.__ano = ano
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
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def setAno(self, ano):
        self.__ano = ano
    
    def getAno(self):
        return self.__ano
    
    ano = property(fget= getAno, fset=setAno)

# c1 = Carro('Fiat', 'Marea Turbo', 2026, 50000, 4)

# car = Carro('Fiat', 'Marea Turbo', 2026, 50000, 4)

# print(car._Carro__preco) #Acessando atributos privados

# car.modelo = "Tempra"

# print(car.modelo)

# print(car.ano)

#Métodos protegidos.

class Servidor:
    def __init__(self, nome, salario, tel):
        self._nome = nome
        self.__salario = salario
        self._tel = tel

    def calcularSalario(self):
        return self.__salario * 12
    
#fulano = Servidor('Leonardo Apolinário', 50000, 31990796285)

#print(dir(fulano))


# staticmethod
class Pessoa:
    _num_pessoa = 0

    def __init__(self, idade):
        self.__idade = idade
        Pessoa._num_pessoa += 1
    
    @staticmethod
    def get_num_pessoas():
        return Pessoa._num_pessoa

p1 = Pessoa(20)
p2 = Pessoa(30)
p3 = Pessoa(40)

#print(str(Pessoa._num_pessoa) + ' ' + str(Pessoa.get_num_pessoas()))

# classmethod

class Cidadao:
    _num_cidadaos = 0
    __slots__ = ['__rg', 'nome']

    def __init__(self, rg, nome):
        self.__rg = rg
        self.nome = nome
        Cidadao._num_cidadaos += 1

    @classmethod
    def get_num_cidadaos(cls):
        return Cidadao._num_cidadaos

c1 = Cidadao(1243123, 'josé')
c2 = Cidadao(8908903, 'maria')
c3 = Cidadao(5398039, 'silva')

#print(Cidadao.get_num_cidadaos())

pp = Cidadao(8908903, 'dutra')

pp.carro = 'Tempra'

print(dir(pp))

# Implementando __slots__



