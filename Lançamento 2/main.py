import Shapes2D
import CoordSystem


plano_cartesiano  = CoordSystem.CartesianBoard()

ponto1 = Shapes2D.Ponto(1, 12, 25)
plano_cartesiano.inserShape(ponto1)
ponto1.printCoord()

ponto2 = Shapes2D.Ponto(2, 7, 13)
plano_cartesiano.inserShape(ponto2)
ponto2.printCoord()

print('\n')

circulo3 = Shapes2D.Circulo(3, 8, 13, 5)
plano_cartesiano.inserShape(circulo3)
circulo3.printCoord()
print(circulo3.getType())
circulo3.area()
circulo3.perimetro()
circulo3.pointIn(ponto1)
circulo3.pointIn(ponto2)

print('\n')


quadrado4 = Shapes2D.Quadrado(4, 5)
plano_cartesiano.inserShape(quadrado4)
quadrado4.area()
quadrado4.perimetro()
quadrado4.diagonal()
print(quadrado4.getType())
quadrado4.uptadeSize(6)
quadrado4.area()

print('\n')

triangulo5 = Shapes2D.Triangulo_equilatero(5, 5)
plano_cartesiano.inserShape(triangulo5)
triangulo5.area()
triangulo5.altura()
print(triangulo5.getType())
triangulo5.perimetro()
triangulo5.uptadeSize(6)
triangulo5.area()

print('\n')

retangulo6 = Shapes2D.Retangulo(6, 5, 4)
plano_cartesiano.inserShape(retangulo6)
retangulo6.area()
retangulo6.perimetro()
retangulo6.diagonal()
print(retangulo6.getType())
retangulo6.uptadeSize(3, 4)
retangulo6.area()


plano_cartesiano.showShapes()

print('\n')

plano_cartesiano.printDetails()


plano_cartesiano.removeShape(ponto1)

plano_cartesiano.showShapes()



Linha3 = Shapes2D.Linha(3, 4, 5, 9, 10)
plano_cartesiano.inserShape(Linha3)
Linha3.tamanho()
Linha3.printCoord()
Linha3.uptadeCoord(6, 7, 12, 15)
Linha3.tamanho()
Linha3.printCoord()

ponto1.printCoord()