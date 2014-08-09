import os, sys, marshal, pickle, difflib, pprint, tkinter
from tkinter import *
from tkinter import messagebox
from time import gmtime, strftime
def createSnapshot():
    def getDirFil():
        directory = E1.get()
        filename = E2.get()  
        cumulative_directories = []
        cumulative_files = []
        for root, dires, files in os.walk(directory):
            cumulative_directories += dires
            cumulative_files += files
        try:      
           output = open(filename, 'wb')
           pickle.dump(cumulative_directories, output, -1)
           pickle.dump(cumulative_files, output, -1)
           output.close()         
        except:           
            messagebox.showinfo("Erorr", "Problemy przy zapisie")
        top.destroy()
        return 

    top = Tk()
    top.minsize(230,50), top.title("Utworz migawke")
    B1 = Button(top, text="OK", width=20,command=getDirFil).pack(side= BOTTOM)
    L1 = Label(top, text="podaj sciezke:").pack(side= TOP)
    E1 = Entry(top, bd =5)
    E1.insert(10, "C:\\snap")
    E1.pack(side= TOP)
    L2 = Label(top, text="podaj nazwe pliku:").pack(side= TOP)
    E2 = Entry(top, bd =5, )
    E2.insert(10, "snap"+strftime("%Y-%m-%d_%H_%M", gmtime())+".snp")
    E2.pack(side=TOP, expand=YES)
    top.mainloop()

def listSnapshots():
    def getExtension():
        extension = E1.get()
        snaplist = []
        filelist = os.listdir(os.curdir)
        for item in filelist:
           if item.endswith(extension)==True:
               snaplist.append(item)
        L2.config(text='Lista migawek:\n'+str(snaplist))

    top = Tk()
    top.minsize(230,50), top.title("Pokaz migawke")
    B1 = Button(top, text="OK",width=20 ,command=getExtension)
    B2 = Button(top, text="CANCEL",width=20 ,command=top.destroy)
    L1 = Label(top, text="Podaj rozszerzenie:")
    L2 = Label(top, text="Lista migawek:\n")
    E1 = Entry(top, bd =5)
    E1.insert(10, "snp")
    L1.grid(row=0)
    E1.grid(row=1)
    B1.grid(row=3)
    L2.grid(row=0, column=1)
    B2.grid(row=3, column=1)
    
def compareSnapshot():
    def compareSnap():
        snapfile1 = E1.get()
        snapfile2 = E2.get()
        try:
           pk1_file = open(snapfile1, 'rb')
           dirs1 = pickle.load(pk1_file)
           files1 = pickle.load(pk1_file)
           pk1_file.close()

           pk2_file = open(snapfile2, 'rb')
           dirs2 = pickle.load(pk2_file)
           files2 = pickle.load(pk2_file)
           pk2_file.close()
        except:                 
           messagebox.showinfo("Erorr", "Wystapily problemy przy odczycie plikow migawek")
           top.destroy()
           return

        result_dirs = list(difflib.unified_diff(dirs1, dirs2))
        result_files = list(difflib.unified_diff(files1, files2))

        added_dirs = []
        removed_dirs = []
        added_files = []
        removed_files = []
    
        for result in result_files:
            if result.endswith("\n")==False:
                if result.startswith('+'):
                    resultadd = result.strip('+')
                    added_files.append(resultadd)
                elif result.startswith('-'):
                   resultsubtract = result.strip('-')
                   removed_files.append(resultsubtract)

        for result in result_dirs:
            if result.endswith("\n")==False:
                if result.startswith('+'):
                    resultadd = result.strip('+')
                    added_dirs.append(resultadd)
                elif result.startswith('-'):
                    resultsubtract = result.strip('-')
                    removed_dirs.append(resultsubtract)

        AD.config(fg="Green",text="Added Directories: "+str(added_dirs))
        AF.config(fg="Green", text="Added Files: "+str(added_files))
        RD.config(fg="Red",text="Removed Directories: "+str(removed_dirs))
        RF.config(fg="Red",text="Removed Files: "+str(removed_files))

        #top.destroy()
        
    top = Tk()
    results=StringVar()
    top.minsize(230,50), top.title("Porownaj migawki")
    B1 = Button(top, text="OK", width=20,command=compareSnap)
    B2 = Button(top, text="CANCEL", width=20,command=top.destroy)
    L1 = Label(top, text="pierwsza migawka:")
    E1 = Entry(top, bd =5)
    E1.insert(10, "snap"+strftime("%Y-%m-%d_%H_%M", gmtime())+".snp")
    L2 = Label(top, text="druga migawka:")
    E2 = Entry(top, bd =5, )
    E2.insert(10, "snap"+strftime("%Y-%m-%d_%H_%M", gmtime())+".snp")
    
    AD = Label(top)
    AF = Label(top)
    RD = Label(top)
    RF = Label(top)
    AD.grid(row=0, column=1)
    AF.grid(row=1, column=1)
    RD.grid(row=2, column=1)
    RF.grid(row=3, column=1)
    L1.grid(row=0)
    E1.grid(row=1)
    L2.grid(row=2)
    E2.grid(row=3)
    B1.grid(row=4)
    B2.grid(row=4, column=1)
    top.mainloop()    
