import socket
from sqlpython import *


def sever():
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc.bind(("192.168.43.202", 80))
        soc.listen(1)
        while True:
            con, ad = soc.accept()
            print(ad)
            messagere = con.recv(1204).decode()
            print(messagere)

            sql = sqlpython()
            sql.RFID(catkytu(messagere, 0), catkytu(messagere, 1))
            # message = "Da nhan"
            # con.send(message.encode())
            # print(message)
    except:
        print("Co loi")

if __name__ == '__main__':
    sever()