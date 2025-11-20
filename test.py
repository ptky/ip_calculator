""" kerdes = int(input("Add meg a prefixet: "))
nums_in_binary = []
nums = [4,8,16,32,64,128]
def wferOPK(ip="255.255.255.0", pfx = kerdes):
    parts = ip.split(".")
    
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
    nums.reverse()
    for i in range(0,ones):
        help+=nums[i]
    print(ones)
    print(help)
     """
    
def f_gw(ip="192.168.10.0",selected_hosts=32):
    # first usable ip
    first_usable = ip.split(".")
    f_ip = int(first_usable[3])
    f_ip += f_ip+(selected_hosts-2)       
    first_usable[3] = str(f_ip)
    
    # broadcast ip
    broadcast_ip = ip.split(".")
    br_ip = int(broadcast_ip[3])
    br_ip = br_ip+(selected_hosts-1)
    broadcast_ip[3] = str(br_ip)
    print(broadcast_ip)
    
    # gateway
    gateway_ip = ip.split(".")
    gw_ip = int(gateway_ip[3])
    gw_ip  += 1
    gateway_ip[3] = str(gw_ip)
    print(gateway_ip)
    return first_usable,broadcast_ip,gateway_ip
f_gw()