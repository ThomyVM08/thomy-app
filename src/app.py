print("==============================")
print("       GESTOR DE TAREAS")
print("==============================")

nombre = input("Cómo te llamas? ")
tareas = int(input("Cuántas tareas tienes pendientes? "))

print(f"Hola {nombre}, tienes {tareas} tareas pendientes.")
print(f"Vamos a organizar tus {tareas} tareas!")

while True:
    print("1. Agregar tarea  2. Ver tareas  3. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        tarea = input("Nombre de la tarea: ")
        print(f"Tarea '{tarea}' agregada.")
    elif opcion == "2":
        print(f"Tienes {tareas} tareas pendientes.")
    elif opcion == "3":
        print("Saliendo de menu")
        break
    else:
        print("Opción no válida")


tareas = []

while True:
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("Ingresa el nombre de la tarea: ")
        tareas.append(tarea)
        print("Tarea agregada correctamente.")

    elif opcion == "2":
        if len(tareas) == 0:
            print("Todavía no hay registros.")
        else:
            for i in range(len(tareas)):
                print(f"{i + 1}. {tareas[i]}")
            print(f"Total de tareas: {len(tareas)}")

    elif opcion == "3":
        print("Saliendo de menu")
        break

    else:
        print("Opción no válida.")