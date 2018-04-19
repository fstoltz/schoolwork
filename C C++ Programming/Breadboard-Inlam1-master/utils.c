/*DEFINITIONER*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <windows.h>
#include <conio.h>
#include "utils.h"



#define X_MAX 30	// LÄGGA TILL KONSTANTER FÖR ALLA FASTA VÄRDEN
#define Y_MAX 10 
#define ADD 1
#define REMOVE 0
#define true 1
#define false 0
#define pos_unavailable '-'


/*skapar myBoard ifrån breadboard strukten*/
struct breadboard myBoard; 

struct components LED, HUMI, OSC;  

myCoorStruct *pos_width_stru_ptr;  

int y = 0; //definierar position y till 0
int x = 0; //definierar position x till 0 

bool welcome_message = true;

char empty = '|';  //default tecken vid tom plats

char users_choice;




void default_board(){
	myBoard.pos[X_MAX][Y_MAX];

	int count = 0; 
	while (count < Y_MAX) {

		myBoard.pos[x][y] = empty; //sätt emptytecknet på x,y positionen
		y++; //flytta neråt ett steg
		count++; //öka count med 1
	}

	x++; //gå till nästa kolumn

	if (x <= X_MAX) {
		y = 0; //återställ y till plats 0
		default_board(); //börja på nästa kolumn
	}
}


void print_board(){ 		
	x = 0;
	y = 0;
	
	int utskrift_y_led = 1;
	/*---Skriver ut siffrorna ovanför i x-ledet-------*/
	for(int i = 1; i <= 9; i++)
		printf("  %d", i);
	for(int i = Y_MAX; i <= X_MAX; i++)
		printf(" %d", i);

	printf("\n");

	while (x < X_MAX){
		printf("  %c", myBoard.pos[x][y]);
		printf("");
		x++;

		if (x == X_MAX){
			/*--Utskrift i y-led. Vill egentligen ha denna på vänster sida. Men går inge bra. Bättre än inget.----*/
			printf(" %d", utskrift_y_led);
			utskrift_y_led++;
			printf("\n");
			y++;
			if (y < Y_MAX)
				x = 0;
		}
	}

}



void comp_config(){ 
	LED.symbol = 'L';
	strcpy(LED.name, "Light emitting diode");

	HUMI.symbol = 'H';
	strcpy(HUMI.name, "Humidity Sensor");

	OSC.symbol = 'Z';
	strcpy(OSC.name, "Crystal Oscillator");
}


void comp_menu(){
	printf("\n\tAvailable components listed below:\n\n"
		   "\t  (name)\t    (symbol)\n"
		   "\t- %s  (%c)\n\t- %s  (%c)\n\t- %s  (%c)\n\n", LED.name, LED.symbol, HUMI.name, HUMI.symbol, OSC.name, OSC.symbol);

}

/*Returnerar en char pekare*/
char* choose_component(){    

	char *ptr_users_choice;

	
	ptr_users_choice = &users_choice;
	

	printf("Please enter the symbol for desired component in capital letter...\n"
		   "\nSelect symbol: ");
	scanf("%c", &users_choice); //behöve ordna bättre validering.. skriver jag in 
								//flera tecken så fungerar inte valideringern korrekt.
								//skriver jag in enbart ETT tecken som är fel
								//så fungerar det.


	if 	(users_choice == LED.symbol ||
	 	 users_choice == HUMI.symbol ||
	  	 users_choice == OSC.symbol){
			return (ptr_users_choice); 
	} else {
		printf("\n\nChosen component does not exist. Please try again...\n");
		scanf("%*c"); 
		choose_component();
	}
}

/*Returnerar en pekare till en myCoorStruct datatyp*/
myCoorStruct* choose_coordinates(bool scenario){   

	myCoorStruct *position;

								/*12 bytes, 3 intar, 3 gånger 4 = 12*/
	position = malloc(sizeof(myCoorStruct));


	/*-------------------Remember to add free() where it's appropriate-----------------*/

	//Låt user mata in ko-ordinaterna
	printf("\n\nRange for X -> 1-%d\nRange for Y -> 1-%d\n"
		   "Ex. 4,7 for column 4, row 7\n", X_MAX, Y_MAX);
	if(scenario == ADD)
		printf("\nEnter desired co-ordinates: ");
	if (scenario == REMOVE)
		printf("\nEnter the initial co-ordinates for the component you wish to remove...\n"
			"Initial co-ordinates: ");
	//scanf("%*c");

	/*---same as writing (*position).x-------*/
	scanf("%d,", &position->x);
	scanf("%d", &position->y);
	
	if(scenario == ADD){
		printf("\nEnter width of component...\n"
			"Ex. 3 will give 3 empty spaces between the legs.\n"
			"Select width: ");
	}
	if(scenario == REMOVE){
		printf("\nEnter the width of the component you wish to remove\n"
			"Select width: ");
	}
	scanf("%d", &position->width);
	
	
	/*--------ADD SCENARIO BELOW-----------*/
	if(scenario == ADD){   /*--------------Validate input data------------*/
		if (position->x <= X_MAX && 
			position->y <= Y_MAX && 
			position->x >= 1 && 
			position->y >= 1 && 
			myBoard.pos[position->x - 1][position->y - 1] == empty &&
			position->width <= X_MAX && position->width >= 1){
			  /*Om den passerar ovanstående satser, returnera positionen*/
				return position;
		}
	}
	if(scenario == ADD)
	{				/*Meddela användaren ifall en komponent redan finns där*/
			if(	myBoard.pos[position->x - 1][position->y - 1] != empty)
				printf("\nYou've already placed a component there.\n");
			/*------------------------------------*/
			printf("\nPlease try again...\n\n");
			Sleep(1000);
			choose_coordinates(ADD); //ADD SCENARIO
	}
		/*--------REMOVE SCENARIO BELOW--------*/
	if (scenario == REMOVE &&
		position->x <= X_MAX &&
		position->y <= Y_MAX && 
		position->x >= 1 && 
		position->y >= 1 && 
		position->width >= 1 && 
		position->width <= X_MAX){
			return position;
	} else {
		printf("\nPlease try again...\n\n");
		Sleep(1000);
		choose_coordinates(REMOVE); //REMOVE SCENARIO
	}
		
}


void place_component(char *component, myCoorStruct *stru_point){

	int i = 1;

	/*Placera komponenten på vald plats*/
	myBoard.pos[stru_point->x - 1][stru_point->y - 1] = *component;

	myBoard.pos[stru_point->x + stru_point->width][stru_point->y - 1] = *component;

	/*Sätt ut bindestreck vid samtliga platser mellan positionerna*/
	while (stru_point->width > 0){
		myBoard.pos[stru_point->x + stru_point->width - i][stru_point->y - 1] = pos_unavailable;
		stru_point->width--;
	}

	free(stru_point);

	printf("\n\tComponent was successfully placed on the board.\n");
	Sleep(1000);

}


/*Tar bort en komponent*/
void remove_component(){
	/*Skapar en myCoorStruct pekare som kommer hålla relevanta värden för funktionen*/
	myCoorStruct *remove_pos;


	remove_pos = choose_coordinates(REMOVE); //REMOVE scenario


	/*Tar bort komponenten från vald plats*/
	myBoard.pos[remove_pos->x - 1][remove_pos->y - 1] = empty;
	myBoard.pos[remove_pos->x + remove_pos->width][remove_pos->y - 1] = empty;

	/*Tar bort bindestrecken*/
	int i = 1;
	while (remove_pos->width > 0){
		myBoard.pos[remove_pos->x + remove_pos->width - i][remove_pos->y - 1] = empty;
		remove_pos->width--;
	}


	printf("Component has been removed from the board.\n");
	free(remove_pos);
	Sleep(1000);
}



/*----MAIN MENU BELOW----*/

enum options user_option;

int main_menu(){

	if (welcome_message){
		printf("\n\t\t --- Welcome to this program. --- \n\n"
			"\tA breadboard has been created for you, sized %dx%d.\n"
			"\tOptions will be presented to you, choose and\n"
			"\thit enter!\n\n", X_MAX, Y_MAX);
		welcome_message = false;
		print_board();
	}

	char ettVal;

	printf("\n\t***MAIN MENU***\n");
	printf("\n\t  [OPTIONS]\n");
	printf("\t\n\tNew component:\t  +"
		   "\n\tView board:\t  V"
		   "\n\tRemove component: -"
		   "\t\n\tExit:\t\t  Q\n");


	printf("\nSelect option: ");
	scanf(" %c", &ettVal);
	scanf("%*c");


	if (ettVal == '+')		
		user_option = add;	
	else if (ettVal == '-') 
		user_option = delete_comp;
	else if (ettVal == 'V' || ettVal == 'v')
		user_option = view;
	else if (ettVal == 'Q' || ettVal == 'q')
		user_option = leave;
	else {
		printf("\aInvalid entry. Try again...\n");
		main_menu();
	}


	switch(user_option){
		case add:
			comp_menu();
			userInput_component = choose_component();
			pos_width_stru_ptr = choose_coordinates(ADD); 
			place_component(userInput_component, pos_width_stru_ptr);
			main_menu();
			break;
		case delete_comp:
			remove_component();
			main_menu();
			break;
		case view:
			print_board();
			main_menu();
			break;
		case leave:
			return (0);  //Exits the program
			break;
		default:
			main_menu();
			break;
	}

}
