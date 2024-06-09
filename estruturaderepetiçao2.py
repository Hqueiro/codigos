opcao = -1

while opcao != 1:
    opcao = int(input("[1] sacar \n [2] extrato \n[0] sair \n: "))

    if opcao ==  1:
        print("sacando...")
        
    elif opcao ==2:
        print("exibindo o extrato...")

    else:
        print("obrigado por usar nosso sistema bancario, ate logo")

        documento = input("todos documentos foram enviados?:  (sim/não): ")

     