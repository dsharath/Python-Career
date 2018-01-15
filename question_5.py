class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

    
def question5(ll,m):
  node = ll
  current_node = ll
  count = 0
  for i in range(count, m):
    if (node == None):
      return None
    node = node.next
  while (node != None):
    node = node.next
    current_node = current_node.next
  return current_node.data

A = Node(2)
B = Node(5)
C = Node(1)
D = Node(9)
E = Node(3)

A.next= B
B.next= C
C.next= D
D.next= E	


print "Test Case1:",question5(A,5)

print "Test Case2:",question5(D,2)	
	
