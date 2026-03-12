#sem função
print ("python é facil")
print ("python é facil")
print ("python é facil")

#com função
def exibirmensagem():
    print("olá mundo")

exibirmensagem()

#função com parâmetro 
def saudar(nome):
    print(f"Olá, {nome}")

saudar("ana")
saudar("bruno")

def exibirmensagem(nome, mensagem):
    print(f"{mensagem}, {nome}")

exibirmensagem("ana", "bom dia")

#parametros nomeados
exibirmensagem(nome = "bruno", mensagem = "boa tarde")


#função que retorna a media
def calcularmedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
resultado = calcularmedia(8.0, 9.0)
print(f"Média: {resultado}")

