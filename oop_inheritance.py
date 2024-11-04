#inheritance
#error handling
#dates
from datetime import datetime, date


class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob = dob
        self.gender = gender
        date_of_birth = datetime.strptime(dob, "%Y-%m-%d") #2024-11-4
        self.age = date.today().year - date_of_birth.year

    def print_details(self):
        print(f"Name: {self.name}\nID: {self.id_number}\nDOB: {self.dob}\nGender: {self.gender}\nAge: {self.age}")

class PermanentEmployee(Employee): #The employee in bracket is the inheritance
    def __init__(self, name, id_number, dob, gender, salary):
        super().__init__(name, id_number, dob, gender) #replaces typing the 4 self
        self.salary = salary

    def print_salary(self):
        print(f"Salary is {self.salary}")

    def print_details(self): #override - because we added the salary part
        super().print_details()
        print(f"Salary is {self.salary}")

class TemporaryEmployee(Employee):
    def __init__(self, name, id_number, dob, gender, hourly_pay, end_date):
        super().__init__(name, id_number, dob, gender)  # replaces typing the 4 self
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"Hourly payment is {self.hourly_pay}")

    def print_end_date(self):
        print(f"End date is {self.end_date}")

#make sure the dob format is strictly as defined in employee - Y-m-d
p1 = PermanentEmployee ('John Kim', '43768374', '1999-12-2', 'M', 10000)
p1.print_details()
p1.print_salary()

t1 = TemporaryEmployee ('Sam Kim', '8779879', '1956-12-2', 'M', 1000, '31/12/2026')
t1.print_details()


