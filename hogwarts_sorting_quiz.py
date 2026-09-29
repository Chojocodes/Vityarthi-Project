def print_logo():
    # the r before the string tells python to print the exact characters, including backslash characters
    print(r"""       ________________
                 .-'                 '-.
               .'                       '.
              /     /\             /\     \
             |     /  \___________/  \     |
             |    /____\         /____\    |
             |         |  _   _  |         |
             |         | | | | | |         |
             |         | | |_| | |         |
             |         | |  _  | |         |
             |         | | | | | |         |
             |         | |_| |_| |         |
             |         |         |         |
             |          \       /          |
              \          \     /          /
               '.         \   /         .'
                 '-._______\_/_______.-'
   """)


def print_house_descriptions():
    print("Before the Sorting Hat begins, let's meet the four Houses of Hogwarts:\n")

    print("🦁 GRYFFINDOR")
    print("Founded by Godric Gryffindor, this house values courage, bravery,")
    print("nerve, and chivalry above all else. Its colors are scarlet and gold,")
    print("and its symbol is the lion.\n")

    print("🦡 HUFFLEPUFF")
    print("Founded by Helga Hufflepuff, this house values hard work, patience,")
    print("loyalty, and fair play. Its colors are yellow and black, and its")
    print("symbol is the badger.\n")

    print("🦅 RAVENCLAW")
    print("Founded by Rowena Ravenclaw, this house prizes intelligence, wit,")
    print("creativity, and a love of learning. Its colors are blue and bronze,")
    print("and its symbol is the eagle.\n")

    print("🐍 SLYTHERIN")
    print("Founded by Salazar Slytherin, this house values ambition, cunning,")
    print("leadership, and resourcefulness. Its colors are green and silver,")
    print("and its symbol is the serpent.\n")


def main():
    print_logo()
    print("✨ Welcome to the Hogwarts Sorting Quiz! ✨")
    print("=" * 55 + "\n")

    print_house_descriptions()

    print("=" * 55)
    print("Answer the following questions to discover your true House!\n")

    # These variables will track the score for each house
    gryffindor_score = 0
    slytherin_score = 0
    ravenclaw_score = 0
    hufflepuff_score = 0

    # Question 1
    print("Question 1: Which of these qualities do you value most?")
    print("A) Courage and bravery")
    print("B) Hard work and loyalty")
    print("C) Wisdom, wit, and a love of learning")
    print("D) Ambition and cunning")

    # The loop keeps repeating until it hits a 'break'
    while True:
        answer1 = input("Enter A, B, C, or D: ").upper()
        if answer1 == "A":
            gryffindor_score += 1
            break
        elif answer1 == "B":
            hufflepuff_score += 1
            break
        elif answer1 == "C":
            ravenclaw_score += 1
            break
        elif answer1 == "D":
            slytherin_score += 1
            break
        else:
            # If it is not A, B, C, D, the loop restarts from the top!
            print("Invalid choice. The Sorting Hat requires you to type exactly A, B, C, or D.")

    # Question 2
    print("\nQuestion 2: You enter a hidden room and see four objects on a table. Which do you pick up?")
    print("A) A gleaming Silver Sword")
    print("B) A Golden Cup that smells like warm earth")
    print("C) An ancient, dusty tome filled with strange runes")
    print("D) A small, black box with a serpent engraved on the lid")

    while True:
        answer2 = input("Enter A, B, C, or D: ").upper()
        if answer2 == "A":
            gryffindor_score += 1
            break
        elif answer2 == "B":
            hufflepuff_score += 1
            break
        elif answer2 == "C":
            ravenclaw_score += 1
            break
        elif answer2 == "D":
            slytherin_score += 1
            break
        else:
            # If it is not A, B, C, D, the loop restarts from the top!
            print("Invalid choice. The Sorting Hat requires you to type exactly A, B, C, or D.")

    # Question 3
    print("\nQuestion 3: A mountain troll is blocking the bridge you need to cross. How do you handle it?")
    print("A) Draw your wand and charge directly at it!")
    print("B) Call your friends so that you can distract it together")
    print("C) Analyze the bridge's structure to find a way to collapse the troll's footing.")
    print("D) Trick the troll into chasing a fake target so you can slip by in the shadows.")

    while True:
        answer3 = input("Enter A, B, C, or D: ").upper()
        if answer3 == "A":
            gryffindor_score += 1
            break
        elif answer3 == "B":
            hufflepuff_score += 1
            break
        elif answer3 == "C":
            ravenclaw_score += 1
            break
        elif answer3 == "D":
            slytherin_score += 1
            break
        else:
            # If it is not A, B, C, D, the loop restarts from the top!
            print("Invalid choice. The Sorting Hat requires you to type exactly A, B, C, or D.")

    # Question 4
    print("\nQuestion 4: What would you most like to be known for in magical history?")
    print("A) Your bold and heroic adventures")
    print("B) Your unwavering kindness and loyalty")
    print("C) Your groundbreaking magical discoveries and intellect")
    print("D) Your immense power and influence")

    while True:
        answer4 = input("Enter A, B, C, or D: ").upper()
        if answer4 == "A":
            gryffindor_score += 1
            break
        elif answer4 == "B":
            hufflepuff_score += 1
            break
        elif answer4 == "C":
            ravenclaw_score += 1
            break
        elif answer4 == "D":
            slytherin_score += 1
            break
        else:
            # If it is not A, B, C, D, the loop restarts from the top!
            print("Invalid choice. The Sorting Hat requires you to type exactly A, B, C, or D.")
        # Question 5
    print("\nQuestion 5: A shadowy Dementor drifts toward you, and only a Patronus Charm can drive it back. What happy memory do you focus on to make your Patronus burst to life?")
    print("A) The electric thrill of facing something terrifying and refusing to back down")
    print("B) A cozy memory of the people who've always had your back, no matter what")
    print("C) The satisfying 'click' of finally solving a puzzle nobody else could crack")
    print("D) The moment everyone realized just how far your ambition could take you")

    while True:
        answer5 = input("Enter A, B, C, or D: ").upper()
        if answer5 == "A":
            gryffindor_score += 1
            break
        elif answer5 == "B":
            hufflepuff_score += 1
            break
        elif answer5 == "C":
            ravenclaw_score += 1
            break
        elif answer5 == "D":
            slytherin_score += 1
            break
        else:
            print("Invalid choice. The Sorting Hat requires you to type exactly A, B, C, or D.")

    # Question 6
    print("\nQuestion 6: You've been entered into a Triwizard-style tournament and get to choose your first trial. Which one do you pick?")
    print("A) Sneaking past a fire-breathing dragon to grab the golden egg")
    print("B) A trial where teamwork and trust with a partner matter more than anything")
    print("C) A fiendishly clever riddle that only the sharpest minds can solve")
    print("D) A high-stakes challenge where outsmarting every other champion is the whole point")

    while True:
        answer6 = input("Enter A, B, C, or D: ").upper()
        if answer6 == "A":
            gryffindor_score += 1
            break
        elif answer6 == "B":
            hufflepuff_score += 1
            break
        elif answer6 == "C":
            ravenclaw_score += 1
            break
        elif answer6 == "D":
            slytherin_score += 1
            break
        else:
            print("Invalid choice. The Sorting Hat requires you to type exactly A, B, C, or D.")

    # Question 7
    print("\nQuestion 7: You step into Ollivanders, and a wand practically leaps into your hand. What makes you certain it's 'the one'?")
    print("A) Holding it makes you feel like you could charge into anything, fearless")
    print("B) It feels instantly warm and familiar, like it already trusts you")
    print("C) It hums with a curious energy that makes you want to master every spell it can do")
    print("D) It sends a spark of pure ambition through you, like it knows you're destined for something big")

    while True:
        answer7 = input("Enter A, B, C, or D: ").upper()
        if answer7 == "A":
            gryffindor_score += 1
            break
        elif answer7 == "B":
            hufflepuff_score += 1
            break
        elif answer7 == "C":
            ravenclaw_score += 1
            break
        elif answer7 == "D":
            slytherin_score += 1
            break
        else:
            print("Invalid choice. The Sorting Hat requires you to type exactly A, B, C, or D.")

    # Question 8
    print("\nQuestion 8: Picture yourself years from now, thriving in the wizarding world. Which path fills you with the most pride?")
    print("A) An Auror, chasing dark wizards down and protecting people on the front line")
    print("B) A Healer at St. Mungo's, devoted to looking after everyone who needs you")
    print("C) A groundbreaking researcher, unlocking magic nobody's ever understood before")
    print("D) The Minister for Magic, steering the future of the entire wizarding world")

    while True:
        answer8 = input("Enter A, B, C, or D: ").upper()
        if answer8 == "A":
            gryffindor_score += 1
            break
        elif answer8 == "B":
            hufflepuff_score += 1
            break
        elif answer8 == "C":
            ravenclaw_score += 1
            break
        elif answer8 == "D":
            slytherin_score += 1
            break
        else:
            print("Invalid choice. The Sorting Hat requires you to type exactly A, B, C, or D.")

    print("\n" + "=" * 55)
    print("The Sorting Hat is making its decision...\n")

    # Using simple comparison operators to find the highest score.
    # If there is a tie, the Hat will favor the house listed first in the logic.
    if gryffindor_score >= hufflepuff_score and gryffindor_score >= ravenclaw_score and gryffindor_score >= slytherin_score:
        print("Congratulations! You have been sorted into House Gryffindor! 🦁")
    elif hufflepuff_score >= gryffindor_score and hufflepuff_score >= ravenclaw_score and hufflepuff_score >= slytherin_score:
        print("Congratulations! You have been sorted into House Hufflepuff! 🦡")
    elif ravenclaw_score >= gryffindor_score and ravenclaw_score >= hufflepuff_score and ravenclaw_score >= slytherin_score:
        print("Congratulations! You have been sorted into House Ravenclaw! 🦅")
    else:
        print("Congratulations! You have been sorted into House Slytherin! 🐍")

    print("\n" + "=" * 55 + "\n")
    input("Press Enter to exit the quiz...")


if __name__ == "__main__":
    main()
