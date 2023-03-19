class node:
    def __init__(self,data):
        self.vertex=data
        self.next=None

class graph:
    def __init__(self,vertices):
        self.num_of_vert=vertices
        self.node_list=[None]* self.num_of_vert

    def add_edge(self,src,dest):
        edge=node(dest)
        edge.next=self.node_list[src]
        self.node_list[src]=edge

        edge=node(src)
        edge.next=self.node_list[dest]
        self.node_list[dest]=edge

    def print_node(self):
        for i in range(self.num_of_vert):
            print(i,end="")
            temp=self.node_list[i]
            while temp:
                print(" ->{}".format(temp.vertex),end="")
                temp=temp.next
            print("\n")

v=3
g=graph(v)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.print_node()


