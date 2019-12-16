# Password Checker
# At least 8 characters
# Contain lowercase and uppercase letters, numbers and $%#@ symbols
# Must end with a number (This is a strong restriction not usually seen in real scenarios)

import re

# Regular expression looking for strong password
pattern = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password = 'adf3asd#%@4'

check = pattern.fullmatch(password)
print(check)