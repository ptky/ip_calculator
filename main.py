import os, time 
def reset():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_info():
    qstn = input("Add meg az IP-t: ")
    prefix_lenght = input("Add meg a prefix lenght-et [nem kell /]: ")
    network_count = input("Add meg hány hálozatnak kell beleférnie: ")    
    return qstn,prefix_lenght,network_count


nums_in_binary = []

ip,prefix_l,network_count = get_info()


def calc(ip=ip,prefix=prefix_l,netw=network_count):
    
    parts = ip.split(".")
    
    print(parts)
    for i in parts:
        szam = int(i)
        binary_nums = []

        while szam > 0:
            binary_nums.append(str(szam%2))
            szam = szam//2
        if binary_nums:
            binary_nums.reverse()
            nums_in_binary.append("".join(binary_nums))
        else:
            nums_in_binary.append("0")
        
        
            
    print(f"IP Address: {ip}")
    print(f"Subnet Mask: ")
    print("")
    print(f"First usable IP: ")
    print(f"Default Gateway: ")
    print(f"Broadcast IP: ")
    
    
