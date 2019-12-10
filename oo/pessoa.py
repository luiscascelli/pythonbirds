class Pessoa:
    olhos = 2 #atributo default

    def __init__(self, *filhos, nome = None, idade = None): #atributos unicos, atributos de instancia
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self): #metodo
        return f'Olá {id(self)}'


if __name__ == '__main__':
    luis = Pessoa('Luis')
    antonio = Pessoa(luis, nome = 'Antonio')
    print(Pessoa.cumprimentar(luis))
    print (id(luis))
    print(luis.cumprimentar())
    print(antonio.filhos)
