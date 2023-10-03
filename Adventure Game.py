import time
import random

# Define the list of creatures globally
creatures = ["mage", "sorcerer", "wizard", "half-draconian", "demon"]


def print_pause(message, delay=0.1):
    words = message.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)
    print("\n")


def get_valid_input(message, valid_options):
    while True:
        user_input = input(message).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")


def choice_wait(creature):
    print_pause("As you wait, you look around and see a golden "
                "sickle lying around.")
    print_pause("You pick up the sickle for extra protection and "
                "hide it in your cloak.")
    print_pause("Less than 10 seconds after picking the sickle, "
                "your entire body involuntarily grows stiff.")
    print_pause(f"You look up and you see a male humanoid with a third eye "
                "in the middle of his forehead, descending from above, "
                f"the {creature}.")

    while True:
        print_pause("What do you do?")
        print_pause(f"1. Greet the {creature} and explain who you are "
                    "and how you found yourself there.")
        print_pause("2. Attack immediately with your golden sickle.")

        choice = get_valid_input("Please enter 1 or 2: ", ["1", "2"])

        if choice == "1":
            print_pause(f"You decide to greet the {creature} and explain "
                        "who you are and how you found yourself there.")
            print_pause(f"As you try to explain, the {creature} ignores "
                        "you and starts chanting an incantation.")

            while True:
                print_pause("What do you do?")
                print_pause(f"1. Politely wait for the {creature} "
                            "to finish his spell.")
                print_pause(f"2. Attack the {creature} mid-incantation "
                            "with your golden sickle.")

                choice = get_valid_input("Please enter 1 or 2: ", ["1", "2"])

                if choice == "1":
                    print_pause("You have turned into a talking flower "
                                "as a result of the spell.")
                    print_pause("You have lost all mobility.")
                    print_pause("You Lost!")
                    return
                elif choice == "2":
                    print_pause(f"You have attacked the {creature}.")
                    print_pause("Your attack has caused a backlash to "
                                f"the {creature}'s spell.")
                    print_pause(f"The {creature} dies.")
                    print_pause("You Won!")
                    return
        elif choice == "2":
            print_pause("You attack immediately with your golden sickle.")
            print_pause(f"The {creature} immediately counter-attacks "
                        "with a killing spell.")
            print_pause("You have died.")
            print_pause("You Lost!")
            return


def choice_run_away(creature):
    print_pause("You trust the talking flowers and run away from "
                "the garden immediately.")
    print_pause("You dash out of the garden, trying to escape, only "
                "to find out that the entire landmass is floating in "
                "the skies and there is no clear way down.")

    while True:
        print_pause("What do you do?")
        print_pause("1. Go back to the garden.")
        print_pause("2. Jump down to see if you can fly.")

        choice = get_valid_input("Please enter 1 or 2: ", ["1", "2"])

        if choice == "1":
            print_pause("You decide to go back to the garden.")
            print_pause("You return to see a male humanoid with a "
                        "third eye in the middle of his forehead.")
            print_pause(f"The humanoid, whom you assume to be the {creature}, "
                        "is currently executing a spell.")
            print_pause("The spell seems to siphon vitality from "
                        "the talking flowers.")
            print_pause(f"The {creature} does not seem to notice you, "
                        "so you look around and see a golden sickle.")
            print_pause("You pick up the sickle for extra protection "
                        "and hide it in your cloak.")

            while True:
                print_pause("What do you do?")
                print_pause(f"1. Politely wait for the {creature} "
                            "to finish its spell.")
                print_pause(f"2. Attack the {creature} mid-incantation "
                            "with your golden sickle.")

                choice = get_valid_input("Please enter 1 or 2: ", ["1", "2"])

                if choice == "1":
                    print_pause(f"The {creature} finishes his spell and "
                                "looks at you.")
                    print_pause("Because you encroached on his feeding time, "
                                "he suspects you are a rival or spy.")
                    print_pause(f"The {creature} attacks you immediately "
                                "with a killing spell.")
                    print_pause("You have died.")
                    print_pause("You Lost!")
                    return
                elif choice == "2":
                    print_pause("You have attacked the creature.")
                    print_pause("Your attack has caused a backlash to "
                                f"the {creature}'s spell.")
                    print_pause(f"The {creature} dies.")
                    print_pause("You Won!")
                    return
        elif choice == "2":
            print_pause("You jump down to see if you can fly.")
            print_pause("You immediately regret your choice as you "
                        "realize you cannot fly.")
            print_pause("You fall to your death.")
            print_pause("You have died.")
            print_pause("You Lost!")
            return


# Introduction message

def intro():
    selected_creature = random.choice(creatures)  # Randomly select a creature
    print_pause("You wake up from a crazy night out with "
                "friends and find yourself in an unfamiliar land.")
    print_pause("You are also wearing strange clothing - "
                "a cloak and sandals.")
    print_pause("You observe your environment trying "
                "to get your bearings.")
    print_pause("You look around and see a garden, filled "
                "with so many weird exotic flowers.")
    print_pause('As you draw closer, suddenly, the flowers '
                'speak! "Run from here, mortal, before '
                f'the {selected_creature} returns!"')
    return selected_creature


def player_choices(creature):
    while True:
        print_pause("What do you do?")
        print_pause("Enter 1 to wait and see what the "
                    f"{creature} looks like out of curiosity.")
        print_pause("Enter 2 to trust the talking flowers and "
                    "run away from the garden immediately.")

        choice = get_valid_input("(Please enter 1 or 2): ", ["1", "2"])

        if choice == "1":
            choice_wait(creature)
            break
        elif choice == "2":
            choice_run_away(creature)
            break

# ...


def play_game():
    selected_creature = intro()
    player_choices(selected_creature)


# Game loop
while True:
    play_game()
    play_again = get_valid_input("GAME OVER\n\nWould you like to play "
                                 "again? (yes/no): ", ["yes", "no"])
    if play_again != "yes":
        break
