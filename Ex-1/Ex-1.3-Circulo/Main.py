#Elabore uma classe Circunferencia capaz de retornar o valor do diâmetro, a área e o perimetro.
# Area = pi * (raio * raio)
# Perimetro = 2 * pi * raio
# Diametro = 2 * raio

class Circunferencia:
    #Método Construtor
    def __init__(self,raio = 0):
        self.raio = raio
    
    def setRaio(self,raio):
        if raio > 0:
            self.raio = raio
        else:
            print(f"O valor {raio} está incorreto portanto não será possível realizar essa alteração")
        
    def getRaio(self):
        return self.raio
    
    def getArea(self):
        return 3.14 * pow(self.raio,2)
    
    def getPerimetro(self):
        return 2 * 3.14 * self.raio
    
    def getDiametro(self):
        return 2 * self.raio

#Programa Principal
circulo = Circunferencia(int(input("Digite o valor do Raio: ")))
print("="*30)
print(f"A Área é de {circulo.getArea():.2f}")
print("="*30)
print(f"O Perimetro é de {circulo.getPerimetro():.2f}")
print("="*30)
print(f"O Diametro é de {circulo.getDiametro():.2f}")