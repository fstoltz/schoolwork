
import unittest

from person import Person
from staff import Staff
from student import Student
from program import Program
from school import School
from school_institution import SchoolInstitution, NotEnoughMoney
import interactive_utils


class TestPerson(unittest.TestCase):
    def test_person_01_constructor( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( str(p), "Person[name=Mark,address=Min Gata 1]" )

    def test_person_02_get_name( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( p.getName(), "Mark" )

    def test_person_03_get_address( self ):
        p = Person("Mark", "Min Gata 1")
        self.assertEqual( p.getAddress(), "Min Gata 1" )

    def test_person_04_set_address( self ):
        p = Person("Mark", "Min Gata 1")
        p.setAddress( "Annan Gata 2" )
        self.assertEqual( p.getAddress(), "Annan Gata 2" )


class TestStudent(unittest.TestCase):
    def test_student_01_constructor( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        sc1.addProgram(pr1)
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000, sc1.getSchoolName() )
        self.assertEqual( str(p), "Student[Person[name=Mark,address=Min Gata 1],program=IoT,year=17,fee=50000.00]" )

    def test_student_02_get_program( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        sc1.addProgram(pr1)
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000, sc1.getSchoolName() )
        self.assertEqual( p.getProgram(), "IoT" )

    def test_student_03_set_program( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        pr2 = Program("3D Design")
        sc1.addProgram(pr1)
        sc1.addProgram(pr2)
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000, sc1.getSchoolName() )
        p.setProgram( "3D Design" )
        self.assertEqual( p.getProgram(), "3D Design" )

    def test_student_04_get_year( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        sc1.addProgram(pr1)
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000, sc1.getSchoolName() )
        self.assertEqual( p.getYear(), 17 )

    def test_student_05_set_year( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        sc1.addProgram(pr1)
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000, sc1.getSchoolName() )
        p.setYear(16)
        self.assertEqual( p.getYear(), 16 )

    def test_student_06_get_fee( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        sc1.addProgram(pr1)
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000, sc1.getSchoolName() )
        self.assertEqual( p.getFee(), 50000 )

    def test_student_07_set_fee( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        sc1.addProgram(pr1)
        p = Student("Mark", "Min Gata 1", "IoT", 17, 50000, sc1.getSchoolName() )
        p.setFee( 125.66 )
        self.assertEqual( p.getFee(), 125.66 )


class TestStaff(unittest.TestCase):
    def test_staff_01_constructor( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( str(p), "Staff[Person[name=Mark,address=Min Gata 1],school=Nackademin,pay=50.00]" )

    def test_staff_02_get_school( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( p.getSchool(), "Nackademin" )

    def test_staff_03_set_school( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        p.setSchool( "Medieinstitutet" )
        self.assertEqual( p.getSchool(), "Medieinstitutet" )

    def test_staff_04_get_pay( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        self.assertEqual( p.getPay(), 50 )

    def test_staff_05_set_pay( self ):
        p = Staff("Mark", "Min Gata 1", "Nackademin", 50)
        p.setPay( 125.66 )
        self.assertEqual( p.getPay(), 125.66 )

class TestProgram(unittest.TestCase):
    def test_program_01_make_program( self ):
        pr1 = Program("IoT")
        self.assertEqual( pr1.getName(), "IoT")

    def test_program_02_make_program_add_students( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        sc1.addProgram(pr1)
        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)

        self.assertEqual(pr1.numberOfStudents(), 2)

    def test_program_03_get_students_nameList( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        sc1.addProgram(pr1)
        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)

        self.assertEqual(pr1.getAllStudentNames(), ['Fredrik', 'Per'])

class TestSchool(unittest.TestCase):
    def test_school_01_staff_totalPay( self ):

        sc1 = School("Nackademin")
        pr1 = Program("IoT")

        staff1 = Staff("Mark", "Karp 231", sc1, 10)
        staff2 = Staff("Carl", "Oskars 15", sc1, 10)
        staff3 = Staff("Jim", "As 32", sc1, 10)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        sc1.addStaff(staff3)


        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 10, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 10, sc1.getSchoolName() )
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)


        sc1.addProgram(pr1)

        self.assertEqual(sc1.getTotalStaffCost(), 30)
        self.assertEqual(sc1.profit(), -10)
        self.assertIsInstance(staff1, Staff)
        self.assertNotEqual(staff1, staff2)

    def test_school_02_program_students_total_fee( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")

        staff1 = Staff("Mark", "Karp 231", sc1, 25000)
        staff2 = Staff("Carl", "Oskars 15", sc1, 35000)
        staff3 = Staff("Jim", "As 32", sc1, 29000)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        sc1.addStaff(staff3)


        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)

        sc1.addProgram(pr1)
        sc1.changeStaffsPay("Mark", 5)

        self.assertEqual(pr1.getTotalIncome(), 95000)
        self.assertEqual(staff1.getPay(), 5)
        #Okej att testa såhär? Det är ju testfall. (använda protected attribut)
        self.assertIn(staff1, sc1._staff)
        self.assertIn(stud2, pr1._students)

    def test_school_03_Balance_school( self ):

        sc1 = School("Nackademin")
        pr1 = Program("IoT")

        staff1 = Staff("Mark", "Karp 231", sc1, 25000)
        staff2 = Staff("Carl", "Oskars 15", sc1, 35000)
        staff3 = Staff("Jim", "As 32", sc1, 29000)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        sc1.addStaff(staff3)


        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)

        sc1.addProgram(pr1)
        sc1.fireStaff("Mark")

        self.assertEqual(sc1.profit(), 31000.0)
        self.assertNotIn(staff1, sc1._staff)

    def test_school_04_no_Balance_school( self ):

        sc1 = School("Nackademin")
        pr1 = Program("IoT")

        staff1 = Staff("Mark", "Karp 231", sc1, 55000)
        staff2 = Staff("Carl", "Oskars 15", sc1, 35000)
        staff3 = Staff("Jim", "As 32", sc1, 45000)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        sc1.addStaff(staff3)


        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)

        sc1.addProgram(pr1)

        self.assertEqual(sc1.profit(), -40000.0)
        self.assertIn(pr1, sc1._programs)

    def test_school_05_as_string( self ):

        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        pr2 = Program("MoB")

        staff1 = Staff("Mark", "Karp 231", sc1, 55000)
        staff2 = Staff("Carl", "Oskars 15", sc1, 35000)
        staff3 = Staff("Jim", "As 32", sc1, 45000)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        sc1.addStaff(staff3)


        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)

        sc1.addProgram(pr1)
        sc1.addProgram(pr2)

        self.assertEqual(str(sc1), "School:Nackademin,\nPrograms:IoT MoB ,\nStaff:Mark Carl Jim ,\nSalaries:135000.0,\nProfit:-40000.0,\nBalance:5000000")

    def test_school_06_change_staff_salary( self ):
        sc1 = School("Nackademin")
        pr1 = Program("IoT")
        pr2 = Program("MoB")
        staff1 = Staff("Mark", "Karp 231", sc1, 55000)
        staff2 = Staff("Carl", "Oskars 15", sc1, 35000)
        staff3 = Staff("Jim", "As 32", sc1, 45000)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        sc1.addStaff(staff3)
        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)
        sc1.addProgram(pr1)
        sc1.addProgram(pr2)

        sc1.changeStaffsPay("Carl", 10000)

        self.assertEqual(str(sc1), "School:Nackademin,\nPrograms:IoT MoB ,\nStaff:Mark Carl Jim ,\nSalaries:110000.0,\nProfit:-15000.0,\nBalance:5000000")

    def test_school__07_change_staff_salary( self ):
            sc1 = School("Nackademin")
            pr1 = Program("IoT")
            pr2 = Program("MoB")
            staff1 = Staff("Mark", "Karp 231", sc1, 55000)
            staff2 = Staff("Carl", "Oskars 15", sc1, 35000)
            staff3 = Staff("Jim", "As 32", sc1, 45000)
            sc1.addStaff(staff1)
            sc1.addStaff(staff2)
            sc1.addStaff(staff3)
            stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
            stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
            pr1.addStudent(stud1)
            pr1.addStudent(stud2)
            sc1.addProgram(pr1)
            sc1.addProgram(pr2)
    
            sc1.changeStaffsPay("Carl", 10000)
    
            self.assertEqual(str(sc1), "School:Nackademin,\nPrograms:IoT MoB ,\nStaff:Mark Carl Jim ,\nSalaries:110000.0,\nProfit:-15000.0,\nBalance:5000000")

    def test_school__08_fire_staff_and_change_salary( self ):
            sc1 = School("Nackademin")
            pr1 = Program("IoT")
            pr2 = Program("MoB")
            staff1 = Staff("Mark", "Karp 231", sc1, 55000)
            staff2 = Staff("Carl", "Oskars 15", sc1, 35000)
            staff3 = Staff("Jim", "As 32", sc1, 45000)
            sc1.addStaff(staff1)
            sc1.addStaff(staff2)
            sc1.addStaff(staff3)
            stud1 = Student("Fredrik", "Malsta 236", pr1, 17, 40000, sc1.getSchoolName() )
            stud2 = Student("Per", "Korpet 32", pr1, 17, 55000, sc1.getSchoolName() )
            pr1.addStudent(stud1)
            pr1.addStudent(stud2)
            sc1.addProgram(pr1)
            sc1.addProgram(pr2)
    
            sc1.fireStaff("Carl")
            sc1.changeStaffsPay("Jim", 10)
    
            self.assertEqual(str(sc1), "School:Nackademin,\nPrograms:IoT MoB ,\nStaff:Mark Jim ,\nSalaries:55010.0,\nProfit:39990.0,\nBalance:5000000")

    def test_school_10_making_changes( self ):
            sc1 = School("Nackademin")
            pr1 = Program("IoT")
            pr2 = Program("MoB")
            staff1 = Staff("Mark", "Karp 231", sc1, 55000)
            staff2 = Staff("Carl", "Oskars 15", sc1, 35000)
            staff3 = Staff("Jim", "As 32", sc1, 45000)
            sc1.addStaff(staff1)
            sc1.addStaff(staff2)
            sc1.addStaff(staff3)
            stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 40000, sc1.getSchoolName() )
            stud2 = Student("Per", "Korpet 32", "IoT", 17, 55000, sc1.getSchoolName() )
            pr1.addStudent(stud1)
            pr1.addStudent(stud2)
            sc1.addProgram(pr1)
            sc1.addProgram(pr2)

            #self.assertEqual(,)

    def test_school_11_initial_balance( self ):
        sc1 = School("Hogwarts")
        self.assertEqual(sc1.getBalance(), 5000000)

class TestSchool_Institution(unittest.TestCase):
    def test_01_schoolInst_schools_list( self ):
        skolverket = SchoolInstitution()
        sc1 = School("Nackademin")
        skolverket.addSchool(sc1)
        self.assertIn(sc1, skolverket._schools)

    def test_02_schoolInst_terminate_school( self ):
        skolverket = SchoolInstitution()
        sc1 = School("Nackademin")
        skolverket.addSchool(sc1)
        skolverket.terminateSchool(sc1)
        self.assertEqual(sc1.getStatus(), False)

    def test_03_schoolInst_takeTaxMoney( self ):
        sc1 = School("Nackademin", 20000)
        staff1 = Staff("Mark", "Karp 231", sc1, 5000)
        staff2 = Staff("Carl", "Oskars 15", sc1, 5000)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 5000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 5000, sc1.getSchoolName() )
        pr1 = Program("IoT")
        pr2 = Program("MoB")
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)
        sc1.addProgram(pr1)
        sc1.addProgram(pr2)

        skolverket = SchoolInstitution()
        skolverket.addSchool(sc1)
        skolverket.takeTaxMoney(sc1)

        self.assertEqual(sc1.getBalance(), 14000)

        skolverket.takeTaxMoney(sc1)

        self.assertEqual(sc1.getBalance(), 8000)

        sc1.expelStudent("Fredrik")
        sc1.expelStudent("Per")

        skolverket.takeTaxMoney(sc1)

        self.assertEqual(sc1.getBalance(), 5000) 

    def test_04_schoolInst_mixed( self ):
        sc1 = School("Nackademin", 20000)
        staff1 = Staff("Mark", "Karp 231", sc1, 5000)
        staff2 = Staff("Carl", "Oskars 15", sc1, 5000)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 5000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 5000, sc1.getSchoolName() )
        pr1 = Program("IoT")
        pr2 = Program("MoB")
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)
        sc1.addProgram(pr1)
        sc1.addProgram(pr2)

        skolverket = SchoolInstitution()
        skolverket.addSchool(sc1)

        self.assertEqual(sc1.expelStudent("Paaazzdd"), "Not found")

        stud3 = Student("Paaazzdd", "123", "IoT", 17, 5000, sc1.getSchoolName() )
        pr1.addStudent(stud3)
        self.assertEqual(sc1.expelStudent("Paaazzdd"), "found")
        self.assertEqual(sc1.getTotalStaffCost(), 10000)

        sc1.fireStaff("Mark")
        self.assertNotIn(staff1, sc1._staff)
        self.assertEqual(sc1.getTotalStaffCost(), 5000)

        self.assertEqual(pr1.numberOfStudents(), 2)
        sc1.expelStudent("Fredrik")
        self.assertEqual(pr1.numberOfStudents(), 1)

        self.assertEqual(staff2.getPay(), 5000)
        sc1.changeStaffsPay("Carl", 3590)
        self.assertEqual(staff2.getPay(), 3590)

        self.assertEqual(sc1.getTaxSheet(), 8590) #<-- 3590 staff pay + 5000 fee for "Per" student


    def test_05_schoolInst_taxAbuse_and_mixed( self ):
        sc1 = School("Nackademin")
        staff1 = Staff("Mark", "Karp 231", sc1, 10000)
        staff2 = Staff("Carl", "Oskars 15", sc1, 10000)
        sc1.addStaff(staff1)
        sc1.addStaff(staff2)
        stud1 = Student("Fredrik", "Malsta 236", "IoT", 17, 5000, sc1.getSchoolName() )
        stud2 = Student("Per", "Korpet 32", "IoT", 17, 5000, sc1.getSchoolName() )
        pr1 = Program("IoT")
        pr2 = Program("MoB")
        pr1.addStudent(stud1)
        pr1.addStudent(stud2)
        sc1.addProgram(pr1)
        sc1.addProgram(pr2)

        skolverket = SchoolInstitution()
        skolverket.addSchool(sc1)

        self.assertEqual(sc1.getBalance(), 5000000)
        for _ in range(0,2000):
            skolverket.takeTaxMoney(sc1) #<-- Checking the robustness of takeTaxMoney
        self.assertEqual(sc1.getBalance(), 5000)

        self.assertEqual(sc1.profit(), -10000)

        stud3 = Student("Klas", "531", "IoT", 17, 15000, sc1.getSchoolName() )
        stud4 = Student("Jim", "9182", "IoT", 17, 15000, sc1.getSchoolName() )
        pr1.addStudent(stud3)
        pr1.addStudent(stud4)
        self.assertEqual(sc1.profit(), 20000)

        sc1.expelStudent("Fredrik")
        self.assertNotIn(stud1, pr1.getStudents())

        sc2 = School("Hogwarts")
        skolverket.addSchool(sc2)
        self.assertIn(sc2, skolverket._schools)

if __name__ == '__main__':
    unittest.main(verbosity=2)


