renda = float(input(" digite sua renda: "))
nome_limpo = str(input(" você tem o nome limpo sim ou não "))
sim = True
não = False


if renda >= 10000:
    print(" financiamento aprovado ")
if renda <= 10000:
     print (" abaixo da renda") 

# nome limpo

     if nome_limpo == "sim":
          print(" parabens", )
     elif nome_limpo == "não":
          print(" regularizar ")     
     else:
          (" não foi possivel realizar a operação")     

  

