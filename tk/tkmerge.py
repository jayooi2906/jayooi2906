from recursion_merge_sort import recur_merge
import tkinter as tk


def main():


    def recur_merge_funct(list):
        list.get().split(",")
        int_list = []
        for i in list:
            int_list.append(int(i))
        recur_merge(int_list)
        print(int_list)




    screen = tk.Tk()
    screen.geometry("250x100")
    Frame1 = tk.Frame(screen)
    Frame2 = tk.Frame(screen)

    L1 = tk.Label(Frame1, text="imput list:", width=9, anchor="e")
    L1.pack(side=tk.LEFT)

    Entry1 = tk.Entry(Frame1)
    Entry1.pack()
    Entry1.delete(tk.END)

    Button1 = tk.Button(Frame2, text = "Submit", command = lambda:recur_merge_funct(Entry1))
    Button1.pack(pady = 10)


    Frame1.pack()
    Frame2.pack()
    screen.mainloop()


if __name__ == "__main__":
    main()