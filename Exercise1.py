
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