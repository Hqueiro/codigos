
# Faça um programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.



tamanho_da_area = int(input(" informe o tamanho da area a ser pintada: "))

litros_necessarios = tamanho_da_area / 3

latas_necessarias = (litros_necessarios / 18)

custo_total = latas_necessarias*80

#resultados

print(F" A area a ser pintada é {tamanho_da_area:.2f} metros quadrados")

print(f" Litros necessarios são {litros_necessarios:.2f} litros ")

print(f"Quantidade de latas de tinta {latas_necessarias:.2f} latas")

print(f" O custo total foi de {custo_total:.2f} reais ")