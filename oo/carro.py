class Motor:

    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade +=1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)
    pass

class Direcao:

    def __init__(self, valor = 'Norte'):
            self.valor = valor

    def girar_direita(self):
        direcoes = ['Norte','Leste','Sul','Oeste']
        i = direcoes.index(self.valor)
        self.valor = direcoes[(i+1)%4]

    def girar_esquerda(self):
        direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']
        i = direcoes.index(self.valor)
        self.valor = direcoes[(i-1)%4]


class Carro:

    def __init__(self, motor = None, direcao = None):
        self.motor = motor
        self.direcao = direcao

    def calc_vel(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calc_dir(self):
        return self.direcao.valor

    def virar_direita(self):
        self.direcao.girar_direita()

    def virar_esquerda(self):
        self.direcao.girar_esquerda()

    pass
