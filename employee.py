"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

import abc
from abc import abstractmethod
from re import A
import re

class Employee:
    def __init__(self, name, salary, comission):
        self.name = name
        self.salary = salary
        self.comission = comission
    
    def getBasePay(self):
        if isinstance(self.salary, Salary):
            return self.salary.getTotalSalary()
        else:
            return 0;
    
    def getComissionDescription(self):
        if isinstance(self.comission, Commision):
            return self.comission.getDescription()
        else:
            return ""
    
    def getSalaryDescription(self):
        if isinstance(self.salary, Salary):
            return self.salary.getDescription()
        else:
            return ""

    def get_pay(self):
        totalPay = self.getBasePay()
        
        if isinstance(self.comission, Commision):
            totalPay += self.comission.getComissionPay()

        return totalPay

    def __str__(self):
        sDescription = self.getSalaryDescription()
        cDescription = self.getComissionDescription()
        return (self.name + sDescription + cDescription + ". Their total pay is " + str(self.get_pay()) + ".") 

class Salary(metaclass = abc.ABCMeta):
    def __init__(self, pay):
        self.pay = pay
    
    @abc.abstractmethod
    def getTotalSalary(self):
        pass
    
    @abc.abstractmethod
    def getDescription():
        pass

class MonthlySalary(Salary):
    def __init__(self, pay):
        super().__init__(pay)
        
    def getTotalSalary(self):
        return self.pay;
    
    def getDescription(self):
        return " works on a monthly salary of " + str(self.pay) + ""

class HourlySalary(Salary):
    def __init__(self, pay, hours):
        super().__init__(pay)
        self.hours = hours
    
    def getTotalSalary(self):
        return self.pay * self.hours
    
    def getDescription(self):
        return " works on a contract of " + str(self.hours) + " hours at " + str(self.pay) + "/hour"
    
class Commision:
    def __init__(self, pay):
        self.pay = pay
    
    def getComissionPay(self):
        return self.pay
    
    def getDescription(self):
        return " and receives a bonus commission of " + str(self.pay)

class ContractComission(Commision):
    def __init__(self, pay, contractNumbers):
        super().__init__(pay)
        self.contractNumbers = contractNumbers
    
    def getComissionPay(self):
        return self.pay * self.contractNumbers
    
    def getDescription(self):
        return " and receives a commission for " + str(self.contractNumbers) + " contract(s) at " + str(self.pay) + "/contract"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlySalary(4000), None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlySalary(25, 100), None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlySalary(3000), ContractComission(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlySalary(25, 150), ContractComission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlySalary(2000), Commision(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlySalary(30, 120), Commision(600))

# testing purposes
# empList = [ billie, charlie, renee, jan, robbie, ariel ]
# for emp in empList:
#    print(emp)