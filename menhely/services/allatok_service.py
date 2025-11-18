from menhely.models.allatok_model import AllatokModel
from menhely.models.kisallat_egeszsegugyi_konyvek_model import KiskonyvekModel

class AllatokService:
    def __init__(self, conn):
        self.allatok_model = AllatokModel(conn)
        self.kiskonyvek_model = KiskonyvekModel(conn)

    #TODO {Minden lekérdezés a kiskönyvel és az oltásokkal kapcsolatban innen kerül lekérdezésre illetve kezelésre az állat classból
    # de a kiskönyv és az oltások classokon keresztül lokális függvényekkel, pl get_oltasok {az oltások classból hívjuk}}

    def getByID(self, id):
        return self.allatok_model.getByID(id)

    def create(self):
        return self.allatok_model.create()

    def read(self):
        return self.allatok_model.read()

    def update(self):
        return self.allatok_model.update()

    def delete(self, id):
        return self.allatok_model.delete(id)

    def orokbefogadhato_allatok(self):
        return self.allatok_model.orokbefogadhato_allatok()

    def orokbefogadott_allatok(self):
        return self.allatok_model.orokbefogadott_allatok()

    def orokbefogadas(self):
        return self.allatok_model.orokbefogadas()