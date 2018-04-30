import Crypto
import paramiko
import getpass
from pick import pick

def valid_ip(potential_ip):
	'''
	Checks to see if an IP address is valid.
	
	Returns either True or False
	
	Taken from a lesson by CCIE emeritus Kirk Byers' (https://pynet.twb-tech.com/) class Python for Network Engineers
	
	'''	

	octets = potential_ip.split('.')
	if len(octets) != 4:
		return False
		
	for i, octet in enumerate(octets):
		try:
			octets [i] = int(octet)
		except ValueError:
			return False
	
	first, second, third, fourth = octets
	if first < 1 or first > 223 or first == 127:
		return False
		
	if first == 169 and second == 254:
		return False

	for octet in (second, third, fourth):
		if octet < 0 or octet > 255:
			return False
			
	else:
		return True

def send_string_and_wait_for_string(command, wait_string, should_print):
	# Function adapted from the work of Tim Mattison, found on his blog at http://blog.timmattison.com/archives/2014/06/25/automating-cisco-switch-interactions/
	# New and improved for Python 3, the primary difference being the += data.decode() statement that otherwise made the recive_buffer nigh unreadable
	# Send the su command
	shell.send(command)

	# Create a new receive buffer
	receive_buffer = ""

	while not wait_string in receive_buffer:
		# Flush the receive buffer
		data = shell.recv(4096)
		receive_buffer += data.decode()

	# Print the receive buffer, if necessary
	if should_print:
		print (receive_buffer)

	return receive_buffer
		
while True:
	# This loop prompts the user to enter an IPv4 address until they enter a valid private IPv4 address
	mgmt_ip = input("Enter the stack management IPv4 address: ")
	if valid_ip(mgmt_ip):
		break
	else:
		print("Not a valid IPv4 Address. Try again.")
		
# Prompts the user for credentials to access the switch mentioned above. Only prompts once currently. If user doesn't have access, the script will terminate with an unhandled error.		
username = input("Username: ")
password = getpass.getpass()

client = paramiko.SSHClient()
# Make sure that we add the remote server's SSH key automatically
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to the client
client.connect(mgmt_ip, username = username, password = password, allow_agent=False, look_for_keys = False)
# Create a raw shell (This creates the 'shell' variable referenced in send_string_and_wait_for_string)
shell = client.invoke_shell()
# Wait for the prompt
send_string_and_wait_for_string("", "#", False)
send_string_and_wait_for_string("terminal length 0\n", "#", False)
# Disable more and primes the receive_buffer in send_string_and_wait_for_string

while True:	
	# Fetches the list of available interfaces on the remote switch and allows the user to select from that list. Loops until an exit string is selected.
	interfaces = send_string_and_wait_for_string("sho run | inc Ethernet\n", "#", False)
	interfaces_list = interfaces.split('\r\n')

	int_prompt = 'Select the interface you would like to configure. \nSelect the "sho" command or the switch hostname to exit.'
	indicator = '==>'
	default_index = 1
	int_option, int_index = pick(interfaces_list, int_prompt, indicator, default_index)
	
	if "Ethernet" not in int_option or "sho" in int_option:
		# Checks to see if the user wants to exit the application
		print ("Exiting application...")
		break
	else:
		# If the user has not elected to exit, prompts the user to select one of the preconfigured interfaces types in the same 'select from list' format. Only executes once and returns to the parent loop.
		int_conf_list = ['Access','ShoreTel Switch','Trunk to MX','Trunk to Wireless Access Point','Guest','Go Back']
		conf_prompt = 'Select the type of configuration for ' + int_option + '.'
		conf_option, conf_index = pick(int_conf_list,conf_prompt,indicator)
		if conf_option == 'Access':
			send_string_and_wait_for_string("conf t\n", "#", False)
			send_string_and_wait_for_string("default " + int_option + "\n", "#", False)
			send_string_and_wait_for_string(int_option + "\n", "#", False)
			send_string_and_wait_for_string("description ///Access Port///\n", "#", False)
			send_string_and_wait_for_string("switchport access vlan 44\n", "#", False)
			send_string_and_wait_for_string("switchport mode access\n", "#", False)
			send_string_and_wait_for_string("switchport nonegotiate\n", "#", False)
			send_string_and_wait_for_string("switchport voice vlan 46\n", "#", False)
			send_string_and_wait_for_string("switchport port-security maximum 2\n", "#", False)
			send_string_and_wait_for_string("switchport port-security\n", "#", False)
			send_string_and_wait_for_string("storm-control broadcast level 65.00\n", "#", False)
			send_string_and_wait_for_string("storm-control multicast level 65.00\n", "#", False)
			send_string_and_wait_for_string("spanning-tree portfast\n", "#", False)
			send_string_and_wait_for_string("ip verify source port-security\n", "#", False)
			send_string_and_wait_for_string("end\n", "#", False)
			input (int_option + ' has been configured as ' + conf_option + '.\nReturning to Interface Select...')
			
		if conf_option == 'ShoreTel Switch':
			send_string_and_wait_for_string("conf t\n", "#", False)
			send_string_and_wait_for_string("default " + int_option + "\n", "#", False)
			send_string_and_wait_for_string(int_option + "\n", "#", False)
			send_string_and_wait_for_string("description ///ShoreTel Switch///\n", "#", False)
			send_string_and_wait_for_string("switchport access vlan 46\n", "#", False)
			send_string_and_wait_for_string("switchport mode access\n", "#", False)
			send_string_and_wait_for_string("switchport nonegotiate\n", "#", False)
			send_string_and_wait_for_string("switchport port-security\n", "#", False)
			send_string_and_wait_for_string("switchport port-security mac-address sticky\n", "#", False)
			send_string_and_wait_for_string("storm-control broadcast level 65.00\n", "#", False)
			send_string_and_wait_for_string("storm-control multicast level 65.00\n", "#", False)
			send_string_and_wait_for_string("spanning-tree portfast\n", "#", False)
			send_string_and_wait_for_string("ip verify source port-security\n", "#", False)
			send_string_and_wait_for_string("end\n", "#", False)
			input (int_option + ' has been configured as ' + conf_option + '.\nReturning to Interface Select...')	
		
		elif conf_option == 'Trunk to MX':
			send_string_and_wait_for_string("conf t\n", "#", False)
			send_string_and_wait_for_string("default " + int_option + "\n", "#", False)
			send_string_and_wait_for_string(int_option + "\n", "#", False)
			send_string_and_wait_for_string("description ///Trunk to MX///\n", "#", False)
			send_string_and_wait_for_string("switchport trunk native vlan 82\n", "#", False)
			send_string_and_wait_for_string("switchport trunk allowed vlan 44,46,50\n", "#", False)
			send_string_and_wait_for_string("switchport mode trunk\n", "#", False)
			send_string_and_wait_for_string("ip dhcp snooping trust\n", "#", False)			
			send_string_and_wait_for_string("end\n", "#", False)
			input (int_option + ' has been configured as ' + conf_option + '.\nReturning to Interface Select...')
			
		elif conf_option == 'Trunk to Wireless Access Point':
			send_string_and_wait_for_string("conf t\n", "#", False)
			send_string_and_wait_for_string("default " + int_option + "\n", "#", False)
			send_string_and_wait_for_string(int_option + "\n", "#", False)
			send_string_and_wait_for_string("description ///AP Port///\n", "#", False)
			send_string_and_wait_for_string("switchport trunk native vlan 82\n", "#", False)
			send_string_and_wait_for_string("switchport trunk allowed vlan 50,55,82\n", "#", False)
			send_string_and_wait_for_string("switchport mode trunk\n", "#", False)
			send_string_and_wait_for_string("switchport nonegotiate\n", "#", False)			
			send_string_and_wait_for_string("end\n", "#", False)
			input (int_option + ' has been configured as ' + conf_option + '.\nReturning to Interface Select...')

		elif conf_option == 'Guest':
			send_string_and_wait_for_string("conf t\n", "#", False)
			send_string_and_wait_for_string("default " + int_option + "\n", "#", False)
			send_string_and_wait_for_string(int_option + "\n", "#", False)
			send_string_and_wait_for_string("description ///Guest Port///\n", "#", False)
			send_string_and_wait_for_string(" switchport access vlan 55\n", "#", False)
			send_string_and_wait_for_string("switchport mode access\n", "#", False)
			send_string_and_wait_for_string("spanning-tree portfast\n", "#", False)
			send_string_and_wait_for_string("end\n", "#", False)
			input (int_option + ' has been configured as ' + conf_option + '.\nReturning to Interface Select...')
		
		else:
			# Allows user to go back to the interface select screen in case they selected an undesired interface.
			input('Exiting menu...')
		
#Joshua Hutchins 2016