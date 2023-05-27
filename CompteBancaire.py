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
