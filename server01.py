import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 80
soc.bind((host, port))
soc.listen()
client, addr = soc.accept()
print(f'Connection recieved from {addr}')
key = 'python_cyber'
password = client.recv(1024).decode()
if password == key:
    client.sendall('access granted'.encode())
    while True:  
        msg = client.recv(1024).decode()  
        if msg =="exit":
            break
        print(f'client>> {msg}')

        data = input("Server>> ")
        client.sendall(data.encode())

        if data =='exit' :
            break
else : 
    client.sendall("access denied".encode())

client.close()
soc.close()
