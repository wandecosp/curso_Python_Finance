class Ativo:
    def calcular(self):
        raise NotImplemented("Nao implementados")


class Opcao(Ativo):
    def calcular(self):
        return 1 + 1


class RF(Ativo):
    def calcular(self):
        return 4


def Precificar(ativo):
    print(ativo.calcular())


a = Ativo()
b = Opcao()
r = RF()

#Precificar(a)
#Precificar(b)
#Precificar(r)
