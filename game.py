
import numpy as np

class Game():
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        self.human = "X"
        self.cpu = "O"
        self.turnNo = 0
        self.winner = None
    
    def __str__(self):
        boardStr = "\n"
        boardStr += "\t {}  |   {}  |   {}".format(
            self.board[0][0],
            self.board[0][1],
            self.board[0][2]
        )
        boardStr += "\n"
        boardStr += "\t {}  |   {}  |   {}".format(
            self.board[1][0],
            self.board[1][1],
            self.board[1][2]
        )
        boardStr += "\n"
        boardStr += "\t {}  |   {}  |   {}".format(
            self.board[2][0],
            self.board[2][1],
            self.board[2][2]
        )
        return boardStr
        
    # General function to check board state to see if there is a winner.
    # Will also set the winner, if specified.  This is kept false if we are
    # checking temporary board states when trying to find the best move.
    def isWon(self, board, setWinner = False, returnWinner = False):
        # Check for row wins
        for row in board:
            rowSet = set(row)

            if len(rowSet) == 1 and rowSet != {"-"}:
                winner = self._identifyWinner(rowSet)
                if setWinner:
                    self.winner = winner
                
                if returnWinner:
                    return winner

                return True

        # Check for column wins, transpose and use row technique
        for col in np.transpose(board):
            colSet = set(col)

            if len(colSet) == 1 and colSet != {"-"}:
                winner = self._identifyWinner(colSet)
                if setWinner:
                    self.winner = winner

                if returnWinner:
                    return winner
                return True
        
        # Check for diagonal wins
        diagSet = set([board[x][x] for x in range(len(board))])
        if len(diagSet) == 1 and diagSet != {"-"}:
            winner = self._identifyWinner(diagSet)
            if setWinner:
                self.winner = winner
            
            if returnWinner:
                return winner
            return True
        
        # Check for diagonal wins
        diagSet = set([board[x][len(board) - x - 1] for x in range(len(board))])
        if len(diagSet) == 1 and diagSet != {"-"}:
            winner = self._identifyWinner(diagSet)
            if setWinner:
                self.winner = winner

            if returnWinner:
                return winner
            return True

        if returnWinner:
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "-":
                        return False
            return "Tie"

        return False

    # Checks if plays are remaining.
    def playsLeft(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    return True
        
        print("No more plays left!")
        return False

    # Checks if there is a winner or board is filled, prints out
    # final game state.
    def isOver(self):
        isOver = not self.playsLeft() or self.winner != None

        if isOver:
            print("Game is over!!!")
            print("\n")

            if self.winner == self.human:
                print("Human has won!")
            elif self.winner == self.cpu:
                print("CPU has won!")
            else:
                "It's a tie!"

            print("Final Game State:")
            print(self)
        return isOver

    def findMove(self):
        bestScore = float("-inf")

        for i in range(3):
            for j in range(3): 
                if self.board[i][j] == "-":
                    # Temporarily update board.
                    self.board[i][j] = self.cpu

                    # Check score.
                    score = self.minimax(self.board, 0, False)

                    # Revert update.
                    self.board[i][j] = "-"

                    # If better score is found, update bestScore
                    # and set the best move.
                    if (score > bestScore):
                        bestScore = score
                        bestMove = [i, j]
        return bestMove

    # Updates board, increments turn, and checks board state.
    def makeMove(self, x, y, player):
        self.board[x][y] = player
        self.turnNo += 1
        self.isWon(self.board, True, False)
    
    # Minimax function.
    def minimax(self, board, depth, cpu):
        # Check if game has been won
        winner = self.isWon(board, False, True)
        if winner == "X":
            return -1
        elif winner == "O":
            return 1
        elif winner == "Tie":
            return 0
        
        # CPU is maximizer.
        if cpu:
            bestScore = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "-":
                        # Temporarily update the board.
                        board[i][j] = self.cpu

                        # Calculate the best score.
                        score = self.minimax(board, depth + 1, False)
                        bestScore = max(score, bestScore)

                        # Revert board update.
                        board[i][j] = "-"
        # Human is minimizer.
        else:
            bestScore = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "-":
                        # Temporarily update the board.
                        board[i][j] = self.human

                        # Calculate the best score.
                        score = self.minimax(board, depth + 1, True)
                        bestScore = min(score, bestScore)

                        # Revert board update.
                        board[i][j] = "-"
        return bestScore

    # Identify the winner based on the winning set contents.
    def _identifyWinner(self, winningSet):
        if winningSet == {"X"}:
            return self.human
        else:
            return self.cpu