nome1 = "ana"
nome2 = "bruno"
nome3 = "caio"

nomes = ["ana, bruno caio"]
print(nomes)

dados = ["carol", 0, 1.70, True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

lista = ["cachorro", "gato"]
print("original: ", lista)
lista.append("coelho") #add no final da lista
print("atualizado: ", lista)

lista.insert(1, "grilo") #add na posição determinada
print("atualizado: ", lista)

lista.extend(["macaco", "ovelha"])#add ,ais um dado de uma vez
print("atualizado: ", lista)