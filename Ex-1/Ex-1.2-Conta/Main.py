#Crie um programa que utilize uma Classe chamada Conta, que mostra o saldo e faz saque e depósito.

class Conta:
    #Método construtor
    def __init__(self,saldo = 0):
        self.saldo = saldo
    
    def saldo(self):
        return self.saldo
    
    def saque(self,valor):
        if valor < 0 or valor > self.saldo:
            print("Erro!!! O valor digitado está errado! Portanto não será realizado o saque")
        else:
            self.saldo -= valor
            print(f"Saque de {valor}  foi realizado com Sucesso!")
    
    def deposito(self,valor):
        if valor < 0:
            print(f"Erro!! O saldo informado não é válido!! Portanto o depósito de {valor} não será realizado")
        else:
            print(f"Depósito de {valor} realizado com Sucesso")
            self.saldo += valor

#Programa Principal

caixa = Conta(1000)
print("="*30)
print(f"O saldo da conta é de {caixa.saldo}")
print("="*30)
caixa.saque(1500)
print("="*30)
caixa.saque(300)
print("="*30)
print(f"O saldo da conta é de {caixa.saldo}")
print("="*30)
caixa.deposito(-1)
print("="*30)
caixa.deposito(500)
print("="*30)
print(f"O saldo da conta é de {caixa.saldo}")