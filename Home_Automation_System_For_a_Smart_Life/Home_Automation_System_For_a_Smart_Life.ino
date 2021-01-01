/*
 *                                          Home Automation System For a Smart Life
 *                                          ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 * Team:
 * Team Name      - RoboSapiens
 * Project Name   - Home Automation System For a Smart Life
 * Professor Name - Dr Ezhil
 * Project Leader - K. Sai Venkata Giri
 * Teamates       - 1) N. Hemangani
 *                  2) T. Pushpa Teja
 *                  3) M. Srinivas
 *                  4) K. Chennika Wangmai
 *                  5)Ch. Praneeth
 * 
 * Coding                   - K. Sai Venkata Giri, M. Srinivas
 * Simulation               - N. Hemangani
 * Hardware                 - K. Sai Vekata Giri
 * Presentation and reports - K. Chennika Wangmai,N. Hemangani
 * Management               - T. Pushpa Teja
 * 
 * ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 * Project Description : 
 * A Brief About the Project
 * 
 *                                         Home Automation System For a Smart Life
 * What do we do?
 * 1) A Door Lock Sytem Based on RFID
 * 2) When Correct Entry Card is shown Lock Opens,Lights and fans gets turned on
 * 3) Dont want lights or fans to run? No problemo. Control With the app Blinky
 * 4) Lazy? Use Google Assistant Buddy
 * 5) Finally While Exiting show Exit Card All lights, fans are turned off, Door is Locked
 * ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 * Pin Connections:
 * ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 * 
 * ESP01 - Arduino Uno
 * ¯¯¯¯¯   ¯¯¯¯¯¯¯¯¯¯¯
 *    TX - TX(1)
 *    RX - RX(0)
 *  3.3V - 3.3V
 *   GND - GND
 *   
 *   LCD - Arduino Uno
 *   ¯¯¯   ¯¯¯¯¯¯¯¯¯¯¯
 *    RS - Pin 6
 *     E - Pin 7
 *    D4 - Pin 2
 *    D5 - Pin 3
 *    D6 - Pin 4
 *    D7 - Pin 5
 *  
 * BLYNK - ARDUINO UNO
 * ¯¯¯¯¯   ¯¯¯¯¯¯¯¯¯¯¯
 * MOTOR - A1
 *   LED - 8
 *     
 * Servo - Arduino Uno
 * ¯¯¯¯¯   ¯¯¯¯¯¯¯¯¯¯¯
 * Attach- A0
 *    5v - 5v
 *   gnd - gnd
 *   
 *  RFID - Arduino Uno 
 *  ¯¯¯¯   ¯¯¯¯¯¯¯¯¯¯¯
 *   SDA - 10
 *   SCK - 13
 *  MOS1 - 11
 *  MIS0 - 12
 *   IRQ - Not Connected
 *   GND - gnd
 *   RST - A2(Not Connected though)
 *  3.3V - 3.3V
 *  
 *   
 * L293D - Arduino Uno               (L293D is MotorDriver used to run DC Motor)
 * ¯¯¯¯¯   ¯¯¯¯¯¯¯¯¯¯¯
 *   enA - A3 
 *   in1 - A5
 *   in2 - A4
 *   
 * 
 *  Pin9 - Turns on When RFID Open Tag is Shown(For LED)
 * PinA1 - Turns on When RFID Open Tag is Shown(For DC MOTOR) 
 *    
 *    
 *   And of Pin8 , pin9  =>LED
 *   And of PinA4, PinA1 =>Motor Driver pin
 *   
 * ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 * Basic Steps Included are
 *      1) Libraries Installation
 *      2) Interfacting Pins
 *      3) Pin  Name Declarations
 *      4) Authorization Key For Blinky
 * Void Setup:
 *     4) Begin Communications
 *     5) Intial Postitions/Status/Configurations
 *     6) Message To be printed On Serial Monitor
 * Void Loop:
 *     7) Blink Reading
 *     8) Tag there or not , Same or different 
 *     9) If Entering Correct Card => On Lights,Fans,Open Lock
 *     10) If Exiting Correct Card => Off All
 *     11) Else Unauthorized
 * Funnctions:
 *     12) On Motors
 *     13) Off Motors
 *     
 *     
 * Block Diagram of Execution:
 * ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 * 
 *                                              ________________________________________
*                                              | Signal From Wifi+Blnky+Google Assistant |-- --- -  
*                                               ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯         |  
                                                                       |                          |
 *                                                                     |                          |
 *                                        On Motor Signal From Blinky  |                          | 
 *                                                                     |                          |
 *                                                                     |                          |
 *                                                                     |                          |
 *                                                                     ___                        |
 *                                   /----On Motor Signal Form RFID- -|AND|---------------------- )-------------------ON Motor        
 *                     /(Correct Card)-----ON LED ----------------------------------------------|AND|-----------------ON LED
 *                  /   (Entry)      \-----ON Servo(Open Lock) 
 *                /
 *             /                       /----OFF Motor                                               
 *        RFID -- -- --(Correct Card)-------OFF LED                                                  
 *             \        (Exit)          \-----OFF Servo(Open Lock)                                  
 *                \       
 *                   \
 *                      \(Wrong Card)----Nothing Changd(No Access) 
 *                      
 *                      
 *                      
 *  A piece of Useful Code 
 *  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 *  blynk-ser.bat -c COM8(Your COM number)
 *  
 *  Installation Of Blynk Library
 *  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 *  1) Go to Sketch/Include Library/Manage Libraries
 *  2) Search For Blynk
 *  3) Install the Library
 *  
 *  Hardware Installation
 *  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 *  1) Make the connections as shown in Pin Connectioncode
 *  2) Connect a Sevro Motor And a Door Lock Using Glue Gun
 *  
 *  Software Installation
 *  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 *  1) Place the RFID Entry code of your card in the code
 *  2) Place the RFID Exit code of your card in the code
 *  
 *  How to Execute?
 *  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 *  1) Make pin Connections as given in Comments
 *  2) Next Upload the Code to Arduino Uno
 *  3) Open CMD(Run as Administrator)
 *  4) Go to scripts folder of blynk library (Will be present in Your installed library Folder.Library Folder will be present in Arduino/Libraries/Blynk if you have used above installation)--------Using cd command
 *  5) Then type the command "blynk-ser.bat -c COM5" (Your COM number)
 *  6) Click Run 
 *  
 *  And Enjoy your Automated Home 😀😀
 *  
 * References:
 * ¯¯¯¯¯¯¯¯¯¯
 *  To Connect to Blynk   : https://www.youtube.com/watch?v=osACD1WX6sg&t=388s
 *  To Connect to IFTTT   : https://www.youtube.com/watch?v=BtndiAyGSzk&t=643s
 *  To See Servo Hardware : https://www.youtube.com/watch?v=Z44f4B6p-Kk
 */         
#include <Servo.h>                              //Library For Servo
#include<LiquidCrystal.h>                       //Library For LCD
#include <MFRC522.h>                            //Library For RFID
#include <SoftwareSerial.h>                     //Library For Serial Communication With Wifimodule+PC
#include <BlynkSimpleStream.h>                  //Library For Blinky

MFRC522 mfrc522(10,A2);                         //Interfacing of RFID  -> SDA,RESET
#define BLYNK_PRINT DebugSerial                 //The Interfacing Data Type of BLYNK_PRINT
SoftwareSerial DebugSerial(0,1);                //Interfacing of Blynk -> RX,TX
LiquidCrystal lcd(6,7,5,4,3,2);                 //register select,enable,db4,db5,db6,db7
Servo myServo;                                  //Servo Variable

int light=9;                                    //Variable declarations for easy undrstanding of Code
int enA = A3;
int in1 = A5;
int in2 = A4;
int Lock_Open_Angle=40;
int Lock_Close_Angle=145;
char auth[] = "xhTgiE44-fo6YUGRGSjAL6s3ZiBj0Xfa";

void setup() 
{
  Serial.begin(9600);                           //Communication With Serial Monitor                             
  mfrc522.PCD_Init();                           //Communication With RFID
  DebugSerial.begin(9600);                      //Communication With Wifi Module+pc
  Blynk.begin(Serial, auth);                    //Communication With Blynk
  lcd.begin(16,2);                              //Communication With LCD

  myServo.attach(A0);                           // Servo Pin Intialising

  pinMode(9,OUTPUT);                            //LED         -Lights in ROOM
  pinMode(enA, OUTPUT);                         //DC MOTOR    -PWM speed Pin
  pinMode(in1, OUTPUT);                         //DC MOTOR    -One pin of H-Bridge gate  
  pinMode(in2, OUTPUT);                         //DC MOTOR    -Second pin of the Pair of the Bridge
  lcd.clear();

  digitalWrite(light,LOW);                      //Initial Lights Status
  turn_off_motors();                            //Initial Motor Status
  myServo.write(Lock_Close_Angle);              //Intitial Servo Position 
}

void loop() 
{
  Blynk.run();
  if ( ! mfrc522.PICC_IsNewCardPresent())       //Look for new cards.No New card = Return Loop
  {
    return;
  }
  
  if ( ! mfrc522.PICC_ReadCardSerial())         //Select one of the cards.No card = Return Loop
  {
    return;
  }
  String content= "";
  byte letter;
  
  for (byte i = 0; i < mfrc522.uid.size; i++)    //Used forr finding the tag ID
  {
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  
  Serial.print("Message : ");
  
  content.toUpperCase();                          
  if (content.substring(1) == "53 9A 6D 0C")     //We need to place that id here-Done change here the UID of the card/cards that you want to give access
    {
      
      lcd.setCursor(1,0);                       //Set Cursor to col 1 row 0 (Rows and cols start with index 0)
      lcd.print("Opening Doors");               //Prints "Opening Doors"
      lcd.setCursor(4,1);                       //Set Cursor to col4 row 1
      lcd.print("Welcome");                     //Prints "Welcome"
      myServo.write(Lock_Open_Angle);           //Opening Lock
      digitalWrite(light, HIGH);                //Turning on Lights(LED)
      turn_on_motors();                         //Turning on Fans(DC MOTOR)
      
    }
 
 else if(content.substring(1) == "57 29 9C 60")
   {
      lcd.clear();                              //Clear LCD Screen
      lcd.setCursor(1,0);                       //Set Cursor to col1 row0
      lcd.print("Closing Doors");               //Prints "Closing Doors"
      myServo.write(Lock_Close_Angle);          //Opening Lock
      digitalWrite(light, LOW);                 //Turning Off Lights(LED)
      turn_off_motors();                        //Turning Off Fans(DC MOTOR)
   }
  else
    {
      lcd.clear();                              //Clear LCD Screen
      lcd.setCursor(1,0);                       //Set Cursor to Col1 row0
      lcd.print("Access Denied");               //Prints "Access Denied"
    }
}

void turn_on_motors()                           //Function to turn on motors
{
  analogWrite(enA, 255);                        //RPM controler using PWM
  analogWrite(in1, 0);                          //Opposite Signs of these open the switch and will work
  analogWrite(in2, 255);                        //To Reverse Directions Make 0->255 and 255->0
};
void turn_off_motors()                          //Function to turn off motors
{
  analogWrite(in1, 0);                          
  analogWrite(in2, 0);                          //Keeping Same Voltage on Both Switches of H-Bridge =>Turning OFF
};
