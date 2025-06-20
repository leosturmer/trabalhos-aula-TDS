### Model

dicionario = {
    "Apple": "Maçã",
    "House": "Casa",
    "Water": "Água",
    "Friend": "Amigo",
    "Happy": "Feliz",
    "Light": "Luz",
    "Table": "Mesa",
    "Chair": "Cadeira",
    "Bread": "Pão",
    "Music": "Música"
}

### View 

palavra_a_traduzir = input("Digite a palavra para traduzir: ")

if palavra_a_traduzir in dicionario:
    print(f'Palavra: {palavra_a_traduzir}. Tradução: {dicionario[palavra_a_traduzir]}')
else:
    print(f'A palavra {palavra_a_traduzir} não está neste dicionário.')


