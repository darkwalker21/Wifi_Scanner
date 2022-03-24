import scapy.all as scapy
import colorama
import time
import re

print(colorama.Fore.RED + r'''   oo_         \\\    ///    \\\    ///       \\\  /// 
  /  _)-<  wWw ((O)  (O))    ((O)  (O))   /)  ((O)(O)) 
  \__ `.   (O)_ | \  / |      | \  / |  (o)(O) | \ ||  
     `. | .' __)||\\//||      ||\\//||   //\\  ||\\||  
     _| |(  _)  || \/ ||      || \/ ||  |(__)| || \ |  
  ,-'   | `.__) ||    ||      ||    ||  /,-. | ||  ||  
 (_..--'       (_/    \_)    (_/    \_)-'   ''(_/  \_) ''')

print(colorama.Fore.GREEN + "\n****************************************************************")
print(colorama.Fore.RED + "\n* Semere Manchawi                                       ")
print("\n* Be An Evil 'Cause Only Bad Guys Can Hack                       ")
print(colorama.Fore.GREEN + "\n****************************************************************")

time.sleep(2)
# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Get the address range to ARP
while True:
    ip_add_range_entered = input(colorama.Fore.RED + "\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(colorama.Fore.GREEN + f"{ip_add_range_entered} is a valid ip address range")
        break


# Try ARPing the ip address range supplied by the user. 
# The arping() method in scapy creates a pakcet with an ARP message 
# and sends it to the broadcast mac address ff:ff:ff:ff:ff:ff.
# If a valid ip address range was supplied the program will return 
# the list of all results.
arp_result = scapy.arping(ip_add_range_entered)