from Tkinter import *

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)
left = Button(m1, text="left button")
right = Button(m1, text="right button")
m1.add(left)
m1.add(right)
# left = Label(m1, text="left pane")
# m1.add(left)
#
# m2 = PanedWindow(m1, orient=VERTICAL)
# m1.add(m2)
#
# top = Label(m2, text="top pane")
# m2.add(top)
#
# bottom = Label(m2, text="bottom pane")
# m2.add(bottom)

mainloop()