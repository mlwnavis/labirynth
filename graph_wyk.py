from vertex import Vertex


class Graph:
    def __init__(self):
        self.vert_list = {} # klucze - klucze wierzchołków, wartosci - wierzcholki (Vertex)

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def add_edge(self, f, t, weight=1):
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __contains__(self, key): # x in g
        return key in self.vert_list

    def __iter__(self):
        return iter(self.vert_list.values())


def graph_test():
    g = Graph()
    for i in range(6):
        g.add_vertex(i)

    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 0)
    g.add_edge(5, 4)
    g.add_edge(5, 2)

    for v in g:
        print(v)


if __name__ == "__main__":
    graph_test()
