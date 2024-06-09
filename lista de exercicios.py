peso = float(input(" digite o peso: "))
kilo_limite = 50
multa_por_kilo = 4
excesso = max(0, peso - kilo_limite)
multa = excesso * multa_por_kilo

print(f"Peso de peixes: {peso} kg" )

if excesso > 0:
    print (F"Excesso de peso: {excesso} kg")
    print(F"Multa a ser paga: {multa}")
else:
    print(" não houve exesso")    





#print(F' O valor de peso é {peso} e a multa a ser paga é {excesso} ')




##valor_multa_por_quilo = 4.00  # em reais

# Leitura do peso dos peixes trazidos por João
#peso = float(input("Digite o peso dos peixes em quilos: "))

# Cálculo do excesso e da multa
#excesso = max(0, peso - limite_peso)
#multa = excesso * valor_multa_por_quilo

# Impressão dos resultados
#print(f"Peso de peixes: {peso} kg")
#if excesso > 0:
    #print(f"Excesso de peso: {excesso} kg")
    #print(f"Multa a ser paga: R$ {multa:}")
#else:
   # print("Não houve excesso de peso. Nenhuma multa a ser paga.")