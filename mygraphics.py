from Tkinter import * 

def oc():
    print "osw"
    v.set("asd")

root = Tk()
frame = Frame(root)
frame.pack()

mainframe = Frame(root)
mainframe.pack(side = LEFT)
l1 = Label(mainframe, text = "Enter Website :")
l1.pack(side = LEFT)

v = StringVar()
l2 = Label(mainframe, textvariable = v)
l2.pack(side = BOTTOM)

e1 = Entry(mainframe, bd = 5)
e1.pack(side = RIGHT)

sideframe = Frame(root)
sideframe.pack( side = RIGHT )

a = e1.get()

button1 = Button(sideframe, text = "Check",fg = "Green", bd = 4, activebackground = "Blue", activeforeground = "White", command = oc)
button1.pack()

root.mainloop()