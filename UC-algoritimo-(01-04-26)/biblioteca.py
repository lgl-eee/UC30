# Dicionario para armazenar livros
catalogo = {}

# Dicionário para armazenar emprestimos	
emprestimoAtivo = {}

#lista para armazenar o histórico de transição
historico = []

def adicionar_livro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com este código {codigo} já existe.")
        return False
    
    catalogo[codigo] = {
        'titulo': titulo,
        'autor': autor,
        'quantidade': quantidade
    }
    
    print(f"Livro '{titulo}' adicionado com sucesso.")
    return True

def 