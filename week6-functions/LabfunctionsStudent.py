# Lab 6- Student management program
# break fucntions part down to smaller parts.
#  create a program that allows a user to
#create new students and to view students.
# Write a function that prints out a menu of commands we can perform, ie add,
#view and quit. The function should return what the user chose.


def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice

def getmodules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    while moduleName != "":
     module = {}
     module["name"]= moduleName            # I am not doing error handling
     module["grade"]=int(input("\t\tEnter grade:"))
     modules.append(module)                  # now read the next module name
     moduleName = input("\tEnter next module name (blank to quit) :").strip()

     return modules

def doAdd(students):
    student = {}
    student["name"] = input("Enter name :")
    student["modules"] = getmodules()
    students.append(student)

def doView(students):
  for student in students:
      print(student["name"])
      for module in student ["modules"]:
          print ("\t", module["name"],"\t:" module["grade"])



students = []                      #main program
choice = displayMenu()
while(choice != 'q'):          # we could do this with lamda functions# I am keeping this basic for the moment

 if choice == 'a':             
   doAdd(students)
 elif choice == 'v':
   doView(students)
 elif choice !='q':
   print("\n\nplease select either a,v or q")
 choice=displayMenu()
