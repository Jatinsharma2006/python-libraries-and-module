#Creating module

"Module - is just a python file with extension .py that can be"
"executed independently(If contain__main__) or can be imported inside"
"another python program to reuse variable,function,and classed defined in module"

#IMP: during import we need to write import filename(without .py)

"steps to create module techdev.py"

#STEPS I: create a file techdev.py and type below code

company="TechDev"

def factorial(n):
    if n<=1: return 1
    else: return n*factorial(n-1)

def show():
    print("Welcome in TechDev")

def square(n):
    return n*n

class Fruit:
    def taste():
        print("Taste is Unknown")



#STEPS II: create another file myuser.py to import module techdev.py

import techdev     #Importing module

print("Factorial=",techdev.facorial(4))

print("Square=",techdev.square(3))

print("Company=",techdev.company)

techdev.show()














        

