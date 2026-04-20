a = 1
filmesdisponiveis = ["teste","Vingadores: Ultimato", "O Rei Leão(Audiodescrição)", "Frozen II", "Toy Story 4", "Coringa", "Star Wars: A Ascensão Skywalker(Audiodescrição)", "Homem-Aranha: Longe de Casa", "Capitã Marvel(Audiodescrição)", "Aladdin", "It: Capítulo Dois", "Dumbo", "Malévola: Dona do Mal(CC)", "O Gato de Botas 2: O Último Pedido", "A Bela e a Fera", "Mulan", "Shazam!", "Dora e a Cidade Perdida(Audiodescrição)", "Jumanji: Próxima Fase(CC)", "Ad Astra: Rumo às Estrelas(Audiodescrição)", "Aves de Rapina: Arlequina e sua Emancipação Fantabulosa(Audiodescrição)"]
filmesalugados = []
dano = "(danificado)"
# fazer sistema de cadastro de usuário, para que o cliente seja reconhecido.

while a == 1:
    print("\n1. Alugar um filme")
    print("2. comprar um filme")
    print("3. devolver um filme")
    print("4. Vender um filme")
    print("5. Ver os filmes disponíveis")
    print("6. Sair")

    escolha = int(input("Digite o número da opção desejada: "))
    if escolha == 1:
        filme = input("Digite o nome do filme que deseja alugar: ")
        if filme in filmesdisponiveis:
            print("Filme alugado com sucesso!")
            filmesdisponiveis.remove(filme)
            filmesalugados.append(filme)
        elif filme in filmesalugados:
            print("Desculpe, esse filme já está alugado, volte em breve para verificar se ele já foi devolvido.")
        else:
            print("Desculpe, esse filme não está disponível para aluguel.")

    elif escolha == 2:
        filme2 = input("Digite o nome do filme que deseja comprar: ")
        if filme2 in filmesdisponiveis:
            print("Filme comprado com sucesso!")
            filmesdisponiveis.remove(filme2)
            filmesalugados.append(filme2)
        else:
            print("Desculpe, esse filme não está disponível para compra.")

    elif escolha == 3:
        filme3 = input("Digite o nome do filme que deseja devolver: ")
        if filme3 in filmesalugados:
            estadofilme = bool(input("O filme está em bom estado? (True/False): "))
            if estadofilme == True: 
                print("Filme devolvido com sucesso")
                filmesalugados.remove(filme3)
                filmesdisponiveis.append(filme3)
            else:                
                print("O filme está danificado, por favor pague a taxa de dano.")
                a2 = filmesdisponiveis.index(filme3)
                filmesdisponiveis[a2] += dano
                filmesdisponiveis.append(filme3)
                filmesalugados.remove(filme3)
        else:
            print("Desculpe, esse filme não está na lista de alugados.")

    elif escolha == 4:
        filme4 = input("Digite o nome do filme que deseja vender: ")
        if filme4 in filmesdisponiveis or filme4 in filmesalugados:
            print("Já possuímos esse filme.")
        else:
            estadofilme2 = bool(input("O filme está em bom estado? (True/False): "))
            if estadofilme2 == False:
                print("O preço do filme será reduzido devido ao estado danificado.")
                a2 = filmesdisponiveis.index(filme4)
                filmesdisponiveis[a2] += dano
                filmesdisponiveis.append(filme4)
            else:
                print("O filme está em bom estado, o preço do filme será o normal.")
            print("Esse filme foi adicionado ao nosso catálogo!")
            filmesdisponiveis.append(filme4)

    elif escolha == 5:
        print("Filmes disponíveis para aluguel e compra:")
        print(filmesdisponiveis)
        print("Filmes que ja foram alugados:")
        print(filmesalugados)

    elif escolha == 6:
        print("Obrigado por usar nosso sistema de aluguel e compra de filmes. Até a próxima!")
        a = 0
