#!/usr/bin/env python
import API
import sys
import time
import pickle
from Node import Node
from BFS import Grapher

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

mappings = {}
current_direction = 0
x = 0
y = 0
steps = 0

direction_to_move = {
        (0,-1)  : 2,
        (0,1)   : 0,
        (1,0)   : 1,
        (-1,0)  : 3
        }

direction_to_move_inverse = {
        2 : (0,-1),
        0 : (0,1),
        1 : (1,0),
        3 : (-1,0)
        }

# CONNECT 2 NODES
def connect(node1, node2):
    node1.neighbours.add(node2)
    node2.neighbours.add(node1)


# MOVE API FROM SOURCE POSITION TO DESTINATION POSITION
def apiMove(source, destination):
    if source.pos == destination.pos :
        return
    global current_direction,steps
    steps += 1
    dx = destination.x - source.x
    dy = destination.y - source.y
    future_direction = direction_to_move[(dx,dy)]

    diff = future_direction-current_direction
    if(diff==1 or diff==-3):
        API.turnRight()
    if(diff==2 or diff==-2):
        API.turnLeft()
        API.turnLeft()
    if(diff==3 or diff==-1):
        API.turnLeft()
    API.moveForward()
    current_direction = future_direction


# USE CURRENT DIRECTION AND LOCAL ADVANCEMENT DIRECTION TO GET FUTURE POSITION
def directionMapper(direction_character):
    global current_direction
    d_num = 0
    if(direction_character=='L'):
        d_num = -1
    elif(direction_character=='R'):
        d_num = 1
    elif(direction_character=='D'):
        d_num = 2
    global_direction = (current_direction+d_num+4)%4
    changes = direction_to_move_inverse[global_direction]
    return (x+changes[0], y+changes[1])


# SCAN THE NEIGHBOURS OF A NODE
def scan(node):
    # order = [3,2,1]
    # order = [1,2,3]
    # order = [2,1,3]
    order = [2,3,1]

    for i in order:
        if i==1:
            if not API.wallLeft():
                predicted_pos = directionMapper('L')
                node2 = None
                try : 
                    node2  = mappings[predicted_pos]
                except:
                    mappings[predicted_pos] = Node(*predicted_pos)
                    node2  = mappings[predicted_pos]
                connect(node, node2)
        if i==2:
            if not API.wallFront():
                predicted_pos = directionMapper('U')
                node2 = None
                try : 
                    node2  = mappings[predicted_pos]
                except:
                    mappings[predicted_pos] = Node(*predicted_pos)
                    node2  = mappings[predicted_pos]
                connect(node, node2)
        if i==3:
            if not API.wallRight():
                predicted_pos = directionMapper('R')
                node2 = None
                try : 
                    node2  = mappings[predicted_pos]
                except:
                    mappings[predicted_pos] = Node(*predicted_pos)
                    node2  = mappings[predicted_pos]
                connect(node, node2)

# MAIN FLOODFILL
def floodfill(node,var):
    global x,y
    scan(node)
    node.processed = True
    # API.setColor(*node.pos, "r")
    API.setText(*node.pos, str(node.pos[0])+","+str(node.pos[1]))
    for i in node.neighbours :
        if not i.processed:
            i.var = var+1
            apiMove(node, i)
            x,y = i.x, i.y
            floodfill(i,var+1)
            apiMove(i, node)
            x,y = node.x, node.y
        else:
            if i.var==var-3:
                i.isEnd = True

def main():
    global mappings
    head = Node(0,0)
    head.var = 0
    floodfill(head,0)
    
    # SAMPLE END
    # mappings[(8,8)].isEnd = True
    
    # LOGGING STEPS
    log("Steps : "+str(steps))

    # REAL ENDING SEARCHING

    # FOR SAVING PURPOSES AND INDEPENDENT ANALYSIS
    pickle.dump(head, open( "HeadNode.p", "wb"))
    pickle.dump(mappings, open( "Mappings.p", "wb"))

    # PATH FINDING
    g = Grapher(head)
    path = g.ShortestPath()

    # FRESH RUN
    if path:
        log("Path Found")
        log("Length : "+str(len(path)))
        curr = head
        API.setText(*curr.pos,'0')
        for ind,i in enumerate(path):
            API.setText(*curr.pos,str(ind))
            API.setColor(*curr.pos, 'b')
            apiMove(curr, i)
            curr = i
        log("Reached")

    else :
        log("No path found :(")
    
if __name__ == "__main__":
    main()
