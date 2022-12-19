#Crie uma programa para utilizar de uma classe chamada Data, onde nela será poissível ver e modificar o dia,mes e ano, além da classe dizer se a data informada é ou não bissexto.

class Data:
    def __init__(self,dia = 1,mes = 1,ano = 1):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.bissext = False
        self.aux = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    def setDia(self,dia):
        while True:
            if dia < 0 or dia > self.aux[self.mes]:
                print("Valor errado, por favor me informe um valor válido")
                dia = int(input("Digite o dia: "))
            else:
                self.dia = dia
                break

    def getDia(self):
        return self.dia
    
    def setMes(self,mes):
        while True:
            if mes < 1 or mes > 12:
                print("Valor do Mês errado!! Por favor informe um mês válido!!")
                mes = int(input("Digite um mês entre 1 e 12: "))
            elif self.bissext:
                self.aux[2] = 29
                self.mes = mes
                break
            else:
                self.mes = mes
                break
    
    def getMes(self):
        return self.mes

    def setAno(self,ano):
        while True:
            if ano < 0:
                print("Valor do ano informado errado!! Por favor informe um ano válido!!!")
                ano = int(input("Digite o ano maior que 0: "))
            else:
                self.ano = ano
                data.bissexto(ano)
                break
    
    def getAno(self):
        return self.ano

    def bissexto(self,ano):
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            self.bissext = True
        else:
            self.bissext = False
    
    def imprime(self):
        print(f"O dia é {self.dia}")
        print(f"O mês é {self.mes}")
        print(f"O ano é {self.ano} e é ",end="")
        if data.bissext:
            print("um ano Bissexto")
            exit()
        else:
            print("um ano NÃO Bissexto")
            exit()

#Programa Principal
data = Data()
data.setAno(int(input("Digite o Ano: ")))
data.setMes(int(input("Digite o Mês: ")))
data.setDia(int(input("Digite o Dia: ")))
print(data.imprime())