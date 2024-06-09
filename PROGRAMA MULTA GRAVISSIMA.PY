velocidade = float(input(" digita uma velocidade: "))

velocidade_maxima = 80


if velocidade < velocidade_maxima:
    print(" não houve multa")
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print("multa leve")
elif velocidade >= velocidade_maxima +11 and velocidade <= velocidade_maxima +20:
    print(" multa grave")
elif velocidade > velocidade_maxima +20:
    print(" multa gravissima")            



#5qs 
# 1 quais os dados de entrada necessários
# velocidade

# 2 o que devo fazer com estes dados
# aplicar multa grave gravissimma e leve de acordo com a velocidade

# 3 quais são as restrições deste problema


# qual é o resultado esperado
# é chegar ao resultado que corresponde ao nive da multa

# qual é a sequência de passos a ser feitas para chegar ao resultado esperado

# digitar a velocidade
# if velocidade <= velocidademaxiamma = não levou multa
# velocidade_maxima=80
# if velocidade > velocidade maxima and velocidade <= velocidade maxima + 10
# multa leve

# if velocidade > velocidade maxima + 11 and velocidade  <= velocidade maxima +20

# if velocidade > velocidade maxima + 20
# multa gravissima