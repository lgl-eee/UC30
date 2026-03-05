numeros = [80, 20, 30, 20, 40, 90, 50]

print("Lista:", numeros)

print("questão 1")
print("1) Número de elementos:", len(numeros))
print("2) Número de vezes que o número 20 aparece:", numeros.count(20))
print("3a) Posição do número 30:", numeros.index(30))
print("3b) O número 100 existe na lista?", 100 in numeros)

import random

numeros2 = [91, 34, 67, 15, 82]

print("Lista original:", numeros2)
numeros2.sort()
print("Lista crescente:", numeros2)
numeros2.sort(reverse=True)
print("Lista decrescente:", numeros2)

numeros3 = [6, 7, 8, 9, 10]
random.shuffle(numeros3)
print("Lista embaralhada:", numeros3)

numeros4 = [1,99, 12, 33, 20, 45, 67]
print("Lista original:", numeros4)
numeros4.sort()
print("Lista crescente:", numeros4)
numeros4.sort(reverse=True)
print("Lista decrescente:", numeros4)
random.shuffle(numeros4)
print("Lista embaralhada:", numeros4)   