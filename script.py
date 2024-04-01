from simpleForm import Form
from classes import RegexSudoku
from utils import clearTerminal as clear

setupPartOne = Form("Regex Sudoku pt.1")

setupPartOne.add(alphabet={
  "type": str,
  "description": "Alfabeto",
  "default": "ABC"
}, size= {
  "type": int,
  "description": "Tamanho da matriz",
  "min": 4,
  "default": 4
})

setupPartOne()

app = RegexSudoku(list(setupPartOne.values['alphabet'].upper()), setupPartOne.values['size'])

while not app.available:
  setupPartOne.clear()

  controls = [ [None] * app.MATRIX_LENGTH ] * 2

  setupPartTwo = Form("Regex Sudoku pt.2")
  setupPartTwo._values = {}
  setupPartTwo.clear()
  kwargs = {}

  for index in range(2):
    for item in range(app.MATRIX_LENGTH):
      kwargs[f"{index}-{item}"] = {
        "type": str,
        "description": f"Conteúdo da {'coluna' if index == 0 else 'linha'} {item + 1}"
      }
  setupPartTwo.add(**kwargs)

  setupPartTwo()
  del setupPartTwo._values

  data = [[item.upper() for key, item in setupPartTwo.values.items() if key.startswith("0")], [item.upper() for key, item in setupPartTwo.values.items() if key.startswith("1")]]

  app.settingControls(*data)

while not app.checkWin():
  clear()
  if not app.hasEmptyPlaces():
    continueQuestion = input("Você perdeu...\nDeseja continuar? (y/ANY)").lower()
    if (continueQuestion != "y"):
      break

    app.generateContent()

  emptyPositions = app.getEmptyPosition()
  app.build()
  app.insert(emptyPositions[0], emptyPositions[1], input("- Informe o seu valor: "));

clear()
app.build()
print("Você venceu!")