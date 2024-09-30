# Problemas encontrados:
# 1. el acumulador "ContadorVaciosM" y "ContadorVaciosV" no disminuyen cuando se alquila un espacio
# 2. error al registrar una salida para motos 

# Fuciones faltantes:
# implentear las tarifas
# implemntar el reloj
# calcular el precio por espacio

parqueaderoV = ["v" + str(i) for i in range(1, 51)]
parqueaderoM = ["m" + str(i) for i in range(1, 26)]

PlacaV = ["Vacio" for i in range (1,51)]
PlacaM = ["Vacio"for i in range (1,26)]

# Muestra el parqueadero
def mostrar_Parqueadero():
    for i in range(0, len(parqueaderoV), 10):
        print(parqueaderoV[i:i+10])
    print(" ")
    for i in range(0, len(parqueaderoM), 10):
        print(parqueaderoM[i:i+10])
        
        
# Alquila Vehiculos      
def AlquilarParqueaderoV(NumPlaca):
    for i in range(len(parqueaderoV)):
        if parqueaderoV[i] !="A" and parqueaderoV[i] !="O":
            print("el espacio ", parqueaderoV[i], "ha sido alquilado por el vehiculo de placa ", NumPlaca)
            parqueaderoV[i] = "A"
            break
              
# Alquila motos     
def AlquilarParqueaderoM(NumPlaca):
    for i in range(len(parqueaderoM)):
        if parqueaderoM[i] !="A" and parqueaderoM[i] !="O":
            print("el espacio ", parqueaderoV[i], "ha sido alquilado por la moto de placa ", NumPlaca)
            parqueaderoM[i] = "A"
            break
        
# Registro de entrada para Vehiculos
def RegistrarEntradaV(NumPlaca):
    for i in range(len(parqueaderoV)):
        if parqueaderoV[i] !="A" and parqueaderoV[i] !="O":
            print("el espacio ", parqueaderoV[i], "ha sido alquilado por el vehiculo de placa ", NumPlaca)
            parqueaderoV[i] = "O"
            break
        
    for i in range(len(PlacaV)):
        if PlacaV[i] == "Vacio":
            PlacaV[i] = NumPlaca
            break
        
# Registro de entrada para Motos
def RegistrarEntradaM(NumPlaca):
    for i in range(len(parqueaderoM)):
        if parqueaderoM[i] !="A" and parqueaderoM[i] !="O":
            print("el espacio ", parqueaderoM[i], "ha sido alquilado por la moto de placa ", NumPlaca)
            parqueaderoM[i] = "O"
            break
        
    for i in range(len(PlacaM)):
        if PlacaM[i] == "Vacio":
            PlacaM[i] = NumPlaca
            break

# Registro de salida para Vehiculos
def RegistrarSalidaV(NumPlaca):
    for i in range(len(parqueaderoV)):
        if PlacaV [i] == NumPlaca:
            PlacaV [i] = "Vacio"
            parqueaderoV [i] = "v"+ str(i+1)
            print("Vehiculo despachado")
            
# Registro de salida para Motos
def RegistrarSalidaM(NumPlaca):
    for i in range(len(parqueaderoM)):
        if PlacaM [i] == NumPlaca:
            PlacaM [i] = "Vacio"
            parqueaderoM [i] = "v"+ str(i+1)
            print("Moto despachada")
            
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
            
    
opcion = 0
while opcion!=7:
    print("1. Mostrar Parqueadero")
    print("2. Alquilar")
    print("3. Registrar Entrada")
    print("4. Registrar Salida")

    opcion = int(input("elija una opcion: "))
    
    match opcion:
        case 1:
            mostrar_Parqueadero()
        case 2:
            Placa = int (input("ingrese la placa: "))
            
            print("Tipo de trasporte ")
            print("1. Vehiculo (v)")
            print("2. Moto (m)")
            TipoTransporte = input("Ingrese una opción (v/m): ").lower()
            
            if TipoTransporte =="v":
                AlquilarParqueaderoV(Placa)
                
            if TipoTransporte =="m":
                AlquilarParqueaderoM(Placa)
                
            if TipoTransporte != "m" and TipoTransporte != "v":
                print ("opcion invalida. ingrese otra opcion")
        case 3:
            Placa = str (input("ingrese la placa: "))
            
            print("Tipo de trasporte ")
            print("1. Vehiculo (v)")
            print("2. Moto (m)")
            TipoTransporte = input("Ingrese una opción (v/m): ").lower()
            
            if TipoTransporte =="v":
                RegistrarEntradaV(Placa)
                
            if TipoTransporte =="m":
                RegistrarEntradaM(Placa)
                
            if TipoTransporte != "m" and TipoTransporte != "v":
                print ("opcion invalida. ingrese otra opcion")
        case 4:
            Placa = str (input("ingrese la placa: "))
            
            print("Tipo de trasporte ")
            print("1. Vehiculo (v)")
            print("2. Moto (m)")
            TipoTransporte = input("Ingrese una opción (v/m): ").lower()
            
            if TipoTransporte =="v":
                RegistrarSalidaV(Placa)
                
            if TipoTransporte =="m":
                RegistrarSalidaM(Placa)
        case 5:
            Estado()
            