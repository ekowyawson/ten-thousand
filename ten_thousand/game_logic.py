import random
from collections import Counter

class GameLogic:
    """GameLogic class for the Ten Thousand dice game.
    It handles the core game mechanics like rolling dice and calculating scores.
    """

    @staticmethod
    def roll_dice(num_dice):
        """Roll dice.

        Args:
            num_dice (int): Number of dice to roll, between 1 and 6.

        Returns:
            tuple: A tuple of integers representing the result of each dice roll.
        """
        # Generate a tuple of random integers between 1 and 6.
        # Each integer represents the outcome of one dice roll.
        return tuple(random.randint(1, 6) for _ in range(num_dice))

    @staticmethod
    def calculate_score(dice_roll):
        """Calculate the score for a given dice roll in the game Ten Thousand.

        Args:
            dice_roll (tuple): A tuple of integers representing a dice roll.

        Returns:
            int: The calculated score based on the rules of the game.
        """
        score = 0
        # Count the occurrences of each number in the dice roll
        dice_count = Counter(dice_roll)
        # Check for straight, three pairs, and six of a kind (instant win)
        if len(dice_count) == 6:
            return 1500  # Straight
        if len(dice_count) == 3 and all(count == 2 for count in dice_count.values()):
            return 1500  # Three pairs

        # Scoring for multiples and single ones or fives
        for num, count in dice_count.items():
            if count >= 3:
                if num == 1:
                    # For three or more ones, multiply by number of ones - 2
                    multiplier = count - 2
                    score += 1000 * multiplier
                else:
                    # For other numbers, score is 100 times (count - 2)
                    multiplier = (count - 2) * 100
                    score += num * multiplier
            elif num == 1 and count <= 2:
                score += count * 100  # 100 points for each single one
            elif num == 5 and count <= 2:
                score += count * 50  # 50 points for each single five

        return score

if __name__ == "__main__":
    # Roll six dice
    dice_roll = GameLogic.roll_dice(6)
    print(f"Dice roll: {dice_roll}")
    # Calculate the score of the roll
    score = GameLogic.calculate_score(dice_roll)
    print(f"Score: {score}")
