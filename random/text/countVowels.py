import argparse

VOWELS = ["a", "e", "i", "o", "u"]
countedVowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

def countVowel(letter):
    if letter in VOWELS:
        countedVowels[letter] += 1

def countTotalVowels(countedVowels):
    vowels = countedVowels.values()
    return sum(vowels)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--word", required=True, help="word to count vowels from")
    arguments = parser.parse_args()
    
    for letter in arguments.word:
        countVowel(letter)
    
    sumOfVowels = countTotalVowels(countedVowels)
    print("Vowels found: \n\t{}\nFor a total of: {} vowels".format(countedVowels, str(sumOfVowels)))
