import ipaddress
import socket

def print_banner():
    print("=" * 40)
    print("      CyberLab Port Scanner")
    print("=" * 40)

print_banner()

def get_ip():
    target = input("\nEnter an IP address: ")
    return target

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
    

target = get_ip()

try:
    ip = ipaddress.ip_address(target)
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


except ValueError:
    print("\nInvalid IP address.")

