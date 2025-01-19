import random

# Words and their hints
words_with_hints = {
    "python": "A popular programming language",
    "hangman": "A word guessing game",
    "computer": "A device which is used to do different tasks and it is very helpful",
    "developer": "A person known to make software :Not a software engineer..",
    "programming": "A process which is used to program a computer",
    "apple": "A popular fruit that's often red or green",
    "book": "Something you read for information or enjoyment",
    "chair": "A piece of furniture you sit on",
    "table": "A flat surface used for dining or working",
    "house": "A place where people live",
    "water": "A liquid that is essential for life",
    "school": "A place where students learn",
    "pizza": "A popular Italian dish with cheese and toppings",
    "phone": "A device used to make calls or send messages",
    "music": "Sounds organized in a way that's pleasing to hear",
    "bread": "A staple food often used for sandwiches",
    "clock": "A device used to tell the time",
    "light": "Something that makes things visible",
    "dog": "A common pet that's often called man's best friend",
    "cat": "A small, furry animal that's a popular pet",
    "tree": "A tall plant with a trunk and branches",
    "sun": "The star at the center of our solar system",
    "milk": "A white liquid often added to coffee or cereal",
    "pen": "A tool used for writing",
    "ball": "A round object used in many sports",
    "shirt": "An item of clothing worn on the upper body",
    "car": "A vehicle with four wheels used for transport",
    "train": "A form of transportation that runs on tracks",
    "hat": "Something you wear on your head",
    "bag": "Used to carry things like books or groceries",
    "fish": "An animal that lives in water",
    "shoe": "Something you wear on your feet",
    "door": "You open this to enter or leave a room",
    "bread": "Used to make sandwiches",
    "road": "A path for cars and vehicles to travel on",
    "cloud": "A fluffy white object in the sky",
    "snow": "Frozen water that falls from the sky",
    "rain": "Water that falls from the clouds",
    "bird": "An animal that can fly and lays eggs",
    "cake": "A sweet dessert often eaten at celebrations",
    "milk": "A white drink that comes from cows",
    "ice": "Frozen water, often added to drinks",
}


# Hangman visual representation
hangman_visual = {
    6: "❤️ ❤️ ❤️ ❤️ ❤️ ❤️",
    5: "❤️ ❤️ ❤️ ❤️ ❤️",
    4: "❤️ ❤️ ❤️ ❤️",
    3: "❤️ ❤️ ❤️",
    2: "❤️ ❤️",
    1: "❤️",
    0: "💀"
}

# Main game loop
while True:
    # Choose a random word and its hint
    word, hint = random.choice(list(words_with_hints.items()))
    guessed_word = ["_"] * len(word)
    lives = 6
    guessed_letters = []

    print("\nWelcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    word = word.lower()  # Ensure case insensitivity

    # Game logic loop
    while lives > 0 and "_" in guessed_word:
        print("\n" + " ".join(guessed_word))
        print(f"Lives left: {hangman_visual[lives]} ({lives})")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        guess = input("Guess a letter or type 'hint' to use a hint (costs 1 life): ").lower()

        # Handle empty input
        if not guess.strip():
            print("Input cannot be empty. Please guess a letter.")
            continue

        if guess == "hint":
            if lives > 1:
                lives -= 1
                print(f"Hint: {hint} (You lost 1 life for using the hint!)")
            else:
                print("You don't have enough lives to use a hint!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed that letter: {guess}")
            continue  # Skip to the next input

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            print("\n" + " ".join(guessed_word))  # Show the updated word immediately
        else:
            print("Wrong guess!")
            lives -= 1

    # Game over
    if "_" not in guessed_word:
        print(f"Congratulations! 🎉 You guessed the word: {''.join(guessed_word)}")
    else:
        print(f"Game over! The word was: {word}")

    # Replay option
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
