from menhely.services.orokbefogadok_service import OrokbefogadoService
from menhely.services.allatok_service import AllatokService
from menhely.services.dolgozok_service import DolgozokService
from menhely.services.cimek_service import CimekService
from menhely.services.telephelyek_service import TelephelyekService
from menhely.services.dolgozok_kepesitesek_service import Dolgozok_kepesitesek_service
from menhely.services.kepesitesek_service import KepesitesekService
from menhely.services.oltasok_service import OltasokService
from menhely.services.befogadhato_allatok_service import Befogadhato_Allatok_Service
from menhely.services.kisallat_egeszsegugyi_konyvek_service import Kiskonyvek_Service
from menhely.services.telephelyek_befogadhato_allatok_service import Telephely_Befogadhato_Allatok_service

class Menu():
    def __init__(self, conn):
        self._kiskonyvek = Kiskonyvek_Service(conn)
        self._allatok = AllatokService(conn)
        self._orokbefogadok = OrokbefogadoService(conn)
        self._dk = Dolgozok_kepesitesek_service(conn)
        self._kepesitesek = KepesitesekService(conn)
        self._dolgozok = DolgozokService(conn)
        self._oltasok = OltasokService(conn)
        self._cimek = CimekService(conn)
        self._befogadhato_allatok = Befogadhato_Allatok_Service(conn)
        self._tba = Telephely_Befogadhato_Allatok_service(conn)
        self._telephelyek = TelephelyekService(conn)
        #self._telephelyek.manage_telephely_befogadhatosag()
        self._subchoice = None

    def _Allatok_menu(self):
        while self._subchoice != 0:
            print('\n--- Állatok kezelése ---')
            print('Válasszon az alábbi lehetőségek közül: ')
            print('1. Állatok listázása')
            #TODO
            print('2. (NINCSEN MEG) Új állatok felvétele')
            print('3. (NINCSEN MEG) Állat adatainak módosítása')
            print('4. (NINCSEN MEG) Oltások kezelése')
            print('0. Vissza')
            self._subchoice = int(input('Választás: '))

            match self._subchoice:
                case 1:
                    for i in self._allatok.read():
                        print(i)
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 0:
                    continue

    def _Telephelyek_menu(self):
        while self._subchoice != 0:
            print('\n --- Telephelyek kezelése--- ')
            print('Válasszon az alábbi lehetőségek közül: ')
            print('1. Telephelyek listázása')
            print('2. Új telephely felvétele')
            print('3. Telephely törlése')
            print('4. Telephely befogadhatóságának kezelése')
            print('0. Vissza')
            self._subchoice = int(input('Választás: '))

            match self._subchoice:
                case 1:
                    for i in self._telephelyek.read(): print(i)
                case 2:
                    self._telephelyek.create()
                case 3:
                    id_to_delete = int(input("Adja meg a törölni kívánt telephely id-át"))
                    self._telephelyek.delete(id_to_delete)
                case 4:
                    self._telephelyek.manage_telephely_befogadhatosag()
                case 0:
                    continue

    def _Dolgozok_menu(self):
        while self._subchoice != 0:
            print('\n --- Dolgozók kezelése--- ')
            print('Válasszon az alábbi lehetőségek közül: ')
            print('1. Dolgozók listázása')
            print('2. Új dolgozó felvétele')
            print('3. Dolgozó eltávolítása')
            print('4. Dolgozók képesítéseinek kezelése')
            print('5. Dolgozó adatainak módosítása')
            print('0. Vissza')

            self._subchoice = int(input('Választás: '))

            if self._subchoice == 1:
                for i in self._dolgozok.read(): print(i)
            elif self._subchoice == 2:
                self._dolgozok.create()
            elif self._subchoice == 3:
                id_to_delete = int(input('Adja meg a törölni kívánt dolgozó id-át: '))
                self._dolgozok.delete(id_to_delete)
            elif self._subchoice == 4:
                self._dolgozok.manage_kepesitesek()
            elif self._subchoice == 5:
                self._dolgozok.update()
            elif self._subchoice == 0:
                continue
            else:
                print('Helytelen választás')
            input('Tovább... [Enter]')

    def _Orokbefogadok_menu(self):
        while self._subchoice != 0:
            print('\n --- Örökbefogadók kezelése--- ')
            print('Válasszon az alábbi lehetőségek közül: ')
            print('1. Örökbefogadók listázása')
            print('2. Új örökbefogadó felvétele')
            print('3. Örökbefogadó törlése')
            print('4. Örökbefogadó adatainak módosítása')
            print('5. Vissza')

            self._subchoice = int(input('Választás: '))

            if self._subchoice == 1:
                for i in self._orokbefogadok.read(): print(i)
            elif self._subchoice == 2:
                self._orokbefogadok.create()
            elif self._subchoice == 3:
                id_to_delete = int(input('Adja meg a törölni kívánt örökbefogadó id-át: '))
                self._orokbefogadok.delete(id_to_delete)
            elif self._subchoice == 4:
                self._orokbefogadok.update()
            elif self._subchoice == 0:
                continue
            else:
                print('Helytelen választás')
            input('Tovább... [Enter]')

    def _Orokbefogadasok_menu(self):
        while self._subchoice != 0:
            print('\n --- Örökbefogadások kezelése ---')
            print('Válasszon az alábbi lehetőségek közül: ')
            print('1. Örökbefogadások listázása')
            print('2. Örökbefogadható állatok listázása')
            #TODO
            print('3. (NINCSEN MEG) Új örökbefogadás  felvétele')
            print('0. Vissza')
            self._subchoice = int(input('Választás: '))

            match self._subchoice:
                case 1:
                    for i in self._allatok.orokbefogadott_allatok():
                        print(i)
                case 2:
                    for i in self._allatok.orokbefogadhato_allatok():
                        print(i)
                case 3:
                    pass
                case 0:
                    continue

    def Menu(self):
        choice = None
        while choice != 0:
            self._subchoice = None
            print(12*'-', 'Állatmenhely adatbázis', 12*'-')
            print('Válasszon az alábbi lehetőségek közül: ')
            print('1. Állatok kezelése')
            print('2. Telephelyek kezelése')
            print('3. Dolgozók kezelése')
            print('4. Örökbefogadók kezelése')
            print('5. Örökbefogadások kezelése')
            print('0. Kilépés')

            choice = int(input('Választás: '))

            match choice:
                case 1:
                    self._Allatok_menu()
                case 2:
                    self._Telephelyek_menu()
                case 3:
                    self._Dolgozok_menu()
                case 4:
                    self._Orokbefogadok_menu()
                case 5:
                    self._Orokbefogadasok_menu()