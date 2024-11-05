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
  Serial.println(value);
  delay(100);                          //Small delay
  
}

