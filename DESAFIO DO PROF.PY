#5qs 
# 1 quais os dados de entrada necessários
# 2 o que devo fazer com estes dados
# 3 quais são as restrições deste problema
# qua l é o resultado esperado
# qual é a sequência de passos a ser feitas para chegar ao resultado esperado



def verificar_multa(velocidade):
  velocidade_maxima = 80

  if velocidade <= velocidade_maxima:
      print('Não levou multa')
  elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
      print('Levou multa leve')
  elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
      print('Levou multa grave')
  elif velocidade > velocidade_maxima + 20:
      print('Levou multa gravíssima')

# Exemplo de uso da função:
velocidade = int(input('Digite sua velocidade: '))
verificar_multa(velocidade)
    
    

   
    



     

