import ipaddress
import socket

print("=" * 40)
print("      CyberLab Port Scanner")
print("=" * 40)

target = input("\nEnter an IP address: ")

try:
    ip = ipaddress.ip_address(target)
    print(f"\nTarget selected: {ip}")

    ports = [22, 80, 443]

    for port in ports:    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        
        result = sock.connect_ex((str(ip), port))

        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED or FILTERED")
    
        sock.close()


except ValueError:
    print("\nInvalid IP address.")
