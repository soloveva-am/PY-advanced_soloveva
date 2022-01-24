import socket                            # Подключаем
import gzip
sock = socket.socket()                   # Создаём
sock.connect(("81.200.31.248", 9000))    # Присоединяемся

#sock.send("register".encode())     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall("Get secret key".encode())     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall("A47".encode())     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall("about".encode())     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall("next".encode())     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
"""Для архивации данных применяется библиотека gzip
метод gzip.compress(data) архивирует (сжимает) байтстроку data
метод gzip.decompress(data) разархивирует"""
sock.sendall("help".encode())     # Отправка
data = sock.recv(1000) # Ответ
data = gzip.decompress(data)
data = data.decode("utf8")
print(data)
sock.sendall(gzip.compress("next".encode()))     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)
sock.sendall(gzip.compress("about".encode()))     # Отправка
data = sock.recv(1000) # Ответ
data = data.decode("utf8")
print(data)