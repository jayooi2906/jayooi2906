

import tkinter as tk


def main():
     def which_function():



     screen = tk.Tk()
     screen.geometry("250x100")
     Frame1 = tk.Frame(screen)
     Frame2 = tk.Frame(screen)
     Frame3 = tk.Frame(screen)
     Frame4 = tk.Frame(screen)

     options = ["pythag_theorem", "dist_formula"]
     choice = tk.StringVar()
     choice.set("Which function are you going to use?")

     op_menu = tk.OptionMenu(Frame1, choice, *options,command = lambda:which_function(choice, Frame4))
     op_menu.pack

     Frame1.pack
     screen.mainloop()


if __name__ == "__main__":
     main()