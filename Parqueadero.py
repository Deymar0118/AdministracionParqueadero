import datetime

parqueaderoV = ["v" + str(i) for i in range(1, 51)]
parqueaderoM = ["m" + str(i) for i in range(1, 26)]

PlacaV = ["Vacio" for i in range(1,51)]
PlacaM = ["Vacio" for i in range(1,26)]

horaEntradaV = ["Vacio" for i in range(1,51)]
horaSalidaV = ["Vacio" for i in range(1,51)]

horaEntradaM = ["Vacio" for i in range(1,26)]
horaSalidaM = ["Vacio" for i in range(1,26)]

# NOTA: Valor del tiempo de ocupacion por hora = $3000
precio_por_hora = 3000

# Muestra la matriz del parqueader
def mostrar_Matriz(): 
    MatrizV = ["v" + str(i) for i in range(1, 51)]
    MatrizM = ["m" + str(i) for i in range(1, 26)]
    print("                         Matriz del Parqueadero                        ")
    print ("---------------------------Zona de Vehiculos---------------------------")
    for i in range(0, len(MatrizV), 10):
        print(MatrizV[i:i+10])
    print ("-----------------------------------------------------------------------\n")
    
    print ("-----------------------------Zona de Motos-----------------------------")
    for i in range(0, len(MatrizM), 10):
        print(MatrizM[i:i+10])
    print ("-----------------------------------------------------------------------\n") 

# Mostrar parqueadero con ocupación actual
def mostrar_Parqueadero():
    print ("---------------------------Zona de Vehiculos---------------------------")
    for i in range(0, len(parqueaderoV), 10):
        print(parqueaderoV[i:i+10])
    print ("-----------------------------------------------------------------------\n")
    
    print ("-----------------------------Zona de Motos-----------------------------")
    for i in range(0, len(parqueaderoM), 10):
        print(parqueaderoM[i:i+10])
    print ("-----------------------------------------------------------------------\n")      

# Alquilar vehículo
def AlquilarParqueaderoV(NumPlaca):
    for i in range(len(PlacaV)):
        if parqueaderoV[i] == "O" and PlacaV[i] == NumPlaca:
            print("El espacio ha sido alquilado por el vehículo de placa", NumPlaca)
            parqueaderoV[i] = "A"
            PlacaV[i] = NumPlaca
            break
        else:
            print("ATENCION: Primero tiene que registrar una hora de entrada")
            break

# Alquilar moto
def AlquilarParqueaderoM(NumPlaca):
    for i in range(len(PlacaM)):
        if PlacaM[i] == "O" and PlacaM[i] == NumPlaca:
            print("El espacio ha sido alquilado por la moto de placa", NumPlaca)
            parqueaderoM[i] = "A"
            PlacaM[i] = NumPlaca
            break
        else:
            print("ATENCION: Primero tiene que registrar una hora de entrada")
            break

# Registrar entrada de vehículo
def RegistrarEntradaV(NumPlaca):
    for i in range(len(parqueaderoV)):
        if parqueaderoV[i] != "A" and parqueaderoV[i] != "O":  
            PlacaV[i] = NumPlaca
            horaEntradaV[i] = input("Ingrese la hora de entrada (HH:MM): ")
            print("El espacio", parqueaderoV[i], " ha sido ocupado por el vehículo de placa ", NumPlaca)
            parqueaderoV[i] = "O"
            break
        else:
            print("El parqueadero esta lleno")
            
# Registrar entrada de moto
def RegistrarEntradaM(NumPlaca):
    for i in range(len(parqueaderoM)):
        if parqueaderoM[i] != "A" and parqueaderoM[i] != "O":
            parqueaderoM[i] = "O"
            PlacaM[i] = NumPlaca
            horaEntradaM[i] = input("Ingrese la hora de entrada (HH:MM): ")
            print("El espacio", parqueaderoM[i] ,"ha sido ocupado por la moto de placa", NumPlaca)
            break
        else:
            print("El parqueadero está lleno")

# Registrar salida de vehículo
def RegistrarSalidaV(NumPlaca):
    for i in range(len(PlacaV)):
        if PlacaV[i] == NumPlaca:
            horaSalidaV[i] = input("Ingrese la hora de salida (HH:MM): ")
            break
        else:
            print("Vehículo no encontrado en el parqueadero")

# Registrar salida de moto
def RegistrarSalidaM(NumPlaca):
    for i in range(len(PlacaM)):
        if PlacaM[i] == NumPlaca:
            horaSalidaM[i] = input("Ingrese la hora de salida (HH:MM): ")
            break
        else:
            print("Moto no encontrada en el parqueadero")

# Calcular precio
def calcular_precio(hora_entrada, hora_salida):
    formato = "%H:%M"
    entrada = datetime.datetime.strptime(hora_entrada, formato)
    salida = datetime.datetime.strptime(hora_salida, formato)
    horas_ocupadas = (salida - entrada).total_seconds() / 3600

    total = horas_ocupadas * precio_por_hora

    # Definir el horario diurno de 6am a 10pm
    hora_inicio_diurna = datetime.datetime.strptime("06:00", formato)
    hora_fin_diurna = datetime.datetime.strptime("22:00", formato)
    
    if entrada >= hora_inicio_diurna and salida <= hora_fin_diurna and horas_ocupadas >= (16 * 0.7):  # 70% de una jornada de 16 horas
        total *= 0.85  # Aplicar el 15% de descuento

    return horas_ocupadas, total

# Facturar
def Facturar(NumPlaca, tipo_transporte):
    if tipo_transporte == "v":
        for i in range(len(PlacaV)):
            if PlacaV[i] == NumPlaca:
                if horaEntradaV[i] != "Vacio" and horaSalidaV[i] != "Vacio":
                    horas, total = calcular_precio(horaEntradaV[i], horaSalidaV[i])
                    print("El vehículo con placa ", NumPlaca, " estuvo ", horas, " horas. Total a pagar: $", total)
                else:
                    print("Debe registrar una hora de entrada y salida.")
                break
    elif tipo_transporte == "m":
        for i in range(len(PlacaM)): 
            if PlacaM[i] == NumPlaca:
                if horaEntradaM[i] != "Vacio" and horaSalidaM[i] != "Vacio":
                    horas, total = calcular_precio(horaEntradaM[i], horaSalidaM[i])
                    print("La moto con placa ", NumPlaca, " estuvo ", horas, " horas. Total a pagar: $", total)
                else:
                    print("Debe registrar una hora de entrada y salida.")
                break

# Estado del parqueadero
def Estado():
    print ("-------Zona de Vehiculos-------")
    contadorAlquiladosV =0
    for i in range(len(parqueaderoV)):
        if parqueaderoV[i] == "A":
            contadorAlquiladosV = contadorAlquiladosV +1
    print("espacios alquilados: ", contadorAlquiladosV)
    contadorAlquiladosV =0
    
    contadorOcupadosV =0
    for i in range(len(parqueaderoV)):    
        if parqueaderoV[i] == "O":
            contadorOcupadosV = contadorOcupadosV +1      
    print("espacios ocupados: ", contadorOcupadosV)
    contadorOcupadosV =0  
      
    contadorVaciosV =0    
    for i in range(len(PlacaV)):
        if PlacaV [i] == "Vacio":
            contadorVaciosV = contadorVaciosV +1
    print("Espacios vacios: ",contadorVaciosV)
    contadorVaciosV =0
    print ("-------------------------------")
    print("")
    
    print ("-------Zona de Motos-------")
    contadorAlquiladosM =0
    for i in range(len(parqueaderoM)):
        if parqueaderoM[i] == "A":
            contadorAlquiladosM = contadorAlquiladosM +1
    print("espacios alquilados: ", contadorAlquiladosM)
    contadorAlquiladosM =0
    
    contadorOcupadosM =0
    for i in range(len(parqueaderoM)):    
        if parqueaderoM[i] == "O":
            contadorOcupadosM = contadorOcupadosM +1      
    print("espacios ocupados: ", contadorOcupadosM)
    contadorOcupadosM =0  
      
    contadorVaciosM =0    
    for i in range(len(PlacaM)):
        if PlacaM [i] == "Vacio":
            contadorVaciosM = contadorVaciosM +1
    print("Espacios vacios: ",contadorVaciosM)
    contadorVaciosM =0
    print ("---------------------------")
    print("")

# Menú principal
opcion = 0
while opcion != 8:
    print("REGISTRO DE TRANSPORTE DEL PARQUEADERO")
    print("1. Mostrar  Matriz del Parqueadero")
    print("2. Alquilar")
    print("3. Registrar Hora de Entrada")
    print("4. Actualizar")
    print("5. Registrar Hora de Salida")
    print("6. Facturar (no disponible)")
    print("7. Informar ocupacion")
    print("8. Salir")
    print("-------------------------------------")

    opcion = int(input("Elija una opción: "))
    match opcion:
        case 1:
            mostrar_Matriz()
        case 2:
            Placa = str (input("Ingrese la placa: "))
            
            print("Tipo de trasporte ")
            print("1. Vehiculo (v)")
            print("2. Moto (m)")
            TipoTransporte = input("Ingrese una opción (v/m): ").lower()
            
            if TipoTransporte =="v":
                AlquilarParqueaderoV(Placa)
                
            if TipoTransporte =="m":
                AlquilarParqueaderoM(Placa)
                
            if TipoTransporte != "m" and TipoTransporte != "v":
                print ("opcion invalida. Ingrese otra opcion")
        case 3:
            Placa = str (input("Ingrese la placa: "))
            
            print("Tipo de trasporte ")
            print("1. Vehiculo (v)")
            print("2. Moto (m)")
            TipoTransporte = input("Ingrese una opción (v/m): ").lower()
            
            if TipoTransporte =="v":
                RegistrarEntradaV(Placa)
                
            if TipoTransporte =="m":
                RegistrarEntradaM(Placa)
                
            if TipoTransporte != "m" and TipoTransporte != "v":
                print ("Opcion invalida. Ingrese otra opcion")
        case 4:
            mostrar_Parqueadero()
        case 5:
            Placa = str (input("Ingrese la placa: "))
            
            print("Tipo de trasporte ")
            print("1. Vehiculo (v)")
            print("2. Moto (m)")
            TipoTransporte = input("Ingrese una opción (v/m): ").lower()
            
            if TipoTransporte =="v":
                RegistrarSalidaV(Placa)
                
            if TipoTransporte =="m":
                RegistrarSalidaM(Placa)
        case 6:
            Placa = str (input("Ingrese la placa: "))
            
            print("Tipo de trasporte ")
            print("1. Vehiculo (v)")
            print("2. Moto (m)")
            TipoTransporte = input("Ingrese una opción (v/m): ").lower()
            Facturar(Placa, TipoTransporte)
        case 7:
            Estado()
        case 8:
            print("Finalizando el programa. Hasta luego.")