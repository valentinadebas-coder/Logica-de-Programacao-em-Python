#O que é uma Função?

#Uma Função é um bloco de código para realizar uma determinada tarefa.
#Ela permite organizar a reutilizar o código.

#1. criando uma função
#Utilizar a palavra def para uma função

def saudacao():
    print("Olá seja bem-vindo!")
saudacao()

#2. Criando uma função com parâmetro

#Parâmetros permitem enviar informações para a função.

def saudacao(nome):
    print(f"Olá {nome}, seja bem-vinda!")

saudacao("Ana")

#3. Mais de um parâmetro

def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria" ,17 )
apresentar("Henrique" ,15 )

#4. Função com cálculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado {resultado}")

somar(10 , 20)
somar(10 , 90)

#5. Retornando um valor
#Devolve o valor para o local onde a função foi chamada.

def somar(numero1, numero2):
    return numero1 + numero2

print(somar(10,5))

#6. Função com uma condição

def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade."
    else:
        return "Menor de idade."

print(verificarIdade(18))

#7. Parâmetro com valor padrão

def saudacao(nome:str = "Aluno"):
    print(f"Olá {nome}")

saudacao("João")
saudacao("Maria")

#8. Função utiluizando lista

def calcularMedia(notas ):
    soma = 0
    for nota in notas:
        soma += nota

    return soma / len(notas)

notas = [8, 7 , 9, 10]
media = calcularMedia(notas)
print(f"Média da notas: {media}")

#9. Funções para organizar um programa

def cadastrar_produto():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto"))
    return nome, preco

def exibir_produto(nome, preco):

    print("\n==== PRODUTO ====")
    print(f"Nome: {nome}")
    print(f"Preço: R$ {preco:.2f}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)

