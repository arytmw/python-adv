import socket

class Scanner:
    def __init__(self,ip):
        self.ip = ip
        self.open_ports = []

    def add_port(self,port):
        self.open_ports.append(port)

    def scan(self,lowerport,upperport):
        for port in range(lowerport,upperport+1):
            if self.is_open(port):
                self.add_port(port)

    def is_open(self,port):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((self.ip,port))
        s.close()
        return result == 0

#def main():
#    ip = input("Enter IP to port scan: ")
#    scanner = Scanner(ip)
#    scanner.scan(1,500)
#    print(scanner.open_ports)
#
#main()
