from menhely.models.orokbefogadasok_model import OrokbedogadasokModel
from menhely.models.allatok_model import AllatokModel
from menhely.models.dolgozok_model import DolgozokModel
from menhely.models.orokbefogadok_model import OrokbefogadokModel
from menhely.models.telephelyek_model import TelephelyekModel

class OrokbefogadasokService:
    def __init__(self, orokbefogadasok_model: OrokbedogadasokModel, allatok_model: AllatokModel, dolgozok_model: DolgozokModel,
                 orokbefogadok_model: OrokbefogadokModel, telephelyek_model: TelephelyekModel):
        self.model = orokbefogadasok_model
        self.allatok_model = allatok_model
        self.dolgozok_model = dolgozok_model
        self.orokbefogadok_model = OrokbefogadokModel
        self.telephelyek_model = TelephelyekModel

    def getByID(self, id):
        return self.model.getByID(id)

    #TODO {Örökbefogadás tranzakció létrehzzása}
    '''
    Orokbefogadas letrehozása:
        -IDk bekérése: ha minden idjó létrehozés
        -Befogadhato allatokbol törlöni az örökbefogadott állatok (classon keresztül)
    '''
    def create(self):
        return self.model.create()

    def read(self):
        return self.model.read()

    def update(self):
        return self.model.update()

    def delete(self, id):
        return self.model.delete(id)