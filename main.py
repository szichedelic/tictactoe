from game import Game

def tictactoe():
    g = Game()
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸")
    print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")
    print("<3 <3 <3 WELCOME TO TIC TAC TOE <3 <3 <3")
    print("♫♪.ılılıll|̲̅̅●̲̅̅|̲̅̅=̲̅̅|̲̅̅●̲̅̅|llılılı.♫♪")
    print("°º¤ø,¸¸,ø¤º°`°º¤ø,¸,ø¤°º¤ø,¸¸,ø¤º°`°º¤ø,¸")

    while not g.isOver():
        print("Current Game Board (#{}):".format(g.turnNo))
        print(g)

        if g.turnNo % 2 == 0:
            # player's turn
            print("Input space you'd like to fill.")
            x = int(input("X-Coordinate: "))
            y = int(input("Y-Coordinate: "))
            
            while x not in range(3):
                print("Invalid input for X.")
                print("Please choose a number between 0 and 2.")
                x = int(input("X-Coordinate: "))
            
            while y not in range(3):
                print("Invalid input for Y.")
                print("Please choose a number between 0 and 2.")
                y = int(input("Y-Coordinate: "))

            while g.board[x][y] in {"X", "O"}:
                print("Space is taken.  Please choose another.")
                x = int(input("X-Coordinate: "))
                y = int(input("Y-Coordinate: "))

            g.makeMove(x, y, g.human)
        else:
            # cpu's turn
            print("CPU is now making a turn.")
            [x, y] = g.findMove()
            g.makeMove(x, y, g.cpu)

if __name__ == "__main__":
    tictactoe()