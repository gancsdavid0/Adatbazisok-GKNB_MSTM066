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

from menhely.models.befogadhato_allatok_model import Befogadhato_Allatok_Model
from menhely.services.befogadhato_allatok_service import Befogadhato_Allatok_Service

from menhely.models.kisallat_egeszsegugyi_konyvek_model import KiskonyvekModel
from menhely.services.kisallat_egeszsegugyi_konyvek_service import Kiskonyvek_Service

from menhely.models.telephelyek_befogadhato_allatok_model import Telephely_Befogadhato_Allatok_Modell
from menhely.services.telephelyek_befogadhato_allatok_service import Telephely_Befogadhato_Allatok_service

DB_NAME = "./allatmenhely.db"

if __name__ == '__main__':
    with sqlite3.connect(DB_NAME) as conn:
        kiskonyvek_m = KiskonyvekModel(conn)
        kiskonyvek = Kiskonyvek_Service(kiskonyvek_m)

        allatok_m = AllatokModel(conn)
        allatok = AllatokService(allatok_m, kiskonyvek_m)
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

        befogadhato_allatok_m = Befogadhato_Allatok_Model(conn)
        befogadhato_allatok = Befogadhato_Allatok_Service(befogadhato_allatok_m)

        tba_m = Telephely_Befogadhato_Allatok_Modell(conn)
        tba = Telephely_Befogadhato_Allatok_service(tba_m)

        telephely_m = TelephelyekModel(conn)
        telephelyek = TelephelyekService(telephely_m, cimek_m, befogadhato_allatok_m, tba_m)

       #telephelyek.manage_telephely_befogadhatosag()



        '''
        if conn:
            print(12*'-', 'Állatmenhely adatbázis', 12*'-')
            choice = print('Válasszon az alábbi lehetőségek közül: ')
            #Táblák
        '''











