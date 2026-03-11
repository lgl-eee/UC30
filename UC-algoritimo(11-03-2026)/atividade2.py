base = float(input("insira o valor base: "))
bonus = float(input("insira o valor do bonus: "))
desconto = float(input("insira o valor do desconto: "))

salario_bruto = base + bonus
salario_liquido = salario_bruto - desconto

print(f"Salário líquido: {salario_liquido:.2f}")
print(f"Salário bruto: {salario_bruto:.2f}")