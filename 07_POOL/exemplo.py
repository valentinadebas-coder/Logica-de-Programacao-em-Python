# 1. Encapsulamento
# Proteger o sálario para que mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario      #privado: dois sublinhados

    def apresentar(self):
        print(f"Sou {self.nome} e ganho R${self.salario}")


    #@property deixa ter o salario como se fosse um atributo
    @property
    def salario(self):
        return self.__salario


    def dar_aumento(self, porcentagem, ):
        if porcentagem <= 0:
            print(f"Aumento inválido para {self.nome}")
        self.__salario = self.__salario * (1 * porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem} % de aumento")

##############################################################################################

ana = Funcionario( "ana", 3000 )
#ana.salario = 4000
print(ana.salario)
ana.apresentar()
ana.dar_aumento(-20)
ana.apresentar()


try:
    ana.salario = 10000
except AttributeError:
    print("Não é permitido alterar o salário diretamente")

try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario nao pode ser acesado de fora.")