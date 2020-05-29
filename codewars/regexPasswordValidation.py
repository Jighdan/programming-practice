"""
You need to write regex that will validate a password to make sure it meets the following criteria:
- At least six characters long
- Contains a lowercase letter
- Contains an uppercase letter
- Contains two numbers
"""

import re

class Password:
    def __init__(self, password):
        self.password = password
        self.validations = {
            "length": True,
            "numbers": True,
            "lowercase": True,
            "uppercase": True
        }

    def search_invalidated(self, password):
        HAS_NUMBERS = re.findall("[1-9]", password)
        HAS_LOWERCASE = re.findall("[a-z]", password)
        HAS_UPPERCASE = re.findall("[A-Z]", password)
        if len(password) < 6:
            self.validations["length"] = False
        if len(HAS_NUMBERS) < 2:
            self.validations["numbers"] = False
        if len(HAS_LOWERCASE) < 0:
            self.validations["lowercase"] = False
        if len(HAS_LOWERCASE) < 0:
            self.validations["uppercase"] = False
        
    def confirm_validation(self):
        self.search_invalidated(self.password)
        errors = {
            "length": "Your password must be at least 6 characters long",
            "numbers": "Your password must contain at least two numbers",
            "lowercase": "Your password must have at least one lowercase character",
            "uppercase": "Your password must have at least one upper case character"
        }

        printable_errors = []
        print(self.validations.keys())
        for invalid in self.validations.keys():
            if self.validations[invalid] == False:
                printable_errors.append(errors[invalid])

        return printable_errors

    def validate(self):
        validation = self.confirm_validation()
        if len(validation) > 1:
            print("Invalid Password!")
            for error in validation:
                print("\t - {}".format(error))
        else:
            print("Valid Password!\n")