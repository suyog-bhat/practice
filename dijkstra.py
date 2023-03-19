import sys
class node:
    def __init__(self,data,wt):
        self.vertex=data
        self.weight=wt
        self.next=None

class graph:
    def __init__(self,vertices):
        self.num_of_vert=vertices
        self.node_list=[None]* self.num_of_vert

    def add_edge(self,src,dest,wt):
        edge=node(dest,wt)
        edge.next=self.node_list[src]
        self.node_list[src]=edge

    def print_node(self):
        for i in range(self.num_of_vert):
            temp=self.node_list[i]
            while temp:
                print("({}->{}) weight={}".format(i,temp.vertex,temp.weight))
                temp=temp.next

def find_min_dist_node(dis,vis):
    i=0
    curr_min=sys.maxsize
    node=0
    for i in range(len(dis)):
        if curr_min>=dis[i] and vis[i]==0:
            curr_min=dis[i]
            node=i
    return node


def dijkstra(graph,src):
    vis=[0] * graph.num_of_vert
    dis=[sys.maxsize] * graph.num_of_vert
    dis[src]=0
    vert=graph.node_list[src]
    while vert:
        dis[vert.vertex]=vert.weight
        vert=vert.next
    
    vis[src]=1
    for i in range(graph.num_of_vert):
        min_dist=find_min_dist_node(dis,vis)
        vis[min_dist]=1
        vert=graph.node_list[min_dist]
        while vert:
            if dis[vert.vertex]>dis[min_dist]+vert.weight:
                dis[vert.vertex]=dis[min_dist]+vert.weight
            vert=vert.next
    print(dis)





v=4
g=graph(v)
g.add_edge(0,1,2)
g.add_edge(0,2,1)
g.add_edge(1,2,5)
g.add_edge(0,3,10)
g.add_edge(1,3,2)
dijkstra(g,0)
g.print_node()