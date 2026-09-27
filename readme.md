# TaskFlow - Proyecto Colaborativo DevOps Jose Ramon Caro Salas

## Rol del líder
Este repositorio es gestionado bajo metodología DevOps.
La rama `main` está protegida.

Nota: Revisar su participacion en los ISSUES del proyecto

## Reglas
- ❌ No se trabaja directo en main
- ✅ Cada cambio va en una branch las ramas deben llamarse con su nombre y función 
Ejemplo: Veronica– delete_task
- ✅ Todo cambio requiere Pull Request
- ✅ Al menos 1 revisión antes de merge

## Ejecución
```bash
python main.py

## Flujo DevOps 

1. Clonar repositorio
2. Crear branch personal
3. Resolver una tarea asignada
4. Hacer commit claros
5. Subir branch a GitHub
6. Crear Pull Request
7. Recibir revisión
8. Corregir si es necesario
9. Merge a main
10. Integración final del sistema

#archivos y funcionamiento:

Revisión de main.py
Se identificó que este módulo funciona como punto de entrada y coordina el menú, la interacción con el usuario, las operaciones de las tareas y el almacenamiento de la información donde se observan las importaciones de tasks.py, storage.py y utils.py, así como la función principal del sistema, 

Revisión de tasks.py
Se analizaron las funciones responsables de administrar las tareas, incluyendo su creación, visualización, completado y eliminación, además de las validaciones utilizadas durante estas operaciones.

Revisión de storage.py
Se identificó que este módulo administra la persistencia de las tareas mediante el archivo tasks.json y realiza validaciones para comprobar que los datos almacenados tengan una estructura válida.

Revisión de utils.py
 Se identificó que este módulo contiene la función encargada de mostrar el menú principal y las opciones disponibles para interactuar con el sistema.