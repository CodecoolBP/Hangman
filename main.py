import random
import os


def guessing_the_word(word):
    print(word)
    empty_line = []
    for i in range(len(word)):
        empty_line.append("_")
    print("".join(empty_line))
    while True:
        guess = input("Give me a letter\n")
        guess = guess.upper()
        if len(guess) > 1 or guess in "12345667890":
            clear_screen()
            handling_with_error("Give me a letter and not a number")
        if guess in word:
            empty_line[word.index(guess)] = guess
            
        print("".join(empty_line))


def the_words(group):
    cities = ["BUDAPEST", "KIEV", "LONDON"]
    animals = ["HELLBENDER", "BLOMBFISH"]
    if group == "1":
        return guessing_the_word(cities[random.randint(0, len(cities)-1)])
    elif group == "2":
        return guessing_the_word(animals[random.randint(0, len(animals)-1)])
    # További csoportokat kell megadni.


def hangman_topic():
    clear_screen()
    file = open("/home/daniel/Desktop/working area/Hangman/name_of_game-txt")
    for i in file:
        print(i.strip('\n'))
    to_the_main_menu = input("Press a button to start the game: \n")
    if to_the_main_menu:
        clear_screen()
        main_menu()


def main_menu():

    menu = "Please select a topic:\nPress [1] if you want to guess a city name. \
    \nPress [2] if you want to guess a animal.\nPress [3] if you want to guess a ...\n"
    chosen_group = input(menu)
    if chosen_group in "123":
        return the_words(chosen_group)
    else:
        clear_screen()
        handling_with_error("Please choose from the menu")
        main_menu()


def handling_with_error(text):  # Ennek nincs értelme hogy ha csap kiprintelsz
    print(text+'\n')


def clear_screen():
    os.system('clear')


def main():
    hangman_topic()


if __name__ == '__main__':
    main()
