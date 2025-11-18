from menhely.models.kepesitesek_model import KepesitesModel

class KepesitesekService:
    def __init__(self, conn):
        self.model = KepesitesModel(conn)

    def getByID(self, id):
        return self.model.getByID(id)

    def create(self):
        return self.model.create()

    def read(self):
        return self.model.read()

    def update(self):
        return self.model.update()

    def delete(self, id):
        return self.model.delete(id)