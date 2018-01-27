'''
# Exercise4:

You are given the following templates (just put them as it is in your script):

access_template = ['switchport mode access',

'switchport access vlan {}',

'switchport nonegotiate',

'spanning-tree portfast',

'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',

'switchport mode trunk',

'switchport trunk allowed vlan {}']

Your program should ask:

‘Enter interface mode (access/trunk):’
‘Enter interface type and number:’
For access interfaces, script should request “Enter VLAN number”. For trunk interface, script should request list of allowed vlans “Enter allowed VLANs:”.
Your script should print the configuration depends on the input.

Example:

Input:

Enter interface mode (access/trunk): access

Enter interface type and number: Fa2/1

Enter VLAN number: 5

Output:

Interface Fa2/1

switchport mode access

switchport access vlan 5

switchport nonegotiate

spanning-tree portfast

spanning-tree bpduguard enable
'''

import re

access_template = ['switchport mode access', 'switchport access vlan {}', 'switchport nonegotiate',
                   'spanning-tree portfast', 'spanning-tree bpduguard enable']
trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk', 'switchport trunk allowed vlan {}']


#Mode selection
mode = input('Enter interface mode (access/trunk):')
#re.match(pattern, string)
while not re.match(r'(^access|^trunk)', mode):
#while not modeMatch.match(mode):
    print('...............................')
    print ('Introduce valid interface mode')
    mode = input('Enter interface mode (access/trunk): ')

#Interface Selection
interface = input('Enter interface type and number: ')
while not re.match(r'(^(Fast\s?\w*|Gigabit\s?\w*|G\s?\w*|Fa\s?\w*)\s?\d?\/\d)', interface):
    print('...............................')
    print ('Introduce valid interface (Fax/x,Gigx/x,FastEthernetx/x...)')
    interface = input('Enter interface type and number: ')

#Vlans Selection
if mode == 'access':
    vlan = input('Enter VLAN number: ')
    while not re.match(r'^([0-3]?\d{1,3}$|40\d[0-4])$',vlan):
        print('...............................')
        print ('Introduce valid vlan number')
        vlan = input('Enter VLAN number: ')
    print('Interface', interface)
    for x in range(len(access_template)):
        print (access_template[x].format(vlan))
elif mode == 'trunk':
    allow = input('Enter allowed VLANs: ')
    allowVlans = list(map(int, re.findall (r'(?P<vlans>[0-3]?\d{1,3}|40\d[0-4])', allow)))
    allowVlans.sort()
    print('Interface', interface)
    for x in range(len(trunk_template)):
        print (trunk_template[x].format(allowVlans))

