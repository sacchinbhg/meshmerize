import pickle
import sys

def main():
    
    mappings = None
    try :
        mappings = pickle.load(open("Mappings.p", "rb"))
    except:
        print("Mapping file not found!")
        sys.exit(0)
    print("Number of mappings :", len(mappings))
    print("Enter comma separated coordinates to analyze child, and -1 to quit")
    while(True):
        inp = input()
        if inp=="-1":
            break
        else:
            x,y = list(map(int, inp.split(',')))
            node = mappings[(x,y)]
            print("The children nodes are : ")
            for i in node.neighbours:
                print(i.pos)
            print()
    
if __name__=="__main__":
    main()
