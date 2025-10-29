from menhely.models.dolgozok_kepesitesek_model import Dolgozo_kepesites_model


class Dolgozok_kepesitesek_service(object):
    def __init__(self, dk_model: Dolgozo_kepesites_model):
        self.model = dk_model

    def getbyid(self, id):
        return self.model.getByID(id)

    def create_with_ids(self, dolgozok_id, kepesitesek_id):
        return self.model.create_with_ids(dolgozok_id, kepesitesek_id)

    def create(self):
        return self.model.create()

    def read(self):
        return self.model.read()

    def update(self):
        return self.model.update()

    def delete(self, dolgozo_id, kepesites_id):
        return self.model.delete(dolgozo_id, kepesites_id)