texto = input("Digite um texto: ")
vogais = "aeiouAEIOU"
contador_vogais = 0

for letra in texto:
    if letra in vogais:
        contador_vogais += 1

print("Número de vogais:", contador_vogais)

