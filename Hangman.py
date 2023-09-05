# Hangman
import requests

# Extracting Raw Data from website
url = "https://www.mit.edu/~ecprice/wordlist.10000"
html = requests.get(url)

# Converts the bytes to regular strings
html_tostring = html.content.decode('utf-8')
words = html_tostring.splitlines()

# removes documentcreatetextnode
words.remove(max(words, key=len))

HANGMAN_ASCII_ART = [
    """
    +---+
        |
        |
        |
       ===
    """,
    """
    +---+
    O   |
        |
        |
       ===
    """,
    """
    +---+
    O   |
    |   |
        |
       ===
    """,
    """
    +---+
    O   |
   /|   |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
   /    |
       ===
    """,
    """
    +---+
    O   |
   /|\\  |
   / \\  |
       ===
    """
]

# Randomly select a word from the list
import random

n = random.randint(0, len(words) - 1)  # Fixed the range
# word_of_day = words[n]
word_of_day = 'book'
word_w_blanks = ['_' for _ in word_of_day]

# Creating GUI
from tkinter import*

base = Tk()
base.title('Hangman Game')

def update_hangman(stage):
    hangman.config(text=HANGMAN_ASCII_ART[stage])

def end_game(condition):
    if condition == 'Win':
        result = " YOU WIN! "
    else:
        result = " YOU LOSE " + '\n' + 'The word was ' + word_of_day
    result_label.config(text=result)
    guess_entry.config(state='disabled')
    result_label.pack()

def validate_input(P):
    if P.isdigit():
        return False
    return True

def clear_entry():
    guess_entry.delete(0, END)

def check_guess():
    global word_w_blanks
    guess = guess_entry.get()
    if validate_input(guess):
        if guess in word_of_day:
            for index in range(len(word_of_day)):
                if word_of_day[index] == guess:
                    word_w_blanks = word_w_blanks[:index] + [guess] + word_w_blanks[index + 1:]
            word_label.config(text=' '.join(word_w_blanks))  # Add space between letters
            if '_' not in word_w_blanks:
                end_game('Win')
        else:
            global mistake
            mistake = mistake + 1
            update_hangman(mistake)
            if mistake == 6:
                end_game('lose')
        clear_entry()

title_label = Label(base, text=" HANGMAN ", font=('Courier', 20, 'italic'))
title_label.grid(row=0, column=0, columnspan=2)

hangman = Label(base, text=HANGMAN_ASCII_ART[0], font=('Courier', 50))
hangman.grid(row=1, column=0, columnspan=2)

# Word Display
word_label = Label(base, text=' '.join(word_w_blanks), font=('Courier', 40))  # Add space between letters
word_label.grid(row=2, column=0, columnspan=2)

# Guess Entry
validate_input_func = base.register(validate_input)
guess_entry = Entry(base, validate='key', validatecommand=(validate_input_func,'%P'), width=2, font=('Courier', 40))
guess_entry.grid(row=3, column=0)
 
# Guess Button
guess_button = Button(base, text=' Guess ', command=check_guess, width=10, height=2)
guess_button.grid(row=3, column=1)

# Result Display
result_label = Label(base, font=('Courier', 30, 'bold'))  # Reduced font size for better fit
result_label.grid(row=4, column=0, columnspan=2)

# Initialize mistakes
mistake = 0
update_hangman(mistake)

base.mainloop()
