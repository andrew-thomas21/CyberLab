# Programming Journal

---

# July 6, 2026

## Project
CyberLab - Python Port Scanner

## What I Built
- Created my first TCP port scanner in Python.
- Validated IPv4 and IPv6 addresses.
- Scanned multiple TCP ports using sockets.
- Added common service names using a dictionary.
- Learned how to safely handle unknown ports with `.get()`.

## Concepts Learned

### Lists
- Lists store multiple values.
- I used a list to hold the ports I wanted to scan.

Example:
```python
ports = [20, 21, 22, 53, 80, 443]
```

### For Loops
- A `for` loop repeats the same code for every item in a list.
- The variable `port` changes each iteration.

### Dictionaries
- Dictionaries store key/value pairs.
- I used a dictionary to map port numbers to service names.

Example:
```python
services = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}
```

### `.get()`
- `.get()` safely looks up a value in a dictionary.
- If the key doesn't exist, it returns a default value instead of crashing.

Example:
```python
services.get(port, "UNKNOWN")
```

### Sockets
- A socket is a software endpoint used to communicate over a network.
- My scanner uses a TCP socket to determine if a port is open.

## Biggest Takeaway

Today I learned that good programming isn't about memorizing syntax.
It's about solving problems with the right tools, like loops, dictionaries, and sockets.