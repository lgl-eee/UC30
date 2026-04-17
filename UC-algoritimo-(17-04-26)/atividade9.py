notas = [2.1, 3.5, 7.9, 8.0, 9.5, 10.0, 4.3, 5.6, 6.7, 8.8]
acimadesete = []

for a in notas:
    if a >= 7.0:
        acimadesete.append(a)

print("numero de notas acima de 7.0:", len(acimadesete))