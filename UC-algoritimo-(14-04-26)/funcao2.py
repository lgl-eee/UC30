x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

def divisao(x,y):
    resultado = x / y
    return resultado
try:
    divisao(x,y)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")