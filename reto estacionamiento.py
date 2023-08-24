 #Acá pedimos los datos pertinentes
print("ESTACIONAMIENTO PLAYA")
horas = int(input("Digite horas:  "))
minutos = int(input("Digite minutos:  "))
dia = str(input("Ingrese el día de la semana (sin tildes y en minuscula):   "))
fracciones = 0
pago = 0
   
    
#Para determinar cuanto paga por día
if dia == "lunes" or dia == "martes" or dia == "miercoles":
        pago = 2.00
elif dia == "jueves" or dia=="viernes":
        pago = 2.50
elif dia == "sabado" or dia=="domingo":
        pago = 3.00
else:
        print("¡Error! El día ingresado no es válido.")
        
        
#Para determinar las fracciones
if minutos > 0 and minutos <= 5: #Acá si son menos de 5 minutos, es decir, no cobra esos 5 minutos o menos.
             fracciones = 0
elif minutos> 5 and minutos <60: #Acá si pasa de 5 minutos, es decir, se cuenta como una hora.
             fracciones = 1

#Para determinar si el tiempo es válido o no.    
if horas <0 or minutos <0:
         print("¡Error! El tiempo ingresado no es válido.")
         precio = 0
         
else:
    precio = (horas+fracciones)*pago
    print("\nFactura"+"\nHoras ocupadas: ",horas,"\nMinutos ocupados: ",minutos,"\nDía: ",dia,"\nTotal a pagar: ",precio)


  




        