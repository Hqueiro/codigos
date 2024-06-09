#5qs 
# 1 quais os dados de entrada necessários - Nota 1   nota 2  media 
# 2 o que devo fazer com estes dados -  calcular a media das notas e fazer a atribuição
# 3 quais são as restrições deste problema - restrição nota maxima até 10 
# qual é o resultado esperado - atribuir media das notas na atribuição correta
# qual é a sequência de passos a ser feitas para chegar ao resultado esperado -  

# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre
# e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo
#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0        A
#Entre 7.5 e 9.0         B
#Entre 6.0 e 7.5         C
#Entre 4.0 e 6.0         D
#Entre 4.0 e zero        E

nota_1 = float(input(" informe a primeira nota : "))
nota_2 = float(input(" informe a segunda nota : "))
media = (nota_1 + nota_2)/ 2


if media >= 9:
    print(f" sua média é {media} conceito A ")
elif media >=7.5  and media < 9:
    print(f" sua média é {media} seu conceito é B ") 
elif media >= 6 and media < 7.5:
    print(f" sua média é {media} e seu conceito é C")  
elif media >= 4 and media < 6:
    print(f" sua média é {media} e seu conceito é D")  
else:
    print(" seu conceito é E")
             


  