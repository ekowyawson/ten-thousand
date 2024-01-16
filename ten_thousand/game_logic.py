import random
from collections import Counter

class GameLogic:
    """
    GameLogic class for the Ten Thousand dice game.
    It handles the core game mechanics like rolling dice and calculating scores.
    """

    @staticmethod
    def roll_dice(num_dice):
        """
        Roll dice.

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
        """
        Calculate the score for a given dice roll in the game Ten Thousand.

        Args:
        dice_roll (tuple): A tuple of integers representing a dice roll.

        Returns:
        int: The calculated score based on the rules of the game.
        """
        # Scoring rules:
        # Three 1's => 1000 points
        # Three numbers (other than 1) => 100 * number
        # One 1 (not part of a set of three) => 100 points
        # One 5 (not part of a set of three) => 50 points
        # Straight 1-6 => 1500 points
        # Three pairs => 1500 points (including 4-of-a-kind and a pair)
        score = 0
        # Count the occurrences of each number in the dice roll
        dice_count = Counter(dice_roll)
        # Check for a straight (1-6)
        if len(dice_count) == 6:
            return 1500
        # Check for three pairs
        if len(dice_count) == 3 and all(count == 2 for count in dice_count.values()):
            return 1500

        # Scoring for triples and single ones or fives
        for num, count in dice_count.items():
            if count >= 3:
                score += 1000 if num == 1 else num * 100
                count -= 3  # Remove the counted triples
            # Scoring for leftover ones and fives
            if num == 1:
                score += count * 100
            elif num == 5:
                score += count * 50
        return score

# Example usage
if __name__ == "__main__":
    # Roll six dice
    dice_roll = GameLogic.roll_dice(6)
    print(f"Dice roll: {dice_roll}")
    # Calculate the score of the roll
    score = GameLogic.calculate_score(dice_roll)
    print(f"Score: {score}")
