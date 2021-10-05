

from random import *
import tkinter as tk

username = ""
password = ""



def changeColor(screen,answer):
    screen.configure(bg = answer.get())

def main():
    def correct_login(U, P, Frame4):
        if U == username and P == password:
            print("welcome Back!")
            Frame1.pack_forget()
            Frame2.pack_forget()
            Frame3.pack_forget()
            Frame4.pack()
        else:
            print("incorrect username or password, please try again")


    screen = tk.Tk()
    screen.geometry("250x100")
    Frame1 = tk.Frame(screen)
    Frame2 = tk.Frame(screen)
    Frame3 = tk.Frame(screen)
    Frame4 = tk.Frame(screen)
    L1 = tk.Label(Frame1, text="Username:", width=10, anchor="e")
    L1.pack(side=tk.LEFT)

    Entry1 = tk.Entry(Frame1)
    Entry1.pack()

    L2 = tk.Label(Frame2, text="Password:", width=10, anchor="e")
    L2.pack(side=tk.LEFT)

    Entry2 = tk.Entry(Frame2, show = "*")
    Entry2.pack()

    options = ["red", "orange", "yellow", "green", "blue", "purple", "indigo", "violet", "aqua", "cyan", "pink",
               "lime", "maroon", "navy", "gold", "coral", "beige", "black", "grey", "white", "brown", "teal",
               "silver", "salmon", "papaya whip"]

    answer = tk.StringVar()
    answer.set("what is your favourite colour?")
    L3 = tk.OptionMenu(Frame4, answer, *options, command = lambda _: changeColor(screen, answer))
    L3.pack()

    Button1 = tk.Button(Frame3, text="Submit", command = lambda:correct_login(Entry1.get(), Entry2.get(), Frame4))
    Button1.pack(pady=10)

    Frame1.pack()
    Frame2.pack()
    Frame3.pack()
    screen.mainloop()


if __name__ == "__main__":
    main()
