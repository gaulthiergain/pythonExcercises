"""
Exercice 4 (Cisco Incubator 2017-2018)
Gaulthier Gain 

Libs used:
/
"""

access_template = ['switchport mode access', 'switchport access vlan {}',
 'switchport nonegotiate', 'spanning-tree portfast', 'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q', 'switchport mode trunk',
 'switchport trunk allowed vlan {}']

interface_mode = raw_input('Enter interface mode (access/trunk): ')
interface_type = raw_input('Enter interface type and number: ')

if interface_mode.lower() == 'access':
    vlan_number = raw_input('Enter VLAN number ')
    print 'Interface ' + str(interface_type)
    print access_template[0]
    print access_template[1].replace("{}",vlan_number)
    print access_template[2]
    print access_template[3]
    print access_template[4]
elif interface_mode.lower() == 'trunk':
    allowed_vlans = raw_input('Enter allowed VLANs: ')
    print 'Interface ' +  str(interface_type)
    print trunk_template[0]
    print trunk_template[1]
    print trunk_template[2].replace("{}", allowed_vlans)
else:
    print 'Invalid interface mode'
