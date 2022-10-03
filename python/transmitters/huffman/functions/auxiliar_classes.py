class node:
    def __init__(self, symbol, probability, code, children):
        self.symbol = symbol
        self.probability = probability
        self.code = code
        self.children = children