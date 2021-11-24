import pickle

class Grapher():

    def __init__(self, h):
        self.root = h

    def ShortestPath(self):
        head = self.root
        visited = [] 
        queue = [[head]] 	
        while queue: 
            path = queue.pop(0)
            node = path[-1]
            if node not in visited: 
                neighbours = node.neighbours
                for neighbour in neighbours: 
                    new_path = list(path) 
                    new_path.append(neighbour) 
                    queue.append(new_path)
                    if neighbour.isEnd:
                        return new_path
                    visited.append(node)
        return None

if __name__ == "__main__":
    head = pickle.load(open("HeadNode.p", "rb"))
    g = Grapher(head)
    path = g.ShortestPath()
    if path :
        print("Length : ", len(path))
        for i in path :
            print(i.pos, end = " , ")
    else:
        print("No path")
