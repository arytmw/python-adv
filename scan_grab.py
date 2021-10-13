from port_scanner import Scanner
from grabber import Grabber

def main():
    ip = input("Enter IP for port scanning and banner grabbing: ")
    scanner = Scanner(ip)
    scanner.scan(1,100)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip,port)
            print(f"{port} -- {grabber.read()}")
            grabber.close()
        except Exception:
            print(f"Error: Port {port} is not responding.")

main() 
