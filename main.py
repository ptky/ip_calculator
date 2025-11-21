import os, time,shutil,colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
netw = []
def reset():
    
    os.system('cls' if os.name == 'nt' else 'clear')
nums = [4,8,16,32,64,128,256,512]

def get_info():
    qstn = input("Add meg az IP-t: ")
    qstn2 = int(input("Hány hálózatot szeretnél: "))

    reset()
    for i in range(qstn2):
        hosts = int(input(f"Add meg hány host kell a(z) n{i+1}. hálózatba: "))
        netw.append((hosts, i))

    def_mask = "255.255.255.0"
    return qstn, def_mask



def center_text(text):
    columns = shutil.get_terminal_size().columns
    lines = text.splitlines()
    return "\n".join(line.center(columns) for line in lines)
    
def find_num(hosts=int):
    for i, n in enumerate(nums):
        if n >= hosts + 2:
            selected_block = n
            prefix_index = i
            return selected_block, prefix_index



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


def mask(pfx=int):
    needed = pfx - 24
    fourth = int("1"*needed + "0"*(8-needed), 2)
    eredmeny = f"255.255.255.{fourth}"
    return eredmeny
    


def f_gw_br(ip,selected_hosts=int,closest=int):
    # first usable ip
    first_usable = ip.split(".")
    fu = int(first_usable[3]) + 1
    first_usable[3] = str(fu)

    
    # broadcast ip
    broadcast_ip = ip.split(".")
    br_ip = int(broadcast_ip[3])
    broadcast_ip[3] = str(br_ip + selected_hosts - 1)
    
    # gateway
    gateway_ip = ip.split(".")
    gw_ip = int(gateway_ip[3])
    gw_ip = gw_ip+(closest-2)
    gateway_ip[3] = str(gw_ip)
    
    fu_str = ".".join(first_usable)
    br_str = ".".join(broadcast_ip)
    gw_str = ".".join(gateway_ip)
    return fu_str, gw_str, br_str




def kiiras_v2(closest,ip,eredmeny,first_usable,gateway_ip,broadcast_ip,n):
    print()
    print(Fore.CYAN + center_text("----------------------------------------"))
    print(center_text(f"Network: n{n}"))
    print(center_text(f"Closest Number to hosts: {closest}  "))        
    print(center_text(f"IP Address: {ip}"))
    print("")
    print(center_text(f"Subnet Mask: {eredmeny} "))
    print(center_text(f"First usable IP: {first_usable} "))
    print(center_text(f"Default Gateway: {gateway_ip} "))
    print(center_text(f"Broadcast IP: {broadcast_ip} "))

    
    
        
    
    
def run():
    ip, def_mask = get_info()
    current_ip = ip
    counter = 0
    netw.sort(key=lambda x: x[0], reverse=True)
    reset()
    print(Fore.CYAN + center_text("Made by Pataky"))
    for hosts,index in netw:
        szam, prefix_l = find_num(hosts)
        eredmeny = mask(pfx=prefix_l)
        fr_u, gw_ip, br_ip = f_gw_br(ip=current_ip, selected_hosts=szam, closest=szam)
        kiiras_v2(closest=szam,ip=current_ip,eredmeny=eredmeny,first_usable=fr_u,gateway_ip=gw_ip,broadcast_ip=br_ip,n=index+1)

        counter+=1
        last = int(br_ip.split('.')[-1])
        base = br_ip.split('.')
        base[-1] = str(last + 1)
        current_ip = ".".join(base)

        counter += 1
    time.sleep(600)
    

run()