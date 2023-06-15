# David Bordalás
import re

# Función que devuelve un listado de años
# recibe una línea del archivo TSV y devuelve una lista de años, extrayendo los elementos separados por tabulaciones después de la primera columna (que contiene el identificador del país).
def get_years(linea:str) -> list:
    return linea.strip().split('\t')[1:]

# Función que carga los datos del PIB de cada País
# recibe todas las líneas del archivo TSV y un patrón de expresión regular. Itera sobre las líneas, busca coincidencias con el patrón en la primera columna y guarda las iniciales del país y el listado de PIB correspondiente en un diccionario.
def get_data(lineas:str, patron:str) -> dict:
    # Creamos un diccionario vacío como resultado
    pib_data = dict()
    # Iteramos todas las líneas para recoger los datos necesarios
    for linea in lineas:
        # Recojemos la línea donde se encuentra el país
        country_line = linea.strip().split('\t')[0]
        # Buscamos si existe una coincidencia con nuestro patrón
        match = re.search(patron, country_line)
        if match:
            # Guardamos las iniciales del país
            country = match.group(1)
            # Recogemos el listado del PIB de ese país
            pib_list = linea.strip().split('\t')[1:]
            # Añadimos al diccionario
            pib_data[country] = pib_list
    return pib_data
# es el punto de entrada principal del programa. Lee todas las líneas del archivo TSV, obtiene los años y el diccionario de PIB llamando a las funciones auxiliares get_years() y get_data(). Luego, solicita al usuario que ingrese las iniciales de un país y muestra el PIB per cápita para ese país, si está disponible en el diccionario.
def run():
    # Leemos todas las líneas del archivo .tsv
    with open('excelpython/sdg_08_10.tsv', 'r') as archivo:
        lineas = archivo.readlines()

    # Listado de los años
    years = get_years(lineas[0])

    # Patrón de la expresión regular
    patron = r'CLV10_EUR_HAB,B1GQ,(.+)'

    # Diccionario de los PIB de cada país
    pib_data = get_data(lineas[1:], patron)

    # Pedimos al usuario que introduzca las iniciales de un país
    user_input = input('Introduce las iniciales de un país: ')
    user_country = user_input.upper()

    # Comprobamos si el país está en el diccionario
    if user_country in pib_data:
        print(f'Producto Interior Bruto per cápita de {user_country}\nAÑO\tPIB')
        # Mostramos los resultados
        for year, pib in zip(years, pib_data[user_country]):
            print(f'{year}\t{pib}')
    else:
        print('No se encuentra el país.')

if __name__ == '__main__':
    run()
