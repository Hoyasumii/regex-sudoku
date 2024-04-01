if __name__=="__main__":
  import sys
  sys.path.append("\\".join(sys.path[0].split('\\')[:-1]))

from tabulate import tabulate
from typing import Union
import re
from utils import isValidRegex, clearString

class RegexSudoku:
  _available: bool = False
  rows: list[str] = []
  columns: list[str] = []
  content: list[list[Union[str, None]]] = None

  def _alphabetValidator(self, alphabet: list[str]) -> None:
    for index in range(len(alphabet)):
      alphabet[index] = clearString(alphabet[index])

      if (len(alphabet[index]) != 1):
        raise Exception("As letras do alfabeto devem ter apenas 1 de comprimento")
      
  def _valideControl(self, pattern: str) -> bool:
    pattern = list(clearString(pattern))

    for item in pattern:
      if (not item in self.alphabet):
        return False
      
    return True
  
  def _generateContent(self) -> None:
    self.content = [ [None] * self.MATRIX_LENGTH ] * self.MATRIX_LENGTH

  def __init__(self, alphabet: list[str],matrixLength: int = 2) -> None:
    self.MATRIX_LENGTH = matrixLength

    self._alphabetValidator(alphabet)

    self.alphabet = alphabet
    self._generateContent()
    self.content = [ [None, "A"], ["B", "C"] ]
  
  def settingControls(self, *data: list[list[str]]) -> bool:
    
    if (len(data) != self.MATRIX_LENGTH):
      return False

    for controls in data:
      if (len(controls) != self.MATRIX_LENGTH):
        return False
      
      for item in controls:
        if (not self._valideControl(item)):
          return False

        if (not isValidRegex(item)):
          return False
        
        if (len(self.rows) < self.MATRIX_LENGTH):
          self.rows.append(item)

        else:
          self.columns.append(item)

    self._available = True
    return True
  
  def build(self) -> None:
    if (not self._available):
      raise Exception("Os controles ainda não foram definidos.")
    displayableContent = []

    for item in range(len(self.rows)):
      displayableContent.append([ self.rows[item], *self.content[item] ])
    
    print(tabulate(displayableContent, [" "] + self.columns, tablefmt="fancy_grid"))
  
  def getRowContent(self, index: int) -> str:
    if (index > self.MATRIX_LENGTH - 1 or index < 0):
      raise Exception("Linha inválida")
    
    return "".join(self.content[index])

  def getColumnContent(self, index: int) -> str:
    if (index > self.MATRIX_LENGTH - 1 or index < 0):
      raise Exception("Coluna inválida")
    
    return "".join([ item[index] if item[index] is not None else "" for item in self.content ])

  def insert(self, row: int, column: int, content: str) -> bool:
    content = content.upper()

    for index in [row, column]:
      if (index > self.MATRIX_LENGTH - 1 or index < 0):
        raise Exception("Posição inválida")

    if (len(content) != 1):
      return False

    if (not content in self.alphabet):
      return False

    if (self.content[row][column] != None):
      return False
    
    self.content[row][column] = content
    return True
  
  def hasEmptyPlaces(self) -> bool:
    for row in self.content:
      for item in row:
        if (item is None):
          return True
    return False
  
  def checkWin(self) -> bool:
    for item in range(self.MATRIX_LENGTH):
      rowPattern = re.compile(self.rows[item])
      columnPattern = re.compile(self.columns[item])

      if rowPattern.fullmatch(self.getRowContent(item)) is None:
            return False
      if columnPattern.fullmatch(self.getColumnContent(item)) is None:
          return False
    
    return True
  
if __name__=="__main__":
  app = RegexSudoku(["A", "B", "C"], 2)
  app.settingControls(["A*", ("(B|C)*")], ["AB", "[CA]*"])
  # print(app.getRowContent(1))
  app.insert(0, 0, "A")
  # print(app.getColumnContent(0))
  print(app.checkWin())
  app.build()