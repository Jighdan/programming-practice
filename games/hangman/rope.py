from executioner import announce, got_it, present_word, used_word, win_game, end_game
from string import ascii_lowercase
from random import choice
import requests

def fetch_word():
    url = "https://raw.githubusercontent.com/Xethron/Hangman/master/words.txt"
    word_text = requests.get(url).text
    word_list = [word.lower() for word in word_text.split("\n")]
    return choice(word_list)

def hide_word(word):
    return list("_"*len(word))

def validate_input(guess_taken):
    try:
        if type(guess_taken) != str or len(guess_taken) > 1:
            return False
        elif guess_taken in ascii_lowercase:
            return True
        else:
            return False
    except (TypeError, IndexError):
        return False

def is_word_uncovered(hidden_word):
    if "_" in hidden_word:
        return False
    else:
        return True

def list_indexes_of_letter(word, letter):
    start_at = -1
    indexes = []
    while True:
        try:
            index = word.index(letter, start_at + 1)
        except ValueError:
            break
        else:
            indexes.append(index)
            start_at = index
    if len(indexes) >= 1:
        return indexes
    else:
        return False

def put_rope_on_neck():
    word = fetch_word()
    hidden_word = list(hide_word(word))
    lives = 5
    used_letters = []
    present_word(word)

    while True:
        if "".join(hidden_word) == word:
            win_game(word)
            break

        guess = input("\nMy guess: ")
        if validate_input(guess) is True:
            if guess not in used_letters:
                used_letters.append(guess)
                indexer = list_indexes_of_letter(word, guess)
                if isinstance(indexer, list) is True:
                    if len(indexer) == 1:
                        hidden_word[indexer[0]] = guess
                    else:
                        for index in indexer:
                            hidden_word[index] = guess
                    got_it(True)
                else:
                    lives -= 1
                    if lives >= 1:
                        got_it(False)
                    elif lives == 0:
                        end_game(True, word)
                        break
            else:
                used_word(guess)

            v_hidden_word = " ".join(hidden_word)
            v_used_letters = "-".join(used_letters)
            announce(v_hidden_word, v_used_letters, str(lives))
        else:
            print("Invalid Input!\n")
