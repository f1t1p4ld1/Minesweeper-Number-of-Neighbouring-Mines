
def getNeighbouringMines(minesweeperBoard, row, column):
  adjacentList = []
  numRows = len(minesweeperBoard)
  numColumns = len(minesweeperBoard[0])
  locations = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  counterMines = 0
  for location in locations:
    rowCordinate = row + location[0]
    columnCordinate = column + location[1]
    if (0 <= rowCordinate < numRows and 0 <= columnCordinate < numColumns):
      adjacentList.append(minesweeperBoard[rowCordinate][columnCordinate])
      counterMines = adjacentList.count(9)  
  return counterMines


def updateMinesweeperBoard(minesweeperBoard):
  for rowLocation in range(len(minesweeperBoard)):
    for columnLocation in range(len(minesweeperBoard[0])):      
        counterMines = getNeighbouringMines(minesweeperBoard, rowLocation, columnLocation)
        if minesweeperBoard[rowLocation][columnLocation] == 0:
          minesweeperBoard[rowLocation][columnLocation] = counterMines
  print(f'{minesweeperBoard[0]}\n{minesweeperBoard[1]}\n{minesweeperBoard[2]}\n{minesweeperBoard[3]}')


def convertMine(minesweeperBoard):
    for rawMines in range(len(minesweeperBoard)):
        for colMines in range(len(minesweeperBoard[0])):
            if minesweeperBoard[rawMines][colMines] == 1:
              minesweeperBoard[rawMines][colMines] = 9
    return updateMinesweeperBoard(minesweeperBoard)


minesweeperBoard = [
  [0, 1, 0, 0],
  [0, 0, 1, 0],
  [0, 1, 0, 1], 
  [1, 1, 0, 0]
]

if __name__ == "__main__":
  print("Minesweeper - Number of Neighbouring Mines!")
  print("Python 3.10.14")
  print('Minesweeper Input:')
  print(f'{minesweeperBoard[0]}\n{minesweeperBoard[1]}\n{minesweeperBoard[2]}\n{minesweeperBoard[3]}')
  print('Minesweeper Ouput:')
  convertMine(minesweeperBoard)