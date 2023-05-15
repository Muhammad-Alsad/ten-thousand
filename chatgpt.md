## promp -01 
 Explane the task to chat Gpt 
 Handle calculating score for dice roll
 Add calculate_score static method to GameLogic class.
 The input to calculate_score is a tuple of integers that represent a dice roll.

## Code
    - import random

    class GameLogic:
    
     @staticmethod
     def calculate_score(dice):
        """
        Calculates the score for a given dice roll.
        
        Args:
        dice (tuple): a tuple of integers representing a dice roll
        
        Returns:
        int: the score for the given dice roll according to the rules of the game
        """
    
## promp -02 
    - The output from calculate_score is an integer representing the roll’s score according to rules of game.
    Handle rolling dice
    Add roll_dice static method to GameLogic class.
    The input to roll_dice is an integer between 1 and 6.
    The output of roll_dice is a tuple with random values between 1 and 6.
    The length of tuple must match the argument given to roll_dice method.

## code from chatgpt 
    -     score = 0
        
        # calculate score for each individual die
        for die in dice:
            if die == 1:
                score += 100
            elif die == 5:
                score += 50
        
        # calculate score for sets of three or more dice with the same value
        for i in range(1, 7):
            if dice.count(i) >= 3:
                if i == 1:
                    score += 1000
                else:
                    score += i * 100
        
        # subtract points for any remaining ones or fives
        score -= dice.count(1) * 100
        score -= dice.count(5) * 50
        
        return score
    
    @staticmethod
    def roll_dice(num_dice):
        """
        Rolls a given number of dice and returns the results.
        
        Args:
        num_dice (int): the number of dice to roll
        
        Returns:
        tuple: a tuple of random values between 1 and 6
        """
        dice = tuple(random.randint(1, 6) for _ in range(num_dice))
        return dice
## prompt-03
   - In the calculate_score method, we first calculate the score for each individual die based on whether it is a 1 or a 5. Then, we check for sets of three or more dice with the same value and calculate the score accordingly. Finally, we subtract points for any remaining ones or fives.
   - In the roll_dice method, we use a list comprehension to generate a tuple of random values between 1 and 6 with a length equal to the num_dice argument.
    - update spme code with conditions         
    - add roll_dice to game logic
    
## final code
    -      if count[num][0] == 1 and count[num][1] <= 2:
                score += 100 * count[num][1]

            if count[num][0] == 1 and count[num][1] > 2:
                score += 1000 * (count[num][1] - 2)
                
            # twos
            if count[num][0] == 2 and count[num][1] >= 3:
                score += 200 * (count[num][1] - 2)

            # threes
            if count[num][0] == 3 and count[num][1] >= 3:
                score += 300 * (count[num][1] - 2)

            # fours
            if count[num][0] == 4 and count[num][1] >= 3:
                score += 400 * (count[num][1] - 2)

            # fives
            if count[num][0] == 5 and count[num][1] <= 2:
                score += 50 * count[num][1]

            if count[num][0] == 5 and count[num][1] > 2:
                score += 500 * (count[num][1] - 2)

            # sixes
            if count[num][0] == 6 and count[num][1] >= 3:
                score += 600 * (count[num][1] - 2)

            # three pair
            if len(count) == 3:
                if count[0][1] == 2 and count[1][1] == 2 and count[2][1] == 2:
                    score = 1500

            # straight
            if len(count) == 6:
                score = 1500

            # 2 triples
            if len(count) == 2:
                if count[0][1] == 3 and count[1][1] == 3:
                    score = 1200  