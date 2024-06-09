import math

# Solicita ao usuário o tamanho da área a ser pintada em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Cálculo da quantidade de tinta necessária
litros_necessarios = area / 3

# Cálculo da quantidade de latas de tinta necessárias (arredondando para cima)
latas_necessarias = math.ceil(litros_necessarios / 18)

# Cálculo do custo total
custo_total = latas_necessarias * 80

# Exibe os resultados
print(f"Área a ser pintada: {area:.2f} metros quadrados")
print(f"Litros de tinta necessários: {litros_necessarios:.2f} litros")
print(f"Quantidade de latas de tinta necessárias: {latas_necessarias} latas")
print(f"Custo total: R$ {custo_total:.2f}")