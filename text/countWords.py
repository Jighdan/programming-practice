import os
import argparse
from pprint import pprint

CONJUCTIONS = ["for", "and", "nor", "but", "or", "yet", "so"]

class TextDocument:
    def __init__(self, file):
        self.file = file
    
    def countWords(self):
        wordList = {}

        with open(self.file) as f:
            text = f.read()
            separatedWords = text.split(" ")
            for word.lower() in separatedWords:
                if word == (" " | "\n") | word in CONJUCTIONS:
                    wordList.remove(word)
                else:
                    wordList[word] = separatedWords.count(word)

        return wordList
    
    def isTextFile(self):
        file = self.file
        if (os.path.isfile(file) & file.endswith(".txt")) == True:
            return True
        else:
            return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="text file to count words from")
    arguments = parser.parse_args()

    textFile = TextDocument(arguments.file)
    if textFile.isTextFile() == True:
        pprint(textFile.countWords())
    else:
        pprint("Invalid Text File")
