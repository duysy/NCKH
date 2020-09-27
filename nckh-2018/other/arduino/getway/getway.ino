#include <SPI.h>
#include <LoRa.h>
#include <WiFiManager.h>
#include <ESP8266HTTPClient.h>
//lora-esp nss = D4(GPIo2) ; mosi D7(GPIo13);miso d6(GPIo12);sck D5(GPIo14);rst D3(GPIO);dio0 =d0(GPIO16)
void httpRequest(unsigned long uidDec);
const char* Passwork ="hethonghethong"; 

#define ss 2 
#define rst 0
#define dio0 16
#define led 5

WiFiManager wifiManager;
HTTPClient http;


void setup() {
  
Serial.begin(115200);
pinMode(led,OUTPUT);
digitalWrite(led,LOW);
//wifiManager.resetSettings();
wifiManager.autoConnect("Gateway",Passwork);
Serial.println("Connect wifi thành công");
digitalWrite(led,HIGH);

LoRa.setPins (ss, rst, dio0);
  Serial.println("LoRa Receiver");
  if (!LoRa.begin(433E6)) {
    Serial.println(".");
  }
  LoRa.setSyncWord (0xF4);
  
}

void loop() {
int packetSize = LoRa.parsePacket();
  if (packetSize) { // Kiem tra co goi tin nao khong 
    Serial.print("Received packet '");

    // read packet
    while (LoRa.available()) {
      String LoRaData = LoRa.readString (); 
      Serial.println(LoRaData);
      httpRequest(LoRaData.substring(0,10),LoRaData.substring(11));
    }
   }
 }

 // gui tin nhan len server
void httpRequest(String uidDec,String Phong){
 // Tao chuổi Json
StaticJsonBuffer<200> JSONdoc;   //Declaring static JSON buffer
JsonObject& JSONdocid = JSONdoc.createObject(); // Tao đối tương mới trong json
JSONdocid["rfid"] = uidDec;
char doc[200];
JSONdocid.prettyPrintTo(doc, sizeof(doc));
Serial.println(doc);
// request lên server
 
///String link = String("http://daotao.sict.udn.vn/diemdanh/" + String(Phong));
String link = String("http://172.16.1.78");
Serial.println(link);
http.begin(link);  //Bat dau voi htttp
Serial.println("1..");
http.addHeader("Content-Type","application/json");             //dinh dang header
Serial.println("2..");
http.POST(doc);   //Gui post len server
Serial.println("3..");
http.end();  // Ngưng 
Serial.println("4..");

}
