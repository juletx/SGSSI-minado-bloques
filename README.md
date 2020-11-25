# Minado de bloques SGSSI
Este repositorio contienen el código de minado para la [cadena de bloques](https://docs.google.com/spreadsheets/d/e/2PACX-1vRcq7exptaE-9KN8gPj-ikgZdfNP87x4oY7HdlGtxE6DTYqXBok1pQ1UlHQ11Ub8PIHr0zF6uNav_xW/pubhtml?gid=0&single=true) de SGSSI (Sistemas de Gestión de Seguridad de Sistemas de Información).

Las carpetas input y output contienen los archivos de entrada y salida. Los archivos de entrada son los bloques que hay que minar. Estos bloques los crea el profesor a partir de las entregas de los alumnos. Los bloques contienen:
* El número de bloque
* El resúmen MD5 del bloque anterior
* El código de la entrega
* El número de entregas
* Los resúmenes MD5 de las entregas de todos los alumnos

Los de salida son los bloques minados propuestos para la cadena de bloques. Se puede ver que algunos de ellos fueron incluidos en la cadena. Para minar un bloque hay que realizar una prueba de trabajo. Esto significa que hay que realizar muchas pruebas para obtener un bloque minado. Tiene que tener los siguientes requisitos:
* Una línea adicional con 8 caracteres en hexadecimal y el identificador del grupo.
* El resumen MD5 del archivo modificado tiene que empezar por muchos ceros.

El repositorio contiene 6 archivos python:

## md5-file.py
Calcula el MD5 de un fichero de entrada y lo inprime.

Uso: ```python md5-file.py filename```

## modify-file-md5.py
Crea un fichero modificado que contiene una línea adicional con 8 caracteres en hexadecimal y el identificador del grupo.
El MD5 de ese fichero empieza por varios ceros.

Uso: ```python modify-file-md5.py filename ```

## modify-file-md5-parallel.py
Crea un fichero modificado que contiene una línea adicional con 8 caracteres en hexadecimal y el identificador del grupo.
El MD5 de ese fichero empieza por varios ceros. Se puede ejecutar en paralelo especificando el númro de procesadores para que sea más rápido.

Uso: ```python modify-file-md5-parallel.py options ```

## check-modified-file.py
Comprueba que el fichero cumple los requisitos descritos en el anterior programa.

Uso: ```python check-modified-file.py filename ```

## sha256-file.py
Calcula el sha-256 de un fichero de entrada y lo inprime.

Uso: ```python sha256-file.py filename```

## modify-file-sha256.py
Crea un fichero modificado que contiene una línea adicional con 8 caracteres en hexadecimal y el identificador del grupo.
El sha-256 de ese fichero empieza por varios ceros.

Uso: ```python modify-file-sha256.py filename ```