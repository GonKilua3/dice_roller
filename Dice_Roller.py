#Note: To Use The Dice Roller, Type "pip install tkinter" In Command Prompt. Thank You For Reading
from tkinter import *
import random
window = Tk()
window.title("Dice Roller")
window.configure(bg="White")
canvas = Canvas(window, width=1800, height=960)
canvas.place(x=0, y=0)
numbers = []
def pickAmount(number):
    global numbers
    for HiThere in range(number):
        numbers.append(random.randint(1, 6))
    choice1.destroy()
    choice2.destroy()
    choice3.destroy()
    choice4.destroy()
    choice5.destroy()
    choice6.destroy()
def doTimer(time):
    if time >= 1:
        topText.config(text="Rolling Dice... {}".format(time))
        window.after(1000, doTimer, time-1)
    else:
        topText.config(text="Done!")
topText = Label(window, text="How Many Die Do You Want To Roll", font="Skia, 35", bg="White", fg="Black")
topText.pack()
choice1 = Button(window, text="1 Die", font="Skia, 30", bg="White", fg="Black", command=lambda: pickAmount(1))
choice2 = Button(window, text="2 Dice", font="Skia, 30", bg="White", fg="Black", command=lambda: pickAmount(2))
choice3 = Button(window, text="3 Dice", font="Skia, 30", bg="White", fg="Black", command=lambda: pickAmount(3))
choice4 = Button(window, text="4 Dice", font="Skia, 30", bg="White", fg="Black", command=lambda: pickAmount(4))
choice5 = Button(window, text="5 Dice", font="Skia, 30", bg="White", fg="Black", command=lambda: pickAmount(5))
choice6 = Button(window, text="6 Dice", font="Skia, 30", bg="White", fg="Black", command=lambda: pickAmount(6))
choice1.pack()
choice2.pack()
choice3.pack()
choice4.pack()
choice5.pack()
choice6.pack()
choice1.lift()
choice2.lift()
choice3.lift()
choice4.lift()
choice5.lift()
choice6.lift()
def wait():
    while choice5.winfo_exists():
        window.update()
wait()
def makeDice(x, y, number):
    canvas.create_rectangle(x, y, x + 80, y + 80, fill="White")
    if number == 1:
        canvas.create_oval(x + 30, y + 30, x + 50, y + 50, fill="Black")
    elif number == 2:
        canvas.create_oval(x + 5, y + 5, x + 25, y + 25, fill="Black")
        canvas.create_oval(x + 55, y + 55, x + 75, y + 75, fill="Black")
    elif number == 3:
        canvas.create_oval(x + 5, y + 55, x + 25, y + 75, fill="Black")
        canvas.create_oval(x + 30, y + 30, x + 50, y + 50, fill="Black")
        canvas.create_oval(x + 55, y + 5, x + 75, y + 25, fill="Black")
    elif number == 4:
        canvas.create_oval(x + 5, y + 5, x + 25, y + 25, fill="Black")
        canvas.create_oval(x + 55, y + 5, x + 75, y + 25, fill="Black")
        canvas.create_oval(x + 5, y + 55, x + 25, y + 75, fill="Black")
        canvas.create_oval(x + 55, y + 55, x + 75, y + 75, fill="Black")
    elif number == 5:
        canvas.create_oval(x + 5, y + 5, x + 25, y + 25, fill="Black")
        canvas.create_oval(x + 55, y + 5, x + 75, y + 25, fill="Black")
        canvas.create_oval(x + 30, y + 30, x + 50, y + 50, fill="Black")
        canvas.create_oval(x + 5, y + 55, x + 25, y + 75, fill="Black")
        canvas.create_oval(x + 55, y + 55, x + 75, y + 75, fill="Black")
    elif number == 6:
        canvas.create_oval(x + 5, y + 5, x + 25, y + 25, fill="Black")
        canvas.create_oval(x + 55, y + 5, x + 75, y + 25, fill="Black")
        canvas.create_oval(x + 5, y + 30, x + 25, y + 50, fill="Black")
        canvas.create_oval(x + 55, y + 30, x + 75, y + 50, fill="Black")
        canvas.create_oval(x + 5, y + 55, x + 25, y + 75, fill="Black")
        canvas.create_oval(x + 55, y + 55, x + 75, y + 75, fill="Black")
y = 135
doTimer(4)
def wait():
    while topText.cget("text") != "Done!":
        window.update()
wait()
topText.config(text="Here Are Your Dice:")
for HiAgain in range(len(numbers)):
    makeDice(639, y, numbers[HiAgain])
    y += 100
window.mainloop()