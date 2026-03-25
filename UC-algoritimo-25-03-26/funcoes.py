#opção a: calculadora com funções 
def soma (a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao (a, b):
    return a * b

def divisao (a, b):
    if b == 0:
        return "Erro, divisão por zero impossível"
    else:
        return a / b
    
def calculadora():
    print("=== CALCULADORA ===")
    print (" 1. soma")
    print (" 2. subtração")
    print (" 3. multiplicacao")
    print (" 4. divisao")
    print (" 5. sair")

    while True:
        opcao = input("\nescolha uma operção 1-5: ")

        if opcao == 5:
            print("ate logo")
            break
        if opcao in ["1", "2", "3", "4"]:
            num1 = float(input("digite o primeiro numero: "))
            num2 = float(input("digite o segundo numero: "))

            if opcao == "1":
                print(f"resultado: {soma(num1, num2)}")
            elif opcao == "2":
                print(f"resultado: {subtracao(num1, num2)}")
            elif opcao == "3":
                print(f"resultado: {multiplicacao(num1, num2)}")
            elif opcao == "4":
                print(f"resultado: {divisao(num1, num2)}")
