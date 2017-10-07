import collections

# Cria uma classe simples que representa cartas individuais
# namedtuple cria classes que com atributos mas sem métodos

Card = collections.namedtuple('Card', ['rank', 'suit'])


# Classe que, embora concisa, representa o baralho completo
class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()


    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]


    def __len__(self):
        return len(self._cards)


    def __getitem__(self, position):
        return self._cards[position]

