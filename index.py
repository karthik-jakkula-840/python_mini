class Employe:
    def __init__(self,name,Email,salary):
        self.name=name
        self.Email=Email
        self.salary=salary
system=[]

def Add_employe():
    name=input("enter Your name:")
    Email=input("enter your Email id:")
    salary=input("enter your salary:")
    system.append(Employe(name,Email,salary))
    print("-"*30)
    print("Employe added successfully !")
    print("-"*30)

def Show_employe():
    for i in system:
        print("-"*30)
        print("Employe name",i.name,"\nEmail:",i.Email,"\nsalary:",i.salary)
        print("-"*30)

def current_employe():
     user=input("Enter your name :")
     for i in system:
        if i.name==user:
         print("-"*30)
         print("yes its currently employe in our company")
         print("-"*30)
         break
     else:
            print("-"*30)
            print("sorry its not employe in our company")
            print("-"*30)

def high_salary_employe():
     high_salary="0"
     for i in system:
        if i.salary > high_salary:
            high_salary=i.salary
            print("-"*30)
     print("high salary  is:",i.name,high_salary)
     print("-"*30)

def monthly_salary():
    user=int(input("Enter your Anival_salary :"))
    monthly_salary=user/12
    print("-"*30)
    print(monthly_salary)
    print("-"*30)
def delete_emp():
   for e in system:
      name=input('enter your name:')
      system.remove(e)
      print("-"*30)
      print(name,'details removed sucessfully!!')
      print("-"*30)
def working_days_salary():
    name = input("Enter employee name: ")
    days = int(input("Enter number of days worked (out of 30): "))

    for i in system:
        if i.name == name:
            monthly_salary = float(i.salary)   
            per_day_salary = monthly_salary / 30
            final_salary = per_day_salary * days

            print("-"*30)
            print("Employee Name:", i.name)
            print("Days Worked:", days)
            print("Salary for working days:", final_salary)
            return

    print("Employee not found!")
    
    print("-"*30)

while True:
    print("1. Add_employe\n2.Show_employe\n3. current_employe\n4.high_salary_employe\n5.monthly_salary\n6.deleteemployee \n7.working_days_salary \n8.exit ") 
    choioc=int(input("entere your choise:"))
    if choioc == 1:
     Add_employe()
    elif choioc == 2:
      Show_employe()
    elif choioc == 3:
      current_employe()
    elif choioc == 4:
      high_salary_employe()   
    elif choioc == 5:
        monthly_salary()
    elif choioc == 6:
        delete_emp()
    elif choioc==7:
         working_days_salary()
    elif choioc==8:
        print("Exit sucessfully!! ")
        break