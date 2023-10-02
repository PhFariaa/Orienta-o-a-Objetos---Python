import math

class Ponto():
	def __init__(self, n, x, y):
		self._numero = n
		self._x = x
		self._y = y
	def distancia_entre_pontos(self, x, y):
		return math.sqrt((self._x - x) * (self._x - x) + (self._y - y) * (self._y - y))

	def getNumber(self):
		return self._numero #Devolve o numero da forma no plano cartesiano, na ordem que foi adicionada

	def uptadeCoord(self, x, y): #atualiza as coordenadas
		self._x = x
		self._y = y

	def getType(self):#devolve a forma geometrica que é o objeto
		return "Point_"

	def printCoord(self):
		print(f'\nO ponto {self._numero} possui as coord: ({self._x}, {self._y}).')

class Circulo(Ponto):
	def __init__(self,n, x, y, raio):

		super().__init__(n, x, y) #super() indica que o círculo ta herdando os atributos da classe Ponto
		self._raio = raio


	def printCoord(self):
		print(f'\nO circulo {self._numero} possui as coord: ({self._x}, {self._y}) e seu raio é {self._raio}.')
	def area(self):
		return print(f'A area do circulo {self._numero} é {3.14 * (self._raio * self._raio)}.')

	def getType(self): #polimorfismo
		return "Circle_"

	def perimetro(self):
		return print(f'O perimetro, ou circunferencia, do circulo {self._numero} é {2 * 3.14 * self._raio}.')


	def uptadeCoord(self, x, y, raio):
		super().uptadeCoord(x, y)
		self._raio = raio

	def pointIn(self, pt):
		distancia = math.sqrt((self._x - pt._x) * (self._x - pt._x) + (self._y - pt._y) * (self._y - pt._y))
		return print(f"O ponto {pt.getNumber()} se encontra dentro do circulo") if distancia <= self._raio else print(f"O ponto {pt.getNumber()} nao esta dentro do circulo")


class Quadrado():
	def __init__(self, n, lado):
		self._lado = lado
		self._numero = n


	def area(self):
		return print(f'A area do quadrado {self._numero} é {self._lado * self._lado}.')


	def perimetro(self):
		return print(f'O perimetro do quadrado {self._numero} é {self._lado * 4}.')


	def diagonal(self):
		return print(f'A diagonal do quadrado {self._numero} é {self._lado * 1.41}.')


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
		return print(f'A area do triangulo equilatero {self._numero} é {area}.')


	def altura(self):
		return print(f'A altura do triangulo equilatero {self._numero} é {(self._lado*1.7)/2}.')


	def getNumber(self):
		return self._numero


	def perimetro(self):
		return print(f'O perimetro do triangulo equilatero {self._numero} é {self._lado*3}.')


	def getType(self):
		return 'Triangulo_'



	def uptadeSize(self, lado):
		super().uptadeSize(lado)




class Retangulo(Quadrado):
	def __init__(self, n , lado, altura):
		super().__init__(n, lado)
		self._lado = lado
		self._altura = altura

	def area(self):
		return print(f'A area do retangulo {self._numero} é {self._lado * self._altura}.')

	def perimetro(self):
		return print(f'O perimetro do retangulo {self._numero} é {(2 * self._lado + 2 * self._altura)}.')

	def diagonal(self):
		return print(f'A diagonal do quadrado {self._numero} é {math.sqrt((self._lado * self._lado) + (self._altura * self._altura))}.')

	def getType(self):
		return 'Retangulo_'

	def uptadeSize(self, lado, altura):
		super().uptadeSize(lado)
		self._altura = altura

	def getNumber(self):
		return self._numero