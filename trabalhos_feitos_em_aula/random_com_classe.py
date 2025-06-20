import random

class Item():
    def __init__(self):
        self.nome = self.gerar_nome_item()

    def gerar_nome_item(self):
        substantivos = [
            {'nome' : 'Pedra', 'gênero': 'F'},
            {'nome' : 'Cinturão', 'gênero': 'M'},
            {'nome' : 'Espada', 'gênero': 'F'},
            {'nome' : 'Arco', 'gênero': 'M'},
            {'nome' : 'Poção', 'gênero': 'F'},
        ]

        adjetivos = [
            {'F': 'Lascada', 'M': 'Lascado'},
            {'F': 'Épica', 'M': 'Épico'},
            {'F': 'Lendária', 'M': 'Lendário'},
            {'F': 'Resistente', 'M': 'Resistente'},
            {'F': 'Brilhante', 'M': 'Brilhante'},
        ]

        nome = random.choice(substantivos)

        adjetivo = random.choice(adjetivos)

        genero_subst = nome['gênero']

        return f'{nome['nome']} {adjetivo[genero_subst]}'

    def __str__(self):
        return self.nome
    
class Bau():
    def __init__(self):
        self.capacidade = self.capacidade_do_bau()   
        self.itens = self.sortear_itens_bau()         

    def capacidade_do_bau(self):
        tamanho_max_bau = [1,2,3,4,5,6,7,8,9,10]

        capacidade = random.choice(tamanho_max_bau)

        return capacidade    

    def sortear_itens_bau(self):
        
        itens = []
        
        capacidade_do_bau = self.capacidade

        while len(itens) < capacidade_do_bau:
            novo_item = Item().gerar_nome_item()
            itens.append(novo_item)

        return itens
    
    

bau1 = Bau()

print(len(bau1.itens))

print(bau1.itens)

print(bau1.capacidade)