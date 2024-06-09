#5qs 
# 1 quais os dados de entrada necessários
# 2 o que devo fazer com estes dados
# 3 quais são as restrições deste problema
# qual é o resultado esperado
# qual é a sequência de passos a ser feitas para chegar ao resultado esperado

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
#e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador 
# e o reajuste segundo o seguinte critério,baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após 
# o aumento ser realizado, informe na tela:
#o salário antes do reajuste
#o percentual de aumento aplicado;
# novo salário, após o aumento.

# salario 280  




salario = int(input("Informe seu salário: "))

if salario == 280:
    reajuste = 20
elif salario > 280 and salario <= 700:
    reajuste = 15
elif salario > 700 and salario <= 1500:
    reajuste = 10
elif salario > 1500:
    reajuste = 5
else:
    reajuste = 0

if reajuste > 0:
    novo_salario = salario + (salario * reajuste / 100)
    print(f"Seu salário era {salario} e teve um reajuste de {reajuste}%. O novo salário é {novo_salario:.2f}")
else:
    print("Não teve aumento")
 
  







   
