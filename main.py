

estudiantes = {}
iterador = int ( input ('cantidad de registros a realizar: '))

for i in range (iterador):
    id_estudiante = len(estudiantes) + 1
    print (f'Registro {i+1}:')
    name = input ('Ingresa el nombre: ')
    lastname  = input ('Ingresa el apellido: ')

    estudiantes [id_estudiante] =    {'name' : name, 'lastname':lastname }
    print (f'Estudiante {name} {lastname} registrado con éxito.\n')    

for id_est, datos in estudiantes.items():
        print(f"{id_est:<5} {datos['name']:<15} {datos['lastname']:<15}")

        print ("-" * 42)
        
print(f"Total de estudiantes: {len(estudiantes)}")