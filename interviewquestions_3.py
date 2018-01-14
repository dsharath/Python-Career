#utility function to find the elements (Using path comparission technique)
def search(string, i):
    if string[i] == i:
        return i
    return search(string, string[i])

#making a union of two sets 
def union(string, stage, i,j):
    iroot = search(string, i)
    jroot = search(string,j)


    # attach small elements under root of high element tree
    if stage[iroot] < stage[jroot]:
        string[iroot] = jroot
    elif stage[iroot] > stage[jroot]:
        string[jroot] = iroot   #if satges are same ther is a increment by one
    else:
        string[jroot] = iroot
        stage[iroot] += 1

        
# main function using kruskals algorithm
def kruskal(graph, A, int_dict):
    results = []
    i =0  # sort edged index variable
    j=0  #resulted index variable
    graph = sorted(graph, key= lambda item: item[2])
    string = []; stage =[]
    for b in range(A):  # creating single substes with 'a'
         string.append(b)
         stage.append(0)
    while j < A -1 :    # selecting the samll element and incrementing the index & iteration to next stage
        x,y,z = graph[i]
        i = i+1
        p = search(string, x)
        q = search(string, y)

        if p != q:
            j = j+1
            results.append([x,y,z])
            union(string, stage, p, q)


    data = []
    final = {}
    for x, y, wgh in results:
        data = [(int_dict[y], wgh)]
        if int_dict[x] not in final:
            final[int_dict[x]] =data
        else:
             final[int_dict[x]] = final[int_dict[x]].append(data)
    return final



def question3(G):
    temp = {}
    int_dict = {}
    i = 0
    x,y,z = None,None,None
    graph = []
    for p in G:
        temp[p] = i
        int_dict[i] = p
        i += 1
        
    for p in G:
        for k in G[p]:
            x,y,z = temp[p], temp[k[0]], k[1]
            graph.append([x,y,z])
    return kruskal(graph, i, int_dict)
    

# testing output
def output():
    G = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}
    print question3(G)

if __name__ == '__main__':
    output()


        
    
