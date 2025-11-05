from menhely.models.allatok_model import AllatokModel
from menhely.models.kisallat_egeszsegugyi_konyvek_model import KiskonyvekModel

class AllatokService:
    def __init__(self, allatok_model: AllatokModel, kiskonyvek_model: KiskonyvekModel):
        self.model = allatok_model
        self.kiskonyvek_model = kiskonyvek_model

    #TODO {Minden lekérdezés a kiskönyvel és az oltásokkal kapcsolatban innen kerül lekérdezésre illetve kezelésre az állat classból
    # de a kiskönyv és az oltások classokon keresztül lokális függvényekkel, pl get_oltasok {az oltások classból hívjuk}}

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