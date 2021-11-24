# Node to solve in the shortest path algorithm 
class Node():

    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.isEnd = False
        self.neighbours = set({})
        self.pos = (self.x,self.y)
        self.processed = False
        self.var = None 

    def n_neighbours(self):
        return len(self.children)
