num = float(input(" digite um numero: "))
num_2= float(input(" digite um numero: "))
num_3= float(input(" digite um numero: "))

maior = num
menor = num

if num_2 > maior:
    maior = num_2
 
if num_3 > maior:
    maior = num_3

if num_2 < menor:
    menor = num_2
if num_3 < menor:
    menor = num_3

print("o maior numero digitado foi {} e o menor {}".format(maior,menor))       
                  

                  #5qs 
# 1 quais os dados de entrada necessários
# 2 o que devo fazer com estes dados
# 3 quais são as restrições deste problema
# qual é o resultado esperado
# qual é a sequência de passos a ser feitas para chegar ao resultado esperado