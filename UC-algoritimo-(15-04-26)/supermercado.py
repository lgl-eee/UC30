produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))

def calcular_total(produto1, produto2):
    return produto1 + produto2

print(f"O total a pagar é: R${calcular_total(produto1, produto2):.2f}")