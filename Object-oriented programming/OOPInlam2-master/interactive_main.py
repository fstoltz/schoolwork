
import interactive_utils
from school_institution import SchoolInstitution

skolverket = SchoolInstitution()

skolverket.addSchool(interactive_utils.sc1)

def main_menu():
	print("\nWelcome to your School System™\n"\
		"A basic school infrastructure has been generated automatically for you...\n")
	while True:

		interactive_utils.displayMenu()

		try:
			usrIn = float(input())
		except ValueError:
			print("\n\n>------- INVALID INPUT -------<\n\n")
			usrIn = None

		if(usrIn == 1.0):
			print("\n")
			print(interactive_utils.sc1)
			print("\n")
		elif(usrIn == 2.0):
			print("\n")
			print(interactive_utils.sc1.getProgramsName())
			print("\n")
		elif(usrIn == 3.0):
			interactive_utils.viewStudentsForAProgram()
		elif(usrIn == 3.1):
			interactive_utils.displayStudentInfo()
		elif(usrIn == 4.0):
			interactive_utils.staffInfo()
		elif(usrIn == 4.1):
			interactive_utils.staffOperation(interactive_utils.sc1.fireStaff, "fireStaff")
		elif(usrIn == 4.2):
			interactive_utils.staffOperation(interactive_utils.sc1.changeStaffsPay, "changePay")
		elif(usrIn == 5.0):
			interactive_utils.createNewProgram()
		elif(usrIn == 6.0):
			interactive_utils.createNewStudent()
		elif(usrIn == 6.1):
			print("\nEnter student name to expel: ", end="")
			interactive_utils.sc1.expelStudent( str(input()) )
		elif(usrIn == 7.0):
			print("\nRequesting tax sheet...")
			skolverket.takeTaxMoney(interactive_utils.sc1)
			print("Processed tax for school: {school}\n".format(school=interactive_utils.sc1.getSchoolName()))
			#print the new balance for the school???
		elif(usrIn == 8.0):
			skolverket.terminateSchool(interactive_utils.sc1)
		elif(usrIn == 9.0):
			skolverket.displayAllSchools()
		elif(usrIn == 10.0):
			skolverket.createNewSchool()
		elif(usrIn == 0.0):
			#Exits program
			return False
		else:
			pass



#####################
#      Start        # 
#####################

main_menu()