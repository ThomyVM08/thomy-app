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
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida")