# stores utility funtions for students




def displayMenu():
 print("What would you like to do?")
 print("\t(a) Add new student")
 print("\t(v) View students")
 print("\t(q) Quit")
 choice = input("Type one letter (a/v/q):").strip()
 return choice

 def doAdd(students):
    student = {}
    student["name"] = input("Enter name :")
    student["modules"] = getmodules()
    students.append(student)

def readmodules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()

    while moduleName != "":
     module = {}
     module["name"]= moduleName            # I am not doing error handling
     module["grade"]=int(input("\t\tEnter grade:"))
     modules.append(module)                  # now read the next module name
     moduleName = input("\tEnter next module name (blank to quit) :").strip()

     
    return modules


def doView(students):
  for student in students:
      print(student["name"])
      for module in student ["modules"]:
          print ("\t", module["name"],"\t:" module["grade"])