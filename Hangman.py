import random

word_list = ['python', 'java', 'kotlin', 'javascript']

answer = random.choice(word_list)

correct_letters = set()
guessed_letters = set()

def show_word():
    word = ''
    for letter in answer:
        if letter in correct_letters:
            word += letter
        else:
            word += '-'
    print(word)
    return word

def hangman_game():
    remainder_guess = 8
    while remainder_guess > 0:
        if show_word() == answer:
            print('You survived!')
            print()
            break

        input_letter = input(f'Input a letter: ')

        if len(input_letter) > 1:
            print('You should input a single letter')
            print()

        elif input_letter.isalpha() and input_letter.islower() == True:
            if input_letter in correct_letters:
                print("You've already guessed this letter")
                print()
            elif input_letter in guessed_letters:
                print("You've already guessed this letter")
                print()
            elif input_letter in answer:
                correct_letters.update(input_letter)
                print()
            elif input_letter not in answer:
                print("That letter doesn't appear in the word")
                remainder_guess -= 1
                guessed_letters.update(input_letter)
                if remainder_guess != 0:
                    print()
                else:
                    print('You lost!')
                    print()
                    break
        else:
            if input_letter.isalpha() == False or input_letter.islower() == False:
                print('Please enter a lowercase English letter')
                print()

print('H A N G M A N')
user_type = input(f'Type "play" to play the game, "exit" to quit: ')
print()

while user_type != 'exit':
    if user_type == 'play':
        hangman_game()
    user_type = input(f'Type "play" to play the game, "exit" to quit: ')
    print()