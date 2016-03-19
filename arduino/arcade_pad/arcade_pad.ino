/* 
   ArcadePad 
   by: Eric Garrigues
   Based on: Gamething (https://github.com/cuddleburrito/gamething-controller)
   From: Florian Maurer
   date: March 13, 2015
   license: Public Domain - please use this code however you'd like.

   This code is provided to turn an arduino into an serial controller 
*/

#include <Bounce2.h>

#define SERIAL_SPEED 115200
#define SERIAL_DELAY 10
#define NUM_BUTTONS 14

//activate the alternative debouncing method.
//This method is a lot more responsive, but does not cancel noise.
#define BOUNCE_LOCK-OUT

//========== CONFIGURATION SETTINGS ==========
#define BOUNCE_WAIT 5
#define BOUNCE_COUNT 1

//pins 2-12, 14(A0), 16(A2), 18(A4)
//for buttons 1-10, up, down, left and right

int buttonPins[] = {
  2,  //button 1
  3,  //button 2
  4,  //button 3
  5,  //button 4
  6,  //button 5
  7,  //button 6
  8,  //button 7
  9,  //button 8
  10, //button 9
  11, //button 10
  12, //joystick up
  14, //joystick down
  16, //joystick left
  18  //joystick right
};

char buttonPresets[] = { 
  '1', //button 1
  '2', //button 2
  '3', //button 3
  '4', //button 4
  '5', //button 5
  '6', //button 6
  '7' ,//button 7
  '8', //button 8
  '9', //button 9
  'a', //button 10
  'b', //joystick up
  'c', //joystick down
  'd', //joystick left
  'e'  //joystick right
};


//========== END CONFIGURATION SETTINGS ==========

// Instantiate button state array
boolean buttonPressed[NUM_BUTTONS];

// Instantiate a Bounce object array to store each debouncer in
Bounce debouncers[NUM_BUTTONS];

//Instantiate a counter array for each button to debounce count timer
int debounceCount[NUM_BUTTONS];

void setup() {

  Serial.begin(SERIAL_SPEED); 
 
  // Create debounce instances :
  for (int i = 0; i < NUM_BUTTONS; i++) {
     debouncers[i] = Bounce();
     debounceCount[i] = 0;
     pinMode(buttonPins[i],INPUT_PULLUP);
     (debouncers[i]).attach(buttonPins[i]);
     (debouncers[i]).interval(BOUNCE_WAIT);
     delay(100);
     buttonPressed[i] = false;
  }   
}

void loop() {
  
  for (int j = 0; j < NUM_BUTTONS; j++) { //iterate over each button (pin)
    
     (debouncers[j]).update(); //check current value
     int value = (debouncers[j]).read();
     
     if ( value == LOW ) { //if button pressed
       
       if(debounceCount[j] == BOUNCE_COUNT && buttonPressed[j] == false) { //the button has been held down long enough and it hasn't been previously registered as pressed
          buttonPressed[j] = 1;
        } else {
            if(debounceCount[j] < BOUNCE_COUNT) { 
              debounceCount[j] = debounceCount[j] + 1; //else increment the count
            }
        }
        
      } else { //button is not pressed
        
        if(debounceCount[j] > 0) {
          debounceCount[j] = debounceCount[j] - 1; //keep decreasing count unless 0
        } else {
           buttonPressed[j] = 0;
        }
      }

      Serial.print(buttonPressed[j]);
      Serial.print(";");
  }

  Serial.print("\n");

  delay(SERIAL_DELAY);

}
