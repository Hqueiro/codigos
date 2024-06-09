
# 3 variaveis numericas
num = float(input(" digite um número :"))
num_2 = float(input(" digite um número :"))
num_3 = float(input(" digite um número :"))

# condições para saber o maior e menor numero

if num > num_2 and num > num_3:
    print("o maior é o primeiro", num)
elif num_2 > num and num_2 > num_3:
    print(" maior é o segundo ", num_2)
elif num_3 > num and num_3 > num_2:
    print("o maior é o terceiro", num_3)

elif num == num_2 and num_2 == num_3:
    print(" numeros iguais ")     
else:
    if num == num_2:
        print("o primeiro numero e o segundo numero sao maiores que o terceiro ")
    elif num == num_3:
        print("o primeiro e o terceiro são maiores que o segundo")
    elif num_2 == num_3:
        print(" o segundo e o terceiro sao maiores que o primeiro")    
       
