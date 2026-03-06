notas = [7.5, 8.0, 9.5, 6.0, 8.5]
print("notas: ", notas)

print("menor nota: ", min(notas))
print("maior nota: ", max(notas))
print("soma: ", sum(notas))
print("média: ", sum(notas) / len(notas))  


nomes = ["adriana", "breno", "carla", "daniel"]

#apenas o elemento
print("usando FOR simples: ")
for nome in nomes:
    print(f"olá, {nome}!")

# indice e elemento
print("\n usando usando enumerate: ")
for indice, nome in enumerate(nomes):
    print(f"Posição{indice}: {nome}")


original = ["a", "b", "c"]
copia = list(original) 

print("original: ", original)
print("copia: ", copia) 
print("são iguais: ", original == copia)

copia.append("d")
print("original: ", original)
print("copia: ", copia) 
print("são iguais: ", original == copia)