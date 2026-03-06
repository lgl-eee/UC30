#estruturas de dados onde uma lista é contida dentro de outra lista, permitindo representar tabelas. serve para organizar grandes conjuntos de dados

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("matriz completa: ", matriz)
for linha in matriz:
    print(linha)

print(f"\n elemento [1][2]: {matriz[1][2]}") 
print(f"\n elemento [0][0]: {matriz[0][0]}")
print(f"\n elemento [2][1]: {matriz[2][1]}")
