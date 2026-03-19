pontos = int(input("Digite a quantidade de pontos: "))
tempo = int(input("Digite o tempo de jogo: "))

def pontuacaototal(pontos, tempo):
    total = pontos
    if tempo < 30:
        total += 50
        print("Ganhou 50 pontos de bônus")
    elif tempo > 100:
        total -= 20
        print("Perdeu 20 pontos de bônus")
    if pontos < 200:
        print("Recorde")
    return total

total = pontuacaototal(pontos, tempo)
print(f"Pontuação total: {total}")