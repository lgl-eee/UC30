idade = int(input("Digite a idade do atleta: "))

if idade < 12 :
    print("Atleta infantil")
elif 12 <= idade < 18 :
    print("Atleta juvenil")
elif 18 <= idade < 60 :
    print("Atleta adulto")
elif idade >= 60 :
    print("Atleta sênior")