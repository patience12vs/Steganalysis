import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
from moviepy.editor import *
import easygui
import Encoder as hidefile
import Decoder as unhide1
import analysis as stegoan


bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"
#vf, base_filename = get_video_filename_base()

def get_video_filename_base(path):
    """Returns filename and base filename"""
    vf = path
    return vf, os.path.splitext(os.path.basename(vf))[0]
def get_frames(video_object, base_filename):
    """Returns all frames in the video object"""
    directory = "output\\" + base_filename + '_frames\\'
    if not os.path.isdir(directory):
        os.makedirs(directory)
    for index, frame in enumerate(video_object.iter_frames()):
        img = Image.fromarray(frame, 'RGB')
        img.save(f'{directory}{index}.png')
        
def Home():
        global window
        def clear():
            print("Clear1")
            txt.delete(0, 'end')    
            txt1.delete(0, 'end')
            txt2.delete(0, 'end')    
            



        window = tk.Tk()
        window.title("Stego Analysis Using Deep Learning")

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="Stego Analysis Using Deep Learning" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=20)

        lbl = tk.Label(window, text="Select Video",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl.place(x=100, y=200)
        
        txt = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt.place(x=400, y=215)

        lbl1 = tk.Label(window, text="Select Frame Folder",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=100, y=270)
        
        txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=400, y=275)
        lbl2 = tk.Label(window, text="Select Secret File",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=100, y=340)
        
        txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt2.place(x=400, y=355)


        

        def browse():
                path=filedialog.askopenfilename()
                print(path)
                txt.delete(0, 'end')
                txt.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Video")     

        def browse1():
                path=filedialog.askopenfilename()
                print(path)
                txt2.delete(0, 'end')
                txt2.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Secret File")    

        def browse2():
                path=filedialog.askdirectory()
                print(path)
                txt1.delete(0, 'end')
                txt1.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Frame Folder")
        def getf():
                path=txt.get()
                if path!="":
                        vf, base_filename = get_video_filename_base(path)
                        video_object = VideoFileClip(vf)
                        get_frames(video_object, base_filename)
                        tm.showinfo("Output", "Frames Saved In output folder")
                else:
                        tm.showinfo("Input error", "Select Video")        

        
        def hide():
                frame_start=int(easygui.enterbox("Enter Starting Frame "))
                frame_end=int(easygui.enterbox("Ending Frame"))
                filename=txt2.get()
                frame_location=txt1.get()
                hidefile.encode(int(frame_start), int(frame_end), str(filename), str(frame_location))
                tm.showinfo("Output", "Data Hided into Frames")
        def unhide():
                frame_start=int(easygui.enterbox("Enter Satring Frame "))
                frame_end=int(easygui.enterbox("Ending Frame"))
                frame_location=txt1.get()
                unhide1.process(frame_start,frame_end,frame_location)
                tm.showinfo("Output", "Un Hiding Successfull")
        def stegoana():
                frame_location=txt1.get()
                num_frames=int(easygui.enterbox("Number of Frames to be analysis"))
                frames=stegoan.process(frame_location,num_frames)
                tm.showinfo("Output", "Analysis Done")
                tm.showinfo("Output", "Stegnography Detected in "+str(frames)+" frames")


        browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse.place(x=650, y=200)

        browse1bt = tk.Button(window, text="Browse", command=browse2  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse1bt.place(x=650, y=270)

        browse2 = tk.Button(window, text="Generate Frames", command=getf  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse2.place(x=10, y=500)

        browse3 = tk.Button(window, text="Browse", command=browse1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse3.place(x=650, y=345)

        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=950, y=200)
         
        proc = tk.Button(window, text="Hide Data", command=hide  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        proc.place(x=260, y=500)
        

        TRbutton = tk.Button(window, text="StegoAnalysis", command=stegoana  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        TRbutton.place(x=460, y=500)


        PRbutton = tk.Button(window, text="UnHide Data", command=unhide  ,fg=fgcolor   ,bg=bgcolor1 ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        PRbutton.place(x=660, y=500)

        


        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=860, y=500)

        window.mainloop()
Home()

