from menhely.models.oltasok_model import OltasokModel

class OltasokService:
    def __init__(self, conn):
        self.model = OltasokModel(conn)

    def getByID(self, id):
        return self.model.getByID(id)

    def create(self, allat_id):
        return self.model.create(allat_id)

    def read(self):
        return self.model.read()

    def update(self):
        return self.model.update()

    def delete(self, id):
        return self.model.delete(id)

    def getBy_KiskonyvID(self, kiskonyvek_id):
        return self.model.getBy_KiskonyvID(kiskonyvek_id)

    def getBy_allatokID(self, allatok_id):
        return self.model.getBy_allatokID(allatok_id)