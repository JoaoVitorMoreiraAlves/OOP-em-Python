#Desenvolver um programa que utilize uma classe chamada Rentagulo que consiga mostrar a altura, base, área e perimetro de um Retangulo.

#Criando a Classe Retangulo
class Retangulo:
    #Método Construtor
    def __init__(self, base = 0, altura = 0):
        self.base = base
        self.altura = altura

    def setBase(self,base):
        if base > 0:
            self.base = base
        else:
            self.base = 1
            return print("Erro!! Valor digitado incorreto!! Portanto o valor atribuido será 1")

    def getBase(self):
        return self.base
    
    def setAltura(self,altura):
        if altura > 0:
            self.altura = altura
        else:
            self.altura = 1
            return print("Erro!! Valor digitado incorreto!!Portanto o valor atribuido será 1")

    def getAltura(self):
        return self.altura
    
    def getArea(self):
        return self.altura * self.base
    
    def getPerimetro(self):
        return 2 * (self.altura + self.base)

#Programa Principal
retang1 = Retangulo(4,5)
retang2 = Retangulo()
print("-="*30)
print("Primeiro Retangulo:")
print(f"Base: {retang1.getBase()}\nAltura: {retang1.getAltura()}\nArea: {retang1.getArea()}\nPerimetro: {retang1.getPerimetro()}")
print("-="*30)
print("Segundo Retangulo:")
retang2.setBase(int(input("Digite o Valor da Base: ")))
retang2.setAltura(int(input("Digite o Valor da Altura: ")))
print(f"Base: {retang2.getBase()}\nAltura: {retang2.getAltura()}\nArea: {retang2.getArea()}\nPerimetro: {retang2.getPerimetro()}")