
#palavra invertida

def verificar_palindromo(string):

   flag = False

   string_invertida = string[::-1]

   if(string == string_invertida):
      flag = True


   return flag

teste = " arara "
print(verificar_palindromo (teste))