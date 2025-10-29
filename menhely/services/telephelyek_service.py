from menhely.models.telephelyek_model import TelephelyekModel
from menhely.models.cimek_model import CimModel

class TelephelyekService:
    def __init__(self, telephelyek_model: TelephelyekModel, cimek_model: CimModel):
        self.model = telephelyek_model
        self.cim_model = cimek_model

    def getByID(self, id):
        return self.model.getByID(id)

    def create(self):
        print("\nÚj Telephely Felvétele")
        print("Válasszon, hogyan szeretné megadni a címet:")
        print("  1. Teljesen új cím létrehozása")
        print("  2. Meglévő cím hozzárendelése")
        choice = input("Választás (1-2): ")

        if choice == '1':
            return self._create_with_new_address()

        elif choice == '2':
            print("Elérhető címek: ")
            all_cimek = self.cim_model.read()
            if not all_cimek:
                print("Nincsenek címek az adatbázisban. Előbb vegyen fel egyet.")
                return

            print("ID | Cím")
            for cim in all_cimek:
                print(cim)

            return self._create_with_existing_address()

        else:
            print("Érvénytelen választás.")

    def _create_with_new_address(self):
        return self.model.create_with_new_address()

    def _create_with_existing_address(self):
        return self.model.create_with_existing_address()

    def read(self):
        return self.model.read()

    def update(self):
        return self.model.update()

    def delete(self, id):
        return self.model.delete(id)