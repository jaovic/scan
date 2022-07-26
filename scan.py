import sys
import socket

def scan(hosts, ports):
    for port in ports:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.settimeout(0.5)
        code = c.connect_ex((hosts, int(port)))
        if code == 0:
            print(f'[+] {hosts}:{port} is Open')

if __name__ == '__main__':
    try:
        if len(sys.argv) >=2:
            hosts = sys.argv[1] 
            if len(sys.argv) >=3:
                port_list = sys.argv[2].split(',')
            else:
                port_list = [21, 22, 23, 25, 80, 443, 445, 8080, 8443, 9090, 9999, 10000, 3306, 139, 135]

            scan(hosts, port_list)
        else:
            print('Usage: python3 scan.py <host> <port> \n'
            '<host> = IP address or hostname \n' 
            '<port> = port number or port range')

    except Exception as err:
        print('[-] Usage: python3 scan.py <host> <port>')
        print('[-] Example: python3 scan.py localhost 21,22,23,25,80,443,445,8080,8443,9090,9999,10000,3306,139,135')