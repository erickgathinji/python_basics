#inheritance
#error handling
#dates

class Employee:
    def __init__(self, name, id_number, dob, gender):
        self.name = name
        self.id_number = id_number
        self.dob = dob
        self.gender = gender
    def print_details(self):
        print(f"Name: {self.name}\nID: {self.id_number}\nDOB: {self.dob}\nGender: {self.gender}")

class PermanentEmployee(Employee): #The employee in bracket is the inheritance
    def __init__(self, name, id_number, dob, gender, salary):
        super().__init__(name, id_number, dob, gender) #replaces typing the 4 self
        self.salary = salary
    def print_salary(self):
        print(f"Salary is {self.salary}")

class TemporaryEmployee(Employee):
