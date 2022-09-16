import os,sys

print("""\033[91m   --------------------------------- 
 !!     DOWNLOADING REQUIREMENTS     !! 
   --------------------------------- \033[0m\n\n""")

try:
    os.system("apt-get update -y && apt-get upgrade -y"
    os.system("apt install git,python -y")
    os.system("pip install lolcat hashlib")
except:
    print("\033[91m  [ERROR]\n\n"+Exception+"\033[0m")

print("""\n\n\033[91m   --------------------------------- 
 !!     Installation Successfull    !! 
   --------------------------------- \033[0m""")
