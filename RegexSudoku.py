from tabulate import tabulate
from typing import Union
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
      
  def _valideControl(self):
    pass

  def __init__(self, alphabet: list[str],matrixLength: int = 2) -> None:
    self.MATRIX_LENGTH = matrixLength

    self._alphabetValidator(alphabet)

    self.alphabet = alphabet
    self.content = [ [None] * self.MATRIX_LENGTH ] * self.MATRIX_LENGTH
    self.content = [ [None, "A"], ["B", "C"] ]
  
  def settingControls(self, *data: list[list[str]]) -> bool:
    
    if (len(data) != self.MATRIX_LENGTH):
      return False

    for controls in data:
      if (len(controls) != self.MATRIX_LENGTH):
        return False
      
      for item in controls:
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
    #TODO: Verificar se o content além de ter len de 1, ele também está no alfabeto 
    for index in [row, column]:
      if (index > self.MATRIX_LENGTH - 1 or index < 0):
        raise Exception("Posição inválida")

    if (self.content[row][column] != None):
      return False
    
    self.content[row][column] = content
    return True
    
  
if __name__=="__main__":
  app = RegexSudoku(["A", "B", "C"], 2)
  app.settingControls(["A*", ("(B|C)*")], ["AB", "[CA]*"])
  print(app.getRowContent(1))
  print(app.getColumnContent(0))
  app.insert(0, 0, "A")
  app.build()