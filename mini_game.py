import random

numero_aleatorio = random.randint(1, 10)

numero_do_usuario = int(input("Tente adivinhar o número de 1 a 10: "))

contagem_de_chances = 0

while numero_do_usuario != numero_aleatorio:
    contagem_de_chances += 1  # Adiciona a contagem de chances 

    if contagem_de_chances > 3:
        print("\nAcabou suas chances ")
    elif numero_do_usuario < numero_aleatorio:
        print("\nUm pouco mais")
    else:
        print("\nUm pouco menos")
        
    # Solicita uma nova tentativa ao usuário
    numero_do_usuario = int(input("Tente novamente: "))

# Adiciona a contagem para a tentativa correta
contagem_de_chances += 1

print("Você acertou, o número era: ", numero_aleatorio, "Você precisou de ", contagem_de_chances, "tentativas. ")