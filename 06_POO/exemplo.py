#A CLASSE: O modelo(a planta)
class Celular:

     def __init__(self,marca,modelo, cor, bateria = 100):
         self.marca = marca
         self.modelo = modelo
         self.cor = cor
         self.bateria = bateria
         self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar.")
        else:
            self.ligado = True
            print(f"{self.modelo} Ligado!")

#Os objetos: Criados a partir da classe (as "casas")
celular1 = Celular (marca = "Iphone", modelo ="17 pro max",cor ="azul")
celular2 = Celular (marca = "Sansung", modelo ="Galaxy A26",cor ="preto")

#Acessando e alterando atributos
print(celular1.marca)

#Também podemos alterar diretamente
celular1.cor = "branco"

#Chamado métodos

