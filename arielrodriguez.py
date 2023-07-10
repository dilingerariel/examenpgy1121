#profesor, nose porque se repiten las cosas pero usted siga poniendo los datos nomas, terminara funcionando
# https://github.com/dilingerariel/examenpgy1121




asistentes=[]
entradas = [20, 30, 50]
precios = [120000, 80000, 50000]
vendidas = [0, 0, 0]
ubicaciones = ['' for i in range(100)]

def comprar():
    print("Entradas")
    print("1. Platinum $120.000(Asientos del 1 al 20)")
    print("2. Gold $80.000(Asientos del 21 al 50)")
    print("3. Silver $50.000(Asientos del 51 al 100)")
    nombre=input("Nombre: ")
    apellido=input("Apellido: ")
    nombre.isalpha()
    apellido.isalpha()

    cantidad = int(input("Cantidad de entradas a comprar (1-3): "))
    while cantidad < 1 or cantidad > 3:
        print("Ingrese un valor entre 1 y 3.")
        cantidad = int(input("Digite la cantidad de entradas a comprar (1-3): "))

    for cantidad in range(cantidad):
        tipo = int(input("Seleccione el tipo de entrada (1-3): "))
        while tipo < 1 or tipo > 3 or entradas[tipo - 1] <= 0:
            print("Entradas no disponible.")
            tipo = int(input("Tipo de entrada (1-3): "))

        indice = tipo - 1
        asiento = int(input("Eliga número de asiento (1-100): "))
        while asiento < 1 or asiento > 100 or ubicaciones[asiento - 1] != '':
            print("Asiento inválido o ya reservado.Seleccione otro asiento.")
            asiento = int(input("Eliga el número de asiento (1-100): "))

        entradas[indice] -= 1
        vendidas[indice] += 1
        ubicaciones[asiento - 1] = 'X'

        rut = input("RUT para confirmar la reserva del asiento(sin guiones ni puntos): ")
        if rut == '-':
            print("Rut Malo.")
        rut = input("RUT para confirmar la reserva del asiento(sin guiones ni puntos): ")
        asistentes.append((rut, asiento))

    print("Compra Exitosa.")

def ubicaciones_disponibles():
    print("Ubicaciones disponibles:")
    for i, disponibles in enumerate(entradas):
        tipo = ""
        if i == 0:
            tipo = "ENTRADA PLATINUM"
        elif i == 1:
            tipo = "ENTRADA GOLD"
        else:
            tipo = "ENTRADA SILVER"
        print(f"{tipo}: {disponibles} disponibles")

    for i in range(100):
        if i % 10 == 0:
            print()
        if ubicaciones[i]=='':
            print(f"{i + 1} ","")
        else:
            print("X ","")
    print()



def lista_asistentes():
    print("Lista de asistentes por RUT:")
    if len(asistentes) == 0:
        print("No hay asistentes registrado con ese RUT.")
    else:
        for rut, asiento in asistentes:
            print(f"RUT: {rut}, Asiento: {asiento}")

def ganancias():
    total = sum([vendidas[i] * precios[i] for i in range(len(precios))])
    print(f"Total: ${total}")

while True:
    print("""
    ***BIENVENIDO A CREATIVOS.CL***
    1. COMPRAR ENTRADA
    2. MOSTRAR UBICACIONES DISPONIBLES
    3. VER LISTADO DE ASISTENTES
    4. MOSTRAR GANANCIAS TOTALES
    5. SALIR""")
    op = input("Seleccione Opción: ")

    match op:
        case '1':
            comprar()
        case '2':
            ubicaciones_disponibles()
        case '3':
            lista_asistentes()
        case '4':
            ganancias()
        case '5':
            print("Saliendo...")
            break
        case other:
            print("Opcion invalida.")



