#include <LiquidCrystal.h>

LiquidCrystal lcd(12,11,5,4,3,2);

int switchPin = 13;
int dnaReaderPin = 13;
// int ledPin = 9;
int sequencingDuration = 1000;
long start=0;


void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);

  pinMode(switchPin, INPUT);

  // pinMode(ledPin, OUPUT);
  pinMode(dnaReaderPin, OUTPUT);
}

void loop() {
  if (millis()-start < 1000) {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Waiting for order.");
    lcd.setCursor(0,1);
    lcd.print("Warming up...");
  } else if (millis()-start > 1000 && millis()-start < 2000) {
    digitalWrite(dnaReaderPin, HIGH);
    // lcd.clear();
    loader();
  } else {
    lcd.clear();
    digitalWrite(dnaReaderPin, LOW);
    lcd.setCursor(0,0);
    lcd.print("Test Done.");
    lcd.setCursor(0,1);
    lcd.print("Success !!");
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
