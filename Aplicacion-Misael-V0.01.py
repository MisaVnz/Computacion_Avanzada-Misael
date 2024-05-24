import json

Suma = 0
ucs = 0

with open("periodo.json", "r") as Cedula:
    data_cedula = json.load(Cedula)

with open("dni.json", "r") as Nombre:
    data_nombre = json.load(Nombre)

with open("UC.json", "r") as Codigo:
    data_codigo = json.load(Codigo)

def nombre_del_alumno(Valor):
    for item in data_nombre:
        if item["dni"] == Valor:
            print(f"Cedula encontrada: {Valor}")
            return item["nombre"] + " " + item["apellido"]

def calculo(item):
    for row in data_codigo:
        global Suma
        global ucs
        if row["Codigo"] == item["Codigo"]:
            Suma += item["nota"] * row["UC"]
            ucs += row["UC"]

def mostrar_menu():
    print("1. Nombre del alumno")
    print("2. Nota y promedio del alumno")
    print("3. Agregar nota")
    print("4. Eliminar nota")
    print("\n0. Salir")

def menu_opcion(opcion):
    if opcion == '1':
        buscar = input("Ingrese la cedula para buscar: ")
        vnombre = nombre_del_alumno(buscar)
        print(f"El nombre del alumno es: {vnombre}")

    elif opcion == '2':
        buscar = input("Ingrese cedula: ")
        promedio_mostrado = False
        for item in data_cedula:
            if item["dni"] == buscar:
                calculo(item)
                prom = Suma / ucs
                vnombre = nombre_del_alumno(buscar)
                if not promedio_mostrado:
                    print(f"Nota, Promedio y Periodo de {vnombre}:")
                    promedio_mostrado = True
                print(f"  - Nota: {item['nota']}, Promedio: {prom:.2f}, Periodo: {item['Periodo']}")

    elif opcion == '3':
        cedula = input("Ingrese cedula del alumno: ")
        codigo = input("Ingrese el código de la materia: ")
        nota = float(input("Ingrese la nota: "))
        
        nota_actualizada = False
        for item in data_cedula:
            if item["dni"] == cedula and item["Codigo"] == codigo:
                item["nota"] = nota
                nota_actualizada = True
                break
        
        if not nota_actualizada:
            nueva_nota = {
                "dni": cedula,
                "Codigo": codigo,
                "nota": nota
            }
            data_cedula.append(nueva_nota)
        
        with open("periodo.json", "w") as file:
            json.dump(data_cedula, file, indent=4)
            
        print("La nota fue agregada exitosamente.")

    elif opcion == '4':
        cedula = input("Ingrese cedula del alumno: ")
        codigo = input("Ingrese el código de la materia a borrar: ")
        
        for item in data_cedula:
            if item["dni"] == cedula and item["Codigo"] == codigo:
                item["nota"] = 0
                with open("periodo.json", "w") as file:
                    json.dump(data_cedula, file, indent=4)
                print("La nota fue eliminada y reemplazada por cero exitosamente.")
                break
        else:
            print("No se encontró la nota a borrar.")

    elif opcion == '0':
        print("!Programa cerrado exitosamente¡")

    else:
        print("Error, Por favor, elija una opción válida (0-4).")

mostrar_menu()
opcion = input("Ingrese la opcion que desea utilizar: ")
menu_opcion(opcion)
