

def doAdd(students):
    student = {}
    student["name"] = input("Enter name :")
    student["modules"] = getmodules()
    students.append(student)

def doView(students):
  for student in students:
      print(student["name"])
      for module in student ["modules"]:
        print ("\t", module["name"], "t:",

def displayModules(modules):
   print ("\tName \tGrade")
   for module in modules:
     print (f"\t module["name"]} \t{ module['grade']}")

