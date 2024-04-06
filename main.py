from tkinter import *
import pandas as pd
import random
import time

window = Tk()
window.title("Typing Test")
window.minsize(400,200)


def generate_word():
    words = pd.read_csv("10000_Words.csv")
    display_word = random.choice(words.words)
    words_to_type.configure(state=NORMAL)
    words_to_type.delete(1.0, END)
    words_to_type.configure(fg='black')
    user_submission.delete(1.0, END)
    words_to_type.insert(END,display_word)
    words_to_type.configure(state=DISABLED)
    user_submission.focus_set()


def check():
    word = words_to_type.get(1.0, END)
    guess = user_submission.get(1.0, END)
    char_num = len(guess) -1
    for letter in range(char_num):
        if guess[letter] == word[letter] and guess[:letter] == word[:letter]:
            words_to_type.configure(fg='green')
        elif guess[letter] != word[letter]:
            words_to_type.configure(fg='red')


def key_press(event):
    global key_pressed
    key = event.char
    check()
    key_pressed += 1


def key_press_enter(event):
    key = event.char
    words_to_type.configure(state=NORMAL)
    word = words_to_type.get(1.0, END)
    guess = user_submission.get(1.0, END)
    if word == guess[:-1]:
        words_to_type.configure(state=DISABLED)
        generate_word()
        wpm()
    else:
        words_to_type.configure(state=DISABLED)
        user_submission.delete(1.0, END)


def wpm():
    end = time.time()
    time_elapsed = end - start_time
    time_in_minutes = time_elapsed/60
    if time_in_minutes > 0:
        wpm = (key_pressed / 5) // time_in_minutes
        wpm_display.configure(text=f"WPM : {round(wpm)}")
    else:
        pass




def start():
    global start_time
    global key_pressed
    key_pressed = 0
    start_time = time.time()
    words_to_type.configure(state=NORMAL)
    words_to_type.delete(1.0,END)
    words_to_type.configure(state=DISABLED)
    user_submission.configure(state=NORMAL)
    user_submission.delete(1.0, END)
    user_submission.configure(state=DISABLED)
    user_submission.configure(state=NORMAL)
    generate_word()
    window.bind('<Return>', key_press_enter)
    window.bind('<Key>', key_press)


title_label = Label(text="Press enter after typing word.")
title_label.grid(column=1, row=0, pady=5)
words_to_type_label = Label(text="Word to type: ")
words_to_type_label.grid(column=0, row=2, padx=5, sticky=E)
words_to_type = Text(width=20, height=1)
words_to_type.grid(column=1, row=2, pady=15,ipady=2)
words_to_type.configure(state=DISABLED)
user_submission_label = Label(text="Type here: ")
user_submission_label.grid(column=0, row=3, padx=5,sticky=E)
user_submission = Text(width=20, height=1)
user_submission.grid(column=1, row=3, ipady=2)
user_submission.configure(state=DISABLED)
wpm_display = Label(text="WPM : ")
wpm_display.grid(column=2, row=3, padx=10, sticky=W)
start_test = Button(text="Start", command=start)
start_test.grid(column=1, row=4)


window.mainloop()



