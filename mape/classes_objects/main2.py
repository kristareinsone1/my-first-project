from datetime import datetime

class Employee:
    def __init__(self, id, name, surname, position):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.start_date = datetime.now()

    def full_name(self):
        return f"{self.name} {self.surname}"
    def initials(self):
        return f"{self.name[0]}.{self.surname[0]}."    

    def find_employee(employees, id):
        elf.id = id

employees = []

employees.append(Employee(34254, 'Anna', 'Henrihsone', 'Finanšu direktore'))
employees.append(Employee(45243, 'Oskars', 'Bērziņš', 'CTO'))
employees.append(Employee(64523, 'Ilze', 'Andersone', 'Programmētāja'))

for e in employees:
    print(f"{e.name} ({e.position}) - Start date: {e.start_date.timestamp()}")
    print(f"{e.full_name()} - {e.position}")
    print(f"Iniciāļi: {e.initials()}")