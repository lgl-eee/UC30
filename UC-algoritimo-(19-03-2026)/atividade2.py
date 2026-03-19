saldo = float(input("Digite o saldo da conta: "))
saque = float(input("Digite o valor do saque: "))

if saque > saldo:
    print("Saldo insuficiente para realizar o saque.")
else:
    final = saldo - saque
    if saque < 1000:
        taxa = saque * 0.02
        final -= taxa
        print(f"Saque realizado com sucesso. Saldo final: R$ {final}")
        print(f"Taxa de 2% aplicada ao valor do saque: R$ {taxa}")
    else:
        print(f"Saque realizado com sucesso. Saldo final: R$ {final}")