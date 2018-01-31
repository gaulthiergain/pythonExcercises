"""
Exercice 2 (Cisco Incubator 2017-2018)
Gaulthier Gain
    
Libs used:
https://docs.python.org/2/library/re.html
https://docs.python.org/2/library/collections.html#collections.Counter
"""

import re
from collections import Counter

filename = 'commands.txt'
pattern = r'(?:^switchport\s+trunk\s+allowed\s+vlan\s+)(?P<vlan>[\d,]+)'

list_vlans = list()
common_vlans = list()
unique_vlans = list()

try:
    file = open(filename, 'r')
    while True:
        line = file.readline()
        if (line == ''):
            break

        # Use regex and then split each digit into a list
        m = re.search(pattern, line)
        if(m):
            for vlan_digit in m.group('vlan').split(","):
                list_vlans.append(vlan_digit)
except IOError:
    print 'The file couldn\'t be found'
    exit()

# Count the number of vlans in the list using a Counter object
for vlan in Counter(list_vlans).iteritems():
    if vlan[1] == 1:
        # vlan appears once
        unique_vlans.append(vlan[0])
    else:
        # several vlans
        common_vlans.append(vlan[0])

# Sort lists by ascending order
common_vlans.sort(key=int)
unique_vlans.sort(key=int)

print 'List_1 =' + str(common_vlans)
print 'List_2 =' + str(unique_vlans)
