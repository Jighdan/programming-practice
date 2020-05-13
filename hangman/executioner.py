from random import choice
import sys

def put_on_mask():
    intro = "Hello there- for your crimes you have been sentenced to hang... unless you can guess what word I'm thinking about in five chances ;)\n1. Go for it | 2. Instructions | 3. Die anyways"
    print(intro)

def show_instructions():
    instructions = "I will think of a word and you will have to guess it, in at least 5 chances"
    return instructions

def present_word(word):
    intro = "\nThe word I'm thinking about has {} letters".format(str(len(word)))
    print(intro)

def announce(word_progress, used_letters, lives):
    announcement = "uncovered word = {}\nused letters = {}\nlives left = {}".format(word_progress, used_letters, lives)
    print(announcement)

def got_it(huh):
    if huh is True:
        right = ["Lucky you", "Could it be that you've got a chance?", "What's nex?", "Aww are you getting excited"]
        print("Correct! {}".format(choice(right)))
    else:
        wrong = ["No-Duh!", "Psst there might be a 'j' or 'k' on that word", "I DO love my profession", "Nope, \"hang\" there bud", "Here is were your spelling comes at play", "That's it! Die faster", "You'll soon meet your Creator", "Almost right", "Better dead than iliterate"]
        print("Wrong! {}".format(choice(wrong)))

def used_word(letter):
    print("You already used the letter \"{}\"!".format(letter.upper()))

def win_game(word):
    congratulate = "Your cleverness evaded death itself! The word indeed was \"{}\"".format(word)
    print("{}\nⓗⓐⓝⓖⓜⓐⓝ by @jighdan".format(congratulate))

def end_game(tell_me, word):
    if tell_me is True:
        print("You are dead, the word you were looking for was \"{}\"\nⓗⓐⓝⓖⓜⓐⓝ by @jighdan".format(word))
    else:
        print("\nⓗⓐⓝⓖⓜⓐⓝ by @jighdan")
    sys.exit()
