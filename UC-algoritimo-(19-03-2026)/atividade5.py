tentativas = 0
senha = input("Digite a senha: ")
usuario = input("Digite o nome de usuário: ")

def verificar_usuario(usuario, senha,tentativas):
    if usuario == "admin" and senha == "1234":
        print("Acesso concedido")
        return True
    elif tentativas == 1:
        print("Acesso negado 2 tentativas restantes")
        tentativas += 1
        return False
    elif tentativas == 2:
        print("Acesso negado 2 tentativas restantes")
        tentativas += 1
        return False
    elif tentativas == 3:
        print("Acesso negado 1 tentativa restante")
        tentativas += 1
        return False
        print("bloqueado")
