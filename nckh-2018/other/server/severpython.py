import socket

def sever():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(("192.168.43.202", 80))
    soc.listen(1)
    a =0
    while True:
        a=a+1
        con,ad = soc.accept()
        print(ad)
        messagere = con.recv(1204).decode()
        print()
        print(messagere)
        message = "Da nhan"
        con.send(message.encode())
        print(message)



if __name__ == '__main__':
    sever()