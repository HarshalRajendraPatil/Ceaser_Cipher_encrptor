import art
from os import system

system("cls");

print(art.logo);

playagain = False;

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(word, slide, c_direction):
    end_text = "";
    if c_direction == "decode":
            slide *= -1;
    for letter in word:
        if letter in alphabet:
            position = alphabet.index(letter);
            new_position = position + slide;
            end_text += alphabet[new_position];
        else:
            end_text += letter;
    print(end_text);

while(playagain != True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower();
    text = input("Type your message:\n").lower();
    shift = int(input("Type the shift number:\n"));
    if shift > 26:
        shift = shift / 26;

    ceaser(word=text, slide=shift, c_direction=direction);

    user_choice = input("Type 'yes' if you want to go again or 'no' to exit.").lower();
    if user_choice == "yes":
        playagain = False;
    else:
        playagain = True
