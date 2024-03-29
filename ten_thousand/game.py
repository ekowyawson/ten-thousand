from ten_thousand.game_logic import GameLogic

def validate_lists(scoring_dice, kept_dice_list):
    for item in scoring_dice:
        try:
            kept_dice_list.remove(item)
        except ValueError:
            print("Cheater!!! Or possibly made a typo...")
            return False
    
    if kept_dice_list:
        print("Cheater!!! Or possibly made a typo...")
        return False
    
    return True

def play(roller=None):
    roller = roller or GameLogic.roll_dice
    total_score = 0
    round_number = 1
    keep_playing = True

    print("Welcome to Ten Thousand")
    start_answer = input(f"(y)es to play or (n)o to decline\n> ").strip().lower()
    
    if not start_answer.startswith('y'):
        print("OK. Maybe another time")
        return
    
    while keep_playing:  # Start of a new round
        print(f"Starting round {round_number}")
        round_score = 0
        dice_to_roll = 6
        dice_kept = []

        while dice_to_roll > 0:  # Continue rolling within the round
            print(f"Rolling {dice_to_roll} dice...")
            roll = roller(dice_to_roll)
            print(f"*** {' '.join(map(str, roll))} ***")

            # Calculate the score and allow user to set aside scoring dice
            roll_score, scoring_dice = GameLogic.calculate_score_and_scoring_dice(roll)

            if scoring_dice:
                # Ask the user which dice to keep
                ask_keep_dice = input(f"Enter dice to keep, or (q)uit:\n> ").strip().lower()
                kept_dice = GameLogic.confirm_keepers(scoring_dice, ask_keep_dice, roll)

                # Quit check
                if kept_dice == 'q':
                    print(f"Thanks for playing. You earned {total_score} points")
                    keep_playing = False
                    return keep_playing

                kept_dice = tuple(map(int, kept_dice))

                if kept_dice:
                    dice_kept.extend(kept_dice)
                    dice_to_roll -= len(kept_dice)
                    round_score += roll_score

                    if dice_to_roll == 0:  # Check if any dice are left to roll
                        dice_to_roll = 6

                    print(f"You have {round_score} unbanked points and {dice_to_roll} dice remaining")
                else:
                    print("Invalid dice selection. Please choose from the scoring dice.")
                
            else:
                print("****************************************")
                print("**        Zilch!!! Round over         **")
                print("****************************************")
                print(f"You banked 0 points in round 1")
                print(f"Total score is {total_score} points")
                break

            if dice_to_roll <= 0:  # Check if any dice are left to roll
                break

            # Check if user wants to bank or roll again
            user_choice = input(f"(r)oll again, (b)ank your points or (q)uit:\n> ")

            if user_choice.lower().startswith('q'):
                print(f"Thanks for playing. You earned {total_score} points")
                keep_playing = False
                return keep_playing

            if user_choice.lower() == 'b':
                print(f"You banked {round_score} points in round {round_number}")
                total_score += round_score
                print(f"Total score is {total_score} points")
                break

        round_number += 1

    print(f"Thanks for playing. You earned {total_score} points")
    return total_score

if __name__ == "__main__":
    play()
