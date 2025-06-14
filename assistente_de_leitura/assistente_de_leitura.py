

class Estante():

    def __init__(self):
        self.meus_livros = list()
        self.leituras = dict()
        
    def adicionar_na_estante(self, livro):
        if livro not in self.meus_livros:
            self.meus_livros.append(livro)
        else:
            print(f"{livro.titulo}: título já cadastrado")
    
    def iniciar_leitura(self, livro):
        self.leituras[livro.titulo] = Leitura(livro)

    def get_leitura(self, titulo_do_livro):
            return self.leituras[titulo_do_livro]
    
    def mostrar_livros_estante(self):
        for livro in self.meus_livros:
            print(f"""
Título: {livro.titulo}
Quantidade de páginas: {livro.quantidade_de_paginas}
                """)
            
#  Status da leitura: {livro.status_de_leitura}

    def mostrar_progresso_leituras(self):
        for titulo, leitura in self.leituras.items():
            print(f"""Título: {titulo}
                Quantidade de páginas: {leitura.livro.quantidade_de_paginas}
                Páginas restantes: {leitura.paginas_restantes}""")




class Livro():

    def __init__(self, titulo, quantidade_de_paginas):
       self.titulo = titulo       
       self.quantidade_de_paginas = quantidade_de_paginas
           
    def __eq__(self, value):        
        return self.titulo == value.titulo
        

        
class Leitura():
    def __init__(self, livro, pagina_atual = 0):
        self.livro = livro
        self.pagina_atual = pagina_atual
        self.paginas_restantes = 0
        self.percentual_de_leitura = 0
        self.status_de_leitura = ''

    def atualizar_leitura(self, pagina_atual):
        self.pagina_atual = pagina_atual

    def calculo_percentual(self):
        self.percentual_de_leitura = (self.pagina_atual / self.livro.quantidade_de_paginas) * 100
        return self.percentual_de_leitura

    def quantidade_paginas_restantes(self):
        self.paginas_restantes = self.livro.quantidade_de_paginas - self.pagina_atual
        return self.paginas_restantes

    def verificacao_de_leitura(self):
        self.status_de_leitura = int(self.percentual_de_leitura)

        if self.percentual_de_leitura == 0:
            self.status_de_leitura = 'Não lido'
        elif self.percentual_de_leitura < 100:
            self.status_de_leitura = 'Lendo'
        elif self.percentual_de_leitura == 100:
            self.status_de_leitura = 'Concluído'        
        return self.status_de_leitura


    ### View 

    def imprimir_progresso(self):
        print(f"""
Livro: {self.livro.titulo}
{int(self.percentual_de_leitura)}% lido
Páginas lidas: {self.pagina_atual} 
Total de páginas: {self.livro.quantidade_de_paginas}
Status da leitura: {self.status_de_leitura}
""")        

    

#####################################################################


# Criando a estante

minha_estante = Estante()

# Criando livros

joaoemaria = Livro('João e Maria', 50)
mobydick = Livro('Moby dick', 500)
tieta = Livro('Tieta', 200)
tieta2 = Livro('Tieta', 200)

# Adicionando livros na estante

minha_estante.adicionar_na_estante(joaoemaria)
minha_estante.adicionar_na_estante(mobydick)
minha_estante.adicionar_na_estante(tieta)
minha_estante.adicionar_na_estante(tieta2)




minha_estante.iniciar_leitura(joaoemaria)
minha_estante.iniciar_leitura(mobydick)
minha_estante.iniciar_leitura(tieta)



minha_estante.get_leitura("João e Maria").atualizar_leitura(50)
minha_estante.get_leitura("Moby dick").atualizar_leitura(450)
minha_estante.get_leitura("Tieta").atualizar_leitura(0)


minha_estante.mostrar_progresso_leituras()