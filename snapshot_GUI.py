# SNAPSHOT.PY
# PROGRAM DO WYKONYWANIE MIGAWEK KATALOGOW I PLIKOW
# KRZYSZTOF GARBALA

import os, sys , tkinter
from tkinter import *
from tkinter import messagebox
import snapshothelper_GUI

def helpHelp():
    help = ''' 
snapshot_GUI.py
PROGRAM DO WYKONYWANIE MIGAWEK KATALOGOW I PLIKOW
POWSTAL NA PODSTAWIE PROJEKTU JAMES'A O. KNOWLTON'A
W KSIĄŻCE "PYTHON PROJEKTY DO WYKORZYSTANIA".
Python: 3.4.1
Platoforma: Windows
KRZYSZTOF GARBALA'''
    messagebox.showinfo("Help", help)
    
discription = '''
============================================
       NARZEDZIE DO POROWNYWANIA PLIKOW I KATALOGOW
============================================
                                         WYBIERZ OPCJE:

	'''  
frame = tkinter.Tk()
frame.minsize(300,200), frame.title("Snapshot")
menu = Label(frame, text=discription, justify=LEFT)
create_snapshot = Button(frame, text ="Utworz migawke",width=20,command=snapshothelper_GUI.createSnapshot)
show_snapshots = Button(frame, text="Pokaz migawki",width=20 ,command=snapshothelper_GUI.listSnapshots)
compare_snapshots = Button(frame, text="Porownaj migawki",width=20 ,command=snapshothelper_GUI.compareSnapshot)
help = Button(frame, text='Pomoc', width=20, command=helpHelp)
quit = Button(frame, text="Zakoncz", width=20,command=frame.destroy)

menu.pack()
create_snapshot.pack()
show_snapshots.pack()
compare_snapshots.pack()
help.pack()
quit.pack()
frame.mainloop()
