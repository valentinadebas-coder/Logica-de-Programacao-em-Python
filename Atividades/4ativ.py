# 4. Cadastro de funcionário

funcionario = {
    "nome": "Ana",
    "idade": 20,
    "cargo": "Vendedora",
    "salario": 2000,
    "setor": "Vendas"
}

# 1. Exibir cada informação
print("Nome:", funcionario["nome"])
print("Idade:", funcionario["idade"])
print("Cargo:", funcionario["cargo"])
print("Salário:", funcionario["salario"])
print("Setor:", funcionario["setor"])


# 2. Alterar o salário
funcionario["salario"] = 2500


# 3. Adicionar uma nova informação
funcionario["cidade"] = "Jaraguá do Sul"


# 4. Remover uma informação
del funcionario["idade"]


# 5. Verificar se uma chave existe
if "cargo" in funcionario:
    print("A chave cargo existe.")
else:
    print("A chave cargo não existe.")


# 6. Percorrer o dicionário
print("\nDados do funcionário:")

for chave, valor in funcionario.items():
    print(chave, ":", valor)
