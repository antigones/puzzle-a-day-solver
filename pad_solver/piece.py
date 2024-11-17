

class Piece:

    def __init__(self, name, points, emoji):
        self.name = name
        self.points = points
        self.emoji = emoji
 
    def __eq__(self, other):
        if isinstance(other, Piece):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
  