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
