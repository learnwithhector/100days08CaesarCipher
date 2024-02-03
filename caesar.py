from art import logo
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(message, shift_amount):
    ciphertext = ""
    for letter in message:
        index = alphabet.index(letter)
        new_index = index + shift_amount
        if new_index > 25:
            new_index %= 26
        ciphertext += alphabet[new_index]
    print(f"The encoded text is {ciphertext}")


def decrypt(ciphertext, shift_amount):
    message = ""
    for letter in ciphertext:
        index = alphabet.index(letter)
        new_index = index - shift_amount
        if new_index < 0:
            new_index %= 26
        message += alphabet[new_index]
    print(f"The decoded text is {message}")


def caesar(input_text, shift_amount, shift_direction):
    if shift_direction.casefold() != 'encode' and shift_direction.casefold() != 'decode':
        print("Shift direction must be either encode or decode")
    else:
        if shift_direction == 'decode':
            shift_amount *= -1
        output_text = ""
        for letter in input_text:
            if not letter.isalpha():
                output_text += letter
            else:
                index = alphabet.index(letter)
                new_index = index + shift_amount
                if new_index < 0 or new_index > 25:
                    new_index %= 26
                output_text += alphabet[new_index]
        print(f"The {'en' if shift_direction == 'encode' else 'de'}coded text is {output_text}")


def main():
    while True:
        os.system('cls')
        print(logo)
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(text, shift, direction)
        again = input("Type `y` to go again or anything else to quit ").casefold()
        if again != 'y' and again != 'yes':
            break


main()
