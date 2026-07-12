import ipaddress
import socket
import time
from datetime import datetime

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

def get_output_mode():
    while True:
        print("\nSelect Output Mode:")
        print("1) Normal (Open ports only)")
        print("2) Verbose (Show all ports)")

        output_choice = input("Choice: ")

        if output_choice == "1":
            return False, "Normal"
        
        elif output_choice == "2":
            return True, "Verbose"
        
        else:
            print("Invalid choice. Enter 1 or 2.")    

def scan_port(ip, port, services, verbose):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.5)

    result = sock.connect_ex((str(ip), port))

    service = services.get(port, "UNKNOWN")

    if result == 0:
        print(f"Port {port} ({service}) is OPEN")
        sock.close()
        return True
    else:
        if verbose:
            print(f"Port {port} ({service}) is CLOSED or FILTERED")
        sock.close()
        return False    

print_banner()

ip = get_ip()
print(f"\nTarget selected: {ip}")

print("\nSelect Scan Type:")
print("1) Quick Scan (17 common ports)")
print("2) Full Scan (Ports 1-1024)")
print("3) Custom Port Scan")

choice = input("Choice: ")

if choice == "1":
    print("Quick Scan selected.")
    scan_type = "Quick"
    ports = [20,21,22,23,53,67,68,69,80,110,123,143,161,389,443,445,3389]

elif choice == "2":
    print("Full Scan selected.")
    scan_type = "Full"
    ports = range(1, 1025)

elif choice == "3":
    print("Custom Port selected.")
    scan_type = "Custom Port"

    while True:
        port_input = input("Enter Port Number: ")

        try:
            port = int(port_input)

            if 1 <= port <= 65535:
                ports = [port]
                break

            print("Invalid port number. Enter a value between 1 and 65535.")

        except ValueError:
            print("Invalid input. Please enter a port number between 1 and 65535.")    


else:
    print("Invalid choice. Exiting.")
    exit()

verbose, output_mode = get_output_mode()

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

open_ports = []

start_time = time.time()

for port in ports:
    if scan_port(ip, port, services, verbose):
        open_ports.append(port)

end_time = time.time()
elapsed_time = end_time - start_time

with open("scan_results.txt", "w") as report:
    report.write("=" * 40 + "\n")
    report.write("CyberLab Port Scanner Report\n")
    report.write("=" * 40 + "\n")
    report.write(
    f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
)
    report.write(f"Target: {ip}\n\n")
    report.write(f"Scan Type: {scan_type}\n")
    report.write(f"Scan Type: {scan_type}\n")
    report.write(f"Output Mode: {output_mode}\n\n")

    for port in open_ports:
        service = services.get(port, "UNKNOWN")
        report.write(f"Port {port} ({service}) OPEN\n")

    report.write("\n")
    report.write(f"Ports scanned: {len(ports)}\n")
    report.write(f"Open ports: {len(open_ports)}\n")
    report.write(f"Time elapsed: {elapsed_time:.2f} seconds\n")
    

print("\n" + "=" * 40)
print("Scan Summary")
print("=" * 40)
print(f"Target: {ip}")
print(f"Scan Type: {scan_type}")
print(f"Output Mode: {output_mode}\n\n")
print(f"Ports scanned: {len(ports)}")
print(f"Open ports found: {len(open_ports)}")
print(f"Time elapsed: {elapsed_time:.2f} seconds")
print("Results saved to scan_results.txt")

