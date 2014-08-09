import os, sys, marshal, pickle, difflib, pprint
def createSnapshot(directory="C:\snap", filename="snapshot.txt"):
    print(directory, filename)
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
       print("udalo sie")
    except:
        print("Problemy przy zapisie")
    input("Nacisniej [Enter]..")
    return

def listSnapshots(extension):
    snaplist = []
    filelist = os.listdir(os.curdir)
    for item in filelist:
        if item.endswith(extension)==True:
            snaplist.append(item)
    print (''' LISTA MIGAWEK
           ================''')
    print(snaplist)
    print (True==1)
    input("Nacisnij [Enter]..")
def compareSnapshot(snapfile1, snapfile2):
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
        print("Wystapily problemy przy odczycie plikow migawek")
        input("Nacisnij [Enter]..")
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

    print ("\n\nAdded Directories:\n")
    print (added_dirs)
    print ("\n\nAdded Files:\n")
    print (added_files)
    print("\n\nRemoved Directories:\n")
    print (removed_dirs)
    print ("\n\nRemoved Files:\n")
    print (removed_files)
    input("\n\nNacinij [Enter]..")
    
def showHelp():
    print('''snapshot.py
PROGRAM DO WYKONYWANIE MIGAWEK KATALOGOW I PLIKOW
POWSTAL NA PODSTAWIE PROJEKTU JAMES'A O. KNOWLTON'A
W KSIĄŻCE "PYTHON PROJEKTY DO WYKORZYSTANIA".
Python: 3.4.1
Platoforma: Windows
KRZYSZTOF GARBALA
    ''')
        
def invalidChoice():
    sys.stderr.write("Nieprawidlowa opcja sprobuj ponowanie\n")
    input("Nacisnij [Enter..]")