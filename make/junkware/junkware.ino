#include <LiquidCrystal.h>

LiquidCrystal lcd(2,3,4,5,6,7);

int dnaMotorPin = 12;
int dnaSwitchPin = 13;

int bluePin = 10;
int greenPin = 11;
int redPin = 10;

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
  
  initBoard();
}

void initBoard() {

  // init
  Serial.println("device reset");
  DNAisReady = false;
  DNAstarted = false;
  DNAinit = false;
  DNAdone = false;

  digitalWrite(bluePin, LOW);
  digitalWrite(redPin, LOW);    
  digitalWrite(greenPin, LOW);
  lcd.clear();

  //
  Serial.println("Device init");
  lcd.clear();
  lcd.setCursor(0,1);
  lcd.print("Warming up...");

  // fake init behaviour
  for(int i=0; i<4; i++) {
    digitalWrite(bluePin, LOW);
    digitalWrite(dnaMotorPin, HIGH);
    delay(200);
    digitalWrite(redPin, HIGH);
    digitalWrite(dnaMotorPin, LOW);
    delay(1000);
    digitalWrite(redPin, LOW);
  }
  Serial.println("device is ready");
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Device Ready.");
    digitalWrite(redPin, HIGH);
}

void loop() {
//  Serial.println(digitalRead(dnaSwitchPin));
  /*
  if( digitalRead(dnaSwitchPin)==LOW) {
    delay(1000); 
    initBoard();
    lcd.setCursor(0,0);
    lcd.print("Waiting for order.");    
    digitalWrite(bluePin, HIGH);
    DNAisReady = true;
    Serial.println("device is ready");
    delay(1000);
  } 
  */

  if (Serial.available()) {
    char order = Serial.read();
    Serial.println(order);
    if(order == 'I') { // && DNAisReady == true) {
      Serial.println("Order received !");
//      initBoard();
      analyzeDNA();
//      DNAisReady = false;
    }
 }
}


void analyzeDNA() {
  
   Serial.println("device up");  
   digitalWrite(bluePin, LOW);
   digitalWrite(greenPin, HIGH);
   digitalWrite(dnaMotorPin, HIGH);
   
   lcd.clear();
   loader();
   delay(sequencingDuration);
   
   Serial.println("device done");  
   digitalWrite(dnaMotorPin, LOW);
   
   digitalWrite(bluePin, HIGH);
   digitalWrite(greenPin, LOW);
   
   lcd.clear();
   lcd.setCursor(0,0);
   lcd.print("Test Done.");
   lcd.setCursor(0,1);
   lcd.print("Success !!");
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
  int total=0;
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
      delay(300);
      total=total+300;
    } 
  }
  Serial.println(total);
}














