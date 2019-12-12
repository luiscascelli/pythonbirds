class Motor():

    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade +=1

    def frear(self):
        if self.velocidade <= 1:
            self.velocidade = 0
        else:
            self.velocidade -= 1
    pass

class Direcao():

    def __init__(self, valor = 'Norte'):
            self.valor = valor

    def girar_direita(self):
        direcoes = ['Norte','Leste','Sul','Oeste']
        i = direcoes.index(self.valor)
        if self.valor == direcoes[3]:
            self.valor = direcoes[0]
        else:
            self.valor = direcoes[i + 1]

    def girar_esquerda(self):
        direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']
        i = direcoes.index(self.valor)
        if self.valor == direcoes[0]:
            self.valor = direcoes[3]
        else:
            self.valor = direcoes[i-1]


    pass
if __name__ == '__main__':
    o = Direcao()
    print (o.valor)
    o.girar_direita()
    print(o.valor)
    o.girar_direita()
    print(o.valor)
    o.girar_direita()
    print(o.valor)
    o.girar_direita()
    print(o.valor)
    o.girar_esquerda()
    print(o.valor)
    o.girar_esquerda()
    print(o.valor)
    o.girar_esquerda()
    print(o.valor)
    o.girar_esquerda()
    print(o.valor)
    o.girar_esquerda()
    print(o.valor)