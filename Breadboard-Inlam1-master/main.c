/*Program för att modellera ett breadboard, samt hantera komponenterna på det*/
					/*Fredrik Stoltz, IoT17, 2017-09*/


/*Preprocessor directives*/

#include "utils.h"
extern struct breadboard myBoard;
extern struct coordinates pozz; 


/*Start of program*/
int main() {

		/*SETUP*/
/*----------------------------*/
	default_board();
	comp_config();
/*----------------------------*/
	  /*END OF SETUP*/


		/*MAIN MENU*/
/*-------------------------*/
	main_menu();  /*Användaren kan här välja mellan att skriva ut brädet,
					lägga till en komponent, ta bort en komponent, eller
					rensa hela brädet, eller avsluta/lämna programmet
					Denna loop bör köras om & om igen tills användaren väljer
					att avsluta programmet.*/
	return (0);
}
