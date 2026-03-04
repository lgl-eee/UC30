nome = input("Digite seu nome: ")

senhacerta = "123456"
tentativas = 3

while tentativas > 0:
    senha = input("Digite sua senha: ")
    if senha == senhacerta:
        print("Olá, ",  nome,". Seja bem-vindo ao nosso banco!")
    tentativas -= 1
    if tentativas == 2:
        print("Senha incorreta! Você ainda tem 2 tentativas.")
    elif tentativas == 1:
        print("Senha incorreta! Você ainda tem 1 tentativa.")
    else:
        print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")