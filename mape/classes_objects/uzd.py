
from datetime import datetime


class Employee:
    def __init__(self, id, name, surname, position, start_date=None, salary=1000):
        self.id = id
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary

        if start_date == None:
            self.start_date = datetime.now()
        else:
            self.start_date = start_date

    def full_name(self):
        return f"{self.name} {self.surname}"

    def change_position(self, new_position):
        self.position = new_position
        print(f"Changed the position of {self.full_name()} to {new_position}")

    def days_employed(self):
        return (datetime.now() - self.start_date).days

    def years_employed(self):
        return self.days_employed() // 365

    def raise_salary(self, percent):
        self.salary = self.salary + self.salary * percent / 100

    def __str__(self):
        return f"{self.full_name()}, {self.position}, alga: {self.salary:.2f} EUR"


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(self.name, "departamentā strādā:")
        for e in self.employees:
            print(e.full_name())

    def total_salary(self):
        total = 0
        for e in self.employees:
            total += e.salary
        return total


def find_employee(employees, id):
    for e in employees:
        if e.id == id:
            print("Atrasts:", e.full_name())
            return e
    print("Darbinieks nav atrasts!")
    return None


employees = []

employees.append(Employee(34254, 'Anna', 'Henrihsone', 'Finanšu direktore', datetime(2018, 3, 15), 3000))
employees.append(Employee(45243, 'Oskars', 'Bērziņš', 'CTO', datetime(2020, 5, 10), 4000))
employees.append(Employee(64523, 'Ilze', 'Andersone', 'Programmētāja', datetime(2022, 8, 20), 2500))
employees.append(Employee(98765, 'Intars', 'Rozentāls', 'Atbalsta speciālists', datetime(2024, 1, 15), 1800))


departments = []
departments.append(Department("Marketinga"))
departments.append(Department("Finanšu"))
departments.append(Department("Klientu atbalsta"))


departments[0].add_employee(employees[1])
departments[0].add_employee(employees[2])
departments[1].add_employee(employees[0])
departments[2].add_employee(employees[3])


find_employee(employees, 64523).change_position("Vecākā Programmētāja")

print("*" * 50)

for d in departments:
    d.show_employees()

print("*" * 50)

for e in employees:
    print(e.full_name(), "strādā", e.days_employed(), "dienas")
    print("Gadi:", e.years_employed())

print("*" * 50)

employees[2].raise_salary(15)

total = 0

for e in employees:
    total = total + e.salary

print("Visu algu summa:", total, "EUR")
print("Vidējā alga:", total / len(employees), "EUR")

highest = employees[0]

for e in employees:
    if e.salary > highest.salary:
        highest = e

print("Lielākā alga:", highest)

for d in departments:
    print(d.name, "algas summa:", d.total_salary(), "EUR")
