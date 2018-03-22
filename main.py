import random
import os


def read_from_file(filename):
    file = open(filename)
    cont = file.readlines()
    for line in cont:
        print(line.strip("\n"))


def guessing_the_word(word):
    good_guess = 0
    max_guess = 5
    empty_line = []
    list_of_wrong_letters = []
    for i in range(len(word)):
        empty_line.append("_")
    print("".join(empty_line))

    while True:
        guess = input("Give me a letter\n")
        guess = guess.upper()
        if len(guess) > 1 or guess in "12345667890":
            clear_screen()
            print("Give me a letter and not a number")
        elif guess in word:
            clear_screen()
            empty_line[word.index(guess)] = guess
            good_guess += 1
        else:
            clear_screen()
            list_of_wrong_letters.append(guess)
            max_guess -= 1

        point_check(good_guess, max_guess, word)
        print("".join(empty_line))
        print("\nThese are your wrong letters\n", ",".join(list_of_wrong_letters))


def point_check(good_guess, max_guess, word):
    game_file = {"win": "/home/daniel/Desktop/working area/Hangman/man.txt",
                 "lose": "/home/daniel/Desktop/working area/Hangman/hangman_drawing.txt"}
    clear_screen()
    if max_guess == 0:
        read_from_file(game_file["lose"])
        print("YOU LOSE\n")       
    elif good_guess == len(word):
        read_from_file(game_file["win"])
        print("YOU WON\n")


def the_words(group):
    all_group = {"1": ["FOSHAN", "BRASÍLIA", "MILANO", "BUKAREST"], "2": [
        "DOLPHIN", "DRAGONFLY", "PIGEON"], "3": ["DONUTS", "WALNUTS", "YOGURT"]}
    return random.choice(all_group[group])


def hangman_topic():
    clear_screen()
    file = open("/home/daniel/Desktop/working area/Hangman/name_of_game-txt")
    for i in file:
        print(i.strip('\n'))
    to_the_main_menu = input("Press a button to start the game: \n")
    if to_the_main_menu:
        clear_screen()


def main_menu():
    chosen_group = "0"
    while chosen_group not in "123":
        menu = "Please select a topic:\nPress [1] if you want to guess a city name. \
        \nPress [2] if you want to guess a animal.\nPress [3] if you want to guess a food\n"
        chosen_group = input(menu)
        clear_screen()
    return chosen_group


def clear_screen():
    os.system('clear')


def main():
    hangman_topic()
    chosen_group = main_menu()
    the_world_to_guess = the_words(main_menu())
    guessing_the_word(the_world_to_guess)


if __name__ == '__main__':
    main()
