import tkinter as tk
from tkinter import ttk
win = tk.Tk()

#Label
alabel=ttk.Label(win, text='Enter a name:').grid(column=0, row=0)

#Button Function
def clickMe():
    action.configure(text='Hello '+ name.get()+' '+numberChosen.get()) #internal lookup
    action.grid(column=2, row=1)
    print (name.get()+' '+numberChosen.get())

#Button
action=ttk.Button(win,text='Click Me!', command=clickMe) #event call
action.grid(column=2, row=1)

#Adding a textbox
name = tk.StringVar() #defining name
nameEntered = ttk.Entry(win, width=12, textvariable=name) #entry wiget/
nameEntered.grid(column=0,row=1)
nameEntered.focus()

#Combo Box
ttk.Label(win, text='Choose a number:').grid(column=1,row=0)
number=tk.StringVar()
numberChosen=ttk.Combobox(win,width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1,2,4,31,42,100)
numberChosen.grid(column=1,row=1)
numberChosen.current=(0)

#Check Buttons
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win, text='Disabled',variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0,row=2, sticky=tk.W) #alignment=west or alignment=left

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win, text='UnChecked',variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=2, sticky=tk.W)

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win, text='Enabled',variable=chVarEn)
check3.select()
check3.grid(column=2,row=2, sticky=tk.W)

#Radio Buttons
#Radio Button Globals
COLOR1='Blue'
COLOR2='Gold'
COLOR3='Red'

#Radio Callback
def radCall():
    radSel=radVar.get()
    if   radSel==1: win.configure(background=COLOR1)
    elif radSel==2: win.configure(background=COLOR2)
    elif radSel==3: win.configure(background=COLOR3)
#Radio Buttons
radVar=tk.IntVar
rad1=tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=4, sticky=tk.W)

rad2=tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=4, sticky=tk.W)

rad3=tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=4, sticky=tk.W)

win.mainloop() #starting the GUI