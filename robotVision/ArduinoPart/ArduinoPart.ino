/*void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  // check if data is available
  if (Serial.available() > 0) {
    // read the incoming string:
    String incomingString = Serial.readStringUntil('\n');

    // prints the received data
    Serial.print("I received: ");
    Serial.println(incomingString);
  }
}*/
int motor1pin1=2;
int motor1pin2=3;
int motor2pin1=4;
int motor2pin2=5;
void setup(){
  pinMode(motor1pin1,OUTPUT);
  pinMode(motor1pin2,OUTPUT);
  pinMode(motor2pin1,OUTPUT);
  pinMode(motor2pin2,OUTPUT);
}
void loop(){
  digitalWrite(motor1pin1,HIGH);
  digitalWrite(motor1pin2,LOW);
  digitalWrite(motor2pin1,HIGH);
  digitalWrite(motor2pin2,LOW);
  delay(1000);
  digitalWrite(motor1pin1,LOW);
  digitalWrite(motor1pin2,HIGH);
  digitalWrite(motor2pin1,LOW);
  digitalWrite(motor2pin2,HIGH);
  delay(1000);
}
