#include <AFMotor.h>
AF_DCMotor M1(3);
AF_DCMotor M2(2);
 
void setup() {
  Serial.begin(9600);
}
 
void loop() {
   M1.setSpeed(150);
   M2.setSpeed(150);

   if (Serial.available() > 0) {
    char received = Serial.read();
    if (received == '1') {
      M1.run(FORWARD);
      M2.run(FORWARD);
    }
    
    else if (received == '2') {
      M1.run(BACKWARD);
      M2.run(BACKWARD);
    }
    else if (received == '3') {
      M1.run(RELEASE);
      M2.run(RELEASE);
    }
}
}
