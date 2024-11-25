opcion=1
print("Bienvenido Usuario")
while opcion!=0:
    print("Ingresa 1. Área triángulo")
    print("Ingresa 2. Área rectángulo")
    print("Ingresa 3. Área círculo")
    print("Ingresa 4. Convertir temperatura °F a °C")
    print("Ingresa 5. Convertir temperatura °C a °F")
    op=int(input("¿Qué operacion quieres realizar?"))

    if (op==1):
        num1=int(input("¿Cual es la bace? "))
        num2=int(input("¿Cual es la altura? "))
        areat=num1*num2/2
        print("El area de tu triangulo es: ",areat)
    elif(op==2):
        num1=int(input("¿Cual es la bace? "))
        num2=int(input("¿Cual es la altura? "))
        arear=num1*num2
        print("La base de tu rectangulo es:",arear)
    elif(op==3):
        num1=int(input("¿Cual es el radio de tu circulo? "))
        areac=num1*num1*3.14159265
        print("El área de tu círculo es:",areac)
    elif(op==4):
        num1=int(input("¿Qué grados fahrenheit quieres covertir? "))
        gradosf=(num1-32)*5/9
        print("tus grados fahrenheit son:",gradosf,"en celsius")
    elif(op==5):
        num1=int(input("¿Qué grados celsius quieres covertir? "))
        gradosc=(num1*9/5)+32
        print("tus grados celsius son:",gradosc,"en fahrenheit")
    else:
            print("No valido")
    opcion=int(input("Deseas continuar?, sino precionar 0. para salir"))