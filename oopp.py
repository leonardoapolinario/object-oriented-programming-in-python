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

# Implementando __slots__

city = object.__new__(Cidadao)

city.__init__(89089009,'Maurílio')

class Functionario(object):
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def mostra_bonus(self):
        return self._salario * 0.10

class Gerente(Functionario):
    def __init__(self, nome, cpf, salario, senha,qtd_subordinados):
        super().__init__(nome,cpf, salario)
        self._senha = senha
        self._qtd_subordinados = qtd_subordinados

    def validacao(self, senha):
        return (self._senha == senha)

    def mostra_bonus(self):
        return self._salario * 0.10 + self._qtd_subordinados * 0.10

class Secretaria(Functionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerentes):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerentes = qtd_gerentes
    
    def mostra_bonus(self):
        return self._salario * 0.10 + self._qtd_gerentes * 0.10

# É um

s1 = Secretaria('Maria', 8908089,8980980, 143123412, 3)

g1 = Gerente('Leonardo', 89089080, 2139082, 8908093, 10)

print(s1.mostra_bonus())

print(g1.mostra_bonus())

class GestaoDeBonus:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, funcionario):
        self._total_bonificacoes += funcionario.mostra_bonus()

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

g1 = Gerente('Manoel', 987, 5600, 1234, 10)
s1 = Secretaria('Maria', 345, 4000, 789,5)



# hasattr

class Engenheiro():
    def __init__(self, nome):
        self._nome = nome
        
e1 = Engenheiro('Manoel')

class GestaoDeBonus:
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, funcionario):
        if(hasattr(funcionario, 'mostra_bonus')):
            self._total_bonificacoes += funcionario.mostra_bonus()
        else:
            print("O objeto {} não possui implementação mostra_bonus".format(self.__class__.__name__))

    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes

gestao = GestaoDeBonus()

gestao.registra(g1)
gestao.registra(s1)

print(gestao.registra(e1))

