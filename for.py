soma = 0

for i in range(1, 4):
    nota = float(input(f"Qual a sua nota {i}: "))
    soma += nota

media = soma /3

if media >= 7:
    print('Parabéns, você foi aprovado: ')
else:
    print("Reprovado: ")

print(f"Sua média final é {media:.2f}")