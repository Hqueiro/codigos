texto = input("informe um texto: ")
vogais = "AEIOU"


for letra in texto:
    if letra.upper() in vogais:
        print(letra, end= "")

else:
    print()      

    # adiciona quebra de linha

    # exemplo utilizando a funçao build- in range

    for numero in range (0, 51, 5):
        print(numero, end=" ")  