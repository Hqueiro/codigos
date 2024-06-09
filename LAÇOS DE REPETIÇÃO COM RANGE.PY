numero = int(input("Digite um numero positivo: "))

if numero < 0: 
    print("Digite apenas numeros positivos")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *=i
    print(f"O fatorial de {numero} é {fatorial}")