# 2. Controle de notas

notas = [8, 7, 9, 6, 10]

print("Notas:", notas)

soma = sum(notas)
media = soma / len(notas)

print("Soma:", soma)
print("Média:", media)

print("Maior nota:", max(notas))
print("Menor nota:", min(notas))

if 10 in notas:
    print("Existe uma nota igual a 10.")
else:
    print("Não existe nota igual a 10.")

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")