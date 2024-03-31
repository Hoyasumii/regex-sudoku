import re

def isValidRegex(pattern: str) -> bool:
  try:
    re.compile(pattern)
    # print(data.findall("AB"), pattern)
    # print(data, data.match("A"), pattern)
    return True
  except re.error:
    return False