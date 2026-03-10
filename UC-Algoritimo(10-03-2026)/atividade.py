paciente = {}

paciente["nome"] = input("qual o seu nome? ")
paciente["idade"] = int(input("quantos anos voce tem? "))
paciente["peso"] = float(input("qual o seu peso? "))    
paciente["altura"] = float(input("qual a sua altura? ")) 

imc = paciente["peso"] / (paciente["altura"] ** 2) 

paciente["imc"] = imc

print("\n Dados")
print("nome: ", paciente["nome"])
print("idade: ", paciente["idade"])
print("peso: ", paciente["peso"])
print("altura: ", paciente["altura"])
print("IMC: ", round(paciente["imc"], 2))