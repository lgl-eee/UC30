while True:
    try:
        peso = float(input("Digite o peso em kg: "))
        altura = float(input("Digite a altura em metros: "))
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

imc = peso / (altura ** 2)

if imc <= 24.9:
    print("magro")
else:
    print("peso normal ou acima do peso")

