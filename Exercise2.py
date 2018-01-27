'''
# Exercise2:

Your program should read the content of the file commands.txt which contains list of different commands(
each command is in a new line). Your program should look only for commands "switchport trunk allowed vlan ..."  all other commands should be ignored. (Example of the good command “switchport trunk allowed vlan 1,3,5,11,25,111,23,8”.)

Your program should:

1. print list of all common vlans in all commands, i.e. any good command from commands.txt contains this vlan
2. print list of all unique vlans, i.e for any vlan number from this list there should be only one command in the commands.txt file containing this vlan.
3. the output lists should not contains duplicated entries and should be sorted in ascending order.

Example of the commands.txt:

switchport trunk allowed vlan 1,3,5,11,25,111,23, 8

switchport trunk allowed vlan 1,11,5,8,111,100,77,75

switchport trunk allowed vlan 5,111,77,88,44,8,112,11,8

switchport mode auto

Example of the output:

List_1=[‘5’,’8’,’11’,’111’]

List_2=[‘3’,’23’,’25’,’44’,’75’,’88’ ,’100’,’112’]

'''


import re

regex = re.compile(r'^switchport trunk allowed vlan [\d,]+')

f = open('commands.txt', 'r')
command = f.readlines()
f.close()

#Extract Values
vlan = []
vlanlist = []
for x in command: 
    if regex.match(x):
        vlan.append(re.sub('[^\d,]','',x))

for x in range(len(vlan)):
    vlan[x] = vlan[x].split(',')
    vlan[x] = list(map(int, vlan[x]))
    vlan[x].sort() 
    vlanlist += vlan[x]

#Creating Lists
list1 = set(vlan[0])
for x in range(len(vlan)):
    list1 = list1.intersection(vlan[x])

#print ('vlanlist:', vlanlist)
list2 = []
for x in vlanlist:
    if vlanlist.count(x) == 1:
        list2.append(x)

list1 = list(list1)
list1.sort()
list2.sort()       

#printing lists
print ('Lista 1(all common vlans):', list1)
print ('Lista 2(all unique vlans):', list2)