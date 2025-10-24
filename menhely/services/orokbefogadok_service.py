from menhely.models.orokbefogadok_model import OrokbefogadokModel

class OrokbefogadoService:
    def __init__(self, orokbefogadok_model: OrokbefogadokModel):
        self.model = orokbefogadok_model

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