#include <HardwareSerial.h>

// Define motor pins
const int motorPins[] = {21, 19, 18, 5, 17, 16, 4, 22, 2, 15};

const int numMotors = sizeof(motorPins) / sizeof(motorPins[0]);
int motorIntensities[numMotors] = {0};

const byte maxDataSize = 2000;
char receivedData[maxDataSize];

void setup() {
  Serial.begin(9600);

  // Initiate motor GPIO pins as output
  for (int i = 0; i < sizeof(motorPins) / sizeof(motorPins[0]); i++) {
    pinMode(motorPins[i], OUTPUT);
  }
  // Output for LED pin that indicates status of serial communication
  pinMode(23,OUTPUT);
}

void loop() {
  
  
  if(Serial.available()){
    // Reads received serial message (expects a string of comma seperated values)
    char c;
    byte i = 0;
    while ((c = Serial.read()) != '\n' && i < maxDataSize - 1) {
      receivedData[i] = c;
      i++;
    }

    receivedData[i] = '\0';
    byte tokenCount = 0;

    // Splits the data at every comma
    char *token = strtok(receivedData, ",");
    while (token != NULL && tokenCount < numMotors) {
      int number = atoi(token);
      Serial.print("Received: ");
      Serial.print(number);
      // Assign the intensity to the motorIntensities array
      motorIntensities[tokenCount] = number;
      tokenCount++;
      token = strtok(NULL, ",");
    }

    // Serial.print(tokenCount);
    if (tokenCount != numMotors) {
      Serial.println("Error: Number of received numbers doesn't match the number of motors");
    }

    // light the LED to signify data reeception
    digitalWrite(23, 1);
    Serial.println("Intensities received");
  }
  
  // Assign PWM signal of received intensity based on the depth frame to each motor
  for (int i = 0; i < numMotors; i++) {
    analogWrite(motorPins[i], motorIntensities[i]);
    Serial.print(motorIntensities[i]);
  }
  // println is used ot sedn the previous serial messages back to Python backend for debugging
  Serial.println("Intensities");

  delay(50);
}
