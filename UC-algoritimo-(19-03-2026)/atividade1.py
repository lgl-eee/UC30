pontos = int(input("Digite a quantidade de pontos: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

def rank_jogador(pontos, derrotas):
    rank_jogador = pontos - (derrotas * 10)
    return rank_jogador

if rank_jogador < 100:
    print("O jogador é Bronze")
elif rank_jogador >= 100 and rank_jogador < 300:
    print("O jogador é Prata")
elif rank_jogador >= 300 and rank_jogador < 600:
    print("O jogador é Ouro")
elif rank_jogador >= 600:
    print("O jogador é Diamante")
else:
    print("O jogador foi banido")