import random

valor_aleatorio = random.randint(1, 10)
acertou = False

while not acertou:
    chute = int(input("Digite o valor do chute de 1 a 10: "))
    
    if chute > valor_aleatorio:
        print("Chute maior que o valor aleatório.")
    elif chute < valor_aleatorio:
        print("Chute menor que o valor aleatório.")
    else:  # Aqui, usamos apenas `else` já que `chute == valor_aleatorio` é a única opção restante.
        acertou = True
        print("Parabéns! Você acertou o valor.")