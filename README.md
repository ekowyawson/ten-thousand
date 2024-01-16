# Lab: Class 06

## Project: Ten Thousand

**Author**: Ekow Yawson
**Version**: 1.0.0

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
  - [ ] Add `calculate_score` **static** **method** to `GameLogic` class.
  - [ ] The **input** to `calculate_score` is a **tuple** of *integers* that represent a dice roll.
  - [ ] The **output** from `calculate_score` is an **integer** representing the roll’s score according to rules of game.

#### Handle rolling dice

- [x] Handle rolling dice.
  - [ ] Add `roll_dice` **static method** to `GameLogic` class.
  - [ ] The **input** to `roll_dice` is an **integer** between **1** and **6**.
  - [ ] The **output** of `roll_dice` is a **tuple** with random values between **1** and **6**.
  - [ ] The *length* of *tuple* must match the argument given to the `roll_dice` method.

#### Docstrings

- [ ] Document every single line of code with a detailed description of what the code is doing.

#### Tests

- [x] Run the provided tests against the code that you obtained from ai.

**Testing - Roll Dice**:

- [x] When rolling 1 to 6 dice ensure…
  - [x] A sequence of correct length is returned
  - [x] Each item in sequence is an integer with value between 1 and 6

**Testing - Calculate Score**:

- [x] **zilch** - roll with no scoring dice should return 0
- [x] **ones** - rolls with various number of 1s should return correct score
- [x] **twos** - rolls with various number of 2s should return correct score
- [ ] **threes** - rolls with various number of 3s should return correct score
- [ ] **fours** - rolls with various number of 4s should return correct score
- [ ] **fives** - rolls with various number of 5s should return correct score
- [ ] **sixes** - rolls with various number of 6s should return correct score
- [ ] **straight** - 1,2,3,4,5,6 should return correct score
- [ ] **three_pairs** - 3 pairs should return correct score
- [ ] **two_trios** - 2 sets of 3 should return correct score
- [ ] **leftover_ones** - 1s not used in set of 3 (or greater) should return correct score
- [ ] **leftover_fives** - 5s not used in set of 3 (or greater) should return correct score

#### Stretch

- [ ] Research parametrized tests in PyTest
- [ ] Research Behavior Driven Development
