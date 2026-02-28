G = {
    'n1' : {'n7' : 2, 'n2' : 9},
    'n2' : {'n3' : 6, 'n6' : 3},
    'n3' : {'n2' : 6, 'n4' : 7},
    'n4' : {'n3' : 7, 'n5' : 8},
    'n5' : {'n4' : 5, 'n6' : 8},
    'n6' : {'n7' : 4, 'n5' : 8, 'n2': 3, 'n3': 3},
    'n7' : {'n1' : 2, 'n6' : 4}
}

all_edges = []
MST = []

for source_node, neighbors in G.items(): # G.items() converts ('n1', {'n7': 2, 'n2': 9})  # WE CAN DECLARE MULTI-VAR ON A FOR LOOP.NO WAY!!!!

    for destination_node, weight in neighbors.items(): # ('n7', 2),('n2', 9)
        
        all_edges.append((weight, source_node, destination_node))
        
all_edges.sort()
if all_edges[0][0] != all_edges[1][0]:
    min_edge = all_edges[0]


print(all_edges)