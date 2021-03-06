#=============================================================****
#Question 1:
#Given two strings s and t, determine whether some anagram of t is a substring of s. 
#For example: if s = "udacity" and t = "ad", then the function returns True. 
#Your function definition should look like: question1(s, t) and return 
#a boolean True or False.
#===============================================================***

def anagram(a,b):
    return sorted(a) == sorted(b)
def question1(s,t):
    i = len(s)
    j = len(t)
    for k in range(i - j + 1):
        if anagram(s[k: k+j], t):
            return True
    return False

#test case1:
print "Test Case2 : ",question1("udacity","ad")

#test case2:
print "Test Case1 : ",question1("UDACITY","KL")
#test case 3:
print "Test Case3 : ",question1("Racecar","Racecar")

#==============================================================******
#Question 2:
#Given a string a, find the longest palindromic substring contained in a. 
#Your function definition should look like question2(a), and return a string.
#=================================================================*************

def substring(s):
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            yield s[j: j+i]

def question2(a):
    for i in substring(a):
        if a==a[::-1]:
            return i
        


#test case1:
print question2("abccba")         
#test case2:

print question2("abccb")

#test case3:
print question2("a")


#================================================================********
# Question 3:
#Given an undirected graph G, find the minimum spanning tree within G. 
#A minimum spanning tree connects all vertices in a graph with the smallest possible 
#total weight of edges. Your function should take in and return an adjacency list 
#structured like this:
#
#{'A': [('B', 2)],
 #'B': [('A', 2), ('C', 5)], 
 #'C': [('B', 5)]}
#
#Vertices are represented as unique strings. The function definition should be question3(G)
#========================================================****************
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
    

# testing case 1:
def output():
    G = {'A': [('B', 2)],
          'B': [('A', 4), ('C', 2)],
          'C': [('A', 2), ('B', 5)]}
    print question3(G)
#test case 2:	
def output():
    G = {'A': [('B', 3)],
          'B': [('A', 5), ('C', 2)],
          'C': [('A', 1), ('B', 4)]}
    print question3(G)
#test case 3:
def output():
    G = {'A': [('B', 3)],
          'B': [('A', 5), ('C', 3)],
          'C': [('A', 3), ('B', 6)]}
    print question3(G)
	
	
if __name__ == '__main__':
    output()


        
    
#=================================================*******
# Question 4:
#Find the least common ancestor between two nodes on a binary search tree. 
#The least common ancestor is the farthest node from the root that is an 
#ancestor of both nodes. For example, 
#the root is a common ancestor of all nodes on the tree, 
#but if both nodes are descendents of the root's left child, 
#then that left child might be the lowest common ancestor. 
#You can assume that both nodes are in the tree, and the tree itself adheres
# to all BST properties. The function definition should look like
# question4(T, r, n1, n2), where T is the tree represented as a matrix,
# where the index of the list is equal to the integer stored in that node and a 1 
#represents a child node, r is a non-negative integer representing the root, 
#and n1 and n2 are non-negative integers representing the two nodes in no particular order.
# For example, one test case might be
#
#question4([[0, 1, 0, 0, 0],
 #          [0, 0, 0, 0, 0],
  #         [0, 0, 0, 0, 0],
   ##       [0, 0, 0, 0, 0]],
     #     3,
      #    1,
       #   4)

#and the answer would be 3.
#=================================================***********
def parent(tree, node): #finding whether node has a parent are not
	for i in range(len(tree)):
	    if tree[i][node] == 1:
		    return i
	return -1

def question4(T, r, n1,n2):
        i = []
        while n1 != r:
                n1 = parent(T, n1)
                i.append(n1)
        if len(i) == 0:
                return -1
                
        while n2 != r:
                n2 = parent(T,n2)
                if n2 in i:
                        return n2
        return -1
        
print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)



