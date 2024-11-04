/* How to use a flex sensor/resistro - Arduino Tutorial
   Fade an LED with a flex sensor
   More info: http://www.ardumotive.com/how-to-use-a-flex-sensor-en.html
   Dev: Michalis Vasilakis // Date: 9/7/2015 // www.ardumotive.com  */
   

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
  mapped = map(value, 0, 1023, 0, 255);//Map value 0-1023 to 0-255 (PWM)
  String str2 = "Mapped value:";
  Serial.print(value);
  Serial.print(" ");
  Serial.print(mapped);
  Serial.println();
  delay(100);                          //Small delay
  
}

