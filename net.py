#!/usr/bin/python3

import nmap
import pyfiglet 


A =  pyfiglet.figlet_format("Automated Network Mapper...")
print(A)

print(""" 
...................................................................................
                Author = Sahil Kute
                Github = https://github.com/Sahilkute
                Linkdin = www.linkedin.com/in/sahil-kute-83a797240/
...................................................................................
      """)


scanner = nmap.PortScanner()

print("Welcome to simple nmap scanning tool!!")
print("- - - - - - - - - - - - - - - - - - - - - - - ")

ip_addr = input("Please enter the IP Address to scan: ")
print("The IP entered is:", ip_addr)

print("Type of IP entered is:", type(ip_addr))
resp = input("""\nPlease Enter the type of Scan you want to Perform:
    1. SYN Scan
    2. UDP Scan
    3. Comprehensive Scan\n""")

print("You have selected:", resp)

resp_dict = {'1': ['-sS -v', 'tcp'], '2': ['-sU -v', 'udp'], '3': ['-sS -vv -O -A -sC', 'tcp']}

if resp not in resp_dict.keys():
    print("Please Enter a valid option!")
else:
    print("Nmap Version", scanner.nmap_version())
    scanner.scan(ip_addr, arguments=resp_dict[resp][0])

if scanner[ip_addr].state() == 'up':
    print("\nHost is up. Scan Result:")

    for proto in scanner[ip_addr].all_protocols():
        print("\nProtocol: {}".format(proto))
        print("Open Ports: {}".format(','.join(map(str, scanner[ip_addr][proto].keys()))))

    for port, info in scanner[ip_addr][proto].items():
        print("\nPort: {}\nService: {}\nState: {}".format(port, info['name'], info['state']))
