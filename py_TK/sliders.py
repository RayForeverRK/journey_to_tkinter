from tkinter import*
from PIL import ImageTk,Image
ray = Tk()
ray.iconbitmap('icony1.ico')
root = LabelFrame(ray,text="frame size",padx=150,pady=180)
root.pack()
#-------------------------------------------
scrol_h = Scale(ray,from_=10,to=110,orient=HORIZONTAL)
scrol_h.pack(anchor=S)
scrol_v = Scale(ray,from_=10,to=110)
scrol_v.pack(anchor=S)
label1 = Label(ray,text="the current location of scale H="+str(scrol_h.get()))
label2 = Label(ray,text="the current location of scale V="+str(scrol_v.get()))
def scroll():
	global label1
	global label2
	label1.forget()
	label2.forget()
	label1 = Label(ray,text="the current location of scale H="+str(scrol_h.get()))
	label1.pack(anchor=N)
	label2 = Label(ray,text="the current location of scale V="+str(scrol_v.get()))
	label2.pack(anchor=N)
buten = Button(ray,text="checl!",font=15,command=scroll)
buten.pack()
mainloop()