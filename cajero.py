#Pau Cañizares López

from datetime import datetime
import math

#Apuntes (ignorar)
#print(datetime.date.today())
#exponent = 5**2
#Esto es una asignación doble, en python está permitido
#a, b = 3, 2


ticket = [
    "1 - filete de ternera - 30 ,23",
    "4 - coca cola - 4,20",
    "-2 - coca cola - 1,40",
    "1 - pan - 0,90"
]


def mostrar_ticket(ticket):
    
    total = 0

    for i in ticket:

                #dividimos el ticket por los guiones

        partes = i.split(" - ")

        #si el ticket tiene 3 partes ( Unidades - Producto - Precio)...

        if len(partes) == 3:
            try:
                #Cogemos la posición 0 del string, y la convertimos en int ( unidades )
                unidades = int(partes[0])
                #cogemos el precio ( posición 2 de cada bloque, lo convertimos en float, sustituimos la coma por el punto para que pueda ser float)
                precio_total = float(partes[2].replace(",", "."))

                # para ver si es compra ( positivo o negativo )
                if unidades > 0:

                    #Si es una compra ( unidades > 0 ), sumamos el total en la variable total
                    total += unidades * precio_total
                elif unidades < 0:


                    # Si es una devolución ( unidades < 0 ), restamos el total en la variable total
                    # el abs, devuelve el valor absoluto, es decir un positivo, ya que si multiplicamos con negativo saldrá negativo
                    total -= abs(unidades) * precio_total
        
                        #Para que no me salte el Valueerror feo
            except ValueError:
                print(f"Error: El formato del ticket es incorrecto: {i}")
        else:
            print(f"Error: El formato del ticket es incorrecto: {i}")

    # Calcular el total con el 16% de iva que pone en el pdf
    total_con_iva = total * 1.16

    # El strftime nos muestra la fecha en el formato que nos pide en la practica
    fecha_compra = datetime.now().strftime("%Y-%m-%d")

    # Imprimir el total con IVA y la fecha de compra
    # El 2f lo he puesto, sirve para mostrar 2 decimales solo, sino me muestra un numero más largo
    # Pongo el f string para que me muestre por consola todo bien    
    print(f"Total a pagar: {total_con_iva:.2f}")
    print(f"Fecha de compra: {fecha_compra}")


mostrar_ticket(ticket)



# Partimos de que un supermercado ha comprado una nueva caja registradora y no tiene programada la función que calcula el ticket total que tiene que pagar el cliente. 
#Tu misión consistirá en desarrollar un software en Python que permita que esta caja pueda calcular la factura de cada cliente a partir de una lista de productos.