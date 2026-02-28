import random

G = {} 
LIST = []
TP_LIST = []

for _ in range(300):
    while G:
        for node in list(G.keys()):  # list(G.keys()) is [1,2,3,4,5,6]
            if G[node]:
                continue
            
            else:
                S.append(node)
                del G[node] # remove a dic element based on key
                
                random.shuffle(S) # provides to find diffrent solution ways

        while S:
            for v in list(S):
                S.remove(v)
                LIST.append(v)
                for node in G:
                    if v in G[node]:
                        G[node].remove(v)
    
    if (LIST not in TP_LIST) and (LIST):
        TP_LIST.append(LIST) 
                      
    G = {1:[], 2:[], 3:[1,2], 4:[1], 5:[3,4], 6:[4,5]}          #G = {1:[],2:[1],3:[1],4:[1,2,3],5:[2],6:[5,4]}                             #G = {1:[3,5],2:[1],3:[2,5],4:[2,5],5:[]}    G = {1:[], 2:[], 3:[1,2], 4:[1], 5:[3,4], 6:[4,5]} 
    LIST = []
    S = []

i = 1
for path in TP_LIST:
    path = "-".join(str(x) for x in path) # convert list to str format: a-b-c....
    print(f"{i}) {path}")
    i += 1

            