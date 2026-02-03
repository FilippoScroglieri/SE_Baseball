import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.squadre= []
        self.G= nx.Graph()

        self.map= {}


    def mappa(self,anno):
        self.squadre= DAO.read_squadre(anno)
        for squadra in self.squadre:
            self.map[squadra.team_code]=squadra # grazie alla mappa io ogni volta che richiamo un team_code mi restituirà direttamente l'oggetto squadra
        return self.map

    def get_anni(self):
        return DAO.read_anni()

    def get_squadre(self,anno):
        return DAO.read_squadre(anno)

    def crea_grafo(self,anno):
        self.G.clear()
        stipendi= DAO.read_stipendi(anno) # stipendi è il dizionario con chiave team_code e valore sum(salary)
        self.squadre= DAO.read_squadre(anno)

        self.G.add_nodes_from(self.squadre) # ora ho tutti i nodi

        for squadra1 in self.squadre:
            stipendio1= stipendi[squadra1.team_code]
            for squadra2 in self.squadre:
                stipendio2= stipendi[squadra2.team_code]
                if squadra1 != squadra2:
                    self.G.add_edge(squadra1,squadra2,weight= stipendio1+stipendio2)
        return self.G

    def dettagli(self,squadra):
        return list(self.G.neighbors(squadra))







