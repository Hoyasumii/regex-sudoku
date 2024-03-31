import os

def clearTerminal() -> None:
  os.system('cls' if os.name == 'nt' else 'clear')