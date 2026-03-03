numero = int(input("Insira um número positivo: "))

quadrado = numero * numero
cubo = numero * numero * numero

if(numero %2==0):
    print("O número é par e ele ao quadrado é: ", quadrado)
else:
    print("O número é ímpar e ele ao cubo é: ", cubo)