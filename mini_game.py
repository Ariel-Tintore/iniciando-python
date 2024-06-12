import random

numero_aleatorio = random.randint(1, 10)

numero_do_usuario = int(input("Tente adivinhar o número de 1 a 10: "))

while numero_do_usuario != numero_aleatorio:
    if numero_do_usuario < numero_aleatorio:
        print("\nUm pouco mais ")
    else:
        print("\nUm pouco menos ")
    # Solicita uma nova tentativa ao usuário
    numero_do_usuario = int(input("\nTente novamente: "))

print("Você acertou, o número era: ", numero_aleatorio)
