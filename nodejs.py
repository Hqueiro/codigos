nota = float(input(" digite uma nota : "))
nota_2 = float(input(" digite uma nota : "))
nota_3 = float(input(" digite uma nota : "))


if nota > nota_2 and nota > nota_3:
    print(f" o maior numero é  a primeira {nota}")

elif nota_2 > nota and nota_2 > nota_3:
    print(f" o maior numero é a segunda {nota_2} ")


elif nota_3 > nota and nota_3 > nota_2:
    print(f" o maior numero é a terceira nota {nota_3}")


elif nota_2 == nota and nota_2 == nota_3:
    print(F" as notas  {nota_2} e {nota} , {nota_3} são iguais ")  

else:
    if nota== nota_2:
        print("o primeiro numero e o segundo numero sao maiores que o terceiro ")
    elif nota== nota_3:
        print("o primeiro e o terceiro são maiores que o segundo")
    elif nota_2 == nota_3:
        print(" o segundo e o terceiro sao maiores que o primeiro")          