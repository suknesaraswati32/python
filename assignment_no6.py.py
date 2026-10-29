class BankAccount:
      def __init__(self, account_holder):
          self.account_holder = account_holder
          self.account_number = self.generate_account_number()
          self.balance = 0.0
      def deposite(self,amount):
           if amount>0:
               self.balance+=amount
               print(amount,"deposited successfully.")
               
      def withdraw(self,amount):
          if amount<=0:
              print("Invalid withdrawal amount.")
          elif self.balance>=amount:
              self.balance-=amount
              print(amount,"withdrawn successfully.")
          else:
              print("Error: Insufficient funds.")
      def display_balance(self):
          print("Current Balance:",self.balance) 
      def transfer(self,amount,other_account):         
          if amount<=0:
              print("Invalid transfer amount.")
          elif self.balance>=amount:
              self.balance-=amount
              other_account.balance+=amount
              print(amount,"transferred successfully from",self.account_holder,"to",other_account.account_holder)
          else:
              print("Error: Insufficient funds for transfer.")
             
account1=BankAccount("Rahul")             
account1.deposite(10000)     
account1.display_balance()        



class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display_person_info(self):
    print("Name:",self.name)
    print("Age:",self.age)
  
class employee(person):
  def __init__(self,name,age,employee_id,salary):
    super().__init__(name,age)
    self.employee_id=employee_id
    self.salary=salary
    
  def display_employee_info(self):
    self.display_person_info()
    print("Employee ID:",self.employee_id)
    print("Salary:",self.salary)  
    
employee1=employee("sara",18,"2001",5000) 
employee1.display_employee_info()

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
    
  def display_person_info(self):
    print('Name:',self.name)
    print('Age:',self.age)  
    
    
class Employee(Person):
  def __init__(self,name,age,employee_id,salary):
    super().__init__(name,age)
    self.employee_id=employee_id
    self.salary=salary
  
  def display_employee_info(self):
    self.display_person_info()
    print('Employee ID:',self.employee_id)  
    print('Salary:',self.salary)    
        
class Manager(Employee):
     def __init__(self,name,age,employee_id,salary,department,team_size):
        super().__init__(name,age,employee_id,salary)
        self.department=department
        self.team_size=team_size
     def display_manager_info(self):
        self.display_employee_info()
        print('Department:',self.department)
        print('Team Size:',self.team_size)
        
Manager1=Manager('sara','18','2001',10000,'IT',5)     
Manager1.display_manager_info()