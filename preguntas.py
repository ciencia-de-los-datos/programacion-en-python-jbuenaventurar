"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


from ast import operator


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    result = [row[1]for row in data]
    result = [int(i) for i in result]
    result = sum(result)
    result
    return result
pregunta_01()

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row[0] for row in data]
    result = {}
    for letra in data:
        if letra in result.keys():
            result[letra] = result[letra]+1
        else:
            result[letra] = 1
    tuplas = [(key, value) for key, value in result.items()]
    from operator import itemgetter
    tuplas = sorted(tuplas, key=itemgetter(0))
    return tuplas
pregunta_02()

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [row[:2]for row in data]
    result = {}
    for letra, valor in data:
        valor = int(valor)
        if letra in result.keys():
            result[letra]= result[letra]+valor
        else:
            result[letra] = valor
    result = [(key, valor) for key, valor in result.items()]
    result = sorted(result, key = itemgetter(0), reverse = False)
    return result
pregunta_03()


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t')[2] for row in data]
    data = [row[5:7] for row in data]
    result = {}
    for letra in data:
        if letra in result.keys():
            result[letra] = result[letra]+1
        else:
            result[letra] = 1
    tuplas = [(key, value) for key, value in result.items()]
    from operator import itemgetter
    tuplas = sorted(tuplas, key=itemgetter(0))
    return tuplas
pregunta_04()


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [row[:2]for row in data]
    result = {}
    for letra, valor in data:
        valor = int(valor)
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra] = [valor]
    result = [(key, max(valor), min(valor)) for key, valor in result.items()]
    result = sorted(result, key = itemgetter(0), reverse = False)
    return result
pregunta_05()

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t')[4] for row in data]
    data = [row.replace('\n', '') for row in data]
    data = [row.split(',') for row in data] 
    data4 = []
    for z in data:
        for x in z:
            data4.append(x)
    data4 = [row.split(':') for row in data4]
    result = {}
    for letra, valor in data4:
        valor = int(valor)
        if letra in result.keys():
            result[letra].append(valor)
        else:
            result[letra] = [valor]
    result = [(key, min(valor), max(valor)) for key, valor in result.items()]
    result = sorted(result, key = itemgetter(0), reverse = False)
       
    return result
pregunta_06()

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t')[:2] for row in data]
    result = {}
    for letra, numero in data:
        numero = int(numero)
        if numero in result.keys():
            result[numero].append(letra)
        else:
            result[numero] = [letra]
    result = [(key, values) for key, values in result.items()]
    result = sorted(result, key=lambda tup: tup[0], reverse=False)
    return result
pregunta_07()

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t')[:2] for row in data]
    result = {}
    for letra, numero in data:
        numero = int(numero)
        if numero in result.keys():
            result[numero].append(letra)
        else:
            result[numero] = [letra]
    for key, values in result.items():
        values = list(set(values))
        values.sort()
        result[key]= values
    result = [(key, values) for key, values in result.items()]
    result = sorted(result, key=lambda tup: tup[0], reverse=False)
    return result
pregunta_08()

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t')[4] for row in data]
    data = [row.replace('\n', '') for row in data]
    data = [row.split(',') for row in data] 
    data4 = []
    for z in data:
        for x in z:
            data4.append(x)
    dataRegistros = []
    for z in data4:
        dataRegistros.append(z[:3])
    result = {}
    for letra in dataRegistros:
        if letra in result.keys():
            result[letra] = result[letra]+1
        else:
            result[letra] = 1
    result = dict(sorted(result.items(), key=lambda item: item[0]))
    return result
pregunta_09()


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [[cadena.replace('\n', '') for cadena in row] for row in data]
    data = [[row[0], row[3], row[4]] for row in data] 
    data = [[cadena.split(',') for cadena in row] for row in data]
    result = [(row[0][0], len(row[1]), len(row[2])) for row in data]
    return result
pregunta_10()

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [[row[1], row[3]] for row in data]
    result = {}
    for row in data:
        numero = int(row[0])
        for letra in row[1].split(','):
            if letra in result.keys():
                result[letra]+= numero
            else:
                result[letra] = numero
    result = dict(sorted(result.items(), key=lambda item: item[0]))
    return result
pregunta_11()

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    from operator import itemgetter
    with open('data.csv', 'r') as file:
        data = file.readlines()
    data = [row.split('\t') for row in data]
    data = [[row[0], row[4].replace('\n', '')] for row in data]
    result = {}
    for row in data:
        row[1] = row[1].split(',')
        row[1] = [cadena.split(':')[1]  for cadena in row[1]]
        row[1] = [int(x) for x in row[1]]
        row[1] = sum(row[1])
    for row in data:
        if row[0] in result.keys():
            result[row[0]]+= row[1]
        else:
            result[row[0]] = row[1]
            
        #import pdb
        #pdb.set_trace()
    result = dict(sorted(result.items(), key=lambda item: item[0]))
    return result
pregunta_12()