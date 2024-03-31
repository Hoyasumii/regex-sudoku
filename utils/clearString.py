import re

def clearString(alphabetLetter: str):
    pattern = re.compile(r'[a-zA-Z0-9]+')
    return "".join(pattern.findall(alphabetLetter))
