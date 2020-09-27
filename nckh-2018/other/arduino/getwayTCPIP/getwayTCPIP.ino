#include <SPI.h>
#include<WiFiClient.h>
#include <WiFiManager.h> 
#include <LoRa.h>

//lora-esp nss = D4(GPIo2) ; mosi D7(GPIo13);miso d6(GPIo12);sck D5(GPIo14);rst D3(GPIO);dio0 =d0(GPIO16)

const char* Passwork ="hethonghethong";
const char* host = "192.168.43.202";

String Code ="843j38n28";     

#define ss 2 
#define rst 0
#define dio0 16
#define led 5

WiFiManager wifiManager;
WiFiClient client;


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
      String LoRaData = LoRa.readString();
       Serial.println(LoRaData);
      if(LoRaData.substring(0,9) == Code){
        sendMsg(LoRaData.substring(9));
        }
        else{
          Serial.println("Co tin nhan tu nguoi la");
          }
    }
   }
 }
 // gui tin nhan len server
void sendMsg(String msg){
  Serial.printf("\n Ket noi toi ", host);
  if (client.connect(host, 80))
  {
    Serial.println("......thanh cong..........\n");
    Serial.println("Dang gui tin nhan toi server .......\n");
    client.print(msg);
    client.stop();
    Serial.println("\n Ngat ket noi");
  }
  else
  {
    Serial.println("Loi ket noi");
    client.stop();
  }
}
