import random
from words import animal_list
from words import city_list
from hangman_stages import display_hangman

category = [animal_list, city_list]


def choose_category(category1):

    print("\n------------Let's play Hangman!------------\n")
    print("Please choose a category: ")
    print("1) Animals.")
    print("2) Cities.\n")
    x = (input("Enter your favorite category to play!(Eg: 1 for Animals,etc.) : "))

    while (not x.isdigit() or int(x) > len(category)):  # Verifying whether x is a valid input or not.
        x = input("Enter a valid category number: ")

    x = int(x)

    return category1[x - 1]


def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()


def play(word):
    complete_word = ''
    for i in word:
        if i == '-':
            complete_word += '-'
        else:
            complete_word += '_'

    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print(display_hangman(tries))
    print(complete_word)
    print("\n")

    while (not guessed and tries > 0):
        guess = input("Please input a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)

            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)

            else:
                print("Great,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(complete_word)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                for index in indices:
                    word_as_list[index] = guess
                complete_word = "".join(word_as_list)

                if "_" not in complete_word:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)

            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)

            else:
                guessed = True
                complete_word = word

        else:
            print("Not a valid guess!")
        print(display_hangman(tries))
        print(complete_word)
        print("\n")
        print("You have " + str(tries) + " tries left.\n")


    if guessed:
        print("Hurray!, you guessed the word correctly! Congrats...")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ", Maybe next time!")


def main():
    choice = choose_category(category)
    word = get_word(choice)
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        choice = choose_category(category)
        word = get_word(choice)
        play(word)


if __name__ == '__main__':
    main()