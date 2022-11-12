import tkinter as tk

# def Select():
from tkinter import RIDGE, messagebox, DISABLED
global oddTurn


def main():
    global oddTurn
    oddTurn = True

    def checkwinner(a, b, c):
        if buttons[a]["text"] == "X" and buttons[b]["text"] == "X" and buttons[c]["text"] == "X":
            buttons[a].config(bg="red")
            buttons[b].config(bg="red")
            buttons[c].config(bg="red")
            messagebox.showinfo("result", "X won the game")
            disableAllButtons()
        elif buttons[a]["text"] == "O" and buttons[b]["text"] == "O" and buttons[c]["text"] == "O":
            buttons[a].config(bg="red")
            buttons[b].config(bg="red")
            buttons[c].config(bg="red")
            messagebox.showinfo("result", "O won the game")
            disableAllButtons()
        else:
            pass

    def disableAllButtons():
        for i in range(len(buttons)):
            buttons[i].config(state=DISABLED)

    def click(button):
        global oddTurn

        if button["text"] == "" and oddTurn:
            button["text"] = "X"
            oddTurn = False
            checkwinner(0, 1, 2)
            checkwinner(3, 4, 5)
            checkwinner(6, 7, 8)
            checkwinner(0, 3, 6)
            checkwinner(1, 4, 7)
            checkwinner(2, 5, 8)
            checkwinner(0, 4, 8)
            checkwinner(2, 4, 6)
        elif button["text"] == "" and oddTurn is False:
            button["text"] = "O"
            oddTurn = True
            checkwinner(0, 1, 2)
            checkwinner(3, 4, 5)
            checkwinner(6, 7, 8)
            checkwinner(0, 3, 6)
            checkwinner(1, 4, 7)
            checkwinner(2, 5, 8)
            checkwinner(0, 4, 8)
            checkwinner(2, 4, 6)
        else:
            pass

    window = tk.Tk()
    window.title("Tic tac toe")
    window_width = 1070
    window_height = 750
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    window.geometry(str(window_width) + "x" + str(window_height) + "+" + str(center_x) + "+" + str(center_y))

    button1 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button1))
    button2 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button2))
    button3 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button3))
    button4 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button4))
    button5 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button5))
    button6 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button6))
    button7 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button7))
    button8 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button8))
    button9 = tk.Button(window, text="", relief=RIDGE, width=19, height=9, command=lambda: click(button9))

    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

    buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]
    window.mainloop()


if __name__ == '__main__':
    main()
