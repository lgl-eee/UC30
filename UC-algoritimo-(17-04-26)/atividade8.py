preco = int(input("Digite o preço do produto: "))

if preco > 500:
    print("desconto de 20%")
    preco_final = preco * 0.8
elif 500 > preco > 200:
    print("desconto de 10%")
    preco_final = preco * 0.9
elif preco < 200:
    print("sem desconto")
    preco_final = preco

print("O preço final do produto é:", preco_final)