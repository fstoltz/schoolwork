# Inlämningsuppgift 1
Fredrik Stoltz, IoT17

**Development environment:**

Win 7, 64-bit

**Compiler:**

gcc 5.3.0 (MinGW)

**Software used:**

Sublime Text 3

cmd.exe
	
**Build instructions:**

```
git clone https://github.com/fstoltz/inlam1.git
cd inlam1
gcc main.c utils.c -o FredrikProgram
```

**Granskare**: 

John S & Hampa L

**Instruktioner för testning**

Efter kompilering & länkning, starta programmet i ett stort terminal fönster så att brädet syns tydligt. Mata sedan in 
```+``` följt av ```H``` för att ange att du vill ha en luftfuktighets-sensor, följt av ```4,7``` för ange kolumn 4, rad 7. Följt av ```3``` för att ange bredden på komponenten till 3. Programmet bör nu meddela att komponenten placerats på brädet, och du bör nu välja ```V``` för att visa brädet. 

För att ta bort komponeten, mata in ```-```, följt av ko-ordinaterna som komponeten sattes in på, nämligen ```4,7```. Följt av bredden, vilket i detta fall blir ```3```. Programmet meddelar sedan att komponten har tagits bort. Tryck på ```V``` för att verifiera att komponenten tagits bort.

Vid felaktig inmatning bör programmet inte godkänna datan, utan be användaren försöka igen. T.ex om användaren anger X / Y värden som är större än brädet, eller om det matas in en siffra när det förväntas ett tecken.


**Fördelar & nackdelar**

En fördel med koden är att den använder sig av egenskapade datastrukturer (structs) och därmed får programmet mer flexibilitet i termer av att expandera programmets funktioner. Pekare används vid funktionsanrop för att minska resurs-användning. Jag har försökt ge namn som antyder vad variabler representerar, så att läsare inte behöver försöka klura ut vilken variabel som håller respektive värde. I början trodde jag att det skulle behövas färre funktioner, men insåg under utveckling att det behövdes många fler & tycker fortfarande det finns lite väl stora funktioner som egentligen bör delas upp i mindre delar. Nackdelar jag ser är att programmets felhantering inte är särskilt bra, det finns grundläggande validering men fortfarande möjligt att krascha programmet genom felaktig inmatning. Vid vissa ställen använder jag lite väl många if-satser som möjligtvis kan göras på ett mer effektivt sätt.

Jag valde att kombinera en if-sats och en switch-sats som huvudmeny, vilket jag nu i efterhand inser kan orsaka problem, pga att jag har flertal ställen där programmet anropar självaste funktionen den är i, vilket jag förstått kan orsaka problem. En meny baserat på en while-loop och en switch-sats skulle kanske passa bättre. Samt skulle jag vilja ha ett mer intuitivt användargränsnitt, t.ex visa sifferordning på vänster sida i Y-ledet. 


