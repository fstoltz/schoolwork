from person import Person
from staff import Staff
from student import Student
from program import Program
from school import School


#######SETTING UP BASIC SCHOOL INFRASTRUCTRE###########

sc1 = School("Nackademin")
pr1 = Program("IoT")
pr2 = Program("3D Design")
sc1.addProgram(pr1)
sc1.addProgram(pr2)

staff1 = Staff("Mark", "Karp 231", sc1, 5000)
staff2 = Staff("Carl", "Oskars 15", sc1, 5000)

stud1 = Student("Fredrik", "Malsta 236", pr1, 17, 1500, sc1.getSchoolName() )
stud2 = Student("Per", "Korpet 32", pr1, 17, 1500, sc1.getSchoolName() )

stud3 = Student("Pelle", "Länne 55", pr2, 17, 1500, sc1.getSchoolName() )
stud4 = Student("Kevin", "Märsta 182", pr2, 17, 1500, sc1.getSchoolName() )

sc1.addStaff(staff1)
sc1.addStaff(staff2)

pr1.addStudent(stud1)
pr1.addStudent(stud2)

pr2.addStudent(stud3)
pr2.addStudent(stud4)

#####################################################
#####################################################

def chooseProgramToView():
		count = 1
		listOfPrograms = sc1.getProgramNameAsList()
		for item in listOfPrograms:
			print("{count}) {prog}".format(count=count, prog=item))
			count += 1
		print("\nSelect program: ", end="")	
		usrIn = int(input())
		if ( usrIn > len(listOfPrograms) ):
			print("Index out of range, please try again...")
			chooseProgramToView()
		elif (usrIn <= len(listOfPrograms)):
			return listOfPrograms[usrIn-1]

##############################################################
def chooseProgramToAddTo():
	programs = sc1.getPrograms()
	userChosenProgram = chooseProgramToView()
	for program in programs:
		if (program.getName() == userChosenProgram):
			return program

##############################################################
def createStudent(program):
	print("\nPlease enter the student name...")
	sName = str(input())
	print("\nPlease enter the student address...")
	sAddr = str(input())
	print("\nPlease enter the student year...")
	sYear = int(input())
	print("\nPlease enter the student fee...")
	sFee = int(input())
	return Student( sName, sAddr, program.getName(), sYear, sFee, sc1.getSchoolName() )

##############################################################
def viewStudentsForAProgram():
	print("\nWhich programmes' students do you wish to view?")
	userChosenProgram = chooseProgramToView()
	for program in sc1.getPrograms():
		if(program.getName() == userChosenProgram):
			print("\n---#### " + userChosenProgram + " student list ####---")
			print("Total number of students in programme: {numbStud}".format(numbStud=program.numberOfStudents()))
			print("Total fee for all students in programme: {fee}".format(fee=program.getTotalIncome()))
			print(program.getAllStudentNames())
			print("\n")

##############################################################
def createNewProgram():
	print("Please enter the name of the new program...\n")
	usrIn = input()
	sc1.addProgram( Program(usrIn) )
	print("\nAdding new program - {newProg} - to default school: {defSchool}\nFinishing...\n".format(newProg=usrIn, defSchool=sc1.getSchoolName()))

##############################################################
def staffInfo():
	print("\nTotal salary for staff: {totalSalary}".format(totalSalary=sc1.getTotalStaffCost()))
	print(sc1.getAllStaffName())
	print("\n")

##############################################################
def createNewStudent():
	#Let user choose what program to add the student to, then create the student
	print("\nWhich programme do you wish to add the student to?")
	program = chooseProgramToAddTo()			
	s = createStudent(program)
	program.addStudent( s )
	print("\n     Successfully added >{name}< to >{program}<\n".format(name=s.getName(), program=s.getProgram()))

##############################################################
def staffOperation(func, choice):
	if choice == "fireStaff":
		print("\n"+sc1.getAllStaffName())
		print("\nEnter name of staff to fire: ", end="")
		func(str(input()))
		#If there's no staff with that name, it will still print the line below..
		print("\n\tSuccessfull termination of employment.\n")
	elif choice == "changePay":
		print("\n"+sc1.getAllStaffName())
		print("\nEnter name of staff to change pay, followed by the new salary: ", end="")
		func( str(input()), int(input()))
		#If there's no staff with that name, it will still print the line below..
		print("\n\tSuccessfull change of salary.\n")

def displayMenu():
		print("-"*60)
		print("1) View School info\n2) View Programs\n3) View a Programs' students\n\t3.1) View all details for a student\n4) View Staff info\n\t4.1) Fire Staff"\
		"\n\t4.2 Change Pay for Teacher\n5) Add Program\n6) Add Student\n\t6.1) Expel Student\n\n\t\tRoot Access Operations Below(School Institution)\
		\n\t\t\t7) Tax School\n\t\t\t8) Terminate School\n\t\t\t9) Display All Schools"\
		"\n\t\t\t10) Register new School\n0) Exit")
		print("-"*60)
		print("Selection: ", end="")


##############################################################
def displayStudentInfo():
	print("\nEnter name of student: ", end="")
	nameOfStudent = str(input())
	for program in sc1.getPrograms():
		for student in program.getStudents():
			if (nameOfStudent == student.getName()):
				print(student.formattedString())
				return
	print("\nStudent not found.\n")
	return

	#Implementera try/expect med en raise "not found student" ist för if sats?
	#Låta user söka igen, eller gå till main menu?
