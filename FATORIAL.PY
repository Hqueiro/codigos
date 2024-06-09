numero = int(input(" digite um valor positivo e inteiro :"))
fatorial = 1

if numero >= 0:
    print(" o numero é positivo ")

if  numero < 0:
    print(" o numero é negativo ")    

fatorial = 1

for item in range (1, numero +1):
    fatorial = fatorial*item

print(f" o fatorial do numero é {fatorial}")
    

