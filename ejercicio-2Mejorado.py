# David Bordalas
import csv

def get_students():
    #  """
    # Función para obtener los datos de los estudiantes desde un archivo CSV.
    # Devuelve una lista de diccionarios, donde cada diccionario representa a un estudiante.
    # """   
    students = []
    headers = []# Lista para almacenar los encabezados de las columnas
# Abrir el archivo CSV y leer las filas
    with open('excelpython/calificaciones.csv', 'r', encoding="Utf-8") as file:
        studens_rows = csv.reader(file, delimiter='\n')

        for i, row in enumerate(studens_rows):
            row_str = row[0]
            if i == 0:
                headers = row_str.lower().split(';')# Convertir los encabezados a minúsculas y dividir por punto y coma
            else:
                student = row_str.split(';')# Dividir los datos de la fila por punto y coma
                students.append(dict(zip(headers, student)))# Crear un diccionario con los encabezados como claves y los datos de la fila como valores
    # Ordenar los estudiantes por apellidos            
    students = sorted(students, key=lambda x: x['apellidos'])


    # print(students) para mostrar el diccionario
    return students

def calculate_final_grade(students):
    # Función para calcular la nota final de los estudiantes.
    # Modifica la lista de estudiantes con el valor de la nota final calculada.
    # Calcular la nota final para cada estudiante
    for student in students:
        # Convertir los valores de parcial1 y parcial2 a float
        student['parcial1'] = float(student['parcial1'].replace(',','.')) 
        student['parcial2'] = float(student['parcial2'].replace(',','.'))
         # Convertir el valor de prácticas a float (si existe) o 0 si está vacío
        practicas = student['practicas']
        student['practicas']  = float(practicas.replace(',', '.') if practicas else 0)
        # Calcular la nota final con los pesos correspondientes
        student['nota_final'] = round(student['parcial1'] * 0.3 + student['parcial2'] * 0.3 + student['practicas']* 0.4 , 2)


def get_results(students):
    passed = []
    failed = []
# Función para determinar qué estudiantes han aprobado y cuáles han suspendido.
#     Devuelve dos listas: una con los nombres de los estudiantes aprobados y otra con los nombres de los estudiantes suspendidos.
    # HEX GREEN = '\x1b[32m{}\x1b[0m'  RED = '\x1b[31m{}\x1b[0m'
    green = '\033[1;32m{}\u001b[0m'
    red = '\033[1;31m{}\u001b[0m'

    for student in students:
        student_fullname = f"{student['apellidos']} {student['nombre']}"
        # student['parcial1'] < 4 or student['parcial2'] < 4 

                            # '75%' = ['7','5','%']
        # Comprobar si el estudiante ha aprobado o suspendido
        if int(student['asistencia'][:-1]) < 75 or student['nota_final'] < 5:
            failed.append(student_fullname)
            student['nota_final'] = red.format(student['nota_final']) 
            student['resultado'] = '\u001b[41m\u001b[30m\u001b[1mSuspendido\u001b[0m'
        else:
            passed.append(student_fullname)
            student['nota_final'] = green.format(student['nota_final'])
            student['resultado'] = '\u001b[42m\u001b[30m\u001b[1mAprobado\u001b[0m'
    
    return passed, failed


def print_table(students):
    # Función para imprimir una tabla con los datos de los estudiantes.
    print(f'{"Nombre del alumno":<28}\tAsistencia\tParcial 1\tParcial 2\tPracticas\tNota final')
    print('-' * 110)
    for student in students:
        print('{apellidos}, {nombre:<12}\t{asistencia:<10}\t{parcial1:<9}\t{parcial2:<9}\t{practicas:<9}\t{nota_final:<10}\t{resultado}'.format(**student))
    print()


def main():
    # Obtener los datos de los estudiantes
    students = get_students()
    # Calcular la nota final de los estudiantes
    calculate_final_grade(students)
    # Obtener los resultados (aprobados y suspendidos)
    passed, failed = get_results(students)
# Imprimir la tabla de estudiantes
    print_table(students)
    # Imprimir la lista de aprobados y suspendidos
    print(f'Lista de aprobados: {passed}')
    print(f'Lista de suspendidos: {failed}')



if __name__ == "__main__":
    main()
