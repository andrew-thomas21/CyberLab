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

Session 2 – Functions, Refactoring, and Input Validation

## Date: July 7, 2026

## Objective

Continue developing the CyberLab Port Scanner by improving its organization, making the code more reusable, and adding input validation to create a more professional and user-friendly application.

# Concepts Learned
Functions

Today I learned that functions allow a program to be broken into smaller pieces that each perform one specific task. Instead of writing one long program, I created separate functions for printing the banner, obtaining a valid IP address, and scanning an individual port. This made the program much easier to read and understand.

# Functions created:

print_banner()
get_ip()
scan_port()
Function Parameters

I learned that parameters provide information to a function so it knows what to work with. Instead of hardcoding an IP address or port number inside a function, values are passed in when the function is called.

Example:

scan_port(ip, port, services)

This allows the same function to be reused for any IP address, port, or service dictionary.

# Return Values

I learned that functions can return information back to the program. Instead of only asking the user for input, get_ip() now validates the address and returns a validated IP object. This allowed me to remove duplicate validation code from the main program.

# Refactoring

Today was my first experience with refactoring. I learned that refactoring improves the structure and readability of code without changing how the program behaves.

# Refactoring completed:

Moved banner printing into print_banner()
Moved user input into get_ip()
Moved socket scanning into scan_port()
Removed duplicate IP validation from the main program

The scanner performs the same task as before but is much more organized.

# Input Validation

I implemented a retry system using a constant:

MAX_ATTEMPTS = 3

The scanner now:

Gives the user three attempts to enter a valid IP address.
Displays the number of remaining attempts after an invalid entry.
Exits the program after the final failed attempt.

This also introduced the concept of avoiding "magic numbers" by defining a constant instead of hardcoding the value throughout the program.

# Python Concepts Reinforced

## Today's session reinforced several important Python concepts:

Functions
Parameters
Return values
Constants
for loops
range()
try / except
Variables created automatically inside loops
Program flow
Code organization
Debugging Experience

Several bugs were encountered during development.

# Problems solved included:

Banner printed at the bottom because the function call was placed in the wrong location.
Typographical error in the service variable.
Typographical error using remain instead of remaining.
Learned that loop variables such as attempt are automatically managed by Python.
Learned that removing a try block requires unindenting the code that belonged to it.
Corrected duplicate IP validation after moving validation into get_ip().

Each bug helped reinforce the importance of reading the program flow carefully instead of assuming Python was doing something wrong.

### Biggest Takeaways

The biggest lesson from today's session was understanding that functions improve much more than code organization. They reduce duplicate code, make debugging easier, and create reusable pieces of software.

I also learned that parameters allow functions to be flexible, while return values allow them to communicate information back to the main program.

Another important lesson was learning to think about how another programmer would read my code. Organizing functions at the top of the file and keeping the main program at the bottom makes the code much easier to understand and maintain.

Git Commits
Refactor scanner into reusable functions
Add IP validation with retry limit
Reflection

Today's session felt very different from simply learning Python syntax. Instead of focusing on individual lines of code, I spent much more time thinking about how the program should be organized and why certain design decisions make software easier to read and maintain. Breaking the scanner into functions showed me how professional software is built one small piece at a time rather than as one large block of code.

One of the biggest things I learned was that writing software is not just about making it work. It is also about making it understandable for the next person who reads the code, including my future self. Refactoring the scanner without changing its behavior demonstrated how software can continuously improve while remaining functional.

I also became much more comfortable debugging my own code. Rather than immediately assuming something was wrong with Python, I learned to follow the flow of execution and identify where I had introduced mistakes. By the end of the session, I found myself asking questions about software design and architecture instead of just Python syntax, which showed me that I am beginning to think more like a software developer than someone simply learning a programming language.

## Next Session Goals

- Add scan timing using the `time` module.
- Count open and closed ports.
- Save scan results to a text file.
- Continue refactoring the scanner to improve readability.