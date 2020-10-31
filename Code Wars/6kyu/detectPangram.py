"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
"""

def detect_pangram(sentence: str) -> bool:
    alphabet: List[str] = ["abcdefghijklmnopqrstuvwxyz"].split("")
    alphabetChecker: Dict[str, bool] = {letter: false for letter in alphabet}
    for char in sentence.lower().split(""):
        if check := alphabetChecker[char] == False:
            check = True

    return False if False in alphabetChecker.values() else True

