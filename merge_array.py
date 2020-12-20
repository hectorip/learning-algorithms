# Crear una función que recibe dos lsitas de eneteros ordenados y tiene que
# mezclarlas manteniendo el orden


# Return sorted array

def merge(a, b):
    c = []
    for e in a:
        if e < b[0]:
            c.append(e)
        else:
            while e > b[0]:
                c.append(b[0])
                b = b[1:]
            c.append(e)

    c += b
    return c

def mergeSort(a):
    l = len(a)



def mergeEasy(a, b):
    return sorted(a + b)

cases = [
    ([1, 2, 3], [3, 4, 5])
]

for c in cases:
    print(merge(*c))
    print(mergeEasy(*c))

# 1 -> No consideré elementos consecutivos menores/mayores que el elemento
# correspondiente en el array

# No reasignaba C + B

# Mi forma de probarlo es lenta
# Debería de tener Test cases

