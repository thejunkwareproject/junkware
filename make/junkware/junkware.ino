#include <LiquidCrystal.h>

LiquidCrystal lcd(2,3,4,5,6,7);

int dnaMotorPin = 12;
int dnaSwitchPin = 13;

int bluePin = 9;
int greenPin = 10;
int redPin = 11;

long start=0;
int sequencingDuration = 1000;

boolean DNAisReady = false;
boolean DNAstarted = false;
boolean DNAinit = false;
boolean DNAdone = false;

void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);

  pinMode(dnaSwitchPin, INPUT);

  pinMode(bluePin, OUTPUT);  
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);

  pinMode(dnaMotorPin, OUTPUT);
}

void resetBoard() {
  Serial.println("device init");
  DNAisReady = true;
  DNAstarted = false;
  DNAinit = false;
  DNAdone = false;
  digitalWrite(bluePin, LOW);
  digitalWrite(redPin, LOW);    
  digitalWrite(greenPin, LOW);
  lcd.clear();
}

void initBoard() {

  // init
  Serial.println("device init");
  lcd.clear();
  lcd.setCursor(0,1);
  lcd.print("Warming up...");

  // fake init behaviour
  for(int i=0; i<4; i++) {
    digitalWrite(bluePin, LOW);
    digitalWrite(dnaMotorPin, HIGH);
    delay(200);
    digitalWrite(bluePin, HIGH);
    digitalWrite(dnaMotorPin, LOW);
    delay(1000);
    digitalWrite(bluePin, LOW);
  }

}

void loop() {

  if( digitalRead(dnaSwitchPin)==LOW) {
    resetBoard();

    Serial.println("device is ready");

    lcd.setCursor(0,0);
    lcd.print("Waiting for order.");    
    digitalWrite(bluePin, HIGH);
    delay(1000);
    delay(1000); 
    DNAstarted = true;
    Serial.println("device start");

  }

  if (DNAisReady == true && DNAstarted == true) {

    if(DNAinit == false && DNAdone == false) {
      initBoard();
//      start = millis();
      DNAinit= true;
    } 
    else if (DNAinit == true && DNAdone == false) {

      Serial.println("device up");  
      digitalWrite(bluePin, LOW);
      digitalWrite(redPin, HIGH);
      digitalWrite(dnaMotorPin, HIGH);

      lcd.clear();
      loader();
      delay(sequencingDuration);
      DNAdone = true;

    }
    else {
      Serial.println("device done");  
      digitalWrite(dnaMotorPin, LOW);

      digitalWrite(redPin, LOW);
      digitalWrite(greenPin, HIGH);

      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("Test Done.");
      lcd.setCursor(0,1);
      lcd.print("Success !!");
    }
  }
}


void loader() {
  byte p20[8] = {
    B10000,
    B10000,
    B10000,
    B10000,
    B10000,
    B10000,
    B10000,
  };
  byte p40[8] = {
    B11000,
    B11000,
    B11000,
    B11000,
    B11000,
    B11000,
    B11000,
  };
  byte p60[8] = {
    B11100,
    B11100,
    B11100,
    B11100,
    B11100,
    B11100,
    B11100,
  };
  byte p80[8] = {
    B11110,
    B11110,
    B11110,
    B11110,
    B11110,
    B11110,
    B11110,
  };
  byte p100[8] = {
    B11111,
    B11111,
    B11111,
    B11111,
    B11111,
    B11111,
    B11111,
  };

  //Make progress characters
  lcd.createChar(0, p20);
  lcd.createChar(1, p40);
  lcd.createChar(2, p60);
  lcd.createChar(3, p80);
  lcd.createChar(4, p100);

  lcd.setCursor(0,0);
  lcd.print("Loading...");
  lcd.setCursor(0,1);
  lcd.print("                ");
  for (int i = 0; i<16; i++) {
    for (int j=0; j<5; j++) {
      lcd.setCursor(i, 1);   
      lcd.write(j);
      delay(100);
    } 
  }
}





