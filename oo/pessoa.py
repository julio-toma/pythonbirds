class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    julio = Pessoa(nome ='Julio')
    alice = Pessoa(julio, nome ='Alice')
    print(Pessoa.cumprimentar(alice))
    print(id(alice))
    print(alice.cumprimentar())
    print(alice.nome)
    print(alice.idade)
    for filho in alice.filhos:
        print(filho.nome)