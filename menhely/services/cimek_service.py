from menhely.models.cimek_model import CimModel

class CimekService:
    def __init__(self, conn):
        self.model = CimModel(conn)

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

    def _delete_cim_trans(self, id):
        return self.model._delete_cim_trans(id)

    def _update_cim_trans(self, id) -> bool:
        return self.model._update_cim_trans(id)