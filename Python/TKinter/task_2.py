from tkinter import *

root = Tk()

but = Button (root,
			text = "Нажми!",
			width = 10, height = 3,
			bg = "white", fg = "red") 
but.pack()

lab = Label(root, text = "Здесь может быть \n Ваша реклама!", font = "Arial 18")
lab.pack()

ent = Entry(root, width = 20, bd = 3)
ent.pack()

tex = Text(root,width = 40,
			font = "Verdana 12",
			wrap = WORD)
tex.pack()
root.mainloop()