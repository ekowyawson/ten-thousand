#!/bin/python3

from ten_thousand.game_logic import GameLogic
# from game_logic import GameLogic

def play(roller=GameLogic.roll_dice):
    total_score = 0
    round_number = 1

    while True:  # Start of a new round
        print(f"Starting round {round_number}")
        round_score = 0
        dice_to_roll = 6
        dice_kept = []

        while dice_to_roll > 0:  # Continue rolling within the round
            print(f"Rolling {dice_to_roll} dice...")
            roll = roller(dice_to_roll)
            print(f"Dice roll: {roll}")

            # Calculate the score and allow user to set aside scoring dice
            roll_score, scoring_dice = GameLogic.calculate_score_and_scoring_dice(roll)
            print(f"Score for this roll: {roll_score}")

            if scoring_dice:
                # Ask the user which dice to keep
                kept_dice = input(f"Which dice would you like to keep from {scoring_dice}? ")
                kept_dice = tuple(map(int, kept_dice.split(',')))

                # Validate the kept dice
                valid_kept_dice = all(die in scoring_dice for die in kept_dice)
                if valid_kept_dice:
                    dice_kept.extend(kept_dice)
                    dice_to_roll -= len(kept_dice)
                    round_score += roll_score
                else:
                    print("Invalid dice selection. Please choose from the scoring dice.")
            else:
                print("No scoring dice. End of this round.")
                break

            if dice_to_roll <= 0:  # Check if any dice are left to roll
                break

            # Check if user wants to bank or roll again
            user_choice = input("Do you want to (b)ank your score or (r)oll again? ")
            if user_choice.lower() == 'b':
                total_score += round_score
                break

        round_number += 1
        if input("Do you want to play another round? (yes/no) ").lower() != 'yes':
            break

    print(f"Final score: {total_score}")
    return total_score

play()