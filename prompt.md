# Ten Thousand v1 - Prompts Used for AI Generation

## Prompt 1

- Below are instructions on coding a python game called ten thousand. Parse the instructions and complete the code please:
  - Project named `ten-thousand`.
  - We will be tackling the highest risk and/or highest priority features - `scoring` and `dice rolling`.
    - Define a `GameLogic` class in `game_logic.py` file.
    - Handle calculating score for dice roll:
      - Add `calculate_score` static method to `GameLogic` class.
      - The input to `calculate_score` is a tuple of integers that represent a dice roll.
      - The output from `calculate_score` is an integer representing the roll’s score according to **rules of game**.
  
    - Handle rolling dice:
      - Add `roll_dice` static method to `GameLogic` class.
      - The input to `roll_dice` is an integer between `1` and `6`.
      - The output of `roll_dice` is a tuple with random values between 1 and 6.
      - The length of tuple must match the argument given to `roll_dice` method.

  - Rules of the Game
    - When rolling 1 to 6 dice ensure:
      - A sequence of correct length is returned
      - Each item in sequence is an integer with value between 1 and 6

  - Calculate Score
    - **zilch** - roll with no scoring dice should return 0
    - **ones** - rolls with various number of 1s should return correct score
    - **twos** - rolls with various number of 2s should return correct score
    - **threes** - rolls with various number of 3s should return correct score
    - **fours** - rolls with various number of 4s should return correct score
    - **fives** - rolls with various number of 5s should return correct score
    - **sixes** - rolls with various number of 6s should return correct score
    - **straight** - 1,2,3,4,5,6 should return correct score
    - **three_pairs** - 3 pairs should return correct score
    - **two_trios** - 2 sets of 3 should return correct score
    - **leftover_ones** - 1s not used in set of 3 (or greater) should return correct score
    - **leftover_fives** - 5s not used in set of 3 (or greater) should return correct score

## AI Response 1

Your instructions outline the requirements for creating a command-line version of the dice game "Ten Thousand" in Python. The key tasks include:

1. **Project Name**: The project is named `ten-thousand`.
2. **Core Features**: The focus is on two main features: `scoring` and `dice rolling`.
    - **GameLogic Class**: This class should be defined in a file named `game_logic.py`.
    - **Calculating Score**:
        - Implement a static method `calculate_score` within the `GameLogic` class.
        - This method takes a tuple of integers representing a dice roll as input.
        - It outputs an integer representing the score of the roll based on the game's rules.
    - **Rolling Dice**:
        - Implement a static method `roll_dice` in the `GameLogic` class.
        - This method takes an integer between 1 and 6 as input.
        - It outputs a tuple of random values between 1 and 6.
        - The length of the output tuple must match the input argument.

Now, let's start coding the `GameLogic` class in Python. We'll tackle the `roll_dice` and `calculate_score` methods.

I've implemented the `GameLogic` class for the "Ten Thousand" dice game in Python, including two key methods:

1. `roll_dice(num_dice)`: This method takes an integer `num_dice`, representing the number of dice to roll (between 1 and 6). It returns a tuple of random integers between 1 and 6, each representing the outcome of one dice roll.

2. `calculate_score(dice_roll)`: This method calculates the score based on a given dice roll, according to the game's rules. The input is a tuple of integers representing a dice roll. The method then calculates the score based on various conditions:
    - Three 1's score 1000 points.
    - Three of any number other than 1's score 100 times the number.
    - A single 1 (not part of a set of three) scores 100 points.
    - A single 5 (not part of a set of three) scores 50 points.
    - A straight (1-6) scores 1500 points.
    - Three pairs score 1500 points.

An example usage is provided at the end, where the program rolls six dice and then calculates the score based on the roll.

### AI Code Provided

```python
import random
from collections import Counter

class GameLogic:
    """
    GameLogic class for the Ten Thousand dice game.
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

```
