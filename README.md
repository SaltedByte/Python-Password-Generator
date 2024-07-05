# Password Generator

## Overview
This is a python project that will generate a unique password upon a users request.  The user has the ability to adjust arguments passed to the generator to comply with unique password requirements for different websites.  Things such as length and invalid characters can be defined.

## Features
You can pass through a few arguments to your password to better align with unique password requirements by defining invalid characters and setting its length.

```
usage: main.py [-h] [length] [invalidChar]

Password Generator capable of creating passwords with unique requirements.

positional arguments:
  length       The length of the password (default: 16)
  invalidChar  List any characters that should not be included in the generated password.

options:
  -h, --help   show this help message and exit
```

for example, `python main.py 8 qwertyuiopasdfghjklzxcvbnm` would return a 8 character long password without any lowercase letters.

## Feature Roadmap
- [x] Allow args to be passed through to specify length and invalid characters to meet unique webpage requirements
- [ ] Add more options like using dictionary words instead of pseudorandom characters
- [ ] Implement a password strength score
- [ ] Display information of how long it would take a computer to crack the password
- [ ] Create a webpage to generate a password with a UI
- [ ] Create an API for password generation

## Skills Demonstrated
As this is a project with the goal of demonstrating python skills, here are the skills that are demonstrated in this project:
- Command-line Argument Parsing (with documentation)
- Using the Random module
- String and List manipulation
