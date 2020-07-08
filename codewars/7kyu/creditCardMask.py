"""
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
"""

def credit_card_mask(text):
    if len(text) >= 4:
        texted = list(text)
        for letter in texted[:4]:
            letter = "#"
    return "".join(texted)

