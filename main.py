import sqlite3
from menhely.models.allatok_model import AllatokModel
from menhely.models.orokbefogadok_model import OrokbefogadokModel
from menhely.services.orokbefogadok_service import OrokbefogadoService
from menhely.services.allatok_service import AllatokService

DB_NAME = "./allatmenhely.db"

if __name__ == '__main__':
    with sqlite3.connect(DB_NAME) as conn:
        allatok_m = AllatokModel(conn)
        allatok = AllatokService(allatok_m)
        orokbefogadok_m = OrokbefogadokModel(conn)
        orokbefogadok = OrokbefogadoService(orokbefogadok_m)

        for i in allatok.orokbefogadott_allatok():
            print(i[0])
            print(i[1])
