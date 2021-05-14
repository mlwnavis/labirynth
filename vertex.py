class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {} # klucze - sąsiady (Vertex), wartości - wagi
        
    def get_id(self):
        return self.id

    def add_neighbor(self, nbr, weight=1):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys() # zwraca obiekt typu dict_keys

    def get_weight(self, nbr):
        return self.connected_to[nbr] # wartość dla klucza nbr to waga połączenia

    def __str__(self):
        return "{} connected to: {}.".format(self.id, [str(x.id) for x in self.connected_to])
