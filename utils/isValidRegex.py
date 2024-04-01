import re

def isValidRegex(pattern: str) -> bool:
  try:
    re.compile(pattern)
    return True
  except re.error:
    return False