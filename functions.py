from data import students

def input_int(message): # FUNCIÓN PARA VALIDAR ENTEROS

    """
    Solicita un número entero al usuario hasta que sea válido.
    """
    while True:
        try:
            value = int(input(message)) 
            if value > 0:
                return value
            print("Error: debe ser un número mayor que 0.\n")
        except ValueError:
            print("Error: debes ingresar una edad valida.\n")

# FUNCIÓN PARA VALIDAR TEXTO
def input_text(message):
    """
    Solicita texto no vacío.
    """
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Error: el campo no puede estar vacío.\n")

# VALIDAR ID ÚNICO
def id_exists(student_id):
    """
    Verifica si un ID ya existe en la lista.
    """
    for student in students:
        if student["id"] == student_id:
            return True
    return False

# AGREGAR ESTUDIANTE
def add_student():
    print("\n--- ADD STUDENT ---")

    # Validar ID único
    while True:
        student_id = input_int("Enter student ID: ")
        if not id_exists(student_id):
            break
        print("Error: ID already exists.\n")

    name = input_text("Enter name: ")
    age = input_int("Enter age: ")
    course = input_text("Enter course: ")
    status = True  # Activo por defecto

    # Crear diccionario del estudiante
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "status": status
    }

    students.append(student)
    print("Student added successfully!\n")

# MOSTRAR ESTUDIANTES
def show_students():
    print("\n--- STUDENT LIST ---")

    # Validar si la lista está vacía
    if not students:
        print("No students registered.\n")
        return

    # Mostrar cada estudiante
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, "
              f"Age: {student['age']}, Course: {student['course']}, "
              f"Status: {'Active' if student['status'] else 'Inactive'}")
    print()


# BUSCAR ESTUDIANTE
def find_student():
    print("\n--- FIND STUDENT ---")

    if not students:
        print("No students available.\n")
        return

    student_id = input_int("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("Student found:")
            print(student, "\n")
            return

    print("Student not found.\n")

# ACTUALIZAR ESTUDIANTE
def update_student():
    print("\n--- UPDATE STUDENT ---")

    if not students:
        print("No students available.\n")
        return

    student_id = input_int("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:

            # Validaciones controladas (no sale hasta ser correctas)
            student["name"] = input_text("New name: ")
            student["age"] = input_int("New age: ")
            student["course"] = input_text("New course: ")

            while True:
                status_input = input("Active? (yes/no): ").lower()
                if status_input in ["yes", "no"]:
                    student["status"] = status_input == "yes"
                    break
                print("Error: enter 'yes' or 'no'.")

            print("Student updated successfully!\n")
            return

    print("Student not found.\n")


# ELIMINAR ESTUDIANTE
def delete_student():
    print("\n--- DELETE STUDENT ---")

    if not students:
        print("No students available.\n")
        return

    student_id = input_int("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:

            # Confirmación real (como app)
            while True:
                confirm = input("Are you sure? (yes/no): ").lower()
                if confirm in ["yes", "no"]:
                    break
                print("Invalid option.")

            if confirm == "yes":
                students.remove(student)
                print("Student deleted.\n")
            else:
                print("Operation cancelled.\n")

            return

    print("Student not found.\n")