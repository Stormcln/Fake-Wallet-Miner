import os, time, secrets, random
from pystyle import *

banner = Center.XCenter(Colorate.Vertical(Colors.red_to_blue,"""
made by storm
 ███╗   ███╗██╗███╗   ██╗███████╗██████╗   
 ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗  
 ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝  
 ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗  
 ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║  
 ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  
"""))

banner1 = Center.XCenter(Colorate.Vertical(Colors.red_to_blue,"""
made by storm
 ███╗   ███╗██╗███╗   ██╗███████╗██████╗   
 ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗  
 ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝  
 ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗  
 ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║  
 ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  

[1] ETH Wallet Miner
[2] BTC Wallet Miner

> """))

num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
hit=0
fail=0
os.system('cls' if os.name == 'nt' else 'clear')


 
choice = int(input(banner1+" "))

if choice not in [1,2]:
    os.system('cls' if os.name == 'nt' else 'clear')
    input(banner + "\nAre you Dumb ? ")

elif choice == 1:
    input(Center.XCenter(Colorate.Horizontal(Colors.purple_to_blue,"\nETH Wallet > ")))
    time.sleep(random.uniform(1, 3))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,f"\n\n[Connecting to eu-pub0{random.choice(num)}]\n")))
    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Done!]\n\n")))

    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Loading Wallet List]\n")))
    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Done!]\n\n")))

    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Matching Hash]")))
    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Done!]\n\n")))

    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Importing Proxies]")))
    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Done!]\n\n")))

    time.sleep(random.uniform(1, 3))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    time.sleep(random.uniform(2, 4))

    cont = True

    ethval = 2300
    while cont == True:
        rand = random.randint(0,50000)
        if rand != 1:
            print((Colorate.Color(Colors.red,f"[-] 0x{secrets.token_hex(22)} || 00.00 ETH [$00.00]")))

        else:
            eth = random.randint(1,50) /100
            print((Colorate.Horizontal(Colors.green_to_cyan,f"[+] 0x{secrets.token_hex(22)} || 0{eth} ETH [${eth * ethval}]")))
            ques = input("[/] Would you like to continue [y/n] > ")
            time.sleep(random.uniform(1.5, 3))
            if ques.lower() not in ["y"]:
                cont = False

elif choice == 2:
    input(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"\nBTC Wallet > ")))
    time.sleep(random.uniform(1, 3))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,f"\n\n[Connecting to eu-pub0{random.choice(num)}]\n")))
    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Done!]\n\n")))

    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Loading Wallet List]\n")))
    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Done!]\n\n")))

    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Matching Hash]")))
    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Done!]\n\n")))

    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Importing Proxies]")))
    time.sleep(random.uniform(1, 1.5))
    print(Center.XCenter(Colorate.Vertical(Colors.purple_to_blue,"[Done!]\n\n")))

    time.sleep(random.uniform(1, 3))

    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    time.sleep(random.uniform(2, 4))
    cont = True

    ethval = 13000
    while cont == True:
        rand = random.randint(0,500000)
        if rand != 1:
            print((Colorate.Color(Colors.red,f"[-] {random.choice(num)}x{secrets.token_hex(22)} || 00.00 BTC [$00.00]")))
                
        else:
            eth = random.randint(1,50) /100
            print((Colorate.Horizontal(Colors.green_to_cyan,f"[+] {random.choice(num)}x{secrets.token_hex(22)} || 0{eth} BTC [${eth * ethval}]")))
            ques = input("[/] Would you like to continue [y/n] > ")
            time.sleep(random.uniform(1.5, 3))
            if ques.lower() not in ["y"]:
                cont = False
