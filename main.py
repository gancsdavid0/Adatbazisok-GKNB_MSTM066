import sqlite3
from typing import final

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

def main():
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

        if conn:
            choice = None
            subchoice = None
            while choice != 0:
                print(12*'-', 'Állatmenhely adatbázis', 12*'-')
                print('Válasszon az alábbi lehetőségek közül: ')
                print('1. Állatok kezelése')
                print('2. Telephelyek kezelése')
                print('3. Dolgozók kezelése')
                print('4. Örökbefogadók kezelése')
                print('5. Örökbefogadások kezelése')
                print('0. Kilépés')
                choice = int(input('Választás: '))
                if choice == 1: #Nincs kész még allatok fv-ek nem fix a menüje, oltások kezelése is idejön
                    while subchoice != 0:
                        print('\n--- Állatok kezelése ---')
                        print('Válasszon az alábbi lehetőségek közül: ')
                        print('1. Állatok listázása')
                        print('2. Új állatok felvétele')
                        print('3. Állat adatainak módosítása')
                        print('0. Vissza')
                        subchoice = int(input('Választás: '))

                elif choice == 2:
                    while subchoice != 0:
                        print('\n --- Telephelyek kezelése--- ')
                        print('Válasszon az alábbi lehetőségek közül: ')
                        print('1. Telephelyek listázása')
                        print('2. Új telephely felvétele')
                        print('3. Telephely törlése')
                        print('4. Telephely befogadhatóságának kezelése')
                        print('5. Új cím felvétele')
                        print('0. Vissza')
                        subchoice = int(input('Választás: '))

                elif choice == 3:
                    while subchoice != 0:
                        print('\n --- Dolgozók kezelése--- ')
                        print('Válasszon az alábbi lehetőségek közül: ')
                        print('1. Dolgozók listázása')
                        print('2. Új dolgozó felvétele')
                        print('3. Dolgozó eltávolítása')
                        print('4. Dolgozók képesítéseinek kezelése')
                        print('5. Dolgozó adatainak módosítása')
                        print('0. Vissza')

                        subchoice = int(input('Választás: '))

                        if subchoice == 1:
                            for i in dolgozok.read(): print(i)
                        elif subchoice == 2:
                            dolgozok.create()
                        elif subchoice == 3:
                            id_to_delete = int(input('Adja meg a törölni kívánt dolgozó id-át: '))
                            dolgozok.delete(id_to_delete)
                        elif subchoice == 4:
                            dolgozok.manage_kepesitesek()
                        elif subchoice == 5:
                            dolgozok.update()
                        elif subchoice == 0:
                            continue
                        else:
                            print('Helytelen választás')
                        input('Tovább... [Enter]')


                elif choice == 4:
                    while subchoice != 0:
                        print('\n --- Örökbefogadók kezelése--- ')
                        print('Válasszon az alábbi lehetőségek közül: ')
                        print('1. Örökbefogadók listázása')
                        print('2. Új örökbefogadó felvétele')
                        print('3. Örökbefogadó törlése')
                        print('4. Örökbefogadó adatainak módosítása')
                        print('5. Vissza')

                        subchoice = int(input('Választás: '))

                        if subchoice == 1:
                            for i in orokbefogadok.read(): print(i)
                        elif subchoice == 2:
                            orokbefogadok.create()
                        elif subchoice == 3:
                            id_to_delete = int(input('Adja meg a törölni kívánt örökbefogadó id-át: '))
                            orokbefogadok.delete(id_to_delete)
                        elif subchoice == 4:
                            orokbefogadok.update()
                        elif subchoice == 0:
                            continue
                        else:
                            print('Helytelen választás')
                        input('Tovább... [Enter]')

                elif choice == 5:
                    while subchoice != 0:
                        print('\n --- Örökbefogadások kezelése ---')
                        print('Válasszon az alábbi lehetőségek közül: ')
                        print('1. Örökbefogadások listázása')
                        print('2. Új örökbefogadás  felvétele')
                        print('0. Vissza')


if __name__ == '__main__':
    main()