nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

print(f"A média das notas é: {media(nota1, nota2, nota3):.2f}")