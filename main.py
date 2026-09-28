from tasks import (
    add_task,
    list_tasks,
    complete_task,
    delete_task
)
from storage import load_tasks, save_tasks
from utils import show_menu


tasks = []


def main():
    """
    Función principal del programa.

    Carga las tareas almacenadas desde el archivo JSON y muestra
    continuamente el menú principal. Permite agregar, listar,
    completar y eliminar tareas.

    Los cambios realizados en las tareas se guardan automáticamente
    en el archivo únicamente cuando una operación se completa
    correctamente.

    Returns:
        None
    """
    global tasks

    # Cargar tareas almacenadas al iniciar el programa
    tasks = load_tasks()

    while True:
        show_menu()

        option = input("Selecciona una opción: ").strip()

        # Validar que la opción sea un número
        if not option.isdigit():
            print("Error: Debes ingresar un número.")
            continue

        # Validar rango de opciones
        if option not in ["1", "2", "3", "4", "5"]:
            print("Error: Opción fuera de rango.")
            continue

        # Agregar tarea
        if option == "1":
            title = input("Título de la tarea: ").strip()

            if add_task(tasks, title):
                save_tasks(tasks)

        # Listar tareas
        elif option == "2":
            list_tasks(tasks)

        # Completar tarea
        elif option == "3":
            try:
                task_id = int(
                    input("ID de la tarea a completar: ").strip()
                )

                if complete_task(tasks, task_id):
                    save_tasks(tasks)

            except ValueError:
                print("ID inválido. Debe ser un número.")

        # Eliminar tarea
        elif option == "4":
            try:
                task_id = int(
                    input("ID de la tarea a eliminar: ").strip()
                )

                if delete_task(tasks, task_id):
                    save_tasks(tasks)

            except ValueError:
                print("ID inválido. Debe ser un número.")

        # Salir
        elif option == "5":
            save_tasks(tasks)
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()