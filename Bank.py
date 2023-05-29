from datetime import *
import time


# fonction pour convertir en datetime ----------------------------------------------------
# function to convert to datetime ----------------------------------------------------
def ToDate(self, vdate: str | date | datetime) -> datetime:
    if isinstance(vdate, date) or isinstance(vdate, datetime):
        d = vdate
    elif isinstance(vdate, str):
        vdate.replace("/", "-")
        d = datetime.strptime(vdate, "%Y-%m-%d %H:%M:%S")
    else:
        d = None
    return d

# ----------------------------------------------------
# classe Operation
# class Operation
class Operation:
    # les attributs -------------------------------------------------------------
    # attributes -------------------------------------------------------------
    __auto = __nOperation = 0
    __dateOperation = __dateValidation = None
    __typeOp = 0
    __modeOp = ""
    __montant = 0.0
    __libelle = ""
    __lesTypeOp = [-1, 1]
    __lesModeOp = ["E", "C", "V", "T", "G", "A", "P"]

    # le constructeur -------------------------------------------------------------
    # constructor -------------------------------------------------------------
    def __init__(self, typeOp: int, modeOp: str, montant: float, libelle: str):
        Operation.__auto += 1
        self.__nOperation = Operation.__auto
        self.DateOperation = datetime.now()
        self.DateValidation = datetime.now()
        self.TypeOp = typeOp
        self.ModeOp = modeOp
        self.Montant = montant
        self.Libelle = libelle
        self.__lesTypeOp = [-1, 1]
        self.__lesModeOp = ["E", "C", "V", "T", "G", "A", "P"]
        # self.__lesTypeOp = dict{-1:"Retrait", 1:"Depos"}
        # self.__lesModeOp = dict{"E":"Espèce", "C":"Chèque", "V":"Virement", "T":"Transfer", "G":"Guichet", "A":"Agios", "P":"Prélévement"}

        
    # les proprietes
    # Properties
    @property
    def NOperation(self) -> int:
        return self.__nOperation

    @property
    def DateOperation(self) -> datetime:
        return self.__dateOperation

    @DateOperation.setter
    def DateOperation(self, value: str | date | datetime):
        self.__dateOperation = ToDate(self, value)

    @property
    def DateValidation(self) -> datetime:
        return self.__dateValidation

    @DateValidation.setter
    def DateValidation(self, value: str | date | datetime):
        if value is None:
            self.__dateValidation = value
        elif (ToDate(self, value) - (self.DateOperation)).days >= 0:
            self.__dateValidation = ToDate(self, value)
        else:
            raise Exception(f"Validation de l'opération impossible, Date de validation : {ToDate(value)} "
                            f"est antérieure à la date de l'opération : {self.DateOperation}")

    @property
    def TypeOp(self) -> int:
        return self.__typeOp

    @TypeOp.setter
    def TypeOp(self, value: int):
        if value in self.__lesTypeOp:
            self.__typeOp = value
        else:
            raise Exception(f"Type de l'opération invalide; valeur : {value}; les valeurs valides : {self.__lesTypeOp}")

    @property
    def ModeOp(self) -> str:
        return self.__modeOp

    @ModeOp.setter
    def ModeOp(self, value: str):
        if value.upper() in self.__lesModeOp:
            self.__modeOp = value.upper()
        else:
            raise Exception(f"Type de l'opération invalide; valeur : {value}; les valeurs valides : {self.__lesModeOp}")

    @property
    def Montant(self) -> float:
        return self.__montant

    @Montant.setter
    def Montant(self, value: float | int):
        if value > 0:
            self.__montant = value
        else:
            raise Exception(f"Montant de l'opération invalide; valeur : {value}")

    @property
    def Libelle(self) -> str:
        return self.__libelle

    @Libelle.setter
    def Libelle(self, value: str):
        if value != "" and value is not None:
            self.__libelle = value
        else:
            raise Exception("Libelle invalide, donner un libelle à l'opération")
     
    
    # Les methodes -------------------------------------------------------------
    # Methods  -------------------------------------------------------------
    def Valider(self, cls, dateValidation: str | date | datetime):
        if isinstance(ToDate(self, dateValidation), datetime):
            self.DateValidation = dateValidation
            # cls.Solde += (self.Montant * self.TypeOp)
        else:
            print("Date validation invalide")
            self.DateValidation = None

    def __str__(self) -> str:
        return f"{self.NOperation:3} ; " \
               f"{self.DateOperation.strftime('%m-%d-%Y %H:%M:%S')} ; " \
               f"{self.DateValidation.strftime('%m-%d-%Y %H:%M:%S')} ; " \
               f"{self.Libelle:50} ; " \
               f"{(self.Montant * self.TypeOp):12.2f} ; " \
               f"{self.TypeOp:2} ; " \
               f"{self.ModeOp}"


# ----------------------------------------------------
# classe Compte
# compte class
class Compte:
    __auto = __nCompte = 0
    __titulaire = ""
    __dateCreation = __dateCloture = __dateAgios = None
    __lesOperation = []
    __solde = 0
    __tauxAgios = 1.5

    @property
    def NCompte(self) -> int:
        return self.__nCompte

    @property
    def Titulaire(self) -> str:
        return self.__titulaire

    @Titulaire.setter
    def Titulaire(self, value: str):
        self.__titulaire = value

    @property
    def Solde(self) -> float:
        return self.__solde

    @Solde.setter
    def Solde(self, value: float | int):
        self.__solde = value
