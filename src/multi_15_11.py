print ('#1')
import threading
import sys


def thread_job():
    global counter
    old_counter = counter
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
print('#1a')
import threading
import random
import time
import sys


def thread_job():
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)


print('#2a')
import os, re
from time import time

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")
begin = time()
for suffix in range(20, 30):
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
print(time()-begin)
print('#2b')

import os, re
from threading import Thread
from time import time

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

def processer(suffix):
    ip = "192.168.178." + str(suffix)
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])
begin = time()
threads = [Thread(target= processer(suffix)) for suffix in range(20, 30) ]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time()-begin)

print('#3')
from random import randint
from threading import Thread
from time import time
M=[ randint (1, 1000) for _ in range (5000)]
def summer(i, input):
    global results
    output = sum(input)
    results[i]=output
for N in range (1, 10):
    begin = time()
    results= [None for i in range(N)]
    Mkeys=[]
    l=len(M)//N
    for i in range (N-1):
        Mkeys.append(M[i*l: (i+1)*l])
    Mkeys.append(M[N*l: len (M)])

    threads = [Thread(target=summer(i, Mkeys[i])) for i in range (N)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(sum(M))

    print (f'{N} threads - {time()-begin} seconds')

print('#4')
import urllib.request
from time import time


urls = [
    'https://www.yandex.ru', 'https://www.google.com',
'https://habrahabr.ru', 'https://www.python.org',
'https://isocpp.org',
]


def read_url(url) -> object:
    with urllib.request.urlopen(url) as u:
       r=u.read()

    return r[10]


start = time()
for url in urls:
     read_url(url)

print(time() - start)

start=time()
threads =[Thread(target=read_url, args=(url,)) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(time() - start)

print('#5')
