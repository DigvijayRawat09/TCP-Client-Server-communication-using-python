import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 80
soc.connect((host, port))

password = input('enter password: ')
soc.sendall(password.encode())
response = soc.recv(1024).decode()

if response == "access denied":
    
    print('Server>> access denied')
    soc.close()
else :

    print("server>> Acess Granted")

    while True:
    
        msg = input('client>> ')
        soc.sendall(msg.encode())
    #print(f'Server>> {soc.recv(1024).decode()}')
        if msg =="exit":
            break
        response = soc.recv(1024).decode()
        print(f'Server>> {msg}')
        if response == 'exit' :
            break
soc.close()