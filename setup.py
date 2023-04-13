#!/usr/bin/python3

import os, sys, platform

# color codes
r ='\033[91m' # red
g ='\033[92m' # green
s_b ='\033[96m' # sky_blue
y ='\033[93m' # yellow
reset = '\033[0m'

try:
	os.system("clear")
	print("")
	print(y+"""   -----------------------------
 !!   """+s_b+"""Installing Requirements"""+y+"""   !!
   -----------------------------"""+reset)
	print(y+"["+s_b+"¤"+y+"]"+s_b+" System Info"+y+":-ᗒ"+s_b, platform.node(), platform.system(), platform.release(),y+"["+s_b+"¤"+y+"]"+reset+"\n")
	print("\n")

	os.system("pip3 install hashlib")
	os.system("clear")

	print(s_b+"""   ------------------------------ 
 !!   """+g+"""Installation Successfull"""+s_b+"""   !!
   ------------------------------"""+reset)
except:
	os.system("clear")
	print(r+"""  [ERROR] : cannot install packages,
	    Check your internet connection, try again later"""+reset)
