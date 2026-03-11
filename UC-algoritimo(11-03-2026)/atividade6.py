nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula do aluno: ")
# aceitar vírgula como separador decimal e garantir que nota1 seja float
while True:
    s = input("Digite a primeira nota: ")
    try:
        nota1 = float(s.replace(',', '.'))
        break
    except ValueError:
        print("Valor inválido. Use números, exemplo: 7.5 ou 7,5")     #professora nao sei fazer isso pedi pra ia fazer desculpa