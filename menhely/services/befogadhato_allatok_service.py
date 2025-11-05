from menhely.models.befogadhato_allatok_model import Befogadhato_Allatok_Model

class Befogadhato_Allatok_Service:
    def __init__(self, bef_allatok_model: Befogadhato_Allatok_Model):
        self.model = bef_allatok_model

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