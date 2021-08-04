from tkinter import Tk
from tkinter.ttk import Button, Frame, Style

class my_button(Frame):
    def __init__(self, master=None, text="", command=None, id=0, underline=-1, width=10):
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
        # self.style.configure("MyBtn.TButton", background=bg_color, relief=relief)

    def grid(self, column=None, row=None, padx=0, pady=0):
        # super().grid()
        self.frm.grid(column=column, row=row)
        self.btn.grid(padx=padx, pady=pady)

    def config_frm(self, bd_color=None):
        self.style.configure(f"MyFrm{self.id}.TFrame", background=bd_color)

if __name__ == "__main__":
    root = Tk()
    for c in range(65, 93):
        btn = my_button(master=root, text="text", id=c, width=8)
        btn.grid(row=c%4-1 if c%4 != 0 else 3, column=(c-65)//4, padx=3, pady=3)
    root.mainloop()