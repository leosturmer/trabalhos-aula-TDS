class Livro():
    def __init__(self, titulo, n_paginas):
        self.titulo = titulo
        self.n_paginas = n_paginas
        self.n_pg_atual = 0 

    def marcar_pagina (self, n_pg_atual):
        self.n_pg_atual = n_pg_atual
        
    def quant_pg_para_terminar(self):
        qt_pgs = self.n_paginas - self.n_pg_atual
    
        return qt_pgs # Quant. de páginas para terminar o livro






umLivro = Livro("um título", 300)
outroLivro = Livro("outro título", 50)



umLivro.marcar_pagina(20)

print(umLivro.quant_pg_para_terminar())


