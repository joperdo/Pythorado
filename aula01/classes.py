class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno,comendo, falando, dormindo):
        self.nome= nomeAluno
        self.peso= pesoAluno
        self.idade= idadeAluno
        self.comendo=False
        self.falando = False
        self.dormindo = False

    def falar(self, palavra):
        if self.falando==True:
            print(f"{self.nome} está falando {palavra}")
        elif self.comendo==True:
            print(f"{self.nome} está comendo {alimento}")
        elif self.dormindo==True:
            print(f"{self.nome} está dormindo uma {sonequinha}")
        else:
            print(f"{self.nome} falou {palavra}")
            self.falando=False

    def pararFalar(self):
        if self.falando == False:
            print(f"{self.nome} não está hablando")
        else:
            print(f"{self.nome} se calou")
            self.falando = False

    def comer(self, alimento):
        if self.falando==True:
            print(f"{self.nome} está falando {palavra}")
        elif self.comendo==True:
            print(f"{self.nome} está comendo {alimento}")
        elif self.dormindo==True:
            print(f"{self.nome} está dormindo uma {sonequinha}")
        else:
            print(f"{self.nome} foi comer {alimento}")
            self.comendo=False
    def pararComer(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo")
        else:
            print(f"{self.nome} fechou a boca")
            self.comendo = False
    def dormir(self, sonequinha):
        if self.falando==True:
            print(f"{self.nome} está falando {palavra}")
        elif self.comendo==True:
            print(f"{self.nome} está comendo {alimento}")
        elif self.dormindo==True:
            print(f"{self.nome} está dormindo uma {sonequinha}")
        else:
            print(f"{self.nome} foi dormir uma {sonequinha}")
            self.dormindo=False

    def pararDormir(self):
        if self.dormindo == False:
            print(f"{self.nome} não está dormindo")
        else:
            print(f"{self.nome} levantou a cabeça")
            self.dormindo = False