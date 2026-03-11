nome = input("Digite o nome do aluno")
nota1 = float(input("Digite a primeira nota"))
nota2 = float(input("Digite a segunda nota"))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"{nome} foi aprovado com média {media:.2f}")
elif media >= 5:
    print(f"{nome} está em recuperação com média {media:.2f}")
else:
    print(f"{nome} foi reprovado com média {media:.2f}")
    