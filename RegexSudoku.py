from tabulate import tabulate
from typing import Union
from utils import isValidRegex

class RegexSudoku:
  _available: bool = False
  rows: list[str] = []
  columns: list[str] = []
  content: list[list[Union[str, None]]] = None

  def __init__(self, alphabet: list[str],matrixLength: int = 2):
    self.matrixLength = matrixLength
    self.content = [ [None] * self.matrixLength ] * self.matrixLength
    self.content = [ ["A", "A"], ["B", "C"] ]
  
  def settingControls(self, *data: list[list[str]]) -> bool:
    
    if (len(data) != self.matrixLength):
      return False

    for controls in data:
      if (len(controls) != self.matrixLength):
        return False
      
      for item in controls:
        if (not isValidRegex(item)):
          return False
        
        if (len(self.rows) < self.matrixLength):
          self.rows.append(item)

        else:
          self.columns.append(item)

    self._available = True
    return True
  
  def build(self) -> Union[Exception, None]:
    if (not self._available):
      raise Exception("Os controles ainda não foram definidos.")
    displayableContent = []

    for item in range(len(self.rows)):
      displayableContent.append([ self.rows[item], *self.content[item] ])
    
    print(tabulate(displayableContent, [" "] + self.columns, tablefmt="fancy_grid"))
  
  def getRowContent(self, index: int):
    pass

  def getColumnContent(self, index: int):
    pass

  def insert(self, row: int, column: int, content: str) -> bool:
    pass
    
  
if __name__=="__main__":
  app = RegexSudoku([], 2)
  app.settingControls(["A*", ("(B|C)*")], ["AB", "[CA]*"])
  app.build()