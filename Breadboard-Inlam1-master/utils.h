
/*DEKLARATIONER*/

char *userInput_component;

char empty;


/*------Message that gets displayed only once, when the user starts the program--------*/
int welcome_message;



typedef int bool;

struct components { 
	char name[50];
	char symbol;
};

struct breadboard {
	char pos[100][100]; 
};

typedef struct coordinates {   
	int x;
	int y;
	int width;
} myCoorStruct;


void default_board();

void print_board();

void comp_config(); 

void comp_menu();

/*Returnerar en char pekare*/
char* choose_component();

/*Returnerar en pekare till en myCoorStruct datatyp*/			
myCoorStruct* choose_coordinates(bool scenario);

			/*argument funktionen tar är en char pekare, och en myCoorStruct pekare*/
void place_component(char *component, myCoorStruct *stru_point);

/*Tar bort en komponent*/
void remove_component();

int main_menu();

enum options {
	add = 0,
	delete_comp = 10,
	view = 20,
	leave = 30
};
