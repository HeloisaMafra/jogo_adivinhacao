import random

numero = random.randint(1, 10)

print("===== JOGO DE ADIVINHAÇÃO =====")
print("Estou pensando em um número de 1 a 10.")
tentativa = int(input("Qual é o seu palpite? "))

if tentativa == numero:
    print("Parabéns! Você acertou!")
else:
    print("Você errou!")
    print("O número era:", numero)
