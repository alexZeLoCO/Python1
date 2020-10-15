import math    #IMPORTA LIBRERÍA MATH. NO TIENE POR QUÉ SER NECESARIO

def suma (a,b):     #DEFINIMOS UNA FUNCIÓN SUMA. RECIBE DOS VALORES (A,B)
    return a+b      #DEVUELVE LA SUMA DE A Y B
def resta (a,b):    #DEFINIMOS UNA FUNCIÓN RESTA. RECIBE DOS VALORES (A,B)
    return a-b      #DEVUELVE LA RESTA DE A Y B

def main ():        #DEFINICIÓN DEL PROGRAMA
    #INPUTS
    x = int (input ("Introduzca un valor: "))       #SOLICITA Y GUARDA VALOR EN X
    y = int (input ("Introduzca un valor: "))       #SOLICITA Y GUARDA VALOR EN Y

    #OUTPUTS
    print ("La suma de los valores introducidos es: ",suma(x,y))        #OUTPUT: LLAMA FUNCIÓN SUMA Y ENTREGA X,Y

    if (x>y):       #CONDICIÓN: SI X ES MAYOR QUE Y
        print ("El primer valor es mayor que el segundo.")      #PRUEBA DE LA CONDICIÓN
        print ("La resta de los valores introducidos es: ",resta(x,y))     #OUTPUT: LLAMA FUNCIÓN RESTA Y ENTREGA X,Y
    elif (x<y):     #CONDICIÓN: SI Y ES MAYOR QUE X
        print ("El primer valor es menor que el segundo.")      #PRUEBA DE LA CONDICIÓN
        print ("La resta de los valores introducidos es. ",resta(y,x))     #OUTPUT: LLAMA FUNCIÓN RESTA Y ENTREGA Y,X
    else:           #CONDICIÓN: SI NO ES MAYOR NI MENOR ==> SON IGUALES
        print ("Los números son iguales, la resta es 0.")       #PRUEBA DE LA CONDICIÓN Y OUTPUT

main()      #LLAMADA A DEFINICIÓN MAIN()

