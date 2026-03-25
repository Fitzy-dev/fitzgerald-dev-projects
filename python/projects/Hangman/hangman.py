# Jordan Fitzgerald
# 3/18/2026
# Hangman Game
# Jordan Fitzgerald
# Hangman Game

import random

# Categories (each category can contain any number of words; counts are shown when choosing a category)
CATEGORIES = {
    "places": [
        "london",
        "paris",
        "tokyo",
        "sydney",
        "berlin",
        "amsterdam",
        "barcelona",
        "seoul",
        "dublin",
        "madrid",
        "rome",
        "moscow",
        "beijing",
        "cairo",
        "delhi",
        "bangkok",
        "singapore",
        "hongkong",
        "newyork",
        "losangeles",
        "chicago"
        "virginia",
        "texas",
        "florida",
        "california",
        "australia",
        "canada"
        "brazil",
        "argentina",
        "unitedkingdom",
        "france",
        "germany",
        "italy",
        "spain",
        "unitedstates",
        "portugal",
        "korea",
        "japan"
        
    ],
    "food": [
        "pizza",
        "burger",
        "sushi",
        "pasta",
        "taco",
        "salad",
        "ramen",
        "curry",
        "bagel",
        "waffle",
        "croissant"
        "fries",
        "steak",
        "lobster",
        "crab",
        "sandwich",
        "hotdog",
        "pancake",
        "omelette",
        "lasagna",
        "crepe",
        "dumpling",
        "burrito",
        "falafel",
        "pretzel",
        "wings",
        "nachos",
        "quesadilla",
        "samosa",
        "springroll",
        "poutine",
        "apple",
        "banana",
        "orange",
        "grape",
        "strawberry",
        "watermelon",
        "blueberry",
        "peach",
        "pie",
        "cake",
        "cookie",
        "brownie",
        "icecream",
        "candy",
        "chocolate",
        "donut",
        "muffin",
        "cupcake",

    ],
    "animals": [
        "elephant",
        "giraffe",
        "dolphin",
        "kangaroo",
        "penguin",
        "alligator",
        "butterfly",
        "squirrel",
        "hamster",
        "rhinoceros",
        "octopus",
        "dog",
        "cat",
        "mouse",
        "rabbit",
        "rat",
        "hamster",
        "snake",
        "lizard",
        "gecko",
        "chameleon",
        "tarantula",
        "scorpion",
        "centipede",
        "dragon",
        "unicorn",
        "lion",
        "panther",
        "tiger",
        "cheetah",
        "falcon",
        "eagle",
        "owl",
        "vulture",
        "crow",
        "raven",
        "cow",
        "pig",
        "sheep",
        "goat",
        "horse",

    ],
    "movies": [
        "inception",
        "gladiator",
        "titanic",
        "avatar",
        "casablanca",
        "rocky",
        "jaws",
        "amelie",
        "memento",
        "goodfellas",
        "rio",
        "kungfupanda",
        "findingnemo",
        "shrek",
        "zootopia",
        "up",
        "frozen",
        "scarface",
        "pulpfiction",
        "thegodfather",
        "howtotrainyourdragon",
        "monstersinc",
        "thelionking",
        "aladdin",
        "beautyandthebeast",
        "thelittlemermaid",
        "cinderella",
        "sleepingbeauty",
        "snowwhite",
        "tangled",
        "brave",
        "moana",
        "avengers",
        "ironman",
        "spiderman",
        "batman",
        "incredibles",
        "sharktale",
        "ratatouille",
    ],
    "sports": [
        "soccer",
        "basketball",
        "baseball",
        "cricket",
        "tennis",
        "hockey",
        "volleyball",
        "badminton",
        "golf",
        "rugby",
        "swimming",
        "gymnastics",
        "wrestling",
        "boxing",
        "archery",
        "fencing",
        "cheerleading",
        "dancing",
        "snowboarding",
        "gaming",
    ],
    "technology": [
        "computer",
        "internet",
        "keyboard",
        "database",
        "algorithm",
        "microchip",
        "smartphone",
        "robotics",
        "network",
        "compiler",
        "artificial",
        "intelligence",
        "machine",
        "learning"
        "network",
        "database",
        "programming",
        "software",
        "hardware"
        "machine",
    ],
}

HIGH_SCORE_FILE = "hangman_score.txt"

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]

MAX_WRONG = len(HANGMAN_PICS) - 1


# ----------------------------
# Load high score
# ----------------------------
def load_high_score():
    # try to open file
    # return score (int)
    # if file doesn't exist → return None
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return None
    pass


# ----------------------------
# Save high score
# ----------------------------
def save_high_score(score):
    # open file in write mode
    # write score
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))
    pass


# ----------------------------
# Display word
# ----------------------------
def display_word(word, guessed):
    # return something like: "_ a _ _"
    if not guessed:
        return "_ " * len(word)
    else:
        return " ".join([letter if letter in guessed else "_" for letter in word])
    pass
# Hint Function
def give_hint(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return letter
    return None



# ----------------------------
# Game logic
# ----------------------------
def play_game(word):
    # word is provided by caller (selected from a category)
    guessed_letters = set()
    wrong_letters = set()
    wrong_count = 0

    while True:
        # print current word state
        # print wrong guesses
        # print guesses remaining
        print("\n==== Welcome to Hangman! ====")
        print(HANGMAN_PICS[wrong_count])
        print(f"You have {MAX_WRONG - wrong_count} guesses allowed.")
        print("Word:", display_word(word, guessed_letters))
        print("Wrong guesses:", " ".join(wrong_letters))
        print("Guesses remaining:", MAX_WRONG - wrong_count)

        guess = input("Enter a letter (or guess the whole word)(or type hint): ").lower().strip()

        if guess == "hint":
            hint_letter = give_hint(word, guessed_letters)

            if hint_letter is not None:
                guessed_letters.add(hint_letter)
                print(f"Hint used! The letter '{hint_letter}' has been revealed")
                wrong_count += 1
            else:
                print("No Hints avaiable. All letters are already revealed.")
        
            continue

        # validate input (letters only)
        if not guess.isalpha():
            print("Invalid input. Please enter letters only.")
            continue

        # if user entered a single letter, handle as before
        if len(guess) == 1:
            if guess in guessed_letters or guess in wrong_letters:
                print("You already guessed that letter.")
                continue

            if guess in word:
                guessed_letters.add(guess)
            else:
                wrong_letters.add(guess)
                wrong_count += 1
        else:
            # user is attempting to guess the whole word
            if guess == word:
                print("Congratulations! You've guessed the word:", word)
                return wrong_count
            else:
                if guess in wrong_letters:
                    print("You already guessed that word.")
                    continue
                print("Incorrect word guess.")
                wrong_letters.add(guess)
                # penalize one wrong guess for an incorrect full-word guess
                wrong_count += 1

        # check WIN condition
        if set(word) == guessed_letters:
            print("Congratulations! You've guessed the word:", word)
            return wrong_count

        # check LOSE condition
        if wrong_count >= MAX_WRONG:
            print("Sorry, you've run out of guesses. The word was:", word)
            return wrong_count

        pass


# ----------------------------
# Main loop
# ----------------------------

def main():
    high_score = load_high_score()

    # print high score if exists
    if high_score is not None:
        print("Current High Score (least wrong guesses):", high_score)
    else:
        print("No high score yet. Be the first to set one!")
    while True:
        # Prompt for category selection
        print("\nChoose a category from the list below or type 'random' to pick any:")
        category_names = list(CATEGORIES.keys())
        for idx, name in enumerate(category_names, start=1):
            print(f"  {idx}. {name.title()} ({len(CATEGORIES[name])} words)")
        choice = input("Enter category name or number (or 'random'): ").strip().lower()

        if choice == "random":
            selected_category = random.choice(category_names)
        else:
            # allow numeric selection
            if choice.isdigit():
                i = int(choice) - 1
                if 0 <= i < len(category_names):
                    selected_category = category_names[i]
                else:
                    print("Invalid number, picking a random category.")
                    selected_category = random.choice(category_names)
            else:
                # accept direct name (partial match allowed)
                matches = [name for name in category_names if name.startswith(choice)]
                if len(matches) == 1:
                    selected_category = matches[0]
                elif choice in category_names:
                    selected_category = choice
                else:
                    print("Unknown category, picking a random category.")
                    selected_category = random.choice(category_names)

        word = random.choice(CATEGORIES[selected_category])
        print(f"Selected category: {selected_category.title()}")

        score = play_game(word)

        # if player wins:
        if score < MAX_WRONG:
             print("You won with", score, "wrong guesses!")
        else:
            print("You lost with", score, "wrong guesses.")

        # check if new high score
        if high_score is None or score < high_score:
            print("New high score! You set a new record with", score, "wrong guesses!")
            save_high_score(score)
            high_score = score
        # save if better
        if score > high_score:
            print("You did not beat the high score of", high_score, "wrong guesses. Try again to set a new record!")
        again = input("Play again? (y/n): ")

        if again != "y":
            break


main()        "steak",
        "lobster",
        "crab",
        "sandwich",
        "hotdog",
        "pancake",
        "omelette",
        "lasagna",
        "crepe",
        "dumpling",
        "burrito",
        "falafel",
        "pretzel",
        "wings",
        "nachos",
        "quesadilla",
        "samosa",
        "springroll",
        "poutine",
        "apple",
        "banana",
        "orange",
        "grape",
        "strawberry",
        "watermelon",
        "blueberry",
        "peach",
        "pie",
        "cake",
        "cookie",
        "brownie",
        "icecream",
        "candy",
        "chocolate",
        "donut",
        "muffin",
        "cupcake",

    ],
    "animals": [
        "elephant",
        "giraffe",
        "dolphin",
        "kangaroo",
        "penguin",
        "alligator",
        "butterfly",
        "squirrel",
        "hamster",
        "rhinoceros",
        "octopus",
        "dog",
        "cat",
        "mouse",
        "rabbit",
        "rat",
        "hamster",
        "snake",
        "lizard",
        "gecko",
        "chameleon",
        "tarantula",
        "scorpion",
        "centipede",
        "dragon",
        "unicorn",
        "lion",
        "panther",
        "tiger",
        "cheetah",
        "falcon",
        "eagle",
        "owl",
        "vulture",
        "crow",
        "raven",
        "cow",
        "pig",
        "sheep",
        "goat",
        "horse",

    ],
    "movies": [
        "inception",
        "gladiator",
        "titanic",
        "avatar",
        "casablanca",
        "rocky",
        "jaws",
        "amelie",
        "memento",
        "goodfellas",
        "rio",
        "kungfupanda",
        "findingnemo",
        "shrek",
        "zootopia",
        "up",
        "frozen",
        "scarface",
        "pulpfiction",
        "thegodfather",
        "howtotrainyourdragon",
        "monstersinc",
        "thelionking",
        "aladdin",
        "beautyandthebeast",
        "thelittlemermaid",
        "cinderella",
        "sleepingbeauty",
        "snowwhite",
        "tangled",
        "brave",
        "moana",
        "avengers",
        "ironman",
        "spiderman",
        "batman",
        "incredibles",
        "sharktale",
        "ratatouille",
    ],
    "sports": [
        "soccer",
        "basketball",
        "baseball",
        "cricket",
        "tennis",
        "hockey",
        "volleyball",
        "badminton",
        "golf",
        "rugby",
        "swimming",
        "gymnastics",
        "wrestling",
        "boxing",
        "archery",
        "fencing",
        "cheerleading",
        "dancing"
        "snowboarding",
        "gaming",
    ],
    "technology": [
        "computer",
        "internet",
        "keyboard",
        "database",
        "algorithm",
        "microchip",
        "smartphone",
        "robotics",
        "network",
        "compiler",
        "artificial",
        "intelligence",
        "machine",
        "learning"
        "network",
        "database",
        "programming",
        "software",
        "hardware"
        "machine",
    ],
}

HIGH_SCORE_FILE = "hangman_score.txt"

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
]

MAX_WRONG = len(HANGMAN_PICS) - 1


# ----------------------------
# Load high score
# ----------------------------
def load_high_score():
    # try to open file
    # return score (int)
    # if file doesn't exist → return None
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return None
    pass


# ----------------------------
# Save high score
# ----------------------------
def save_high_score(score):
    # open file in write mode
    # write score
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))
    pass


# ----------------------------
# Display word
# ----------------------------
def display_word(word, guessed):
    # return something like: "_ a _ _"
    if not guessed:
        return "_ " * len(word)
    else:
        return " ".join([letter if letter in guessed else "_" for letter in word])
    pass



# ----------------------------
# Game logic
# ----------------------------
def play_game(word):
    # word is provided by caller (selected from a category)
    guessed_letters = set()
    wrong_letters = set()
    wrong_count = 0

    while True:
        # print current word state
        # print wrong guesses
        # print guesses remaining
        print("\n==== Welcome to Hangman! ====")
        print(HANGMAN_PICS[wrong_count])
        print(f"You have {MAX_WRONG - wrong_count} guesses allowed.")
        print("Word:", display_word(word, guessed_letters))
        print("Wrong guesses:", " ".join(wrong_letters))
        print("Guesses remaining:", MAX_WRONG - wrong_count)

        guess = input("Enter a letter (or guess the whole word): ").lower()

        # validate input (letters only)
        if not guess.isalpha():
            print("Invalid input. Please enter letters only.")
            continue

        # if user entered a single letter, handle as before
        if len(guess) == 1:
            if guess in guessed_letters or guess in wrong_letters:
                print("You already guessed that letter.")
                continue

            if guess in word:
                guessed_letters.add(guess)
            else:
                wrong_letters.add(guess)
                wrong_count += 1
        else:
            # user is attempting to guess the whole word
            if guess == word:
                print("Congratulations! You've guessed the word:", word)
                return wrong_count
            else:
                if guess in wrong_letters:
                    print("You already guessed that word.")
                    continue
                print("Incorrect word guess.")
                wrong_letters.add(guess)
                # penalize one wrong guess for an incorrect full-word guess
                wrong_count += 1

        # check WIN condition
        if set(word) == guessed_letters:
            print("Congratulations! You've guessed the word:", word)
            return wrong_count

        # check LOSE condition
        if wrong_count >= MAX_WRONG:
            print("Sorry, you've run out of guesses. The word was:", word)
            return wrong_count

        pass


# ----------------------------
# Main loop
# ----------------------------
def main():
    high_score = load_high_score()

    # print high score if exists
    if high_score is not None:
        print("Current High Score (least wrong guesses):", high_score)
    else:
        print("No high score yet. Be the first to set one!")
    while True:
        # Prompt for category selection
        print("\nChoose a category from the list below or type 'random' to pick any:")
        category_names = list(CATEGORIES.keys())
        for idx, name in enumerate(category_names, start=1):
            print(f"  {idx}. {name.title()} ({len(CATEGORIES[name])} words)")
        choice = input("Enter category name or number (or 'random'): ").strip().lower()

        if choice == "random":
            selected_category = random.choice(category_names)
        else:
            # allow numeric selection
            if choice.isdigit():
                i = int(choice) - 1
                if 0 <= i < len(category_names):
                    selected_category = category_names[i]
                else:
                    print("Invalid number, picking a random category.")
                    selected_category = random.choice(category_names)
            else:
                # accept direct name (partial match allowed)
                matches = [name for name in category_names if name.startswith(choice)]
                if len(matches) == 1:
                    selected_category = matches[0]
                elif choice in category_names:
                    selected_category = choice
                else:
                    print("Unknown category, picking a random category.")
                    selected_category = random.choice(category_names)

        word = random.choice(CATEGORIES[selected_category])
        print(f"Selected category: {selected_category.title()}")

        score = play_game(word)

        # if player wins:
        if score < MAX_WRONG:
             print("You won with", score, "wrong guesses!")
        else:
            print("You lost with", score, "wrong guesses.")

        # check if new high score
        if high_score is None or score < high_score:
            print("New high score! You set a new record with", score, "wrong guesses!")
            save_high_score(score)
            high_score = score
        # save if better
        if score > high_score:
            print("You did not beat the high score of", high_score, "wrong guesses. Try again to set a new record!")
        again = input("Play again? (y/n): ")

        if again != "y":
            break


main()
