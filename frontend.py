#!/usr/bin/env python3

# https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.englishclub.com%2Fimages%2Fesl-games%2Fhangman-150.png&imgrefurl=https%3A%2F%2Fwww.englishclub.com%2Fesl-games%2Fhangman&tbnid=DxT3rciERUl0dM&vet=12ahUKEwiUsKSl5OjxAhWwgM4BHXgaAiAQMygNegUIARDRAQ..i&docid=Rhrl4KExmOWbLM&w=150&h=217&q=hangman%20game&hl=pt-PT&client=ubuntu&ved=2ahUKEwiUsKSl5OjxAhWwgM4BHXgaAiAQMygNegUIARDRAQ
# https://www.englishclub.com/esl-games/hangman/
# https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.com%2FBenjamin-Wirtschafter-HangMan-Free%2Fdp%2FB074LTNMVS&psig=AOvVaw3JX1dfRHpJHCMq2RTV5U59&ust=1626565897123000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCJjhub7k6PECFQAAAAAdAAAAABAJ
# https://www.amazon.com/Benjamin-Wirtschafter-HangMan-Free/dp/B074LTNMVS
# Hangman

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import ImageTk, Image
from my_widgets import my_button
from backend import *
import threading
from time import sleep


class MainWindow():
    def __init__(self):
        """Initializes some attributes of the backend and frontend game.
        This method does:
        - initializes backend,
        - sets the lives,
        - sets the word,
        - sets the word letters,
        - sets the background color,
        - initializes the frontend,
        - sets some string vars to update some labels later,
        - sets the name and the geometry of the app,
        - the frames of the window,
        - the labels of the window,
        - some Styles (for frames and labels),
        - sets the values of some string vars,
        - reads the user input by keyboard.
        """
        self.game = Game(words)
        self.game.lives = 7
        self.game.choose_word()
        # self.game.word = "abcd".upper()
        self.game.set_word_letters()

        self.bgcolor = "lightgrey" 
        self.root = Tk()
        self.word_list = StringVar()
        self.lives_var = StringVar()
        self.used_letters_var = StringVar()
        self.errorvar = StringVar()
        self.root["bg"] = self.bgcolor
        self.root.title("Hangman")
        self.root.geometry("950x300")
        self.root.minsize(950, 300)
        # https://stackoverflow.com/questions/34276663/tkinter-gui-layout-using-frames-and-grid
        # grid problem: object.grid() returns None but object returns the object
        self.style = Style()
        self.style.configure("TFrame", background= self.bgcolor)
        self.imgframe = Frame(self.root, style="TFrame")
        self.imgframe.grid(row=0, column=0, sticky=W)
        self.btnframe = Frame(self.root, style="TFrame")
        self.btnframe.grid(row=0, column=1)
        self.infframe = Frame(self.root, style="TFrame")
        self.infframe.grid(row=1, column=0)
        self.style.configure("TLabel", background=self.bgcolor)
        self.liveslbl = Label(self.infframe, textvariable=self.lives_var, style="TLabel")
        self.liveslbl.grid(row=0, column=0, sticky=W)
        self.lives_var.set(f"lives: {self.game.lives}")
        self.usedletterslbl = Label(self.infframe, textvariable=self.used_letters_var, style="TLabel", width=45)
        self.usedletterslbl.grid(row=0, column=1, sticky=W)
        self.used_letters_var.set("used letters: ")
        self.style.configure("Error.TLabel", foreground="red")
        self.errorlbl = Label(self.infframe, textvariable=self.errorvar, style="Error.TLabel") 
        self.errorlbl.grid(row=1, columnspan=2, sticky=W)
        self.root.bind("<Key>", self.try_a_letter)


    def place_image(self, img):
        """Method to place a image in the image frame.

        Args:
            img (str): The name of the file with the image.
        """
        # https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python
        # https://stackoverflow.com/questions/32060837/remove-border-of-tkinter-button-created-with-an-image

        self.img = Image.open(img)
        self.img = ImageTk.PhotoImage(self.img, Image.ANTIALIAS)
        self.imglabel = Label(master=self.imgframe, image=self.img, style="TLabel")
        self.imglabel.image = self.img
        self.imglabel.grid()


    def update_image(self, img):
        """Method to update the previous image of the image frame.

        Args:
            img (str): The name of the file with the image.
        """
        self.img = Image.open(img)
        self.img = ImageTk.PhotoImage(self.img, Image.ANTIALIAS)
        self.imglabel.configure(image=self.img)
        self.imglabel.image = self.img


    def place_buttons(self):
        # in the end I don't used this ↓
        # https://stackoverflow.com/questions/47352833/no-way-to-color-the-border-of-a-tkinter-button
        """Method to create and place all the alphabet buttons of the game.
        It was used customizable buttons because of the borders of tkinter.
        """
        for c in range(65, 93):
            self.btn = my_button(master=self.btnframe, text=chr(c) if c <= 90 else None, id=c, underline=0, width=7, command=lambda char = chr(c) if c <=90 else None: self.try_a_letter(char))
            self.btn.grid(row=c%4-1 if c%4 != 0 else 3, column=(c-65)//4, padx=3, pady=3)

    
    def clean_lbl(self, time):
        """A function to update the errorvar after some seconds.

        Args:
            time (int): Time in seconds to maintaine the message after reset it.
        """
        sleep(time)
        if threading.active_count() <= 2 and self.game.word not in self.errorvar.get():
            self.errorvar.set("")


    def start_thread(self, function, *args):
        """A method to execute a thread.

        Args:
            function (function): A function what do you want to execute.
            If you want you can add args to the function with *args variable.
        """
        thread = threading.Thread(target=function, args=(*args,), daemon=True)
        thread.start()


    def try_a_letter(self, character):
        """Method that continues the game. Reads the input character,
        by button click or keyboard, and verifies if the letter is in
        the word. Also if you don't have lives or you win the game this
        method ends it. There are some mesage errors in this method too.

        Args:
            character (char/str): Any letter in upper case.
        """
        try:
            character = character.char.upper()
        except AttributeError:
            pass
        if character in self.game.alphabet - self.game.used_letters:
            self.game.used_letters.add(character)
            if self.game.lives and self.game.word_letters:
                used_letters = " ".join(self.game.used_letters)
                self.used_letters_var.set(f"used letters: {used_letters}")

            if character in self.game.word_letters and self.game.lives:
                self.game.word_letters.remove(character)
                self.update_underlines()
                if not self.game.word_letters:
                    self.end_game(f"You win, congratulations! The word were {self.game.word}!")
                    # self.errorvar.set(f"You win, congratulations! The word were {self.game.word}!")
            elif self.game.lives and self.game.word_letters:
                self.game.lives -= 1
                self.lives_var.set(f"lives: {self.game.lives}")
                self.update_image(f"img/hangman_{7-self.game.lives}.png")
                if not self.game.lives:
                    # self.errorvar.set(f"You lose. The word were {self.game.word}!")
                    self.end_game(f"You lose. The word were {self.game.word}!")
        elif character not in self.game.alphabet and self.game.lives and self.game.word_letters:
            self.errorvar.set("This character isn't valid!") # update label with a error msg, character not valid
            self.start_thread(self.clean_lbl, 3)
        elif character in self.game.used_letters and self.game.lives and self.game.word_letters:
            self.errorvar.set("You already used this character!") # character already used
            self.start_thread(self.clean_lbl, 3)
        

    def update_underlines(self):
        """Change the initial underlines for the respective letters if match
        with the used letters.
        """
        temp_list = [letter if letter in self.game.used_letters else '_' for letter in self.game.word]
        word = " ".join(temp_list)
        self.word_list.set(word)


    def set_underlines(self):
        """Place as many underlines as the number of letters in the word label.
        """
        self.lblword = Label(master=self.infframe, textvariable=self.word_list, width=30)
        self.lblword.grid(columnspan=2, sticky=W)
        self.update_underlines()


    def end_game(self, msg):
        """A method to open a new window to decide if the user wants to
        restart the game or not.

        Args:
            msg (str): The final message what you want to show to the user in the new window.
        """
        self.newroot = Toplevel(self.root)
        self.finish_game = FinishGameWindow(self.newroot, msg)
        self.finish_game.place_win_lbl()
        self.finish_game.place_question_lbl()
        self.finish_game.place_buttons(command_yes=self.command_yes, command_no=self.command_no)
        self.finish_game.root.grab_set()
        # _class(self.new)


    def command_yes(self):
        """Destroy the new window and restarts the game.
        """
        self.finish_game.root.grab_release()
        self.finish_game.root.destroy()
        self.restart_game()
    

    def command_no(self):
        """Destroy the new window and finishes the game.
        """
        self.finish_game.root.destroy()
        self.root.destroy()


    def main_loop(self):
        """Mainloop method.
        """
        self.root.mainloop()

    
    def start_game(self):
        """Method to execute the app once.
        """
        self.place_image("img/hangman.png")
        self.set_underlines()
        self.place_buttons()
        self.main_loop()


    def restart_game(self):
        """Method to restart the game.
        """
        self.update_image("img/hangman.png")
        self.game.lives = 7
        self.game.choose_word()
        # self.game.word = "abcd".upper()
        self.game.set_word_letters()
        self.update_underlines()
        self.lives_var.set(f"lives: {self.game.lives}")
        self.used_letters_var.set("used letters:")




class FinishGameWindow():
    def __init__(self, root="", msg=""):
        """Initializes some attributes of the new window.
        Some of these attributes are:
        - Initializes the window,
        - Makes the size of the window fixed,
        - Sets the background color,
        - Sets the final message to show to user.

        Args:
            root (str, optional): The root of the new window. Defaults to "".
            msg (str, optional): The final message to show to user. Defaults to "".
        """
        self.root = root
        self.root.resizable(width=False, height=False)
        self.bg_color ="lightgrey"
        self.root["bg"] = self.bg_color
        self.msg = msg
    
    
    def place_win_lbl(self):
        """Method to place the win/lose label.
        """
        self.win_lbl = Label(self.root, text=self.msg, background=self.bg_color)
        self.win_lbl.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


    def place_question_lbl(self):
        """Method to place the yes or no question to the user.
        Basically if he wants to continue playing or not.
        """
        self.question_lbl = Label(self.root, text="Do you want to play again?", background=self.bg_color)
        self.question_lbl.grid(row=1, column=0, padx=10, pady=10, columnspan=2)


    def place_buttons(self, command_yes=None, command_no=None):
        """Method to place the yes/no buttons.

        Args:
            command_yes (function, optional): The function to execute if the answer is yes. Defaults to None.
            command_no (function, optional): The function to execute if the answer is no. Defaults to None.
        """
        self.btn_yes = my_button(self.root, text="Yes", id=1, command=command_yes)
        self.btn_yes.grid(row=2, column=0, padx=3, pady=3)
        self.btn_yes = my_button(self.root, text="No", id=2, command=command_no)
        self.btn_yes.grid(row=2, column=1, padx=3, pady=3)


if __name__ == '__main__':
    hangman = MainWindow()
    hangman.start_game()
