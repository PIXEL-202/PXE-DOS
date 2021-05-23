![x-word](logo.png)



The tool to 
test the 
penetration 
of websites 
affected by 
the denial 
of service 
attack( DOS attack )
or what called 
syn flooding
, where a
tool send
large number
of requests 
and a larg 
size of bits
are sent to 
the server 
to try to 
stop the ,tool
you can send
400 requests
per second

# Setup 

first you must install some modules (pyfiglet,termcoloer) 

If you haven't installed pip , install it for cont 
$$ apt update

$$ apt isntall python3-pip

isntalling the modules 

$$ pip3 install termcolor

$$ pip3 install pyfiglet 

next ; 

        $$ git clone https://www.github.com/PIXEL-202/PXE-DOS.git

        $$ cd PXE-DOS

       $$ python3 PXE-DOS.py 

now you are install the script 

# using

          python3 PXE-DOS.py {target} {port} {The number of requests}
 
 tagert = ip addrss or hostname or website 
 
 port  = The port by which you want to communicate with the target (default 80)  
 
 The number of requests = count of syn messages (default 100000000)
 
 if you run : 
 
                  python3 PXE-DOS goole.com 
                  
   the tool Will continue by default port 80 
   and the default count of syn messages 10000000
if you run: 
                 python3 PXE-DOS.PY google.com 443
                 
                 the tool Will continue with prot 443
                 and the default count of syn messages 100000000
if you run : 
                 python3 PXE-DOS.py google.com 443 5
                 
                 the tool Will continue with port 443
                 with  5 syn messages 
                 
