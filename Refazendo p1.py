class Livro():
    def __init__(self, titulo, autor_principal, ano, editora, isbn):

        self.autor_principal = autor_principal
        self.titulo = titulo
        self.ano = ano
        self.editora = editora
        self.isbn = isbn 
        self.estado = 'disponivel' 
        self.quantidade_de_emprestimo = 0

    def emprestar(self):
        if self.estado == 'disponivel':
            self.estado = 'emprestado'
            self.quantidade_de_emprestimo += 1
            print('Livro disponivel para emprestimo!')
        else:
            print('O livro não está disponivel')

    def devolver(self):
        if self.estado == "emprestado":
            self.estado = "disponivel"
            print("Livro devolvido com sucesso!")
        else:
            print("O livro já está disponível.")

    def exibir(self):
        print('Titulo:',self.titulo)
        print('Autor: ',self.autor_principal)
        print('Ano: ',self.ano)
        print('Editora: ',self.editora)
        print('ISBN: ',self.isbn)
        print('Estado: ',self.estado)
        print('Quantidade de empréstimos: ',self.quantidade_de_emprestimo)


class Revista():
    def __init__(self, titulo, ano, editora, issn):
        self.titulo = titulo
        self.ano = ano
        self.editora = editora 
        self.issn = issn  
    
    def exibir(self):
        if 2024 - self.ano <= 5:
            print('Titulo: ',self.titulo)
            print('Ano: ',self.ano)
            print('Editora: ',self.editora)
            print('ISSN: ',self.issn)
        else:
            print('Desculpe...Não podemos exibir os dados da revista')
    
    
class Bibliotecario():
    def __init__(self, nome, matricula, telefone, email, tempo_de_servico):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
        self.tempo_de_servico = tempo_de_servico  
        
    def calcular_salario(self):
        salario_base = 2000
        aumento_por_ano = 0.10
        salario = salario_base + (salario_base * aumento_por_ano * self.tempo_de_servico)
        return salario
    
    def exibir(self):
        print('Nome: ',self.nome)
        print('Matricula: ',self.matricula)
        print('Telefone: ',self.telefone)
        print('Email: ',self.email)
        print('Tempo de serviço: ',self.tempo_de_servico)

class Assistente():
    def __init__(self, nome, matricula, telefone, email, tempo_de_servico):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
        self.tempo_de_servico = tempo_de_servico

    def exibir(self):
        print('Nome: ',self.nome)
        print('Matricula: ',self.matricula)
        print('Telefone: ',self.telefone)
        print('Email: ',self.email)
        print('Tempo de serviço: ',self.tempo_de_servico)


class Leitor():
    def __init__(self, nome, endereco, telefone, email, idade):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.idade = idade   

    def validar(self):
        if self.idade < 18:
            print('O leitor não pode fazer empréstimo de livros')
        else:
            print('Os empréstimo estão liberados!')

    def incrementar_idade(self):
        self.idade += 1

    def diminuir_idade(self):
        if self.idade > 0:
            self.idade -= 1

    def exibir(self):
        print('Nome: ',self.nome)
        print('Endereço: ',self.endereco)
        print('Telefone: ',self.telefone)
        print('Email: ',self.email)
        print('Idade: ',self.idade)

class Emprestimo:
    def __init__(self, livro, leitor):
        self.livro = livro
        self.leitor = leitor
    
    def realizar_emprestimo(self):
        self.livro.emprestar()

livro1 = Livro('O pecado que te seduz', 'Alice Barros', 2013, 'Alice barros', 3091)
revista1 = Revista('Big bang', 2015, 'MVP', 901)
bibliotecario1 = Bibliotecario('Jorge', 202313575, 24993311741, 'jorge@gmail.com', 2)
assistente1 = Assistente('Márcia', 202313587, 24992925319, 'marcia@gmail.com', 1)
leitor1 = Leitor('Lavinia', 'Rua 33, numero 33, casa, Bairro Nobre, Montinho Verde, RJ, 27700000', 24993311741, 'lavinia@gmail.com', 19)

livro1.exibir()
print()
print('----------------------')
bibliotecario1.exibir()
print('----------------------')
print()
assistente1.exibir()
print()
print('----------------------')
leitor1.exibir()
print()
print('----------------------')

emprestimo1 = Emprestimo(livro1, leitor1)
emprestimo1.realizar_emprestimo()
livro1.exibir()
assistente1.exibir()

