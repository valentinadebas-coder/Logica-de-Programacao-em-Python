
# 1. Listas
#Listas são utilizadas para armazenar vários valores dentro
#de uma única variável.
nomes = ["Ana", "Carlos", "João", "Maria"]
print(nomes)



# 2. Acessando Elementos da Lista
print(nomes[0])

#Podemos acessar o último elemento usando 0 -1
print(nomes[-1])



# 3. Alterando Elementos

nomes[0] = "Pedro"
print(nomes)



# 4. Adicionar Elementos

#append() adiciona um elemento em uma posição específica.
nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma posição específica.
nomes.insert( 1 , "Mariana")
print(nomes)



# 5. Removendo Elementos
#remove um elemento pelo valor

nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo indice
nomes.pop(0)



# 6. Tamanho da Lista
#len() informa a quantidade de elementos
print(len(nomes))



# 7. Percorrendo uma Lista
for nomes in nomes:
    print(nomes)



# 8. Verificando se um elemento existe

if "João" in nomes:
    print("João esta na lista")
else:
    print("João não está na lista")



# 9. Lista com diferentes tipos de dados
dados = ("João", 18 , 1.75 , True)
print(dados)



# 10. Lista de Numeros
notas = (7, 5, 8, 0, 6, 5, 9, 0)

soma = 0

for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(f"Média: {media}")



# 11. Tuplas
#Tuplas são semelhantes ás listas.
#As tuplas não podem ser alteradas.

coordenadas = (10, 20)
print(coordenadas)



# 12. Dicionários
#dicionários armazenam informações no formato: chave: valor
aluno = {
    "nome": "Carlos",
    "idade": 10,
    "aluno": 8.5
}

print(aluno)



# 13. Acessando valores de dicionário

print(aluno["nome"])
print(aluno["idade"])
print(aluno["nota"])



# 14. Alterando valores
aluno["nota"] = 9.0
print(aluno)


# 15. Adicionando novos dados
aluno["curso"] = "informática"
print(aluno)


# 16. Removendo dados
del aluno["curso"]
print(aluno)


# 17. Podemos acessar chave e valor ao mesmo tempo.
for chave, valor in aluno.items():
    print(chave)

#Podemos acessar chave e valor ao mesmo tempo.
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")


# 18. Percorrendo um Dicionário

if "nome" in aluno:
    print("A chave nome existe")


# 19. Dicionário com Lista
aluno = {
    "nome": "Maria",
    "notas": [8.0, 7.5, 9.0]

}


#O que é uma Função?
#Uma Função é um bloco de código para realizar uma determinada tarefa.
#Ela permite organizar a reutilizar o código.

