
dia = abs ( int ( input ( " ingrese el numero del dia: " ))) # aqui se ingresa el numero del dia
mes = abs ( int ( input ( " ingrese el numero del mes: " ))) # aqui se ingresa el numero del mes
centuria = abs ( int ( input ( " ingrese los primeros 2 numeros del año: " ))) # aqui se pondrán los 2 primeros numeros del año
años = abs ( int ( input ( " ingrese los ultimos 2 numeros del año:: " ))) # aqui se pone los 2 ultimos numeros del año
calculodia = int((dia + 2.6 * (mes + 1 ) + años + (años // 4 ) + (centuria // 4 ) - 2 * centuria) % 7)  # la función nos arroja numeros desde el 0 que equivale asabado hasta el1 que es domingo
if calculodia==0:
    print("el dia es sabado")
elif calculodia==1:
    print("el dia es domingo")
elif calculodia==2:
    print("el dia es lunes")
elif calculodia==3:
    print("el dia es martes")
elif calculodia==4:
    print("el dia es miercoles")
elif calculodia==5:
    print("el dia es jueves")
elif calculodia==6:
    print("el dia es viernes")
