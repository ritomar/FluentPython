from math import hypot


class Vector:
    """Classe que representa um vetor bidimensional com métodos especiais"""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """Representação textual do vetor"""
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        """Calcula a magnitude

        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0

        """
        return hypot(self.x, self.y)

    def __bool__(self):
        """Implementação de bool que retorna False se a magnitude for zero

        >>> v = Vector(2, 4)
        >>> bool(v)
        True

        >>> bool(Vector())
        False
        """
        return bool(abs(self))

    def __add__(self, other):
        """Implementa o operador +

        >>> v1 = Vector(2, 4)
        >>> v2 = Vector(2, 1)
        >>> v1 + v2
        Vector(4, 5)

        """

        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """Implementa o operdor *

        >>> v = Vector(3, 4)
        >>> v * 3
        Vector(9, 12)
        >>> abs(v * 3)
        15.0

        """
        return Vector(self.x * scalar, self.y * scalar)
