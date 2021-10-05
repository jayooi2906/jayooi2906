

from random import *
import tkinter as tk
def main():
    def temp(C, F):
        C = C.rstrip(" ")
        F = F.rstrip(" ")
        if C.isdigit() and not F.isdigit():
            F = ""
            C = int(C)
        elif not C.isdigit() and F.isdigit():
            C = ""
            F = int(F)
        if C != "" and F == "":
            F = C*9/5 + 32
            print(f"{C} celsius ,{F} fahrenheit")
        elif F != "" and C == "":
            C = (F-32)*5/9
            print(f"{C} celsius ,{F} fahrenheit")
        else:
            print("error! Please input either Celsuis or Fahrenheit")

    screen = tk.Tk()
    screen.geometry("250x100")
    Frame1 = tk.Frame(screen)
    Frame2 = tk.Frame(screen)
    Frame3 = tk.Frame(screen)

    L1 = tk.Label(Frame1, text = "Celsius:", width = 9, anchor = "e")
    L1.pack(side = tk.LEFT)

    Entry1 = tk.Entry(Frame1)
    Entry1.pack()

    L2 = tk.Label(Frame2, text="Fahrenheit:", width = 9, anchor = "e")
    L2.pack(side=tk.LEFT)

    Entry2 = tk.Entry(Frame2)
    Entry2.pack()

    Button1 = tk.Button(Frame3, text = "Submit", command = lambda:temp(Entry1.get(), Entry2.get()))
    Button1.pack(pady = 10)

    Frame1.pack()
    Frame2.pack()
    Frame3.pack()
    screen.mainloop()
if __name__ == "__main__":
    main()
