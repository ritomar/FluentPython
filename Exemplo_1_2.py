from math import hypot


# Classe que representa um vetor bidimensional com métodos especiais
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Representação do objeto em string
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # Calcula a magnitude
    def __abs__(self):
        return hypot(self.x, self.y)

    # Implementação de bool que retorna False se a magnitude for zero
    def __bool__(self):
        return bool(abs(self))

    # Implemta o operador +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # Implementa o operaador *
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
