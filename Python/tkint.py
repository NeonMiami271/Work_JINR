from tkinter import *


class But_print:
	def __init__(self):
		self.but = Button(root)
		self.but["text"] = "Нажми на меня!"
		self.but.bind("Button", self.printer)
		self.but.pack()
	def printer (self,event):
		print("Ты говоришь миру привет, но он не отвечает в ответ")

root = Tk()
object_1 = But_print()
root.mainloop()




