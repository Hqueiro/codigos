# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
#ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida 
#em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
###misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
#considere latas cheias.

import math

tamanho_metro = float(input(" informe o valor do metro quadrado: "))
quantidade_de_lata_valor = 80
lata_de_tintas = 18
galoes = 3.6
preço_galao = 25

litros_necessarios = (tamanho_metro / 6)*1.10 

latas_necessarias = math.ceil (lata_de_tintas / 18)

custo_das_latas = latas_necessarias*80

galoes_necessario = math.ceil ( latas_necessarias / 3.6)

custo_dos_galoes = galoes_necessario * 25





