# Author: Harvey Ng
# GitHub username: greyducko
# Date: 06/11/2023
# Description: The code in this file represents the Othello game. It contains the Player class with the get_name and
# get_color methods, and the Othello class with the print_board, create_player, assign_player_to_color,
# return_available_positions, make_move, play_game, and return_winner methods.

class Player:
    """A class to represent a player in the Othello game. Used by the Othello class to create players."""

    def __init__(self, player_name, color):

        self._name = player_name
        self._color = color

    def get_name(self):
        """Gets the name of the player. Used by the Othello class to get a player name."""

        return self._name

    def get_color(self):
        """Gets the color the player is playing as. Used by the Othello class to get the color of a player."""

        return self._color


class Othello:
    """The Othello class represents a game of Othello, played by two players. One player is black, the other player is
    white. Black moves first. Players take turns placing their pieces on the 8x8 board.To capture pieces, a player must
    place their piece adjacent to an opponent's piece, forming a straight line of adjacent pieces (horizontal, vertical,
    or diagonal) with their piece at each end. Multiple chains/directions of pieces can be captured all at once in a
    single move, and the captured pieces are converted to the capturing player's color.The game starts with four pieces
    placed in the middle of the board, forming a square with same-colored pieces on a diagonal. Once a piece is placed,
    it cannot be moved to a new square. If a player cannot make a valid move(a capturing move), their turn passes to the
    other player. The game ends when neither player can move, and the player with the most pieces on the board wins.
    A tie occurs if both players have the same number of pieces. Uses the Player class to get the player names and
    colors."""

    def __init__(self):
        self._white = None
        self._black = None
        self._player_list = []
        self._board = [
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "O", "X", ".", ".", ".", "*"],
            ["*", ".", ".", ".", "X", "O", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", ".", ".", ".", ".", ".", ".", ".", ".", "*"],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]]

    def print_board(self):
        """Prints out the current board, including the boundaries"""

        for row in self._board:
            for element in row:
                print(element + " ", end="")
            print()

    def create_player(self, player_name, color):
        """Adds a player to the list of players in the game"""

        self._player_list.append(Player(player_name, color))

    def assign_player_to_color(self):
        """Assigns a player to a color so the player's color can be accessed by the Othello class"""

        for player in self._player_list:
            if player.get_color() == "white":
                self._white = player.get_name()
            if player.get_color() == "black":
                self._black = player.get_name()

    def return_available_positions(self, color):
        """Return a list of all the positions that are possible moves on the current board for the player with
        the given color"""

        if color == "black":
            black_positions = []
            available_positions = []
            row_counter = 0

            for row in self._board:                                   # check for positions of black pieces
                row_counter += 1
                column_counter = 0
                for element in row:
                    column_counter += 1
                    if element == "X":
                        black_positions.append((row_counter-1, column_counter-1))

            for position in black_positions:                          # checks for possible moves above black piece
                row, column = position
                row -= 1
                while self._board[row][column] == "O":
                    row -= 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in black_positions:                        # checks for possible moves below black piece
                row, column = position
                row += 1
                while self._board[row][column] == "O":
                    row += 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in black_positions:                   # checks for possible moves to the left of black piece
                row, column = position
                column -= 1
                while self._board[row][column] == "O":
                    column -= 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in black_positions:                   # checks for possible moves to the right of black piece
                row, column = position
                column += 1
                while self._board[row][column] == "O":
                    column += 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in black_positions:         # checks for possible moves in the top left diagonal of black piece
                row, column = position
                row -= 1
                column -= 1
                while self._board[row][column] == "O":
                    row -= 1
                    column -= 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in black_positions:       # checks for possible moves in the top right diagonal of black piece
                row, column = position
                row -= 1
                column += 1
                while self._board[row][column] == "O":
                    row -= 1
                    column += 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in black_positions:     # checks for possible moves in the bottom left diagonal of black piece
                row, column = position
                row += 1
                column -= 1
                while self._board[row][column] == "O":
                    row += 1
                    column -= 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in black_positions:     # checks for possible moves in the bottom right diagonal of black piece
                row, column = position
                row += 1
                column += 1
                while self._board[row][column] == "O":
                    row += 1
                    column += 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

        if color == "white":
            white_positions = []
            available_positions = []
            row_counter = 0

            for row in self._board:                                              # check for positions of white pieces
                row_counter += 1
                column_counter = 0
                for element in row:
                    column_counter += 1
                    if element == "O":
                        white_positions.append((row_counter - 1, column_counter - 1))

            for position in white_positions:                              # checks for possible moves above white piece
                row, column = position
                row -= 1
                while self._board[row][column] == "X":
                    row -= 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in white_positions:                              # checks for possible moves below white piece
                row, column = position
                row += 1
                while self._board[row][column] == "X":
                    row += 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in white_positions:                     # checks for possible moves to the left of white piece
                row, column = position
                column -= 1
                while self._board[row][column] == "X":
                    column -= 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in white_positions:                    # checks for possible moves to the right of white piece
                row, column = position
                column += 1
                while self._board[row][column] == "X":
                    column += 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in white_positions:        # checks for possible moves in the top left diagonal of white piece
                row, column = position
                row -= 1
                column -= 1
                while self._board[row][column] == "X":
                    row -= 1
                    column -= 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in white_positions:       # checks for possible moves in the top right diagonal of white piece
                row, column = position
                row -= 1
                column += 1
                while self._board[row][column] == "X":
                    row -= 1
                    column += 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in white_positions:    # checks for possible moves in the bottom left diagonal of white piece
                row, column = position
                row += 1
                column -= 1
                while self._board[row][column] == "X":
                    row += 1
                    column -= 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

            for position in white_positions:   # checks for possible moves in the bottom right diagonal of white piece
                row, column = position
                row += 1
                column += 1
                while self._board[row][column] == "X":
                    row += 1
                    column += 1
                    if self._board[row][column] == ".":
                        available_positions.append((row, column))

        available_positions = list(set(available_positions))                # remove duplicates in available_positions
        available_positions.sort()
        return available_positions

    def make_move(self, color, piece_position):
        """Place a piece of the specified color at the given position and update the board accordingly.
        Returns the current state of the board."""

        if color == "black":
            row, column = piece_position
            self._board[row][column] = "X"                             # place black piece

            above = []
            below = []
            left = []
            right = []
            top_left_diagonal = []
            top_right_diagonal = []
            bottom_left_diagonal = []
            bottom_right_diagonal = []
            positions_to_flip = []

            row -= 1
            while self._board[row][column] == "O":        # look for white pieces above and add to appropriate list
                above.append((row, column))
                row -= 1
                if self._board[row][column] == "X":
                    positions_to_flip.append(above)

            row, column = piece_position
            row += 1
            while self._board[row][column] == "O":        # look for white pieces below and add to appropriate list
                below.append((row, column))
                row += 1
                if self._board[row][column] == "X":
                    positions_to_flip.append(below)

            row, column = piece_position               # look for white pieces to the left and add to appropriate list
            column -= 1
            while self._board[row][column] == "O":
                left.append((row, column))
                column -= 1
                if self._board[row][column] == "X":
                    positions_to_flip.append(left)

            row, column = piece_position              # look for white pieces to the right and add to appropriate list
            column += 1
            while self._board[row][column] == "O":
                right.append((row, column))
                column += 1
                if self._board[row][column] == "X":
                    positions_to_flip.append(right)

            row, column = piece_position    # look for white pieces in the top left diagonal and add to appropriate list
            row -= 1
            column -= 1
            while self._board[row][column] == "O":
                top_left_diagonal.append((row, column))
                row -= 1
                column -= 1
                if self._board[row][column] == "X":
                    positions_to_flip.append(top_left_diagonal)

            row, column = piece_position  # look for white pieces in the top right diagonal and add to appropriate list
            row -= 1
            column += 1
            while self._board[row][column] == "O":
                top_right_diagonal.append((row, column))
                row -= 1
                column += 1
                if self._board[row][column] == "X":
                    positions_to_flip.append(top_right_diagonal)

            row, column = piece_position            # look for white pieces in the bottom left diagonal and add to list
            row += 1
            column -= 1
            while self._board[row][column] == "O":
                bottom_left_diagonal.append((row, column))
                row += 1
                column -= 1
                if self._board[row][column] == "X":
                    positions_to_flip.append(bottom_left_diagonal)

            row, column = piece_position           # look for white pieces in the bottom right diagonal and add to list
            row += 1
            column += 1
            while self._board[row][column] == "O":
                bottom_right_diagonal.append((row, column))
                row += 1
                column += 1
                if self._board[row][column] == "X":
                    positions_to_flip.append(bottom_right_diagonal)

        if color == "white":
            row, column = piece_position
            self._board[row][column] = "O"                          # place white piece

            above = []
            below = []
            left = []
            right = []
            top_left_diagonal = []
            top_right_diagonal = []
            bottom_left_diagonal = []
            bottom_right_diagonal = []
            positions_to_flip = []

            row -= 1
            while self._board[row][column] == "X":        # look for black pieces above and add to list
                above.append((row, column))
                row -= 1
                if self._board[row][column] == "O":
                    positions_to_flip.append(above)

            row, column = piece_position
            row += 1
            while self._board[row][column] == "X":          # look for black pieces below and add to list
                below.append((row, column))
                row += 1
                if self._board[row][column] == "O":
                    positions_to_flip.append(below)

            row, column = piece_position               # look for black pieces to the left and add to list
            column -= 1
            while self._board[row][column] == "X":
                left.append((row, column))
                column -= 1
                if self._board[row][column] == "O":
                    positions_to_flip.append(left)

            row, column = piece_position               # look for black pieces to the right and add to list
            column += 1
            while self._board[row][column] == "X":
                right.append((row, column))
                column += 1
                if self._board[row][column] == "O":
                    positions_to_flip.append(right)

            row, column = piece_position          # look for black pieces in the top left diagonal and add to list
            row -= 1
            column -= 1
            while self._board[row][column] == "X":
                top_left_diagonal.append((row, column))
                row -= 1
                column -= 1
                if self._board[row][column] == "O":
                    positions_to_flip.append(top_left_diagonal)

            row, column = piece_position          # look for black pieces in the top right diagonal and add to list
            row -= 1
            column += 1
            while self._board[row][column] == "X":
                top_right_diagonal.append((row, column))
                row -= 1
                column += 1
                if self._board[row][column] == "O":
                    positions_to_flip.append(top_right_diagonal)

            row, column = piece_position         # look for black pieces in the bottom left diagonal and add to list
            row += 1
            column -= 1
            while self._board[row][column] == "X":
                bottom_left_diagonal.append((row, column))
                row += 1
                column -= 1
                if self._board[row][column] == "O":
                    positions_to_flip.append(bottom_left_diagonal)

            row, column = piece_position        # look for black pieces in the bottom right diagonal and add to list
            row += 1
            column += 1
            while self._board[row][column] == "X":
                bottom_right_diagonal.append((row, column))
                row += 1
                column += 1
                if self._board[row][column] == "O":
                    positions_to_flip.append(bottom_right_diagonal)

        for list_of_positions in positions_to_flip:                 # flip pieces
            for position in list_of_positions:
                row, column = position
                if color == "white":
                    self._board[row][column] = "O"
                elif color == "black":
                    self._board[row][column] = "X"

        return self._board

    def play_game(self, player_color, piece_position):
        """Tries to make a move for the player with the given color at the position specified. If the move is
        invalid, no move should be made and the function should return "Invalid move" and print out "Here are the valid
        moves:" followed by the list of possible moves. If there are no valid moves, the returned list is empty. If the
        position is valid, the move is made and the board is updated. If the game is then ended, the function prints
        "Game is ended white piece: number black piece: number" and calls the return_winner method."""

        self.assign_player_to_color()

        black_available_positions = self.return_available_positions("black")
        white_available_positions = self.return_available_positions("white")
        total_available_positions = []

        for position in black_available_positions:
            total_available_positions.append(position)
        for position in white_available_positions:
            total_available_positions.append(position)

        if not total_available_positions:                       # if both colors/players have no valid moves
            black_counter = 0
            white_counter = 0
            for row in self._board:                             # count number of pieces for each color
                for element in row:
                    if element == "X":
                        black_counter += 1
                    if element == "O":
                        white_counter += 1
            print("Game is ended white piece: " + str(white_counter) + " black piece: " + str(black_counter))
            self.return_winner()

        else:
            available_positions = self.return_available_positions(player_color)
            if piece_position not in available_positions:               # if trying to make an invalid move
                print("Here are the valid moves:", available_positions)
                return "Invalid move"

            if piece_position in available_positions:                  # if the move (position) is valid
                self.make_move(player_color, piece_position)

    def return_winner(self):
        """Returns the winner of the game. If the number of pieces are equal, returns "It's a tie" """

        black_counter = 0
        white_counter = 0
        for row in self._board:                                 # count number of pieces for each color
            for element in row:
                if element == "X":
                    black_counter += 1
                if element == "O":
                    white_counter += 1
        if white_counter > black_counter:
            return "Winner is white player: " + self._white
        if black_counter > white_counter:
            return "Winner is black player: " + self._black
        else:
            return "It's a tie"
