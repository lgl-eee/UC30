a = 1 

while a == 1:
    try:
        print("1-soma")
        print("2-subtração")
        print("3-multiplicação")
        print("4-divisão")
        print("5-sair")
     
        b = int(input("Escolha uma opção: "))

        if b == 1:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado:", num1 + num2)

        elif b == 2:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado:", num1 - num2)

        elif b == 3:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("Resultado:", num1 * num2)

        elif b == 4:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if num2 != 0:
                print("Resultado:", num1 / num2)
            else:
                print("Erro: Divisão por zero não é permitida.")

        else:
            a = 0 
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")