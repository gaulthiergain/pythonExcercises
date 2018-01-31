"""
Exercice 3 (Cisco Incubator 2017-2018)
Gaulthier Gain 

Libs used:
https://docs.python.org/2/library/re.html
"""

import re

filename = 'ShowIpRoute.txt'

# Regex used. Note that only the dynamic routing protocol are searched
pattern=re.compile(r'^(?P<Protocol>R|B|D|EX|O|IA|N1|N2|E|O E2|O E1|i L1|i L2|i|ia)\s+(?P<Prefix>\b\d[\d|\.]+\d\b)\s+(?P<AD>.*)\s+via\s+(?P<Nhops>\b\d[\d|\.]+\d\b).*\s+(?P<LU>\b\d[\d|\:]+\d\b),\s+(?P<Interface>.*)$')

# Dictonnary that maps symbols and labels
dic={'L':'local', 'C':'connected', 'S':'static', 'R':'RIP', 'M':'Mobile',
	'B':'BGP', 'D':'EIGRP', 'EX':'EIGRP external', 'O':'OSPF', 
	'IA':'OSPF inter area', 'N1':'OSPF NSSA external type 1',
	'N2':'OSPF NSSA external type 2', 'O E2':'OSPF external type 2',
	'i L1':'IS-IS level-1', 'E':'EGP', 'O E1':'OSPF external type 1',
	'i L2':'IS-IS level-2', 'i':'IS-IS', 'ia':'IS-IS inter area',
	'*':'candidate default', 'U ':'per-user static route',
	'o ':'ODR', 'P ':'periodic downloaded static route', 'H ':'NHRP',
	'l ':'LISP', 'a ':'application route', '+':'replicated route',
	'%':'next hop override'}

try:
	file = open(filename, 'r')
	while True:
			line = file.readline()
			if (line == ''):
				break

			# Match only dynamic routing protocols
			result = pattern.match(line)
			if(result):
				print 'Protocol: {:>30}'.format(dic[result.group('Protocol')])
				print 'Prefix: {:>32}'.format(result.group('Prefix'))
				print 'printAD/Metric: {:>24}'.format(result.group('AD'))
				print 'Next-hop: {:>30}'.format(result.group('Nhops'))
				print 'Last Update: {:>27}'.format(result.group('LU'))
				print 'Outbound interface: {:>20}'.format(result.group('Interface'))
				print '----------------------------------------'

except IOError:
	print 'The file couldn\'t be found'
	exit()
