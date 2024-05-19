class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo=False, falando=False, dormindo=False):
        self.nome= nomeAluno
        self.peso= pesoAluno
        self.idade= idadeAluno
        self.comendo= comendo
        self.falando = falando
        self.dormindo = dormindo

    def falar(self, palavra):
        if self.falando== False and self.comendo== False and self.dormindo== False:
            self.falando = True
            print(f"{self.nome} está hablando {palavra}")
        elif self.falando==True:
            print(f"{self.nome} já está hablando")
        elif self.comendo==True:
            print(f"{self.nome} está comendo")
        elif self.dormindo==True:
            print(f"{self.nome} está dormindo")
        else:
            print(f"{self.nome} hablou {palavra}")
            self.falando=False

    def pararFalar(self):
        if self.falando == True:
            self.falando = False
            print(f"{self.nome} não está hablando")
        elif self.comendo==True:
            print(f"{self.nome} não pode parar de falar, pois está comendo")
        elif self.dormindo == True:
            print(f"{self.nome} não pode parar de falar, pois está dormindo")
        elif self.falando == False:
            print(f"{self.nome} se calou")

    def comer(self, alimento):
        if self.comendo== False and self.falando== False and self.dormindo== False:
            self.comendo = True
            print(f"{self.nome} está comendo {alimento}")
        elif self.comendo==True:
            print(f"{self.nome} já está comendo")
        elif self.falando==True:
            print(f"{self.nome} está falando")
        elif self.dormindo==True:
            print(f"{self.nome} está dormindo")
        else:
            print(f"{self.nome} foi comer {alimento}")
            self.comendo=False
    def pararComer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} não está comendo")
        elif self.falando==True:
            print(f"{self.nome} não pode parar de comer, pois está falando")
        elif self.dormindo == True:
            print(f"{self.nome} não pode parar de comer, pois está dormindo")
        elif self.comendo == False:
            print(f"{self.nome} fechou a boca")


    def dormir(self, sonequinha):
        if self.dormindo== False and self.comendo== False and self.falando== False:
            self.dormindo = True
            print(f"{self.nome} está dormindo {sonequinha}")
        elif self.dormindo==True:
            print(f"{self.nome} já está dormindo")
        elif self.falando==True:
            print(f"{self.nome} está falando")
        elif self.comendo==True:
            print(f"{self.nome} está comendo")
        else:
            print(f"{self.nome} foi dormir {sonequinha}")
            self.dormindo=False

    def pararDormir(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f"{self.nome} não está dormindo")
        elif self.falando==True:
            print(f"{self.nome} não pode parar de dormir, pois está falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode parar de dormir, pois está comendo")
        elif self.dormindo == False:
            print(f"{self.nome} levantou a cabeça")