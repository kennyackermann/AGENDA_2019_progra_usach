#entrada
#para encontrar una fecha
d=abs(int(input("ingrese el numero del dia:")))#aqui se ingresa el numero del dia
m=abs(int(input("ingrese el numero del mes:")))#aqui se ingresa el numero del mes
k=abs(int(input("ingrese el numero del año de centuria:")))#aqui se pone los 2 ultimos numeros del año
j=abs(int(input("ingrese el numero del centuria:")))#aqui se ponen los 2 primeros numeros del año
calculodia=(d+2.6*(m+1)+k+(k//4)+(j//4)-2*j)%7 #la funcion nos arroja numeros desde el 0 que equivale asabado hasta el1 que es domingo
print("su dia es:",calculodia)
#proceso
#salida
