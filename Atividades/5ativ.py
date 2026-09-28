# 5. Sistema de estoque

estoque = [
    {"nome": "Notebook", "categoria": "Informática", "preco": 2500, "quantidade": 5},
    {"nome": "Mouse", "categoria": "Periféricos", "preco": 50, "quantidade": 15},
    {"nome": "Teclado", "categoria": "Periféricos", "preco": 100, "quantidade": 8},
    {"nome": "Monitor", "categoria": "Informática", "preco": 800, "quantidade": 12},
    {"nome": "Fone", "categoria": "Áudio", "preco": 150, "quantidade": 6}
]

# 1. Exibir todos os produtos
print("Produtos cadastrados:")

for produto in estoque:
    print(produto)


# 2. Exibir nome, preço e quantidade
print("\nInformações dos produtos:")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print()


# 3. Quantidade total de itens
total_itens = 0

for produto in estoque:
    total_itens = total_itens + produto["quantidade"]

print("Total de itens:", total_itens)


# 4. Valor total do estoque
valor_total = 0

for produto in estoque:
    preco = float(produto["preco"])
    quantidade = int(produto["quantidade"])
    valor_total = valor_total + (preco * quantidade)



print("Valor total do estoque: R$", valor_total)


# 5. Produtos com menos de 10 unidades
print("\nProdutos com menos de 10 unidades:")

for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])



# 6. Verificar se um produto está cadastrado
nome = "Mouse"
encontrado = False

for produto in estoque:
    if produto["nome"] == nome:
        encontrado = True

if encontrado:
    print("\nO produto", nome, "está cadastrado.")
else:
    print("\nO produto", nome, "não está cadastrado.")



# 7. Alterar a quantidade de um produto
for produto in estoque:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 20



# 8. Adicionar um novo produto
novo_produto = {
    "nome": "Webcam",
    "categoria": "Periféricos",
    "preco": 200,
    "quantidade": 7
}

estoque.append(novo_produto)



# 9. Relatório final
print("\nRELATÓRIO FINAL")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Categoria:", produto["categoria"])
    print("Preço: R$", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print("--------------------")

