import ipaddress
import socket

MAX_ATTEMPTS = 3


def print_banner():
    print("=" * 40)
    print("      CyberLab Port Scanner")
    print("=" * 40)

def get_ip():
    for attempt in range(MAX_ATTEMPTS):
        target = input("\nEnter an IP address: ")

        try:
            ip = ipaddress.ip_address(target)
            return ip
        
        except ValueError:
            remaining = MAX_ATTEMPTS - attempt - 1
            attempt_text = "attempt" if remaining == 1 else "attempts"
        
        if remaining > 0:
            print(f"\nInvalid IP address. {remaining} {attempt_text} remaining.")
        else:
            print("\nInvalid IP address. Maximum attempts reached. Exiting.")
            exit()
    

def scan_port(ip, port, services):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    result = sock.connect_ex((str(ip), port))

    service = services.get(port, "UNKNOWN")

    if result == 0:
        print(f"Port {port} ({service}) is OPEN")
    else:
        print(f"Port {port} ({service}) is CLOSED or FILTERED")
    
    sock.close()

print_banner()

ip = get_ip()
print(f"\nTarget selected: {ip}")
ports = [20,21,22,23,53,67,68,69,80,110,123,143,161,389,443,445,3389]

services = {
    20: "FTP-Data",
    21: "FTP",        
    22: "SSH",
    23: "Telnet",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    123: "NTP",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

for port in ports:    
    scan_port(ip, port, services)


