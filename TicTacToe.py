grid = [['_','_','_'],['_','_','_'],['_','_','_']]

#Checks if a player has made a line
def line(player):
     line = False
     for i in range(3):
          if grid[i][0] == grid[i][1] == grid[i][2] == player:
               line = True
          if grid[0][i] == grid[1][i] == grid[2][i] == player:
               line = True
     if grid[0][0] == grid[1][1] == grid[2][2] == player:
          line = True
     if grid[0][2] == grid[1][1] == grid[2][0] == player:
          line = True
     return line

#Makes sure a choice is in the grid and whether or not the space is filled
def is_valid(row, col):
     if 0 > row or 2 < row:
          print "Out of bounds"
          return False
     if 0 > col or 2 < col:
          print "Out of bounds"
          return False
     if grid[row][col] != '_':
          print "Cell already taken"
          return False
     return True

def print_grid():
     print ""
     print "  0" + "   " + "1" + "   " + "2"
     print "0 " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2]
     print "  ---------"
     print "1 " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2]
     print "  ---------"
     print "2 " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2]

def main():
     x_turn = True
     turns = 1
     print "Please input choices in the form (row, col)"
     while not line('x') and not line('o') and turns <= 9:
          print_grid()
          
          if x_turn:
               print "X's turn"
          else:
               print "O's turn"

          row, col = input("Where do you want to place your piece? ")
          if is_valid(row, col):
               if x_turn:
                    grid[row][col] = 'x'
               else:
                    grid[row][col] = 'o'
               x_turn = not x_turn
               turns += 1

     print_grid()
     if turns > 9:
          print "Tie game"
     else:
          if x_turn:
               print "O wins"
          else:
               print "X wins"


if __name__ == "__main__":
     main()
