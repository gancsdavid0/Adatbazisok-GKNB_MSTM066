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
            print('2. Új állatok felvétele')
            print('3. Állat adatainak módosítása')
            print('4. Oltások kezelése')
            print('0. Vissza')
            self._subchoice = int(input('Választás: '))

            match self._subchoice:
                case 1:
                    h = f'  {'ID':3} {'Név':10} {'Ivar':8} {'Súly':6} {'Szín':10} {'Ivartalanitva':4} \t {'Méret':9} {'Mikrochip száma':20} \t {'Születesi idő':12} \t {'Egészsegi állapot':20}'
                    print(h)
                    print("-"*(len(h)+2))
                    for i in self._allatok.read():
                        print(f'{i.id:3}   {i.nev:10} {i.ivar:7} {i.suly:6} {i.szin:10} {i.ivartalanitva:11} \t\t {i.meret:10} {str(i.mikrochip_szam):20} \t {str(i.szuletesi_ido):12} \t {i.egeszsegi_allapot:20}' )

                case 2:
                    print(f"{'ID':<5} {'Fajta':<15} {'Megjegyzés'}")
                    print("-" * 40)

                    for i in self._befogadhato_allatok.read():
                        print(f"{i.id:<5} {i.allat_fajtaja:<15} {i.megjegyzes}")
                    befogadhato_allatok_id = int(input("Add meg a felvenni kívánt állat típusának ID-ját: "))

                    print(f"{'ID':<4} {'RefID':<6} {'IRSZ':<6} {'Város':<15} {'Utca':<25} {'Házszám'}")
                    print("-" * 70)
                    for i in self._telephelyek.read():
                        print(f"{i[0]:<4} {i[1]:<6} {i[2]:<6} {i[3]:<15} {i[4]:<25} {i[5]}")

                    telephelyek_id = int(input("Add meg a telephely ID-ját: "))

                    self._allatok.create(befogadhato_allatok_id, telephelyek_id)
                case 3:
                    h = f'  {'ID':3} {'Név':10} {'Ivar':8} {'Súly':6} {'Szín':10} {'Ivartalanitva':4} \t {'Méret':9} {'Mikrochip száma':20} \t {'Születesi idő':12} \t {'Egészsegi állapot':20}'
                    print(h)
                    print("-" * (len(h) + 2))
                    for i in self._allatok.read():
                        print(f'{i.id:3}   {i.nev:10} {i.ivar:7} {i.suly:6} {i.szin:10} {i.ivartalanitva:11} \t\t {i.meret:10} {str(i.mikrochip_szam):20} \t {str(i.szuletesi_ido):12} \t {i.egeszsegi_allapot:20}')
                    id = int(input("Adja meg a frissíteni kívánt állat ID-ját: "))

                    self._allatok.update(id)
                case 4:
                    oltasokChoise = None
                    while oltasokChoise != 0:
                        print('\n--- Oltások kezelése ---')
                        print('Válasszon az alábbi lehetőségek közül: ')
                        print('1. Oltások kiírása állat ID alapján')
                        print('2. Új oltás felvétele')
                        print('3. Oltás törlése')
                        print('0. Vissza')
                        oltasokChoise = int(input('Választás: '))
                        match oltasokChoise:
                            case 1:
                                h = f'  {'ID':3} {'Név':10} {'Ivar':8} {'Súly':6} {'Szín':10} {'Ivartalanitva':4} \t {'Méret':9} {'Mikrochip száma':20} \t {'Születesi idő':12} \t {'Egészsegi állapot':20}'
                                print(h)
                                print("-" * (len(h) + 2))
                                for i in self._allatok.read():
                                    print(f'{i.id:3}   {i.nev:10} {i.ivar:7} {i.suly:6} {i.szin:10} {i.ivartalanitva:11} \t\t {i.meret:10} {str(i.mikrochip_szam):20} \t {str(i.szuletesi_ido):12} \t {i.egeszsegi_allapot:20}')
                                allatok_id = int(input("Adja meg az állat ID-ját az oltásainak lekérdezéséhez: "))

                                print(f'{'ID':<3} {'RefID':<3}   {'Oltás tipusa':<15} {'Oltás időpontja':<12} {'Oltás érvényessége':<12} {'Orvos':<20} {'Megjegyzés'}')
                                print("-" * 95)
                                for i in self._oltasok.getBy_allatokID(allatok_id):
                                    print(
                                        f'{i.id:<3}  {i.kisallat_egeszsegugyi_konyvek_id:<3}   {i.oltas_tipusa:<15} {i.oltas_idopontja:<12} {i.oltas_ervenyessege:<12} {i.allatorvos_neve:<20}  {i.megjegyzes}')
                            case 2:
                                h = f'  {'ID':3} {'Név':10} {'Ivar':8} {'Súly':6} {'Szín':10} {'Ivartalanitva':4} \t {'Méret':9} {'Mikrochip száma':20} \t {'Születesi idő':12} \t {'Egészsegi állapot':20}'
                                print(h)
                                print("-" * (len(h) + 2))
                                for i in self._allatok.read():
                                    print(f'{i.id:3}   {i.nev:10} {i.ivar:7} {i.suly:6} {i.szin:10} {i.ivartalanitva:11} \t\t {i.meret:10} {str(i.mikrochip_szam):20} \t {str(i.szuletesi_ido):12} \t {i.egeszsegi_allapot:20}')
                                id = int(input("Melyik állathoz szeretnél oltást adni?"))
                                self._oltasok.create(id)
                            case 3:
                                print(
                                    f'{'ID':<3} {'RefID':<3}   {'Oltás tipusa':<15} {'Oltás időpontja':<12} {'Oltás érvényessége':<12} {'Orvos':<20} {'Megjegyzés'}')
                                print("-" * 95)
                                for i in self._oltasok.getBy_allatokID(allatok_id):
                                    print(f'{i.id:<3}  {i.kisallat_egeszsegugyi_konyvek_id:<3}   {i.oltas_tipusa:<15} {i.oltas_idopontja:<12} {i.oltas_ervenyessege:<12} {i.allatorvos_neve:<20}  {i.megjegyzes}')
                                id = int(input("Adja meg az oltás ID-ját: "))
                                self._oltasok.delete(id)
                            case 0:
                                continue

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
                    print(f"{'ID':<4} {'RefID':<6} {'IRSZ':<6} {'Város':<15} {'Utca':<25} {'Házszám'}")
                    print("-" * 70)
                    for i in self._telephelyek.read():
                        print(f"{i[0]:<4} {i[1]:<6} {i[2]:<6} {i[3]:<15} {i[4]:<25} {i[5]}")
                case 2:
                    address_id = self._cimek.create()
                    self._telephelyek.create(int(address_id.id))
                case 3:
                    id_to_delete = int(input("Adja meg a törölni kívánt telephely id-át"))
                    telephely = self._telephelyek.getByID(id_to_delete)
                    address_id = telephely.cimek_id
                    self._cimek.delete(address_id)
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
                print(f"{'ID':<4} {'Név':<20} {'Pozíció':<21} {'Telefon':<15} {'Email'}")
                print("=" * 80)
                for i in self._dolgozok.read():
                    teljes_nev = f"{i.vezeteknev} {i.keresztnev}"
                    print(f"{i.id:<4} {teljes_nev:<20} {i.pozicio:<21} {i.telefonszam:<15} {i.email}")
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
                print(f'{'ID':<4} {'Név':<20} {'Születési Dátum':<16} {'Telefon':<15} {'Email':30} {'Lakcím':36} {'Felvétel Détuma':<20} {'Okmány sz.'} ')
                print('-' * 160)
                for i in self._orokbefogadok.read():
                    teljes_nev = f"{i.vezeteknev} {i.keresztnev}"
                    print(f"{i.id:<3} {teljes_nev:<20}  {i.szuletesi_datum:<16} {i.telefonszam:<15} {i.email:<30} {i.lakcim:<36} {i.felvetel_datuma:<20} {i.azonosito_okmany_szam} ")
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
            print('3. örökbefogadás indítása')
            print('0. Vissza')
            self._subchoice = int(input('Választás: '))

            match self._subchoice:
                case 1:
                    fejlec = (
                        f"{'ID':<4} {'Név':<20} {'Szül.Dátum':<12} {'Telefon':<14} {'Email':<25} {'Lakcím':<35} {'Okmány sz.':<20} | "
                        f"{'A.ID':<4} {'A.Név':<10} {'Ivar':<8} {'Súly':<6} {'Szín':<10} {'Chip':<15} {'Születesi idő':<12} {'Egészség'}"
                    )
                    print(fejlec)
                    print("-" * len(fejlec))

                    for i in self._allatok.orokbefogadott_allatok():
                        teljes_nev = f"{i[1].vezeteknev} {i[1].keresztnev}"
                        orokbefogado_resz = f"{i[1].id:<4} {teljes_nev:<20} {i[1].szuletesi_datum:<12} {i[1].telefonszam:<14} {i[1].email:<25} {i[1].lakcim:<35}  {i[1].azonosito_okmany_szam:<20}"
                        allat_resz = f"{i[0].id:<4} {i[0].nev:<10} {i[0].ivar:<8} {i[0].suly:<6} {i[0].szin:<10} {str(i[0].mikrochip_szam):<15} {i[0].szuletesi_ido:<12} {i[0].egeszsegi_allapot}"
                        print(f"{orokbefogado_resz} | {allat_resz}")
                case 2:
                    h = f'  {'ID':3} {'Név':10} {'Ivar':8} {'Súly':6} {'Szín':10} {'Ivartalanitva':4} \t {'Méret':9} {'Mikrochip száma':20} \t {'Születesi idő':12} \t {'Egészsegi állapot':20}'
                    print(h)
                    print("-" * (len(h) + 2))
                    for i in self._allatok.orokbefogadhato_allatok():
                        print(f'{i.id:3}   {i.nev:10} {i.ivar:7} {i.suly:6} {i.szin:10} {i.ivartalanitva:11} \t\t {i.meret:10} {str(i.mikrochip_szam):20} \t {str(i.szuletesi_ido):12} \t {i.egeszsegi_allapot:20}')
                case 3:
                    h = f'  {'ID':3} {'Név':10} {'Ivar':8} {'Súly':6} {'Szín':10} {'Ivartalanitva':4} \t {'Méret':9} {'Mikrochip száma':20} \t {'Születesi idő':12} \t {'Egészsegi állapot':20}'
                    print(h)
                    print("-" * (len(h) + 2))
                    for i in self._allatok.orokbefogadhato_allatok():
                        print(f'{i.id:3}   {i.nev:10} {i.ivar:7} {i.suly:6} {i.szin:10} {i.ivartalanitva:11} \t\t {i.meret:10} {str(i.mikrochip_szam):20} \t {str(i.szuletesi_ido):12} \t {i.egeszsegi_allapot:20}')
                    allatok_id = int(input("Adja meg az örökbe fogadni kívánt állat ID-ját: "))

                    print(f"{'ID':<4} {'Név':<20} {'Pozíció':<21} {'Telefon':<15} {'Email'}")
                    print("=" * 80)
                    for i in self._dolgozok.read():
                        teljes_nev = f"{i.vezeteknev} {i.keresztnev}"
                        print(f"{i.id:<4} {teljes_nev:<20} {i.pozicio:<21} {i.telefonszam:<15} {i.email}")
                    dolgozok_id = int(input("Adja meg a dolgozó ID-ját: "))

                    print(f'{'ID':<4} {'Név':<20} {'Születési Dátum':<16} {'Telefon':<15} {'Email':30} {'Lakcím':36} {'Felvétel Détuma':<20} {'Okmány sz.'} ')
                    print('-' * 160)
                    for i in self._orokbefogadok.read():
                        teljes_nev = f"{i.vezeteknev} {i.keresztnev}"
                        print(
                            f"{i.id:<3} {teljes_nev:<20}  {i.szuletesi_datum:<16} {i.telefonszam:<15} {i.email:<30} {i.lakcim:<36} {i.felvetel_datuma:<20} {i.azonosito_okmany_szam} ")
                    orokbefogadok_id = int(input("Adja meg az örökbefogadó ID-ját: "))

                    print(f"{'ID':<4} {'RefID':<6} {'IRSZ':<6} {'Város':<15} {'Utca':<25} {'Házszám'}")
                    print("-" * 70)
                    for i in self._telephelyek.read():
                        print(f"{i[0]:<4} {i[1]:<6} {i[2]:<6} {i[3]:<15} {i[4]:<25} {i[5]}")
                    telephelyek_id = int(input("Adja meg a telephely ID-ját: "))

                    i = self._allatok.orokbefogadas(allatok_id , dolgozok_id, orokbefogadok_id, telephelyek_id)
                    h = f'  {'ID':3} {'Név':10} {'Ivar':8} {'Súly':6} {'Szín':10} {'Ivartalanitva':4} \t {'Méret':9} {'Mikrochip száma':20} \t {'Születesi idő':12} \t {'Egészsegi állapot':20}'
                    print(h)
                    print("-" * (len(h) + 2))
                    print(f'{i.id:3}   {i.nev:10} {i.ivar:7} {i.suly:6} {i.szin:10} {i.ivartalanitva:11} \t\t {i.meret:10} {str(i.mikrochip_szam):20} \t {str(i.szuletesi_ido):12} \t {i.egeszsegi_allapot:20}')
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