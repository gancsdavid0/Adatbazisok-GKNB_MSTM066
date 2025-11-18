from menhely.models.telephelyek_befogadhato_allatok_model import Telephely_Befogadhato_Allatok_Modell


class Telephely_Befogadhato_Allatok_service(object):
    def __init__(self, conn):
        self.model = Telephely_Befogadhato_Allatok_Modell(conn)

    def getbyid(self, id):
        return self.model.getByID(id)

    def create(self):
        return self.model.create()

    def read(self):
        return self.model.read()

    def update(self):
        return self.model.update()

    def delete(self, id):
        return self.model.delete(id)

    def set_kapacitas(self, telephely_id, allatfajta_id, max_kapacitas):
        return self.set_kapacitas(telephely_id, allatfajta_id, max_kapacitas)

    def delete_kapcsolat(self, telephely_id, allatfajta_id):
        return self.delete_kapcsolat(telephely_id, allatfajta_id)

