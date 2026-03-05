nomes = ["ana", "bruno", "carlos", "diana"]
print("nomes: ", nomes)

nomes.remove("bruno")
print("lista atualizada: ", nomes)

#removido = nomes.pop()
removido = nomes.pop(1)
print(f"removido: {removido}")
print("Após pop:", nomes)

#del - remover pelo indice
del nomes[0]
print("Após del nomes[0]:", nomes)

#clear: esvaziar
nomes.clear()
print("lista atualizada: ", nomes)