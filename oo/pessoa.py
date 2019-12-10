class Pessoa:
    def __init__(self, *filhos, nome = None, idade = None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    luis = Pessoa('Luis')
    antonio = Pessoa(luis, nome = 'Antonio')
    print(Pessoa.cumprimentar(luis))
    print (id(luis))
    print(luis.cumprimentar())
    print(antonio.filhos)
