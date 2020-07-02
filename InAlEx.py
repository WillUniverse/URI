#coding: utf-8
import random

lista = []
for x in range (0, 4):
    lista.append(int(random.random()*10))
print("Original List: %s" % lista)

lista.append(15)
print("Adding element 15 in the end: %s" % lista)

lista.insert(0, 100)
print("Adding element 100 in the begin: %s" % lista)

lista[0] = 'Hello'
print("Changing the first element: %s" % lista)

#lista.clear() Didn't work

lista.pop(len(lista)-1)
print("Delete the last element: %s" % lista)

del(lista[1:3])
print("Deleting elements: %s" % lista)