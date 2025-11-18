from menhely.models.allatok_model import AllatokModel
from menhely.models.kisallat_egeszsegugyi_konyvek_model import KiskonyvekModel

class AllatokService:
    def __init__(self, conn):
        self.allatok_model = AllatokModel(conn)
        self.kiskonyvek_model = KiskonyvekModel(conn)

    def getByID(self, id):
        return self.allatok_model.getByID(id)

    def create(self, befogadhato_allatok_id, telephelyek_id):
        return self.allatok_model.create(befogadhato_allatok_id, telephelyek_id)

    def read(self):
        return self.allatok_model.read()

    def update(self, id):
        return self.allatok_model.update(id)

    def delete(self, id):
        return self.allatok_model.delete(id)

    def orokbefogadhato_allatok(self):
        return self.allatok_model.orokbefogadhato_allatok()

    def orokbefogadott_allatok(self):
        return self.allatok_model.orokbefogadott_allatok()

    def orokbefogadas(self, allatok_id , dolgozok_id, orokbefogadok_id, telephelyek_id):
        return self.allatok_model.orokbefogadas(allatok_id , dolgozok_id, orokbefogadok_id, telephelyek_id)