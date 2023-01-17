#Modele e implemente uma classe que represente um Retângulo a partir de seus atributos: base e altura
#Ela deve ser capaz de instanciar objetos a partir de 2 parâmetros (base e altura)
#Caso base e altura não sejam informados, instancie um retângulo de base = 2 e altura = 1;
#Cada instância deve ser capaz de:
#Devolver os valores de: Área; Perímetro; Base; Altura;
#Informar se o objeto é um quadrado (boolean)
#Imprimir todas as informações sobre o objeto instanciado



#Classe
class Retangulo:
    def __init__(self,base = 2,altura = 1):
        self.__base = base
        self.__altura = altura
        self.__quadrado = False

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, base_nova):
        self.__base = base_nova
    
    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura_nova):
        self.__altura = altura_nova


    def pegar_area(self):
        return (self.__altura * self.__base)
    
    def pegar_perimetro(self):
        return 2*(self.__base + self.__altura)

    def quadrado(self):
        return True if self.__base == self.__altura else False


    def __str__(self):
        return f'''
        Dados do Retângulo:
            Base: {self.__base}
            Altura: {self.__altura}
            Area: {self.pegar_area()}
            Perimetro: {self.pegar_perimetro()}
            O Retângulo é quadrado? {self.quadrado()}'''

#Programa Principal

base = int(input('Digite a base do Retângulo: '))
altura = int(input('Digite a altura do Retângulo: '))
retangulo = Retangulo(base,altura)
print(retangulo)