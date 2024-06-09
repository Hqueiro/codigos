maior_idade = 18
idade_especial = 17

idade = int(input("informe sua idade:  "))


if idade >= maior_idade:
    print ("maior de idade pode tirar cnh")

if idade < maior_idade:
    print ("ainda não pode tirar cnh")

if idade >= maior_idade:
    print ("maior de idade pode tirar cnh")
else:
    print("ainda não pode tirar a cnh.")

if idade >= maior_idade:
    print ("maior de idade pode tirar cnh")
elif idade == idade_especial:  
    print("pode fazer aula teorica, e nao praticas")    
else:
    print("ainda não pode tirar a cnh.")


