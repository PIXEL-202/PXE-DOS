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

If you haven't installed pip , install it for cont 

$$ sudo apt update

$$ sudo apt isntall python3-pip

isntalling the modules 

$$ sudo pip3 install -r requirements.txt

next ; 

  $$ sudo git clone https://www.github.com/PIXEL-202/PXE-DOS.git

  $$ cd PXE-DOS

  $$ sudo python3 PXE-DOS.py 

now you are install the script 

# using

   python3 PXE-DOS.py {target} {port} {The number of requests}
 
 tagert = ip addrss or hostname or website 
 
 port  = The port by which you want to communicate with the target (default 80)  
 
 The number of requests = count of syn messages (default 100000000)
 
the tool take first argv for website
and secount for port numper (default 80 )  and third for count syn messages (default 100000000) 

# Explanatory video

![x](video.gif)


# فلسطين_لن_تهود

# Contact

If you encounter any problem or want to inquire about something, do not hesitate to contact me

insta : www.instagram.com/al_ghonime

email : alghonime_27@yahoo.com
