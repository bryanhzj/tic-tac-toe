class Game:
    def __init__(self) -> None:
        self.CONSTANTS = {
            "COMPUTER": -1,
            "EMPTY": 0,
            "PLAYER": 1,
            "TOP_LEFT": 0,
            "TOP_CENTER": 1,
            "TOP_RIGHT": 2,
            "MID_LEFT": 3,
            "MID_CENTER": 4,
            "MID_RIGHT": 5,
            "BOT_LEFT": 6,
            "BOT_CENTER": 7,
            "BOT_RIGHT": 8
        }
        self.status = True

    def render_board(self):
        vertical_divider = "!"
        horizontal_divider = "---+---+---"
        lines = []
        lines.append(vertical_divider.join(self.space_mapping[space] for space in self.board[0:3]))
        lines.append(horizontal_divider)
        lines.append(vertical_divider.join(self.space_mapping[space] for space in self.board[3:6]))
        lines.append(horizontal_divider)
        lines.append(vertical_divider.join(self.space_mapping[space] for space in self.board[6:9]))
        return "\n".join(lines)

    def player_place_symbol(self):
        while True:
            move = int(input("\nWHERE DO YOU MOVE? (ENTER 0 TO RESET) "))
            if move == 0:
                self.status = True
                break

            if move > 9:
                print("ONLY INPUT 1 TO 9 ACCEPTED.\n\n")
                continue

            if self.board[move - 1] is not self.CONSTANTS["EMPTY"]:
                print("THAT SQUARE IS OCCUPIED.\n\n")
                continue

            self.board[move - 1] = self.CONSTANTS["PLAYER"]
            break

    def computer_place_symbol(self):
        for position in range(len(self.board)):
            if self.board[position] is self.CONSTANTS["EMPTY"]:
                self.board[position] = self.CONSTANTS["COMPUTER"]
                break

    def check_result(self):
        # check horizontal
        for i in range(self.CONSTANTS["TOP_LEFT"], len(self.board), 3):
            if sum(self.board[i:i + 3]) == -3:
                self.winner = "COMPUTER"
                return
            if sum(self.board[i:i + 3]) == 3:
                self.winner = "PLAYER"
                return

        # check vertical
        for i in range(self.CONSTANTS["TOP_LEFT"], self.CONSTANTS["TOP_RIGHT"] + 1):
            if sum(self.board[i: len(self.board): 3]) == -3:
                self.winner = "COMPUTER"
                return
            if sum(self.board[i: len(self.board): 3]) == 3:
                self.winner = "PLAYER"
                return

        # check diagonal
        if sum(self.board[self.CONSTANTS["TOP_LEFT"]: self.CONSTANTS["BOT_RIGHT"] + 1: self.CONSTANTS["MID_LEFT"] + 1]) == -3 or sum(self.board[self.CONSTANTS["TOP_RIGHT"]: self.CONSTANTS["BOT_RIGHT"] + 1: self.CONSTANTS["TOP_RIGHT"]]) == -3:
            self.winner = "COMPUTER"
            return
        if sum(self.board[self.CONSTANTS["TOP_LEFT"]: self.CONSTANTS["BOT_RIGHT"] + 1: self.CONSTANTS["MID_LEFT"] + 1]) == 3 or sum(self.board[self.CONSTANTS["TOP_RIGHT"]: self.CONSTANTS["BOT_RIGHT"] + 1: self.CONSTANTS["TOP_RIGHT"]]) == 3:
            self.winner = "PLAYER"
            return

        # entire board is filled and no winning condition
        if self.CONSTANTS["EMPTY"] not in self.board:
            self.winner = "TIE"
            return
    
    def declare_winner(self):
        if self.winner == "TIE":
            print("IT IS A TIE!")
            print(self.render_board())

        if self.winner:
            print(self.winner + " WINS!")
            print(self.render_board())
        
        restart = input("\nDO YOU WANT TO RESTART? Y/N ").upper()
        if restart == "Y":
            self.status = True

        return

    def set_up(self):
        symbol = input("DO YOU WANT 'X' OR 'O'? ").upper()

        # Default state
        self.winner = None
        self.status = False
        self.board = [self.CONSTANTS["EMPTY"]] * 9
        self.current_player = self.CONSTANTS["PLAYER"]
        self.space_mapping = {
            self.CONSTANTS["EMPTY"]: "   ",
            self.CONSTANTS["PLAYER"]: " X ",
            self.CONSTANTS["COMPUTER"]: " O ",
        }

        if symbol != "X":
            self.space_mapping[self.CONSTANTS["PLAYER"]] = " O "
            self.space_mapping[self.CONSTANTS["COMPUTER"]] = " X "
            self.current_player = self.CONSTANTS["COMPUTER"]
        

    def play(self):
        while True:
            if self.current_player is self.CONSTANTS["PLAYER"]:
                self.player_place_symbol()
                if self.status:
                    return
                self.check_result()
                if self.winner:
                    self.declare_winner()
                    return
                self.current_player = self.CONSTANTS["COMPUTER"]

            if self.current_player is self.CONSTANTS["COMPUTER"]:
                self.computer_place_symbol()
                self.check_result()
                if self.winner:
                    self.declare_winner()
                    return
                self.current_player = self.CONSTANTS["PLAYER"]
            
            print(self.render_board())

if __name__ == "__main__":
    game = Game()
    while game.status:
        game.set_up()
        game.play()