class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        dic = {}
        for i in self.nodes:
            val = i.value
            for j in i.edges:
                if j.value in dic.keys():
                    dic[j.value].append(val)
                else:
                    dic[j.value] = [val]
        edge_list = []
        for i in dic:
            lst = [i]
            lst.extend(dic[i])
            edge_list.append(tuple(lst))
        return edge_list

    def get_adjacency_list(self):
        dic = {}
        max_index = len(self.edges)
        adjacency_list = [None] * (max_index + 1)
        edg_lst = self.get_edge_list()
        for i in edg_lst:
            if (i[1] in dic.keys()):
                dic[i[1]].append((i[2], i[0]))
            else:
                dic[i[1]] = [(i[2], i[0])]
        # print(dic)
        for i in range(max_index + 1):
            if (i in dic.keys()):
                adjacency_list[i] = (dic[i])
        # print(adjacency_list)
        return adjacency_list
    
    
    def get_adjacency_matrix(self):
        max_index = len(self.edges)
        # print(len(self.nodes))
        adjacency_matrix = [[0 for i in range(max_index + 1)] for j in range(max_index + 1)]
        edg_lst = self.get_edge_list()
        # print(edg_lst)
        for i in edg_lst:
            adjacency_matrix[i[1]][i[2]] = i[0]
        # print(adjacency_matrix)
        return adjacency_matrix


if __name__ == "__main__":
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)
    # print(graph.get_edge_list())
    print(graph.get_adjacency_list())
