distancia = float(input("Digite a distância em kilometros: "))
kmporlitro = float(input("Digite o consumo do carro em km/litro: "))
gasolina = 5.5
litros = distancia / kmporlitro
custo = litros * gasolina

print(f"Para percorrer {distancia} km, o carro consumirá {litros:.2f} litros de combustível.")
print(f"O custo da viagem será de R$ {custo:.2f}.")