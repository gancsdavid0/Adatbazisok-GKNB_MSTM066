from menhely.models._base import Model
from dataclasses import dataclass

@dataclass
class Oltas:
    id: int
    kisallat_egeszsegugyi_konyvek_id: int
    oltas_tipusa: str
    oltas_idopontja: str
    oltas_ervenyessege: str
    allatorvos_neve: str
    megjegyzes: str

class OltasokModel(Model):
    def __init__(self, conn):
        self.conn = conn

    def _get_params(self) -> dict:
        params = {
                  "kisallat_egeszsegugyi_konyvek_id": input("Kisállat egészségügyi könyv id: "),
                  "oltas_tipusa": input("Oltás típúsa: "),
                  "oltas_idopontja": input("Oltás időpontja: "),
                  "oltas_ervenyessege": input("Oltás érvényessége: "),
                  "allatorvos_neve": input("Állatorvos neve: "),
                  "megjegyzes": input("Megjegyzés: "),
                }
        return params


    def getByID(self, id) -> Oltas | None:
        query = "SELECT * FROM oltasok WHERE id = ?"
        result = self.conn.execute(query, (id,)).fetchone()

        #print(result)
        return Oltas(result[0], result[1], result[2], result[3], result[4], result[5], result[6],) if result else None

    def create(self, allat_id) -> Oltas:
        query_id = ("""SELECT kisallat_egeszsegugyi_konyvek.id FROM kisallat_egeszsegugyi_konyvek
            where allatok_id = :allatok_id""")

        query = (
            "INSERT INTO oltasok (kisallat_egeszsegugyi_konyvek_id, oltas_tipusa, oltas_idopontja, oltas_ervenyessege, allatorvos_neve, megjegyzes)"
            " VALUES (:kisallat_egeszsegugyi_konyvek_id, :oltas_tipusa, :oltas_idopontja, :oltas_ervenyessege, :allatorvos_neve, :megjegyzes)")

        try:
            cursor = self.conn.cursor()

            cursor.execute(query_id, {"allatok_id" :allat_id})
            result = cursor.fetchone()

            if result is None:
                print("Hiba: Ennek az állatnak nincs egészségügyi kiskönyve!")
                return None

            konyv_id = result[0]

            params = {
                "kisallat_egeszsegugyi_konyvek_id": konyv_id,
                "oltas_tipusa": input("Oltás típúsa: "),
                "oltas_idopontja": input("Oltás időpontja: "),
                "oltas_ervenyessege": input("Oltás érvényessége: "),
                "allatorvos_neve": input("Állatorvos neve: "),
                "megjegyzes": input("Megjegyzés: "),
            }
            cursor.execute(query, params)
            new_id = cursor.lastrowid

            self.conn.commit()
            return self.getByID(new_id)

        except Exception as e:
            print(f"Hiba az oltás létrehozása közben: {e}")
            self.conn.rollback()
            return None


    def read(self) -> list[Oltas] | None:
        oltasok = []
        cursor = self.conn.execute("SELECT * FROM oltasok")
        rows = cursor.fetchall()
        for result in rows:
            oltasok.append(
                Oltas(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
        return oltasok

    def update(self) -> None:
        for i in self.read():
            print(i.id, i.kisallat_egeszsegugyi_konyvek_id, i.oltas_tipusa, i.oltas_idopontja, i.oltas_ervenyessege, i.allatorvos_neve,  i.megjegyzes)
        print("Melyiket szeretnéd módosítani?")

        try:
            id_to_update = int(input("ID: "))
        except ValueError as e:
            print("Hibás ID", e)
            return

        current_data = self.getByID(id_to_update)
        if not current_data:
            print("Hiba, nincsen ilyen oltás")
            return

        params = self._get_params()
        params["id"] = id_to_update

        sql = """
              UPDATE oltasok \
              SET kisallat_egeszsegugyi_konyvek_id      = :kisallat_egeszsegugyi_konyvek_id, \
                  oltas_tipusa                          = :oltas_tipusa, \
                  oltas_idopontja                       = :oltas_idopontja, \
                  oltas_ervenyessege                    = :oltas_ervenyessege, \
                  allatorvos_neve                       = :allatorvos_neve, \
                  megjegyzes                            = :megjegyzes
              WHERE id = :id \
              """

        self.conn.execute(sql, params)
        self.conn.commit()

        print(f"\nA(z) {id_to_update} ID-jú oltás adatai sikeresen frissítve!")

    def delete(self, id) -> None:
        current_data = self.getByID(id)
        if not current_data:
            print('Nem létezik ilyen rekord')
            return

        sql = "DELETE FROM oltasok WHERE id = :id"

        self.conn.execute(sql, {"id": id})
        self.conn.commit()

        print(f"{id}. rekord törölve lett")

    def getBy_KiskonyvID(self, kiskonyvek_id):
        query = "SELECT * FROM oltasok WHERE kisallat_egeszsegugyi_konyvek_id = ?"
        result = self.conn.execute(query, (kiskonyvek_id,)).fetchone()
        return Oltas(result[0], result[1], result[2], result[3], result[4], result[5], result[6], ) if result else None

    def getBy_allatokID(self, allatok_id):
        query = """SELECT o.id, o.kisallat_egeszsegugyi_konyvek_id, o.oltas_tipusa, o.oltas_idopontja, o.oltas_ervenyessege, o.allatorvos_neve, o.megjegyzes from allatok
            INNER JOIN main.kisallat_egeszsegugyi_konyvek kek on allatok.id = kek.allatok_id
            INNER JOIN main.oltasok o on kek.id = o.kisallat_egeszsegugyi_konyvek_id
                where allatok.id = :allatok_id"""
        # allatok.id, o.id, o.oltas_tipusa, o.oltas_idopontja, o.oltas_ervenyessege, o.oltas_ervenyessege, o.allatorvos_neve, o.megjegyzes
        try:
            cursor = self.conn.cursor()

            params = {"allatok_id": allatok_id}

            cursor.execute(query, params)

            rows = cursor.fetchall()
            oltasok = []
            for result in rows:
                oltasok.append(
                    Oltas(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
            return oltasok

        except Exception as e:
            print(f"Hiba az oltások lekérdezésekor: {e}")
            return []