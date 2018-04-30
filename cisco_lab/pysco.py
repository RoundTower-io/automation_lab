import json
import xmltodict
from pycsco.nxos.device import Device

switch = Device(ip='192.168.200.50',username='cisco',password='!cisco123!')
get_sh_ver = switch.show('show version') 
sh_ver_dict = xmltodict.parse(get_sh_ver[1])
simple = sh_ver_dict['ins_api']['outputs']['output']['body']
print simple['rr_sys_ver']
#6.1(2)I3(1)
print simple['kick_file_name']
#bootflash:///n9000-dk9.6.1.2.I3.1.bin

commands = ['interface Ethernet1/1', 'no switchport', 'ip address 1.1.1.1/24', 'shutdown']
cmds_to_string = ' ; '.join(commands)
switch.config(cmds_to_string)

status = switch.config(cmds_to_string)