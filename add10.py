lista = [1, 2, 3, 4]

i_lista = []

for x in range (len(lista)):
    i_lista.append(x)

for item in i_lista:
    lista[item] += 10
print(lista)


