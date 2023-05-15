import random
from collections import Counter


# Define GameLogic class with roll_dice static method.
class GameLogic:
    """
    Game Logic: Contains the main methods for the game of calculating the
     score, rolling the dice, and banking.
    """

    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num_dice=6):
        roll = tuple(random.randint(1, 6) for die in range(0, num_dice))
        return roll

    @staticmethod
    def calculate_score(roll):
        score = 0
        count_pair = 0
        count = Counter(roll).most_common()
        num = len(count)
        for num in range(0, len(count)):

            #  ones
            if count[num][0] == 1 and count[num][1] <= 2:
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

        return score

    

if __name__ == '__main__':
    print(GameLogic.calculate_score([3, 3, 3, 5, 2, 4]))
    print(GameLogic.calculate_score([3, 3, 3, 2, 2, 2]))
    print(GameLogic.calculate_score([3, 3, 3, 3, 3, 3]))
    print(GameLogic.calculate_score([1, 5, 5, 5, 5, 5]))
    print(GameLogic.calculate_score([3, 3, 4, 4, 5, 5]))
    print(GameLogic.calculate_score([3, 3, 4, 4, 5, 5]))
    print(GameLogic.calculate_score([1, 3, 4, 4, 5, 1]))
    print(GameLogic.calculate_score([1, 3, 4, 3, 1, 1]))