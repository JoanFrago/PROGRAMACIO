const int speaker = 11;

int LENGTH = 400;
int notes[4] = {100, 350, 600, 850};
int gamepattern[20];
int difficulty = 1;

void setup() {
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, INPUT);

    pinMode(7, INPUT);
    pinMode(8, INPUT);
    pinMode(9, INPUT);

    Serial.begin(9600);
    }

void loop(){
    setPins(); // Set the LED and Button pins HIGH

    main_menu();
}

void main_menu(){
    while (1 == 1){
        if (digitalRead(6) == LOW){
            difficulty = 1;
            generate_game();
            play_game();
            }
        if (digitalRead(7) == LOW){
            difficulty = 2;
            generate_game();
            play_game();
            }
        if (digitalRead(8) == LOW){
            difficulty = 3;
            generate_game();
            play_game();
            }
        if (digitalRead(9) == LOW){
            difficulty = 4;
            generate_game();
            play_game();
            }
        }
    }

void setPins(){
    for (int i=2; i<10; i++){
        digitalWrite(i, HIGH);
        }
    }

void play_game(){
    int roundCount = 0;
    int playerTurn = 1;
    bool buttonPress = false;
    int currentNote;
    int userInput = 0;
    bool loss = false;
    play_note(1, 100);
    play_note(2, 100);
    play_note(3, 100);
    play_note(4, 100);
    delay(1000);
    for (int currentRound=1; (currentRound - 1)<=(difficulty * 5); currentRound++){ // Number of rounds to play
        roundCount += 1;

        playerTurn = 1;
        buttonPress = false;
        userInput = 0;
        for (int j = 1; j != currentRound; j++){
            play_note(gamepattern[j - 1], LENGTH);
            }
        while (playerTurn < currentRound){
            currentNote = gamepattern[playerTurn - 1];
            Serial.println(currentNote);
            while (buttonPress == false){
                if (digitalRead(6) == LOW){
                    buttonPress = true;
                    userInput = 1;
                    }
                if (digitalRead(7) == LOW){
                    buttonPress = true;
                    userInput = 2;
                    }
                if (digitalRead(8) == LOW){
                    buttonPress = true;
                    userInput = 3;
                    }
                if (digitalRead(9) == LOW){
                    buttonPress = true;
                    userInput = 4;
                    }
                if (buttonPress == true){
                    play_note(userInput, LENGTH);
                    if (currentNote == userInput){
                        playerTurn++;
                        }
                    else{ // You pushed the wrong one! :(
                        game_over(false);
                        }
                    }
                }
                buttonPress = false;
            }
        }
        if (loss == false){
            Serial.println("You Win!");
            game_over(true);
            }
    }

void generate_game() {
    randomSeed(analogRead(1));
    for (int i=0; i<(difficulty * 5); i++){ // For each level of difficulty, add 5 more turns to the game
        gamepattern[i] = random(1, 5);
}
}

void play_note(int index, int notespeed) {
    digitalWrite(index + 1, LOW);

    tone(speaker, notes[ index - 1 ], notespeed);
    delay(notespeed * 2);
    digitalWrite(index + 1, HIGH);

}

void game_over(bool win) {
    if (win) {
        Serial.println("You Win!");
        for (int i = 0; i < 10; i++){
        play_note(1, 50);
        play_note(2, 50);
        play_note(3, 50);
        play_note(4, 50);
}
}

    else {
        Serial.println("You Lose!");
        for (int i = 0; i < 6; i++){
    play_note(4, 100);
    play_note(3, 100);
    play_note(2, 100);
    play_note(1, 100);
}
}
Serial.println("Game over");
    main_menu();
}

void testButtons() // Created this function to test buttons without having to run the entire
    game
{

while (1 == 1){
    if (digitalRead(6) == LOW)
{
        Serial.println("Button 1 Pressed");
        play_note(1, LENGTH);
}
    if (digitalRead(7) == LOW)
{
        Serial.println("Button 2 Pressed");
        play_note(2, LENGTH);
}
    if (digitalRead(8) == LOW)
{
        Serial.println("Button 3 Pressed");
        play_note(3, LENGTH);
}
    if (digitalRead(9) == LOW)
{
        Serial.println("Button 4 Pressed");
        play_note(4, LENGTH);
}
}
}