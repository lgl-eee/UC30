a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

def soma_segura(a,b):
    resultado = a + b
    return resultado
try:
    soma_segura(a,b)
except TypeError:
    print("Erro: Os valores devem ser números.")
