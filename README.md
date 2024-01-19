# Lab: Class 07

## Project: Ten Thousand

**Author**: Ekow Yawson
**Version**: 2.0.0

### Links and Resources

---

- [rules of game](https://en.wikipedia.org/wiki/Dice_10000)
- [Play the Game Online](http://www.playonlinedicegames.com/farkle)
- [Python Scope](https://realpython.com/python-scope-legb-rule/)
- [Big O notation is simpler than you might think](https://www.youtube.com/watch?v=dNorFNlDbX0)
- [Rolling Dice Examples](https://web.archive.org/web/20220608035657/https://artofproblemsolving.com/wiki/index.php/Basic_Programming_With_Python#Random)

### Setup

---

**Requirements:**

- Install **pytest**: run `pip3 install pytest`

**Tests:**

- To run all tests, run the following command at the root of the project:

```bash
python -m pytest

# Or, if you are in a virtual env i.e., venv:
pytest
```

### Overview

---

This program showcases an adaptation of the game **Dice 10000**: a family dice game played with 6 dice in which each player the dice to get matching numbers and gain points based on the number of matching dice. The game is played until a player reaches 10,000 points.

### Feature Tasks and Requirements

---

#### Prompt

- [x] Create a **prompt.md** file. This file will include:
  - The prompt that you used to generate code.
  - The actual code you got from the ai you used.
  - Any subsequent prompts that you asked for changes.

#### GameLogic Class

- [x] Define a `GameLogic` class in `ten_thousand/game_logic.py` file.

#### Handle calculating score for dice roll

- [x] Handle calculating score for dice roll
  - [x] Add `calculate_score` **static** **method** to `GameLogic` class.
  - [x] The **input** to `calculate_score` is a **tuple** of *integers* that represent a dice roll.
  - [x] The **output** from `calculate_score` is an **integer** representing the roll’s score according to rules of game.

#### Handle rolling dice

- [x] Handle rolling dice.
  - [x] Add `roll_dice` **static method** to `GameLogic` class.
  - [x] The **input** to `roll_dice` is an **integer** between **1** and **6**.
  - [x] The **output** of `roll_dice` is a **tuple** with random values between **1** and **6**.
  - [x] The *length* of *tuple* must match the argument given to the `roll_dice` method.

#### Docstrings

- [x] Document every single line of code with a detailed description of what the code is doing.

### Tests

- [x] Run the provided tests against the code that you obtained from ai.

**Testing - Roll Dice**:

- [x] When rolling 1 to 6 dice ensure…
  - [x] A sequence of correct length is returned
  - [x] Each item in sequence is an integer with value between 1 and 6

**Testing - Calculate Score**:

- [x] **zilch** - roll with no scoring dice should return 0
- [x] **ones** - rolls with various number of 1s should return correct score
- [x] **twos** - rolls with various number of 2s should return correct score
- [x] **threes** - rolls with various number of 3s should return correct score
- [x] **fours** - rolls with various number of 4s should return correct score
- [x] **fives** - rolls with various number of 5s should return correct score
- [x] **sixes** - rolls with various number of 6s should return correct score
- [x] **straight** - 1,2,3,4,5,6 should return correct score
- [x] **three_pairs** - 3 pairs should return correct score
- [x] **two_trios** - 2 sets of 3 should return correct score
- [x] **leftover_ones** - 1s not used in set of 3 (or greater) should return correct score
- [x] **leftover_fives** - 5s not used in set of 3 (or greater) should return correct score

#### Stretch

- [ ] Research parametrized tests in PyTest
- [ ] Research Behavior Driven Development

#### Version 2 Requirements

**Testing - Roll Dice**:

- [x] Application should implement all features from previous version
- [x] Application should allow user to set aside dice each roll
- [x] Application should allow “banking” current score or rolling again.
- [x] Application should keep track of total score
- [x] Application should keep track of current round

#### Version 3 Requirements

**Testing - Roll Dice**:

- [ ] Application should implement features from versions 1 and 2
- [ ] Should handle setting aside scoring dice and continuing turn with remaining dice.
- [ ] Should handle when cheating occurs.
  - Or just typos.
  - E.g. roll = `[1,3,5,2]` and user selects `1, 1, 1, 1, 1, 1`
- [ ] Should allow user to continue rolling with 6 new dice when all dice have scored in current turn.
- [ ] Handle zilch
  - No points for round, and round is over
