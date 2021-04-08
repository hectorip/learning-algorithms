lista = [
  "uno",
  "dos",
  "tres",
  "uno",
  "dos",
  "cuatro",
]

repetidos = set()
clean_list = set()
for el in lista:
  if el not in clean_list:
    clean_list.add(el)
  else:
    repetidos.add(el)

print(repetidos)
