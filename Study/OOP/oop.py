import datetime


# Python OOP
class Employee:

    raise_amount = 1.04
    nums_of_emps = 0

    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = f"{firstname}.{lastname}@shatteredrealms.com"
        Employee.nums_of_emps += 1

    @classmethod
    def from_string(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Vasya", "Pupkin", 60000)
emp_2 = Employee("Masha", "Ivanova", 60000)
emp_3 = Employee("Test", "User", 1)

# my_date = datetime.date(2022, 1, 17)
#
# print(Employee.is_workday(my_date))


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, list_of_emps=None):
        super().__init__(first, last, pay)
        if list_of_emps is None:
            self.list_of_emps = []
        else:
            self.list_of_emps = list_of_emps

    def add_emp(self, emp):
        if emp not in self.list_of_emps:
            self.list_of_emps.append(emp)

    def remove_emp(self, emp):
        if emp not in self.list_of_emps:
            raise Exception("This employee is not in a list")
        self.list_of_emps.remove(emp)

    def display_emps(self):
        for emp in self.list_of_emps:
            print("-->", emp.fullname())


dev_1 = Developer("Vasya", "Pupkin", 60000, "C#")
dev_2 = Developer("Masha", "Ivanova", 60000, "Python")

mgr_1 = Manager("Artem", "Dreyer", 100000, [dev_1, dev_2])

print(mgr_1.fullname())
mgr_1.display_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))



