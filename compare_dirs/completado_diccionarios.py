# Tenemos dos carpetas con los mismos archivos conceptualmente
# pero en diferentes formatos ejemplo: docx y pdf
# Encontrar los archivos que no están en ambos formatos

import glob
import os


def clean_name(name):
    """
    /A/B/C/hola.txt -> hola
    """
    # Obteniendo el nombre del archivo
    name = os.path.basename(name)
    ## Devolviendo el nombre sin extensión
    return os.path.splitext(name)[0]


def compare(path1, path2):
    files_1 = glob.glob(path1 + '/*')
    files_2 = glob.glob(path2 + '/*')

    # completado de diccionarios
    files_1 = {clean_name(f): f for f in files_1}
    files_2 = {clean_name(f): f for f in files_2}

    return [files_1[k] for k in files_1 if k not in files_2]

print(compare('t1', 't2'))
