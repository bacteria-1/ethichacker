import port


target_ip = input('[+] * Enter Target to scan for vulnerable open ports: ')
port_number = int(input('[+] * Enter amount of ports to be scanned: '))
vul_file = input('[+] * Enter path to the file with vulnerable softwares: ')
print('\n')

target = port.PortScan(target_ip, port_number)
target.scan()
