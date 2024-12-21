# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
        
#     @classmethod
#     def from_hourly_wage(cls,name,hourly_wage,hours_per_week=40):
#         annual_salary=hourly_wage*hours_per_week*52
#         return cls(name,annual_salary)

# employee1=Employee('John Doe',80000)
# print(f"{employee1.name},Annual Salary :${employee1.salary}")

# employee2=Employee.from_hourly_wage('Jane Doe',15)
# print(f"{employee2.name},Annual Salary :${employee2.salary}")


# main.py

from views.account_ui import AccountUI

if __name__ == '__main__':
    account_ui = AccountUI()
    account_ui.start()
    # print