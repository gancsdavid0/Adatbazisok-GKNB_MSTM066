from menhely.models.kisallat_egeszsegugyi_konyvek_model import KiskonyvekModel

class Kiskonyvek_Service:
    def __init__(self, kiskonyvek_model: KiskonyvekModel):
        self.model = kiskonyvek_model

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