'''Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. 
    ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? 
    Realice el algoritmo y represente la solución mediante el diagrama de flujo, el 
    pseudocódigo y el diagrama N/S, utilizando el ciclo apropiado.'''

    #Definir Variables
    acumuladorsalario=0.0

    # Ingresar Datos    
    tiempo=int(input("Ingrese los años disponible del incremento: "))
    salario=float(input(f"Ingrese su salario: "))
    #Calcular salario
    for x in range(tiempo+1):
        if x==0:
            print(f"El Salario total del año {x} es ",salario, " dolares")
        else:   
            incremeto=salario*0.10
            salarioTotal= salario+incremeto
            salario=salarioTotal
            if x!=tiempo:
                print(f"El Salario total del año {x} es ", round(salarioTotal,2), " dolares")
            else:
                print("")
                print(f"El ultimo salario  a percibir del año {x} es de ", round(salarioTotal,2), "dolares")
            acumuladorsalario+=salarioTotal
    #El salario total
    print("")
    print()
    print(f"El salario total recibido durante los {tiempo} años fue de: ",round(acumuladorsalario,2),"dolares")
    print("")
