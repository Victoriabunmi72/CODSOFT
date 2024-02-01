/To-Do-List$ cat main.py
import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,True)

task_list= []

#icon
image_icon=PhotoImage(file="Image/task.png")
root.iconphoto(False,image_icon)

#top bar
TobImage=PhotoImage(file="Image/topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="Image/doc.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)
