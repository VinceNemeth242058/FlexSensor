//Constants:
const int flexPin = A0; //pin A0 to read analog input

//Variables:
int value; //save analog value
int mapped;


void setup(){
  
  Serial.begin(9600);       //Begin serial communication

}

void loop(){
  
  value = analogRead(flexPin);
              //Print value
  mapped = map(value, 30, 1023, 0, 255);//Map value 30-1023 to 0-255 (PWM)
  Serial.print(value);
  Serial.print(" ");
  Serial.print(mapped);
  Serial.println();
  delay(100);                          //Small delay
  
}

