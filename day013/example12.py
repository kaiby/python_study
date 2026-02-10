"""
example12 - 

Author: kaiby
Date: 2024/1/10 17:22
"""
from abc import abstractmethod


class Employee:

    def __init__(self, name, no):
        self.name = name
        self.no = no

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def get_salary(self):
        return 15000


class Programmer(Employee):

    def __init__(self,name, no):
        super().__init__(name, no)
        self.hours = 0

    def get_salary(self):
        return 200 * self.hours


class SalesPerson(Employee):

    def __init__(self,name, no):
        super().__init__(name, no)
        self.sales = 0

    def get_salary(self):
        return 1800 + self.sales * 0.05


def main():
    manager = Manager("Tom", '001')
    print(manager.get_salary())
    programer = Programmer('Jerry', '002')
    programer.hours = 2.5
    print(programer.get_salary())
    sales_person = SalesPerson('Lily', '003')
    sales_person.sales = 8000
    print(sales_person.get_salary())


if __name__ == '__main__':
    main()
