from menhely.models.dolgozok_model import DolgozokModel
from menhely.models.kepesitesek_model import KepesitesModel
from menhely.models.dolgozok_kepesitesek_model import Dolgozo_kepesites_model

class DolgozokService:
    def __init__(self, dolgozok_model: DolgozokModel, kepesites_model: KepesitesModel, dk_model: Dolgozo_kepesites_model):
        self.model = dolgozok_model
        self.kepesites_model = kepesites_model
        self.dk_model = dk_model

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

    def get_kepesitesek_byid(self, id):
        return self.model.get_kepesitesek_byid(id)

    def _list_all_kepesitesek(self):
        print("\n--- Választható Képesítések ---")
        kepesitesek = self.kepesites_model.read()
        if not kepesitesek:
            print("Nincsenek képesítések.")
            return False
        for i in kepesitesek:
            print(i)
        return True

    def manage_kepesitesek(self):
        print("\n--- Dolgozói Képesítések Kezelése ---")
        if not self.model.read():
            return

        try:
            dolgozo_id = int(input("Adja meg a dolgozó ID-jét, akit kezelni szeretne: "))
            if not self.getByID(dolgozo_id):
                print(f'Nem létezik dolgozó ezzel az ID-vel')
                return
            print(f"\nA(z) {dolgozo_id} ID-jű dolgozó JELENLEGI képesítései:")
            jelenlegi = self.model.get_kepesitesek_byid(dolgozo_id)
            if not jelenlegi:
                print("Nincs még képesítése.")
            else:
                for i in jelenlegi:
                    print(i)

            print("\nVálasszon műveletet:")
            print("  1. Képesítés hozzáadása")
            print("  2. Képesítés eltávolítása")
            print("  0. Vissza a főmenübe")
            choice = input("Választás: ")

            if choice == '1':
                print("\nKépesítés hozzáadása:")
                print("  1. Választás a meglévő képesítések listájából")
                print("  2. Új képesítés létrehozása és azonnali hozzárendelése")
                sub_choice = input("Választás (1-2): ")

                if sub_choice == '1':
                    if not self._list_all_kepesitesek():
                        return

                    kepesites_id = int(input("Adja meg a HOZZÁADANDÓ képesítés ID-jét: "))

                    uj_kapcsolat_id = self.dk_model.create_with_ids(dolgozo_id, kepesites_id)
                    if uj_kapcsolat_id:
                        print("Képesítés sikeresen hozzáadva.")
                    else:
                        return

                elif sub_choice == '2':
                    uj_id = self.kepesites_model.create()
                    if uj_id:
                        print(f'Képesítés létrehozva ID: {uj_id}')
                        uj_kapcsolat_id = self.dk_model.create_with_ids(uj_id, dolgozo_id)
                        if uj_kapcsolat_id:
                            print('Új hozzárendelés létrehozva ID: {uj_kapcsolat_id}')
                        else:
                            print(f'Hiba a hozzárendelés létrehozása során.')
                    else:
                        print(f'Hiba az új képesítés létrehozása során.')
            elif choice == '2':
                if not jelenlegi:
                    print("Nincs mit eltávolítani.")
                    return

                kepesites_id = int(input("Adja meg az ELTÁVOLÍTANDÓ képesítés ID-jét: ", "id"))

                self.dk_model.delete(dolgozo_id, kepesites_id)
                print("Képesítés sikeresen eltávolítva.")

            elif choice == '0':
                return

        except Exception as e:
            print(f"HIBA a művelet közben: {e}")