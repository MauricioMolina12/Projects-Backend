
texto = input("Ingresa una palabra o frase(sin tildes): ") #Pedimos la palabra o frase 
T = [] #Acá creamos el vector que contendrá esa frase



for letra in texto.lower(): #el .lower nos permite que el programa ignore si las letras son mayusculas o minusculas
  
    if letra!=" ": #esta línea de código simplemente lo que hace es ignorar los espacios entre frases
      
        T.append(letra) #esta línea de código lo que hace es agregar cada letra al vector gracias al append.

# Acá comparamos la palabra o frase normal con la palabra o frase invertida,
# para luego determinar si la palabra o frase es palindroma o no.


if T == T[::-1]:
  print("La palabra o frase es un palíndromo")
else:
  print("La palabra o frase no es un palíndromo")


  




        