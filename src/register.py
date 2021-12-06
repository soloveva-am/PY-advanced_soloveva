import socket                            # Подключаем

sock = socket.socket()                   # Создаём
sock.connect(("81.200.31.248", 9000))    # Присоединяемся

#sock.send("register".encode())     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall("Register".encode())     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall('A47'.encode())
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall('Solovyeva Anna Michailovna'.encode())
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall('B03-007'.encode())
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
