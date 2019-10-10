# AGENDA_2019_progra_usach
#para calcular la fecha
d=abs(int(input("ingrese el numero del dia:")))
m=abs(int(input("ingrese el numero del mes:")))
k=abs(int(input("ingrese el numero del año de centuria:")))
j=abs(int(input("ingrese el numero del centuria:")))
calculodia=(d+2.6*(m+1)+k+(k//4)+(j//4)-2*j)%7
print("su dia es:",calculodia)
