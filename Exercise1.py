'''
# Exercise1:

Your program should ask two inputs from the user:

    “Enter Ip address:”
    “Enter subnet mask in decimal format:”

Program should:

    Check the validity of ip address. If address is invalid, it should generate the error “Invalid IP address format” and prompt again “Enter ip address:”
    Check the validity of the subnet mask. If subnet mask is not in decimal format or incorrect, then generate the error “Subnet mask is invalid” and prompt again “Enter subnet mask in decimal format”
    The program should present the ip address in the binary formal like in example below (each number in decimal ip address has it’s own row of width 10 symbols).
    Your program should print the network address and broadcast address for the given ip

Example of the input:

Please enter the ip address: 10.1.1.1

Please enter the subnet mask: /24

Example of the output:
      10 	       1 	       1 	       1
00001010 	00000001 	00000001 	00000001

 network address is: 10.1.1.0/24 

 broadcast address is: 10.1.1.255/24 
'''


import ipaddress
#import regex
import re

#regex expression
regexIP = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)$')
regexMask = re.compile (r'^([\d]|[1-2]\d|3[0-2])$')

ip = "None"
validIP = regexIP.match(ip)
mask = "None"
validMask = regexMask.match(mask) 


#IP input
while validIP == None:
    ip = input("Enter IP address <xxx.xxx.xxx.xxx>:")
    validIP = regexIP.match(ip)
    if validIP == None:
        print ("IP not valid.")
#Mask input
while validMask == None:
    mask = input("Enter subnet mask in decimal format </xx or xx>:")
    if mask[0] == "/":
        mask = mask[1:]
        validMask = regexMask.match(mask)
    else:
        validMask = regexMask.match(mask)
    if validMask == None:
        print ("Mask not valid.")

#Conversion to decimal to binary
ipnum = ip.split('.')
for x in ipnum:
    print (format(int(x),'>8'), end ='\t')

print('\n')
for x in ipnum:
    print (format(int(x), '08b'), end ='\t')
              
#Network and broadcast addresses        
addr = ipaddress.ip_interface(ip+"/"+mask)

netaddr = addr.network
print ('\n'+'Network address is:' + str(netaddr))

addrbroad = netaddr.broadcast_address
print ('broadcast address is:'+ str(addrbroad)+"/"+mask)