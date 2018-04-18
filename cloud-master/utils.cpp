//utils.cpp
#include "utils.hpp"
#include <string>
#include <vector>
#include <iostream>

#define NO_VALUE 0
#define DEF_TEMP 19

#define ON 1
#define OFF 0

#define TEMP_UNIT 5
#define STAND_UNIT 10
#define ALL 15



//-----------------------------------------
//-----------------------------------------
//-----------------UNIT CLASS--------------
//-----------------------------------------
//-----------------------------------------

//Konstruktor
Unit::Unit(const std::string input_name, const int initial_status){
	name = input_name;
	status = initial_status;
}
//Destruktor
Unit::~Unit(){
	//tom konstruktor
}
//För temp sensorn konsturkotr
Unit::Unit(){

}
//Medlemsdefinitioner
void Unit::print_basic_info(){
	std::cout << "\nName: " << name << "\n" << "Status: " << status << std::endl;
	std::cout << "\n";
}

int Unit::get_status(){
	return status;
}

//-----------------------------------------
//-----------------------------------------
//-------------CLOUD CLASS-----------------
//-----------------------------------------
//-----------------------------------------

//Konstruktor
Cloud::Cloud(){

	unit_vec_PTR = &unit_vec;

	temp_vec_PTR = &temp_vec;

}
//Destruktor
//ingen destruktor
//Medlemsdefinitioner
int Cloud::menu(){

	/*get_unit_ptr and get_temp_ptr are memberfunctions to Cloud
	They return a pointer to each vector, which is what's needed
	to construct a Dashboard object*/
	Dashboard my_dash(get_unit_ptr(), get_temp_ptr());



		while(true){
			std::cout << "\n(1) Create new unit\n (2) Show all units\n  (3) Show all active units\n   (4) Dashboard\n"
			"    (5) Change Status\n     (6) Change Temp\n      (7) Remove Unit\n       (8) Exit Program\n";
			unsigned int user_input;
			std::cout << "\nSelect: ";
			std::cin >> user_input;
			std::cout << "\n\n";
			switch(user_input){
				case 1:
					std::cout << "\nWhat type of unit?\n\n(1) Standard Unit\n(2) Temperature Sensor\n";
					std::cout << "\nSelect: ";
					std::cin >> user_input;
					if(user_input == 1){
						create_unit();
					} else if(user_input == 2){
						create_temp_unit();
					}
					break;
				case 2:
					show_all(ALL);
					break;
				case 3:
					show_active_units();
					break;
				case 4:
					{
					my_dash.dash_panel();
					}
					break;
				case 5:
					//Ändra status på en enhet från PÅ/AV 1/0
					{
					show_all(ALL);
					std::string usr_inp_name;
					std::cout << "Enter name of unit you wish to switch on / off:\n";
					std::cin >> usr_inp_name;
	
					for(unsigned int i = 0; i < unit_vec.size(); i++){
						Unit &unit_ref = unit_vec[i];
						if(unit_ref.name == usr_inp_name){
							//Sätter PÅ om den är AV, Stänger AV om den är PÅ
							if(unit_ref.status == ON)
								unit_ref.status = OFF;
							else if(unit_ref.status == OFF)
								unit_ref.status = ON;
						}
					}


					for(unsigned int i = 0; i < temp_vec.size(); i++){
						Temp_unit &temp_ref = temp_vec[i];
						if(temp_ref.name == usr_inp_name){
							//Sätter PÅ om den är AV, Stänger AV om den är PÅ
							if(temp_ref.status == ON)
							temp_ref.status = OFF;
							else if(temp_ref.status == OFF)
							temp_ref.status = ON;
						}
					}

					std::cout << "\nSwitched status successfully.\n\n";

					}
					break;
				case 6:
					{
					//Kolla att vektorn inte är tom, om den är det, be user
					//att skapa en temp unit.
					if(temp_vec.size() != 0){

					std::cout << "Where do you want to change temperature?\n";

					int obj_in_vect;
					//show options
					for(unsigned int i = 0; i < temp_vec.size(); i++){
						int ID = 1;
						Temp_unit &temp_ref = temp_vec[i];
						std::cout << "ID: " << ID;
						temp_ref.print_location();
						temp_ref.print_current_temp();
						ID++;
					}
					std::cout << "\n\nSelect ID: ";
					std::cin >> obj_in_vect;

					//Skapar en temp referens, denna skickas sedan in till change_temp
					//Referensens värde avgörs av vilket obj user valde
					Temp_unit &temp_refer = temp_vec[obj_in_vect - 1];

					//Låt user mata in önskad temperatur
					int desired_temp;
					std::cout << "What is your desired temperature?\n";
					std::cout << "Select: ";
					std::cin >> desired_temp;


					change_temp(temp_refer, desired_temp);

					std::cout << "\nNew "; 
					temp_refer.print_current_temp();
					} else
						std::cout << "Please add a temp unit first...";
					}
					break;
				case 7:
					char user_option;
					std::cout << "(S)tandard Unit or (T)emperature Unit?\n";
					std::cin >> user_option;
					std::cout << "\n";

					int scenario;

					if(user_option == 'S')
						scenario = STAND_UNIT;
					else if(user_option == 'T')
						scenario = TEMP_UNIT;

					remove_unit(user_option, scenario);
					break;
				case 8:
					return 0;
				default:
					break;
		}
	}
}

void Cloud::create_unit(){
	std::string in_name;
	int ini_status;

	//Användaren matar in namnet för unit
	std::cout << "Enter name of unit: ";
	std::cin >> in_name;
	std::cout << std::endl;
	//Användaren matar in om enheten är på/av som start-värde
	std::cout << "Enter inital status (1/0, ON/OFF): ";
	std::cin >> ini_status;
	std::cout << std::endl;

	//Skapa ett nytt unit object med inmatad data
	Unit new_unit_obj(in_name, ini_status);
	//Lägg in nyskapade unit objektet i Clouds unit vektor
	unit_vec.push_back(new_unit_obj);
}

void Cloud::create_temp_unit(){
	std::string in_name;
	int ini_status = NO_VALUE;
	int max_temp = NO_VALUE; //No value is alias for 0 (just to have it initizaled)
	signed int min_temp = NO_VALUE; //minimum temperature
	int default_temp = DEF_TEMP; //default temp is 19
	std::string ini_location;


	//Användaren matar in namnet för unit
	std::cout << "Enter name of unit: ";
	std::cin >> in_name;
	std::cout << std::endl;
	//Användaren matar in om enheten är på/av som start-värde
	std::cout << "Enter inital status (1/0, ON/OFF): ";
	std::cin >> ini_status;
	std::cout << std::endl;

	//Användaren matar in temperatur-sensorns MAX-värde
	std::cout << "Enter MAX temp(celsius) for the sensor: ";
	std::cin >> max_temp;
	std::cout << std::endl;

	//Användaren matar in temperatur-sensorns MIN-värde
	std::cout << "Enter MIN temp(celsius) for the sensor: ";
	std::cin >> min_temp;
	std::cout << std::endl;

	//Användaren matar in platsen för temp-sensorn
	std::cout << "Enter location for the sensor: ";
	std::cin >> ini_location;
	std::cout << std::endl;

	//Skapa ett nytt unit object med inmatad data
	Temp_unit new_temp_obj(in_name, ini_status, max_temp, min_temp, default_temp, ini_location);
	//Lägg in nyskapade temp objektet i Clouds temp vektor
	temp_vec.push_back(new_temp_obj);
}


void Cloud::show_all(int scenario){
	//Stegar igenom varje obj i unit vectorn
	//och anropar print_basic_info inom varje obj.
	//Antal element i vektorn hämtas genom unit_vec.size()
	int ID = 1;

	if(scenario == STAND_UNIT){
		for(unsigned int i = 0; i < unit_vec.size(); i++){
			Unit &unit_ref = unit_vec[i];
			std::cout << "ID: " << ID;
			unit_ref.print_basic_info();
			ID++;
		}	
	}

	//Stegar igenom varje obj i temp vectorn
	//och anropar print_basic_info inom varje obj.
	//Antal element i vektorn hämtas genom temp_vec.size()
	if(scenario == TEMP_UNIT){
		for(unsigned int i = 0; i < temp_vec.size(); i++){
			Temp_unit &temp_ref = temp_vec[i];
			std::cout << "ID: " << ID;
			temp_ref.print_basic_info();
			ID++;
		}
	}

	if(scenario == ALL){
			for(unsigned int i = 0; i < temp_vec.size(); i++){
				Temp_unit &temp_ref = temp_vec[i];
				std::cout << "ID: " << ID;
				temp_ref.print_basic_info();
				ID++;
			}

			for(unsigned int i = 0; i < unit_vec.size(); i++){
				Unit &unit_ref = unit_vec[i];
				std::cout << "ID: " << ID;
				unit_ref.print_basic_info();
				ID++;
		}
	}
}

void Cloud::show_active_units(){
	for(unsigned int i = 0; i < unit_vec.size(); i++){
		Unit &unit_ref = unit_vec[i];
		//Om status är annat än 0, så är enheten "på".. Tänker mig att en enhet kan ha flera olika lägen. Typ standby kanske är 2 eller dylikt.
		if(unit_ref.get_status() != 0){
			unit_ref.print_basic_info();
		}
	}

	for(unsigned int i = 0; i < temp_vec.size(); i++){
		Temp_unit &temp_ref = temp_vec[i];
		//Om status är annat än 0, så är enheten "på".. Tänker mig att en enhet kan ha flera olika lägen. Typ standby kanske är 2 eller dylikt.
		if(temp_ref.get_status() != 0){
			temp_ref.print_basic_info();
		}
	}
}

void Cloud::remove_unit(const char option, const int scenario){

	//Visa alla enheter, med ID vid sidan av
	show_all(scenario);
	//Variablen som kommer hålla användarens inmatningsdata
	int user_input_remove = 0;
	std::cout << "Please enter ID of the unit you wish to remove...\n";
	std::cout << "Enter ID: ";
	std::cin >> user_input_remove;
	//Tar bort enheten användaren specifierat. 
	if (option == 'S' && unit_vec.size() >= 1){
		unit_vec.erase(unit_vec.begin()+user_input_remove - 1);
		std::cout << "\nRemove operation successfull.\n\n";
	}
	else if (option == 'T' && temp_vec.size() >= 1){
		temp_vec.erase(temp_vec.begin()+user_input_remove - 1);
		std::cout << "\nRemove operation successfull.\n\n";
	}
	else 
		std::cout << "\n\n#ERR# Your containers are empty. Please add units...\n\n";
}


void Cloud::change_temp(Temp_unit &tm_ref, const int new_val){
	tm_ref.current_temp = new_val;
}


std::vector<Unit>* Cloud::get_unit_ptr(){
	return unit_vec_PTR;
}

std::vector<Temp_unit>* Cloud::get_temp_ptr(){
	return temp_vec_PTR;
}



//-----------------------------------------
//----TEMP_SENS CLASS(derived from unit)-----
//-----------------------------------------

//Konstruktor
Temp_unit::Temp_unit(const std::string ini_name, const int ini_status, const int max, const signed int min, const int temp_now, const std::string ini_location){

	//name och status har ärvts ifrån Unit klassen
	name = ini_name;
	status = ini_status;

	max_temp = max;
	min_temp = min;
	current_temp = temp_now;
	location = ini_location;
}

void Temp_unit::print_current_temp(){
	std::cout << "Temp: " << current_temp << " degrees celsius\n";
	if(current_temp >= 40)
		std::cout << "-----> WARNING! Temp is high, potentially lethal <-----\n\n";
}


void Temp_unit::print_available_temp_range(){
	std::cout << "Temp range: " << min_temp << " to " << max_temp << "\n\n";
}

void Temp_unit::print_location(){
	std::cout << "\nLocation: " << location << "\n";
}









//-----------------------------------------
//------------DASHBOARD CLASS--------------
//-----------------------------------------

Dashboard::Dashboard(std::vector<Unit>* ptr_input_unit, std::vector<Temp_unit>* ptr_input_temp){
	//Nu är alltså dash_unit/temp_ptr en pekare till my_clouds unit/temp vektor
	dash_unit_ptr = ptr_input_unit;

	dash_temp_ptr = ptr_input_temp;
}


void Dashboard::dash_panel(){


	/*(right-hand side)I have to use *dash_unit_ptr because this is a 
	pointer to a pointer scenario. The content of unit/temp ptr 
	is in itself a pointer to the vectors in my_cloud.
	(left-hand side)Here I create references, which means these references will always
	be an alias for the vectors*/
	std::vector<Unit>& unit_vec_ref = *dash_unit_ptr;

	std::vector<Temp_unit>& temp_vec_ref = *dash_temp_ptr;

	std::cout << "############################\n";

	std::cout << "#      -DASHBOARD-         #\n";

	std::cout << "############################\n";

	//Prints the amount of standard and temp units
	//std::cout << unit_vec_ref.size();
	//std::cout << temp_vec_ref.size();


	for(unsigned int i = 0; i < unit_vec_ref.size(); i++){
		Unit &unit_ref = unit_vec_ref[i];
		unit_ref.print_basic_info();
		std::cout << "############################\n";
		std::cout << "############################\n";
	}	

	for(unsigned int i = 0; i < temp_vec_ref.size(); i++){
		Temp_unit &temp_ref = temp_vec_ref[i];
		//print_basic_info is inherited from the Unit class.
		temp_ref.print_basic_info();
		//Skriver ut vart temp-sensorn är placerad
		temp_ref.print_location(); 
		//Om enheten är påslagen, visa en temperaturläsning
		if(temp_ref.get_status() == 1)
			temp_ref.print_current_temp();
		//Skriv ut möjligt omfång för temperaturkomponenten
		temp_ref.print_available_temp_range();
		std::cout << "############################\n";
		std::cout << "############################\n";
	}	
	

}