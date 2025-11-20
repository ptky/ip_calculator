import os, time,shutil,colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
def reset():
    
    os.system('cls' if os.name == 'nt' else 'clear')
nums = [4,8,16,32,64,128,256,512]

def get_info():
    qstn = input("Add meg az IP-t: ")
    network_count = 0
    while network_count < 2 or network_count > 254:
        reset() 
        network_count = int(input("Add meg hány hálozatnak kell beleférnie: "))
    
    def_mask = "255.255.255.0"
    return qstn,network_count,def_mask

ip,network_count,def_mask = get_info()

def center_text(text):
    columns = shutil.get_terminal_size().columns
    lines = text.splitlines()
    return "\n".join(line.center(columns) for line in lines)
    
def find_num(hosts=network_count):
    for i, n in enumerate(nums):
        if n >= hosts + 2:
            selected_block = n
            prefix_index = i
            return selected_block, prefix_index


closest, prefix_index = find_num()
prefix_l = 32 - (prefix_index + 2)


def calc(addr:str):
    inside = []
    parts = addr.split(".")
    
    for i in parts:
        szam = int(i)
        binary_nums = []

        while szam > 0:
            binary_nums.append(str(szam%2))
            szam = szam//2
        if binary_nums:
            binary_nums.reverse()
            inside.append("".join(binary_nums))
        else:
            inside.append("0")
    return inside


def mask(pfx=prefix_l):
    nums_in_binary = calc("255.255.255.0")
    needed = pfx-24
    insert = "1" * needed + "0" * (8 - needed)
    nums_in_binary[3] = insert
    print(nums_in_binary)
    ones = 0
    help = 0
    for i in nums_in_binary[3]:
        if i == "1":
            ones+=1
        else:
            continue
    rev = nums[::-1]
    for i in range(0,ones):
        help+=rev[i]
    eredmeny = f"255.255.255.{help}"
    return eredmeny
        
    
eredmeny = mask(pfx=prefix_l)

def f_gw_br(ip=ip,selected_hosts=closest):
    # first usable ip
    first_usable = ip.split(".")
    fu = int(first_usable[3]) + 1
    first_usable[3] = str(fu)

    
    # broadcast ip
    broadcast_ip = ip.split(".")
    br_ip = int(broadcast_ip[3])
    broadcast_ip[3] = str(br_ip + selected_hosts - 1)
    print(broadcast_ip)
    
    # gateway
    gateway_ip = ip.split(".")
    gw_ip = int(gateway_ip[3])
    gw_ip = gw_ip+(closest-2)
    gateway_ip[3] = str(gw_ip)
    
    fu_str = ".".join(first_usable)
    br_str = ".".join(broadcast_ip)
    gw_str = ".".join(gateway_ip)
    return fu_str, br_str, gw_str

first_usable,broadcast_ip,gateway_ip = f_gw_br()

def kiiras_v1():
    
    reset()
    i = 0
    direction = 1
    max_nigg = 3
    while True:
        print(Fore.CYAN + center_text(f'{"-"*i}Made by Pataky{"-"*i}'))
        print()
        print(center_text(f"Closest Number to hosts: {closest}  "))        
        print(center_text(f"IP Address: {ip}"))
        print("")
        print(center_text(f"Subnet Mask: {eredmeny} "))
        print(center_text(f"First usable IP: {first_usable} "))
        print(center_text(f"Default Gateway: {gateway_ip} "))
        print(center_text(f"Broadcast IP: {broadcast_ip} "))
        time.sleep(1)
        reset()
        i += direction
        if i >= max_nigg:
            direction = -1
        elif i <= 0:
            direction = 1

def kiiras_v2():
    
    reset()
    print(Fore.CYAN + center_text("Made by Pataky"))
    print()
    print(center_text(f"Closest Number to hosts: {closest}  "))        
    print(center_text(f"IP Address: {ip}"))
    print("")
    print(center_text(f"Subnet Mask: {eredmeny} "))
    print(center_text(f"First usable IP: {first_usable} "))
    print(center_text(f"Default Gateway: {gateway_ip} "))
    print(center_text(f"Broadcast IP: {broadcast_ip} "))
    time.sleep(600)
    
        
    
    
    
kiiras_v2()