from menhely.models.telephelyek_model import TelephelyekModel
from menhely.models.cimek_model import CimModel
from menhely.models.befogadhato_allatok_model import Befogadhato_Allatok_Model
from menhely.models.telephelyek_befogadhato_allatok_model import Telephely_Befogadhato_Allatok_Modell

class TelephelyekService:
    def __init__(self, conn) -> None:
        self.model = TelephelyekModel(conn)
        self.cim_model = CimModel(conn)
        self.befogadhato_allatok_model = Befogadhato_Allatok_Model(conn)
        self.telephelyek_befogadhato_allatok_Model = Telephely_Befogadhato_Allatok_Modell(conn)

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

    def manage_telephely_befogadhatosag(self):
        print("\n--- Telephely Befogadóképességének Kezelése ---")

        if not self.read():
            return
        else:
            for i in self.model.read():
                print(i)
        try:
            telephely_id = input("Válassza ki a kezelni kívánt telephely ID-jét: ")

            if not self.model.getByID(telephely_id):
                print("HIBA: Nincs ilyen ID-jű telephely.")
                return

            while True:
                print(f"\nKezelt telephely (ID: {telephely_id}). Jelenlegi beállítások:")

                kapacitas = self.model.get_kapacitasok_by_telephely_id(telephely_id)
                if kapacitas== -1:
                    return
                else:
                    for (id, allat_neve, max_db) in kapacitas:
                        print(f'ID: {id} - {allat_neve} - Befogadható: {max_db} db')

                print("\nMit szeretne tenni?")
                print("  1. Kapacitás beállítása / módosítása")
                print("  2. Befogadott állatfajta eltávolítása a telephelyről")
                print("  3. ÚJ állatfajta felvétele a rendszerbe és hozzárendelés)")
                print("  0. Vissza")

                choice = input("Választás: ")

                if choice == '1':
                    if not self.model.get_kapacitasok_by_telephely_id(telephely_id): continue


                    allatfajta_id = input("Melyik állatfajta ID-jét állítja be? ")

                    max_db = input("Adja meg az új maximális kapacitást (0-tól): ")

                    self.telephelyek_befogadhato_allatok_Model.set_kapacitas(telephely_id, allatfajta_id, max_db)
                    print("Kapacitás frissítve.")

                elif choice == '2':
                    if not kapacitas:
                        print("Nincs mit eltávolítani.")
                        continue

                    if not self.model.get_kapacitasok_by_telephely_id(telephely_id): continue

                    allatfajta_id = input("Melyik állatfajta ID-jét távolítja el? ")

                    self.telephelyek_befogadhato_allatok_Model.delete_kapcsolat(telephely_id, allatfajta_id)
                    print("Kapcsolat törölve.")

                elif choice == '3':
                    print("\nÚj állatfajta felvétele a globális listára...")
                    new_id = self.befogadhato_allatok_model.create()

                    if new_id:
                        print(
                            f"Új állatfajta (ID: {new_id}) létrehozva. Most már beállíthatja a kapacitását.")

                elif choice == '0':
                    print("Visszatérés a telephely választáshoz...")
                    break
                else:
                    print("Érvénytelen választás.")

        except KeyboardInterrupt:
            print("\nMűvelet megszakítva.")
        except Exception as e:
            print(f"HIBA: Váratlan hiba történt: {e}")

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

    def get_befogadato_allatok_byid(self, id):
        return self.model.get_befogadato_allatok_byid(id)