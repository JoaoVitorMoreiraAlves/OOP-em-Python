#Crie uma programa para utilizar de uma classe chamada Data, onde nela será poissível ver e modificar o dia,mes e ano, além da classe dizer se a data informada é ou não bissexto.

class Data:
    def __init__(self,dia = 1,mes = 1,ano = 1):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.bissext = False
        self.aux = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    def mudar_dia(self,dia):
        while True:
            if dia < 0 or dia > self.aux[self.mes]:
                print("Valor errado, por favor me informe um valor válido")
                dia = int(input("Digite o dia: "))
            else:
                self.dia = dia
                break

    def pegar_dia(self):
        return self.dia
    
    def mudar_mes(self,mes):
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
    
    def pegar_mes(self):
        return self.mes

    def mudar_ano(self,ano):
        while True:
            if ano < 0:
                print("Valor do ano informado errado!! Por favor informe um ano válido!!!")
                ano = int(input("Digite o ano maior que 0: "))
            else:
                self.ano = ano
                data.bissexto(ano)
                break
    
    def pegar_ano(self):
        return self.ano

    def bissexto(self,ano):
        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            self.bissext = True
        else:
            self.bissext = False
    
    def __str__(self):
        detalhe = 'um ano Bissexto' if data.bissext else 'um ano NÃO Bissexto'
        return print(f"O dia é {self.dia}\nO mês é {self.mes}\nO ano é {self.ano} e é {detalhe}")

#Programa Principal
data = Data()
data.mudar_ano(int(input("Digite o Ano: ")))
data.mudar_mes(int(input("Digite o Mês: ")))
data.mudar_dia(int(input("Digite o Dia: ")))
print(data)