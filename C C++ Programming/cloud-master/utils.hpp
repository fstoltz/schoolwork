//utils.hpp
#include <string>
#include <vector>
#include <iostream>




//-----------------------------------------
//-----------------------------------------
//-------------UNIT CLASS------------------
//-----------------------------------------
//-----------------------------------------

class Unit
	{
	private:
		//tomt
		//Privata medlemmar
	protected:

	public:
		int status;
		std::string name;
		//Ändrade name från protected till public
		//för att kunna ändra på status, (5) i switch satsen
		//Konstruktor
		Unit(const std::string input_name, const int initial_status);
		Unit();
		//Destruktor
		~Unit();
		//Medlemsdeklarationer
		void print_basic_info();
		//Returnerar status värdet
		int get_status();
	};



//-----------------------------------------
//-----------------------------------------
//----TEMP_SENS CLASS(derived from unit)---
//-----------------------------------------
//-----------------------------------------

class Temp_unit: public Unit
	{
	private:
		//Privata medlemmar
		//här finns nu name & status(eller kanske ligger de i Publika delen?..)
		int max_temp;
		int min_temp;
		std::string location;
	public:
		int current_temp;
		//Konstruktor
		Temp_unit(const std::string ini_name, const int ini_status, const int max, const signed int min, const int temp_now, const std::string ini_location);
		//Medlemsdeklarationer
		/*här finns print_basic_info() get_status()
		ärvt ifrån Unit klassen*/
		void print_current_temp();
		void print_available_temp_range();
		void print_location();
	};






//-----------------------------------------
//-----------------------------------------
//-----------------CLOUD CLASS-------------
//-----------------------------------------
//-----------------------------------------


class Cloud
	{

	private:
		//Privata medlemmar
		std::vector<Unit> unit_vec;
		std::vector<Temp_unit> temp_vec;

		//Pekare till unit_vec, pekaren initieras i konstruktorn
		std::vector<Unit>* unit_vec_PTR;
		//Pekare till temp_vec, pekaren initieras i konstruktorn
		std::vector<Temp_unit>* temp_vec_PTR;
	public:
		//Konstruktor
		Cloud();
		//Destruktor

		//Medlemsdeklarationer
		void create_unit();
		void create_temp_unit();
		void show_all(int scenario);
		void show_active_units();
		int menu();
		void remove_unit(const char option, const int scenario);

		/*Här vill jag ta ett specifikt objekt ifrån
		temp vektorn och ändra på dens current_temp varibel*/
		void change_temp(Temp_unit &tm_ref, const int new_val);

		/*Dashboard funktionalitet under här, returnerar pekare till
		vektorerna*/
		std::vector<Unit>* get_unit_ptr();

		std::vector<Temp_unit>* get_temp_ptr();


	};








//-----------------------------------------
//-----------------------------------------
//------------DASHBOARD CLASS--------------
//-----------------------------------------
//-----------------------------------------

/*Denna klass ska ha tillgång till my_clouds vektorer*/

class Dashboard
	{

	private:
		std::vector<Unit>* dash_unit_ptr;
		std::vector<Temp_unit>* dash_temp_ptr;
	protected:

	public:
		//Konstruktor
		Dashboard(std::vector<Unit>*, std::vector<Temp_unit>*);

		//Medlemsfunktioner
		void dash_panel();

	};










