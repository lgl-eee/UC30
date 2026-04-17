vendas = [1, 6, 19, 20, 11, 323, 100, 322, 112, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]

pares = []

for num in vendas:
    if num % 2 == 0:
        pares.append(num)

a = sum(pares)
print("Soma dos números pares:", a)
