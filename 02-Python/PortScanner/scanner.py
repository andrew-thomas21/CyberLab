import ipaddress

print("=" * 40)
print("      CyberLab Port Scanner")
print("=" * 40)

target = input("\nEnter an IP address: ")

try:
    ip = ipaddress.ip_address(target)
    print(f"\nTarget selected: {ip}")

except ValueError:
    print("\nInvalid IP address.")