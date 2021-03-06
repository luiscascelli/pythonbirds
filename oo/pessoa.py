class Pessoa:
    olhos = 2 #atributo default

    def __init__(self, *filhos, nome = None, idade = None): #atributos unicos, atributos de instancia
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self): #metodo
        return f'Olá {self.nome}'

    @staticmethod #@ = decorator
    def metodo_estatico(): #funcao de classe, funcao atrelada à classe Pessoa
        return 42
    @classmethod #acessar dados da propria classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Mutante(Pessoa): #Pessoa classe pai. Homem herda os atributos de Pessoa (metodos, atributos, etc)
    olhos = 3

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mao'

if __name__ == '__main__':
    luis = Mutante(nome = 'Luis')
    antonio = Homem(luis, nome = 'Antonio')
    print(Pessoa.cumprimentar(luis))
    print (id(luis))
    print(luis.cumprimentar())
    print(antonio.filhos)
    print (Pessoa.metodo_estatico(),luis.metodo_estatico())
    print (Pessoa.nome_e_atributos_de_classe(), luis.nome_e_atributos_de_classe())
    print (luis.olhos)
    print (antonio.olhos)
    print(luis.cumprimentar())
    print(antonio.cumprimentar())