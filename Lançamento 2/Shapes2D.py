import math

class Ponto():
	def __init__(self, n, x1, y1):
		self._numero = n
		self._x1 = x1
		self._y1 = y1
	def distancia_entre_pontos(self, x, y):
		return math.sqrt((self._x1 - x) * (self._x1 - x) + (self._y1 - y) * (self._y1 - y))

	def getNumber(self):
		return self._numero #Devolve o numero da forma no plano cartesiano, na ordem que foi adicionada

	def uptadeCoord(self, x, y): #atualiza as coordenadas
		self._x1 = x
		self._y1 = y

	def getType(self):#devolve a forma geometrica que é o objeto
		return "Point_"

	def printCoord(self):
		print(f'\nO {self.getType()}{self._numero} possui as coord: ({self._x1}, {self._y1}).')




class Linha(Ponto):

	def __init__(self, n, x1, y1, x2, y2):
		super().__init__(n, x1, y1)
		self._x2 = x2
		self._y2 = y2

	def uptadeCoord(self, x1, y1, x2, y2):
		super().uptadeCoord(x1, y1)
		self._x2 = x2
		self._y2 = y2

	def getType(self):
		return 'Linha_'

	def getNumber(self):
		return self._numero

	def printCoord(self):
		return print(f'A {self.getType()}{self._numero} começa no ponto ({self._x1}, {self._y1}) e termina no ponto ({self._x2}, {self._y2})')

	def tamanho(self):
		return print(f'O tamanho da {self.getType()}{self._numero} é {math.sqrt((self._x1 - self._x2) * (self._x1 - self._x2) + (self._y1 - self._y2) * (self._y1 - self._y2))}.')

class Circulo(Ponto):
	def __init__(self,n, x, y, raio):

		super().__init__(n, x, y) #super() indica que o círculo ta herdando os atributos da classe Ponto
		self._raio = raio


	def printCoord(self):
		print(f'\nO {self.getType()}{self._numero} possui as coord: ({self._x1}, {self._y1}) e seu raio é {self._raio}.')
	def area(self):
		return print(f'A area do {self.getType()}{self._numero} é {3.14 * (self._raio * self._raio)}.')

	def getType(self): #polimorfismo
		return "Circle_"

	def perimetro(self):
		return print(f'O perimetro, ou circunferencia, do {self.getType()}{self._numero} é {2 * 3.14 * self._raio}.')


	def uptadeCoord(self, x, y, raio):
		super().uptadeCoord(x, y)
		self._raio = raio

	def pointIn(self, pt):
		distancia = math.sqrt((self._x1 - pt._x1) * (self._x1 - pt._x1) + (self._y1 - pt._y1) * (self._y1 - pt._y1))
		return print(f"O ponto {pt.getNumber()} se encontra dentro do circulo") if distancia <= self._raio else print(f"O ponto {pt.getNumber()} nao esta dentro do circulo")


class Quadrado():
	def __init__(self, n, lado):
		self._lado = lado
		self._numero = n


	def area(self):
		return print(f'A area do {self.getType()}{self._numero} é {self._lado * self._lado}.')


	def perimetro(self):
		return print(f'O perimetro do {self.getType()}{self._numero} é {self._lado * 4}.')


	def diagonal(self):
		return print(f'A diagonal do {self.getType()}{self._numero} é {self._lado * 1.41}.')


	def getType(self):
		return "Quadrado_"

	def getNumber(self):
		return self._numero

	def uptadeSize(self, lado):
		self._lado = lado


class Triangulo_equilatero(Quadrado):
	def __init__(self, n, lado):
		super().__init__(n, lado)


	def area(self):
		area = ((self._lado*self._lado)*1.7)/4
		return print(f'A area do {self.getType()}{self._numero} é {area}.')


	def altura(self):
		return print(f'A altura do {self.getType()}{self._numero} é {(self._lado*1.7)/2}.')


	def getNumber(self):
		return self._numero


	def perimetro(self):
		return print(f'O perimetro do {self.getType()}{self._numero} é {self._lado*3}.')


	def getType(self):
		return 'Triangulo Equilatero_'



	def uptadeSize(self, lado):
		super().uptadeSize(lado)




class Retangulo(Quadrado):
	def __init__(self, n , lado, altura):
		super().__init__(n, lado)
		self._lado = lado
		self._altura = altura

	def area(self):
		return print(f'A area do {self.getType()}{self._numero} é {self._lado * self._altura}.')

	def perimetro(self):
		return print(f'O perimetro do {self.getType()}{self._numero} é {(2 * self._lado + 2 * self._altura)}.')

	def diagonal(self):
		return print(f'A diagonal do {self.getType()}{self._numero} é {math.sqrt((self._lado * self._lado) + (self._altura * self._altura))}.')

	def getType(self):
		return 'Retangulo_'

	def uptadeSize(self, lado, altura):
		super().uptadeSize(lado)
		self._altura = altura

	def getNumber(self):
		return self._numero