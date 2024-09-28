parqueaderoV = ["v" + str(i) for i in range(1, 51)]
parqueaderoM = ["v" + str(i) for i in range(1, 26)]

def mostrar_Parqueadero():
    for i in range(0, len(parqueaderoV), 10):
        print(parqueaderoV[i:i+10])
    print(" ")
    for i in range(0, len(parqueaderoM), 10):
        print(parqueaderoM[i:i+10])
        
def AlquilarParqueaderoV():
    for i in range( len(parqueaderoV)):
        if parqueaderoV[i] !="A" and parqueaderoV[i] !="O":
            parqueaderoV[i] = "A"
            break
        
def AlquilarParqueaderoM():
    for i in range( len(parqueaderoM)):
        if parqueaderoM[i] !="A" and parqueaderoM[i] !="O":
            parqueaderoM[i] = "A"
            break
            

opcion =0
while opcion!=7:
    print("1. Mostrar parqueadero")
    print("2. Alquilar")

    opcion = int(input("elija una opcion: "))
    
    match opcion:
        case 1:
            mostrar_Parqueadero()
        case 2:
            print("Tipo de trasporte ")
            print("1. Vehiculo (v)")
            print("2. Moto (m)")
            
            TipoTransporte = input("Ingrese una opción (v/m): ").lower()
            
            if TipoTransporte =="v":
                AlquilarParqueaderoV()
                
            if TipoTransporte =="m":
                AlquilarParqueaderoM()
                
            else:
                print ("opcion invalida. ingrese otra opcion")
                
            
        