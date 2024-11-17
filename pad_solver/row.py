class Row:

    def __init__(self, name, nodes:list, emoji):
        self.name = name
        self.nodes = nodes
        self.emoji = emoji
 
    def __eq__(self, other):
        if isinstance(other, Row):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return self.name+" "+str(self.nodes)

    def __repr__(self):
        return self.name
    