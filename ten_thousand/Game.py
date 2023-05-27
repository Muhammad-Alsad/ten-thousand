import sys
from ten_thousand.banker import Banker
from ten_thousand.game_logic import GameLogic
from collections import Counter



class Game:

    def __init__(self, num_rounds=20):
        self.banker = Banker()
        self.scorer = GameLogic()
        self.roller = None
        self.round_ = 0
        self.dice_count = 0
        self.keep_dice = []
        self.rolled_dice = None
        self.num_games = None
        self.num_rounds = num_rounds

    def play(self, num_games=1, roller=GameLogic.roll_dice):
        self.roller = roller
        self.num_games = num_games

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
            sys.exit()
        if response == "y":

            while True:
                self.dice_count = 6
                self.round_ += 1
                print(f"Starting round {self.round_}")
                self.play_round()
    
    def play_round(self):
            print(f"Rolling {self.dice_count} dice...")
            self.rolled_dice = self.roller(self.dice_count)
            self.keep_or_quit()

    def keep_or_quit(self):                 
        roll_string = self.str_formatter(self.rolled_dice)
        print(f"*** {roll_string} ***")
        if self.scorer.calculate_score(self.rolled_dice) == 0:
            self.zilch()
        print("Enter dice to keep, or (q)uit:")
        keep_or_quit = input("> ").replace(" ", "")
        if keep_or_quit == "q":
            self.game_end()
        else:
            self.keep_dice = []
            for j in keep_or_quit:
                self.keep_dice.append(int(j))
                
            self.check_cheater()

            self.dice_count -= len(self.keep_dice)
            self.banker.shelf(self.scorer.calculate_score(self.keep_dice))
            print(f"You have {self.banker.shelved} unbanked points and {self.dice_count} dice remaining")
            print('(r)oll again, (b)ank your points or (q)uit:') 

            r_b_q = input("> ")

            if r_b_q == "r":
                if self.dice_count == 0:
                    self.dice_count = 6
                self.play_round()

            if r_b_q == "b":
                banked_points = self.banker.bank()
                print(f"You banked {banked_points} points in round {self.round_}")
                print(f"Total score is {self.banker.balance} points")
                self.num_rounds -= 1
                if self.num_rounds == 0:
                    self.game_end()

            if r_b_q == "q":
                self.game_end()
              
    def str_formatter(self, string):
        stringify = str(string)
        final = stringify.replace(",", "").replace("[","").replace("]", "").replace("(", "").replace(")", "")
        return final

    def check_cheater(self):
        # check_list = self.keep_dice
        # check_rolled = [x for x in self.rolled_dice]
        # #print(f"rolled dice: {check_rolled}")
        # #print(f"keep dice: {check_list}")

        # for i in check_list:
        #     if i in check_rolled:
        #         check_rolled.remove(i)
        #     else:
        if self.scorer.validate_keepers(self.rolled_dice, self.keep_dice) is False:    
            print("Cheater!!! Or possibly made a typo...")
            self.keep_or_quit()

    def zilch(self):
        '''
        check rolled dice vs score sheet, if score sheet = 0 run zilch
        '''
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        
        print(f"You banked {self.banker.balance} points in round {self.round_}")
        print(f"Total score is {self.banker.balance} points")
        self.num_rounds -= 1
        if self.num_rounds == 0:
            self.game_end()
        
        self.dice_count = 6
        self.round_ += 1

        self.banker.clear_shelf()

        print(f"Starting round {self.round_}")
        self.play_round()

    def game_end(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

if __name__ == "__main__":
    # banker =Banker() 
    game = Game()
    game.play()
