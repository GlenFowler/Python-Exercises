'''
# Excercise3:

your program should read information from the file ShowIpRoute.txt (the file contains only output of “show ip route”) and for each entry of dynamic routing protocol presented in the file you need to print the output like:
Protocol: 	
Prefix: 	
AD/Metric: 	
Next-Hop: 	
Last update: 	
Outbound interface: 	

Example:

for the line “D 10.67.10.0 [200/128] via 10.119.254.244 , 0:02:22, Ethernet2” you should print:

Protocol:  	            EIGRP
Prefix:                 10.67.10.0   	
AD/Metric: 	            200/128
Next-Hop: 	            10.119.254.244
Last Update: 	        0:02:22
Outbound interface:  	Ethernet2

'''

import re

f = open('ShowIpRoute.txt', 'r')
commands = f.readlines()
f.close()

#Routing Protocols (RIP, EIGRP, OSPF, IS-IS, EGP)
protocols = {'R':'RIP', 'B':'BGP', 'D':'EIGRP', 'D EX':'EIGRP external','O':'OSPF', 'O IA': 'OSPF inter area',
            'O N1':'OSPF NSSA external type 1', 'O N2':'OSPF NSSA external type 2', 'O E1':'OSPF external type 1',
            'O E2':'OSPF external type 2', 'E':'EGP','i':'IS-IS','su': 'IS-IS summary', 'i L1': 'IS-IS level-1',
            'i L2': 'IS-IS level-2', 'i ia':'IS-IS inter area', '*':'candidate default'}

#'L':'Local', 'C':'Connected', 'S':'Static', 'M':'Mobile', 'U':'per-user static route', 'o':'ODR',
#'P':'periodic downloaded static route', 'H':'NHRP', 'l':'LISP', 'a': 'application route', '+':'replicated route',
#'%':'next hop override'

#RegEx

for x in commands:
    matchOBJ = re.match(r'(^[R|D|O|i|B|E]([\s|\*][A-Z]+[A-Z|\d])?)\s\d',x)
    if matchOBJ:
        prot = re.search(r'^(?P<protocol>[R|D|O|i|B|E]([\s|\*][A-Z]+[A-Z|\d])?)', x).group('protocol')
        prefix = re.search(r'(?P<prefix>((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?))', x).group('prefix')
        metric = re.search(r'\[(?P<metric>.*)]',x).group('metric')
        hop = re.search(r'via (?P<hop>((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]?))', x).group('hop')
        update = re.search(r'(?P<update>\d{1,2}:\d{1,2}:\d{1,2})', x).group('update')
        outbound = re.search(r'(?P<outbound>[\w|\/]+$)', x).group('outbound')

#Protocol conversion
        if prot.count('*')>0:
            prot = re.sub(r'\*',' ',prot)
            protocol = protocols[prot] + '\t' +protocols['*']
        else:
            protocol = protocols[prot]
        
        
#Data print                
        print (x, end='')
        print ('Protocol:', protocol)
        print ('Prefix:', prefix)
        print ('AD/Metric:', metric)
        print ('Next-Hop:', hop)
        print ('Last Update:', update)
        print ('Outbound interface:',outbound,'\n')

     
