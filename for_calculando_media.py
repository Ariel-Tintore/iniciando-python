""""soma = 0

for i in range(1, 4):
    nota = float(input(f"Qual a sua nota {i}: "))
    soma += nota

media = soma /3

if media >= 7:
    print('Parabéns, você foi aprovado: ')
else:
    print("Reprovado: ")

print(f"Sua média final é {media:.2f}")
"""""
def ler_nota(mensagem):
    nota = input(mensagem).replace(',', '.')
    return float(nota)

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    quantidade = int(input("Quantas notas você deseja inserir? "))
    notas = []

    for i in range(quantidade):
        nota = ler_nota(f"Digite a nota {i+1}: ")
        notas.append(nota)

    media = calcular_media(notas)

    print(f"\nSua média final é {media:.1f}")

    if media >= 7.0:
        print("\nParabéns, você foi aprovado!")
    else:
        print("\nQue decepcão, você foi reprovado!")

if __name__ == "__main__":
    main()
