"""
Exercice 1 (Cisco Incubator 2017-2018)
Gaulthier Gain 

Libs used:
https://docs.python.org/3/library/ipaddress.html
"""

import ipaddress

"""
Check the validity of mask
"""
def checkMask(mask):
	try:
		mask_number = int(mask.split('/')[1])
	except:
		return False

	if mask_number < 1 or mask_number > 32:
		return False
	return True

"""
Check the validity of ip address
"""
while True:
	ip_address = raw_input("Enter Ip address: ")
	try:
		#Use ipaddress module to check the validity of ip address
		ip_address = unicode(ip_address, "UTF-8")
		ip_address = ipaddress.ip_address(ip_address)
		break
	except ValueError:
		print("Invalid IP address format")
	

while True:
	ip_mask = raw_input("Enter subnet mask in decimal format: ")
	try:
		if(not checkMask(ip_mask)):
			#Raise exception if the mask is invalid
			raise Exception('Invalid Mask Exception')
		break
	except:
			print("Subnet mask is invalid")

print('{:8}'.format(' ') .join(x for x in str(ip_address).split('.')))
print(' ' .join(format(int(x), '08b') for x in str(ip_address).split('.')))

ip_network = ipaddress.ip_network(unicode(str(ip_address) + ip_mask), strict=False)
print ("network address is: "+ str(ip_network))
print("broadcast address is: " + str(ip_network.broadcast_address) + ip_mask)