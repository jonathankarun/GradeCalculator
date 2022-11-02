#Setup

grades = []
going = True
add = 0
total = 0

#Introduction

print("Welcome to Jonathan's Grade Calculator!")

#Get the user's grades

sclass = ""
sclass = input("First, What class do you want to calculate your grades for?: ")
print("")
print("Great! Next, we need to get the grades you currently have in " + sclass)
print("Please enter them in sequential order. When done, enter \"Done\".")
print("")
while going == True:
    add = input("Grade: ")
    if add == "Done":
        break
    else:
        if not add.isdigit():
            print()
            print("Uh oh, You can only input digits. Try again!")
            print()
        else:
            grades.append(add)
            total += int(add)
        
      
#Ask how many more assignments are in the grading period

print("")
more = int(input("Now, how many more grades are going to be taken in the grading period: "))

#Ask the user what grade they want

wanted = float(input("Now, what grade do you want to achieve in the class?: "))

#Return what they need to average on remaining assignments for that grade
            
avg = total / len(grades)
gradestring = ", ".join(grades)

found = False
needed = 0
num = 0
while found == False:
    if wanted <= (avg * len(grades) + num * more) / (len(grades) + more):
        needed = num
        found = True
    else:
        num += 1
        
            

print("")
print("Here is a list of your current grades in " + sclass + ": " + gradestring)
print("Your grade in " + sclass + " is currently a(n) " + str(avg) + ".")
print("To achieve a(n) " + str(wanted) + ", you are going to need an average grade of at least a(n) " + str(needed) + " on all future assignments.")
if needed > 100:
    print("Meeting this requirement may be tricky. Try asking your teacher for some extra credit.")
