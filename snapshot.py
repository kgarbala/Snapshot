#SNAPSHOT.PY
#PROGRAM DO WYKONYWANIE MIGAWEK KATALOGOW I PLIKOW
# KRZYSZTOF GARBALA

import os, sys , tkinter
import snapshothelper
def temp():
	print ('')
def menu():
	
	print ('''
NARZEDZIE DO POROWNYWANIA PLIKOW I KATALOGOW
	============================================
	Wprowadz odpowidnia liczbe i nacisnij Enter
	1. Utworz migawke1
	2. Wypisz pliki migawek
	3. Porownaj migawki
	4. Pomoc
	5. Koniec
	''')
	choice=input("\t")
	
	return choice
frame = tkinter.Tk()
frame.minsize(300,300), frame.title("Snapshot")
create_snapshot=tkinter.Button(frame, text ="Utworz migawke",command=snapshothelper.createSnapshot)
show_snapshots=tkinter.Button(frame, text="Pokaz migawki", command=temp)
compare_snapshots=tkinter.Button(frame, text="Porownaj migawki", command=temp)


create_snapshot.pack()
show_snapshots.pack()
compare_snapshots.pack()
frame.mainloop()
choice=''

while choice!="5":
	
    choice=menu()
    os.system('cls')
    if choice=='1':
		
        print ('''UTWORZ MIGAWKE
        ========================''')
        
        snapshothelper.createSnapshot()
    elif choice=='2':
        os.system('cls')
        print('''
        WYPISZ PLIK MIGAWKI
        wpisz rozszerzenie migawek (np 'snp')''')
        extension=input('\t\t')
        snapshothelper.listSnapshots(extension)
    elif choice=='3':
        os.system('cls')
        print ('''
        POROWNAJ MIGAWKI
        ================''')
        snap1=input("Wproawdz migawke 1: ")		
        snap2=input("Wproawdz migawke 2: ")
        snapshothelper.compareSnapshot(snap1,snap2)
    elif choice=='4':
        os.system('cls')
        snapshothelper.showHelp()
        
    else:
        if choice !='5':
            snapshothelper.invalidChoice()