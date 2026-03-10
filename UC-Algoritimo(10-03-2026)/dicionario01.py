#sem dicionario 
matricula = 2026001
nome1 = "ana silva"
telefone = "9999-8888"

#com dicionario 
aluno = {
    "matricula": 2026001,
    "nome": "ana silva",
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camilaqueiroz": "Camila queiroz",
    "@brunamarquezine": "Bruna M.",
    "@sheronmenezes":  "Sheron M.",
    "@paolaoliveira": "Paola O.",
    "@joao": "joao o." 
}

print(contato)
print(type(contato))

#Acesso direto
print(contato["@camilaqueiroz"])

#acesso seguro com get()
print(contato.get("@paolaoliveira"))
print(contato.get("@inesistente"))
print(contato.get("@inesistente", "Nao encontrado"))

#add novo elemento
contato["@giovanna"] = "giovannia"
print("Após add: ", contato)

#atualiza elemento existe
contato["@paolaoliveira"] = "Paola Oliveira"

contato.update({
    "@brunamarquezine" : "Bruna marquezine",
    "@camilaqueiroz" : "Camila Q."
})

print("Após atualização: ", contato)



#pop remove e retorna
removido = contato.pop("@paolaoliveira")
print(f"removido: {removido}")
print("apos o pop: ", contato)

#del remove sem retornar
del contato["@camilaqueiroz"]
print("apos o del: ", contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("após clear: ", contato)
print("cópia:", copia)

print("numero de contatos: ", len(contato)) #tamanho dicio

#verificar existencia
if "@joao" in contato:
    print(f"encontrado {contato['@joao']}")

if "@inexistente" in contato:
    print("existe")
else:
    print("não existe")