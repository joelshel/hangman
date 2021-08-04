#!/usr/bin/env python3

from tkinter import Tk
from tkinter.ttk import Button, Frame, Style

class my_button(Frame):
    def __init__(self, master=None, text="", command=None, id=0, underline=-1, width=10):
        """Method to create a customized button with border.

        Args:
            master (widget, optional): The widget/frame where would be placed the button. Defaults to None.
            text (str, optional): The button text. Defaults to "".
            command (function, optional): A function to execute when the button is clicked. Defaults to None.
            id (int, optional): The buttons identifier. Defaults to 0.
            underline (int, optional): The number of the position of the letter you want to underline.
            If -1 no letters will be underlined. Defaults to -1.
            width (int, optional): Width of the button equivalent to the number of characters the button can show. Defaults to 10.
        """
        super().__init__()
        self.id = id
        self.style = Style()
        self.frm = Frame(master=master, style=f"MyFrm{self.id}.TFrame")
        self.style.configure(f"MyFrm{self.id}.TFrame", background="lightgrey")
        self.btn = Button(master=self.frm, text=text, command=command, takefocus=False, style="MyBtn.TButton", underline=underline, width=width)
        self.style.map("MyBtn.TButton",
                       foreground=[("pressed", "green"), ("active", "blue"), ("!active", "black")],
                       background=[("pressed", "#F3F3EA"), ("active", "white"), ("!active", "lightgrey")],
                       relief=[("pressed", "flat"), ("active", "flat"), ("!active", "flat")],
                    #    borderwidth=[("pressed", 2)],
                       ) 
        self.btn.bind("<Button-1>", lambda exec: self.config_frm("lightgreen"))
        self.btn.bind("<ButtonRelease-1>", lambda exec: self.config_frm("lightgrey"))

    def grid(self, column=None, row=None, padx=0, pady=0):
        """Method to grid the button.

        Args:
            column (int, optional): Column position in master. Defaults to None.
            row (int, optional): Row position in master. Defaults to None.
            padx (int, optional): How many pixels to pad widget horizontally. Defaults to 0.
            pady (int, optional): How many pixels to pad widget vertically. Defaults to 0.
        """
        self.frm.grid(column=column, row=row)
        self.btn.grid(padx=padx, pady=pady)

    def config_frm(self, bd_color=None):
        """Method to configure the border color of the button.

        Args:
            bd_color (str, optional): Border color. Defaults to None.
        """
        self.style.configure(f"MyFrm{self.id}.TFrame", background=bd_color)

if __name__ == "__main__":
    root = Tk()
    for c in range(65, 93):
        btn = my_button(master=root, text="text", id=c, width=8)
        btn.grid(row=c%4-1 if c%4 != 0 else 3, column=(c-65)//4, padx=3, pady=3)
    root.mainloop()