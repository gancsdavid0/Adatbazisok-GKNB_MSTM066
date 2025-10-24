from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def getByID(self, id):
        """Lekérdezi ID alapján"""
        pass

    @abstractmethod
    def create(self, id):
        """Létrehozol egy új rekordot"""
        pass

    @abstractmethod
    def read(self):
        """Lekérdezi az összes rekordot"""
        pass


    @abstractmethod
    def update(self, id):
        """Módosítasz ID alapján"""
        pass

    @abstractmethod
    def delete(self, id):
        """Törölsz id alapján"""
        pass
