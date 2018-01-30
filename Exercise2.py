"""
Exercice 2 (Cisco Incubator 2017-2018)
Gaulthier Gain 

Libs used:

"""

import re
from collections import Counter

filename = 'commands.txt'
pattern = r'(?:^switchport\s+trunk\s+allowed\s+vlan\s+)(?P<vlans>[\d,]+)'

listVlans = list()
common_vlans = list()
unique_vlans = list()

try:
	file = open(filename, 'r')
	while True:
			line = file.readline()
			if (line == ''):
				break
			
			m=re.search(pattern, line)
			if(m):
				for vlan_digit in m.group('vlans').split(","):
					listVlans.append(vlan_digit)
except IOError:
	print 'The file couldn\'t be found'
	exit()

counter = Counter(listVlans)
for vlan in counter.iteritems():
	if vlan[1] == 1:
		unique_vlans.append(vlan[0])
	else:
		common_vlans.append(vlan[0])

common_vlans.sort(key=int)
unique_vlans.sort(key=int)

print "List_1 =", common_vlans
print "List_2 =", unique_vlans