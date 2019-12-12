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
    direcoes = ['Norte','Leste','Sul','Oeste']

    def __init__(self, valor = direcoes[0]):
        self.valor = valor

    def girar_direita(self):
        if



    pass
if __name__ == '__main__':
    o = Motor()
    print (o.velocidade)
    o.acelerar()
    print(o.velocidade)
    o.frear()
    print (o.velocidade)