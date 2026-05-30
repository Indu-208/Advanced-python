import re
email = "test@gmail.com"
pattern = r'@gmail\.com$'
if re.search(pattern, email):
    print("Valid Gmail")
else:
    print("Invalid")