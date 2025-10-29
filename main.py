import sqlite3
from menhely.models.allatok_model import AllatokModel
from menhely.models.orokbefogadok_model import OrokbefogadokModel

from menhely.services.orokbefogadok_service import OrokbefogadoService
from menhely.services.allatok_service import AllatokService

from menhely.models.dolgozok_model import DolgozokModel
from menhely.services.dolgozok_service import DolgozokService

from menhely.models.cimek_model import CimModel
from menhely.services.cimek_service import CimekService

from menhely.models.telephelyek_model import TelephelyekModel
from menhely.services.telephelyek_service import TelephelyekService

from menhely.models.dolgozok_kepesitesek_model import  Dolgozo_kepesites_model
from menhely.services.dolgozok_kepesitesek_service import Dolgozok_kepesitesek_service

from menhely.models.kepesitesek_model import KepesitesModel
from menhely.services.kepesitesek_service import KepesitesekService

from menhely.models.oltasok_model import OltasokModel
from menhely.services.oltasok_service import OltasokService

DB_NAME = "./allatmenhely.db"

if __name__ == '__main__':
    with sqlite3.connect(DB_NAME) as conn:
        allatok_m = AllatokModel(conn)
        allatok = AllatokService(allatok_m)
        orokbefogadok_m = OrokbefogadokModel(conn)
        orokbefogadok = OrokbefogadoService(orokbefogadok_m)
        dk_m = Dolgozo_kepesites_model(conn)
        dk = Dolgozok_kepesitesek_service(dk_m)
        kepesitesek_m = KepesitesModel(conn)
        kepesitesek = KepesitesekService(kepesitesek_m)

        dolgozok_m = DolgozokModel(conn)
        dolgozok = DolgozokService(dolgozok_m, kepesitesek_m, dk_m)

        oltasok_m = OltasokModel(conn)
        oltasok = OltasokService(oltasok_m)

        cimek_m = CimModel(conn)
        cimek = CimekService(cimek_m)


        telephely_m = TelephelyekModel(conn)
        telephelyek = TelephelyekService(telephely_m, cimek_m)

        for i in dolgozok.read():
            print(i)
        print()
        for i in kepesitesek.read():
            print(i)
        print()
        for i in dk.read():
            print(i)
        print()

        dolgozok.manage_kepesitesek()











