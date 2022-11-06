import repository.monitor_db as monitor_db
import models.employee as employee
from random import randint
from datetime import datetime, timedelta

user = employee.Employee("Jorge Luiz", 
        randint(27, 41),
        "Operador de Campo")

timestamp = datetime.now()

def generate_vitals():

        values = (
            user.name,
            randint(27,41),
            user.role,
            randint(70, 190),
            randint(9, 18),
            randint(6, 10),
            randint(-1, 1),
            timestamp.strftime("%Y/%m/%d %H:%M:%S"),
            1 if randint(1, 1000) > 800 else 0
        )
        monitor_db.insert(values)