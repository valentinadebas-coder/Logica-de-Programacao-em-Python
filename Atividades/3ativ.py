# 3. Informações de um produto

produto = ("Notebook", "Informática", 2500.00, 12345)

# 1. Exibir cada informação
print("Nome:", produto[0])
print("Categoria:", produto[1])
print("Preço:", produto[2])
print("Código:", produto[3])

# 2. Exibir todas as informações
print("\nTodas as informações:")

for informacao in produto:
    print(informacao)

# 3. Quantidade de informações
print("\nQuantidade de informações:", len(produto))

# 4. Tentativa de alteração
# produto[0] = "Computador"

# 5. Explicação
print("\nNão é possível alterar uma informação da tupla.")
print("As tuplas não podem ser modificadas depois de criadas.")