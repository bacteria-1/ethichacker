import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 scanning Target] ' + str(target))
    for port in range(1, 500):
        banner = scan_port(converted_ip, port)
        if banner:
            print('[+] Open port ' + str(port) + ' : ' + str(banner))


def get_banner(s):
    return s.recv(1024).decode().strip()


def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        result = sock.connect_ex((ipaddress, port))
        if result == 0:
            try:
                sock.send(b'Hello\r\n')
                banner = get_banner(sock)
                return banner
            except:
                return "Open port"
        sock.close()
    except socket.error:
        return "Couldn't connect to the server."


if __name__ == "__main__":
    targets = input('[+] Enter target(s) to scan (split multiple targets with a comma): ')
    if ',' in targets:
        for ip_add in targets.split(','):
            print("Scanning target:", ip_add)  # Debug print
            scan(ip_add.strip())
    else:
        print("Scanning target:", targets)  # Debug print
        scan(targets)
