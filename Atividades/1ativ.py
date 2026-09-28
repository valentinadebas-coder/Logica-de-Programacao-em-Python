# 1. Cadastro de filmes

filmes = ["Avatar", "Titanic", "Vingadores", "Shrek", "Toy Story"]

print("Filmes cadastrados:")
print(filmes)

print("Primeiro filme:", filmes[0])
print("Último filme:", filmes[-1])

filmes.append("Harry Potter")
print("Depois de adicionar:", filmes)

filmes.insert(2, "Homem-Aranha")
print("Depois de inserir:", filmes)

filmes.remove("Shrek")
print("Dep, filmes)

filmes[0] = "Interestelar"
print("Depois de alterar:", filmes)

print("Quantidade de filmes:", len(filmes))

if "Titanic" in filmes:
    print("Titanic está na lista.")
else:
    print("Titanic não está na lista.")

