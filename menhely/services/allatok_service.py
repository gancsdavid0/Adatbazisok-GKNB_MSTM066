from menhely.models.allatok_model import AllatokModel

class AllatokService:
    def __init__(self, allatok_model: AllatokModel):
        self.model = allatok_model

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

    def orokbefogadhato_allatok(self):
        return self.model.orokbefogadhato_allatok()

    def orokbefogadott_allatok(self):
        return self.model.orokbefogadott_allatok()

    def orokbefogadas(self):
        return self.model.orokbefogadas()