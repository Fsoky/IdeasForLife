from tkinter import *
from pyfirmata import Arduino

window = Tk()
window.geometry("100x100")

board = Arduino("COM6")


def light_on():
	board.digital[13].write(1)


def light_off():
	board.digital[13].write(0)

Button(text="Включить", command=light_on).pack()
Button(text="Выключить", command=light_off).pack()

window.mainloop()