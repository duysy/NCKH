#include <SPI.h>
#include <MFRC522.h>
#include <LoRa.h>
/*
  
   -----------------------------------------------------------------------------------------------------
               MFRC522      Arduino       Arduino   Arduino    Arduino          Arduino      ESP8266
               Reader/PCD   Uno/101       Mega      Nano v3    Leonardo/Micro   Pro Micro
   Signal      Pin          Pin           Pin       Pin        Pin              Pin
   ------------------------------------------------------------------------------------------------------
   RST/Reset   RST          9             5         D9         RESET/ICSP-5     RST             D3(GPIO)
   SPI SS      SDA(SS)      10            53        D10        10               10              D4(GPIo2)
   SPI MOSI    MOSI         11 / ICSP-4   51        D11        ICSP-4           16              D7(GPIo13)
   SPI MISO    MISO         12 / ICSP-1   50        D12        ICSP-1           14              D6(GPIo12)
   SPI SCK     SCK          13 / ICSP-3   52        D13        ICSP-3           15              D5(GPIo14)
*/

//lora-rfid nss = 6 ; mosi 11;miso 12;sck 13;rst 9;dio0 =2

void sendLora(String msg);
void readCard();
#define RST_PIN         9
#define SS_PIN          10

#define ss 6 
#define rst 9 
#define dio0 2

#define CoiChip  3

String Code ="843j38n28";
const String Phong =" B304";
unsigned long uidDec, uidDecTemp; 

MFRC522 mfrc522(SS_PIN, RST_PIN);
void setup() {
Serial.begin(115200);

pinMode(10,OUTPUT);
digitalWrite(10,HIGH);
pinMode(6,OUTPUT);
digitalWrite(6,HIGH);

pinMode(CoiChip,OUTPUT);
digitalWrite(CoiChip,LOW);

}
void loop() {
readCard();
}
void readCard() {
  SPI.begin();
  mfrc522.PCD_Init();
  Serial.println("Khoi tao thanh cong");
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }
  Serial.println("ID thẻ: ");
  Serial.print(uidDec);
  for (byte i = 0; i < mfrc522.uid.size; i++) {
      uidDecTemp = mfrc522.uid.uidByte[i];
      uidDec = uidDec*256+uidDecTemp;
    } 
  Serial.println("");
  Serial.print(uidDec);
  Serial.println("");
  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();
  SPI.end(); delay(100);
  sendLora(String(uidDec));
  digitalWrite(CoiChip,HIGH);
  delay(500);
  digitalWrite(CoiChip,LOW);
}
void sendLora(String msg){
  delay(random(40,1000));
  Serial.println(random(40,1000));
  LoRa.setPins(ss,rst,dio0);
  Serial.println("LoRa Sender");
  if (!LoRa.begin(433E6)) {
    Serial.println(".");
  }
  LoRa.setSyncWord (0xF4);
  Serial.print("Sending packet: ");
  LoRa.beginPacket();
  LoRa.print(Code + msg + Phong);
  Serial.println(Code + msg + Phong);
  LoRa.endPacket();
  LoRa.sleep();
  Serial.println("Da gui thanh cong");
  delay(500);
  
  

}
