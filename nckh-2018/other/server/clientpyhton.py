import socket

HOST = '10.10.43.172'    # Cấu hình address server
PORT = 80              # Cấu hình Port sử dụng
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cấu hình socket
s.connect((HOST, PORT)) # tiến hành kết nối đến server
message = "sy dep tra1i"
s.sendall(message.encode()) # Gửi dữ liệu lên server
# data = s.recv(1024).decode() # Đọc dữ liệu server trả về
# print(type(str(data)))
# print(data)