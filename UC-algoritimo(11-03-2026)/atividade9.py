preco = float(input("Digite o preço: "))

if preco <100:
    print("sem desconto")
    preco_final = preco
elif 100 <= preco < 500:
    print("desconto de 5%")
    preco_final = preco * 0.95
elif 1000 > preco >= 500:
    print("desconto de 10%")
    preco_final = preco * 0.90
else:
    print("desconto de 15%")
    preco_final = preco * 0.85