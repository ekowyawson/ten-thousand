import random
from collections import Counter

class GameLogic:
    """GameLogic class for the Ten Thousand dice game.
    It handles the core game mechanics like rolling dice and calculating scores.
    """
    def __init__(self):
       """Initializes round score and total score to 0."""
       self.round_score = 0
       self.total_score = 0


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


    @staticmethod
    def calculate_score_and_scoring_dice(dice_roll):
        """Calculate the score for a given dice roll in the game Ten Thousand and return scoring dice.
        Args:
            dice_roll (tuple): A tuple of integers representing a dice roll.
        Returns:
            tuple: A tuple containing the score and a list of integers representing the scoring dice.
        """
        score = 0
        scoring_dice = []
        dice_count = Counter(dice_roll)

        # Check for straight, three pairs, and six of a kind (instant win)
        if len(dice_count) == 6:
            return 1500, list(dice_roll)  # Straight
        if len(dice_count) == 3 and all(count == 2 for count in dice_count.values()):
            return 1500, list(dice_roll)  # Three pairs

        # Scoring for multiples and single ones or fives
        for num, count in dice_count.items():
            if count >= 3:
                if num == 1:
                    # For three or more ones
                    multiplier = count - 2
                    score += 1000 * multiplier
                    scoring_dice.extend([1] * count)
                else:
                    # For other numbers
                    multiplier = (count - 2) * 100
                    score += num * multiplier
                    scoring_dice.extend([num] * count)
            elif num == 1 and count <= 2:
                score += count * 100  # 100 points for each single one
                scoring_dice.extend([1] * count)
            elif num == 5 and count <= 2:
                score += count * 50  # 50 points for each single five
                scoring_dice.extend([5] * count)

        return score, scoring_dice


    @staticmethod
    def confirm_keepers(scoring_dice, kept_dice, roll):
        """Compares two lists (scoring dice and kept dice) and prompts the user if any kept dice is not found in scoring dice.
        Args:
            scoring_dice: The first list to compare.
            kept_dice: The second list to compare.
        Returns:
            True: If all values in kept_dice are present in scoring_dice.
            False: If any value in kept_dice is not present in scoring_dice.
        """
        if kept_dice.startswith('q'):
            return 'q'
        kept_dice = list(kept_dice.strip())
        kept_dice = [item for item in kept_dice if item != ' ' and item != '']
        kept_dice = list(map(int, kept_dice))
        temp_scoring_dice = scoring_dice.copy()
        for num in kept_dice:
            if num in temp_scoring_dice:
                temp_scoring_dice.remove(num)
            else:
                print("Cheater!!! Or possibly made a typo...")
                print(f"*** {' '.join(map(str, roll))} ***")
                kept_dice = input(f"Enter dice to keep, or (q)uit:\n> ").strip().lower()
                return GameLogic.confirm_keepers(scoring_dice, kept_dice, roll)
        return kept_dice


    @staticmethod
    def validate_keepers(roll, keepers):
        # Convert tuple1 to a list for easier manipulation
        temp_list1 = list(roll)
        # Check each element in tuple2
        for item in keepers:
            if item in temp_list1:
                # Remove one occurrence of the item from temp_list1
                temp_list1.remove(item)
            else:
                # If the item is not in tuple1, return an error
                return False
        # If all items in tuple2 are in tuple1, return a success message
        return True


    def update_score(self, round_score):
       """Updates round score and total score."""
       self.round_score = round_score
       self.total_score += round_score


    def reset_round_score(self):
       """Resets the round score to 0."""
       self.round_score = 0


if __name__ == "__main__":
    # Roll six dice
    dice_roll = GameLogic.roll_dice(6)
    print(f"Dice roll: {dice_roll}")
    # Calculate the score of the roll
    score = GameLogic.calculate_score(dice_roll)
    print(f"Score: {score}")
