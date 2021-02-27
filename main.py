from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
from tkinter import ttk
import sys

def read_data(file_to_read,pos,grab):
    with open(file_to_read,"rb") as opened_file:
        opened_file.seek(pos,0)
        grabed_data=opened_file.read(grab)
    return grabed_data

def make_backup(filebkp):
    with open(filebkp,"rb") as rf_exe:
        chunk_size=4096
        with open(Path(filebkp).stem+".bak","wb") as wf_exe:
            rf_exe_chunk = rf_exe.read(chunk_size)
            while len(rf_exe_chunk) >0:
                wf_exe.write(rf_exe_chunk)
                rf_exe_chunk = rf_exe.read(chunk_size)

def create_reg(game):
    if PC_serial.get()=='':
        code='NXUDPACVEM2XKPC96AYU'
    else:
        code=PC_serial.get()
    code=code.replace(" ", "").replace("-", "")
    if game=='KONAMIPES5' or game=='KONAMIWE9':
        with open("Installer run as administrator.bat", "w+") as myfile:
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V code /T REG_SZ /F /D \""+code+"\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V installdir /T REG_SZ /F /D \"%~dp0\\\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V installfrom /T REG_SZ /F /D %~d0\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_e /T REG_DWORD /F /D \"1\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_f /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_g /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_i /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_s /T REG_DWORD /F /D \"0\"\n")
            if game=='KONAMIWE9':
                myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V text_e /T REG_DWORD /F /D \"1\"\n")
                myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V text_s /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\\"+game+"\\"+ PC_valor4.get() + "\\1.0\" /F\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V code /T REG_SZ /F /D \""+code+"\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V installdir /T REG_SZ /F /D \"%~dp0\\\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V installfrom /T REG_SZ /F /D %~d0\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_e /T REG_DWORD /F /D \"1\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_f /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_g /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_i /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_s /T REG_DWORD /F /D \"0\"\n")
            if game=='KONAMIWE9':
                myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V text_e /T REG_DWORD /F /D \"1\"\n")
                myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V text_s /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\\1.0\" /F\n")
        with open("uninstaller run as administrator.bat", "w+") as myfile:
            myfile.write("reg delete \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /F\n")
            myfile.write("reg delete \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /F\n")
        with open("serial.txt", "w+") as myfile:
            myfile.write("The serial that you select for your game is " +code)
    if game=='KONAMI':
        with open("Installer run as administrator.bat", "w+") as myfile:
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V code /T REG_SZ /F /D \""+code+"\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V installdir /T REG_SZ /F /D \"%~dp0\\\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V installfrom /T REG_SZ /F /D %~d0\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V text_k /T REG_DWORD /F /D \"1\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_k /T REG_DWORD /F /D \"1\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /V login /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\\"+game+"\\"+ PC_valor4.get() + "\\1.0\" /F\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V code /T REG_SZ /F /D \""+code+"\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V installdir /T REG_SZ /F /D \"%~dp0\\\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V installfrom /T REG_SZ /F /D %~d0\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V text_k /T REG_DWORD /F /D \"1\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V lang_k /T REG_DWORD /F /D \"1\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /V login /T REG_DWORD /F /D \"0\"\n")
            myfile.write("reg add \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\\1.0\" /F\n")
        with open("uninstaller run as administrator.bat", "w+") as myfile:
            myfile.write("reg delete \"HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\\"+game+"\\"+ PC_valor4.get() + "\" /F\n")
            myfile.write("reg delete \"HKEY_LOCAL_MACHINE\SOFTWARE\\"+game+"\\"+ PC_valor4.get() + "\" /F\n")
        with open("serial.txt", "w+") as myfile:
            myfile.write("The serial that you select for your game is " +code)

def save_changes(game):
    if game=='KONAMIPES5':
        if len(PC_valor22.get())>22:
            messagebox.showerror(title=app_name,message="The name for option file folder\nexceeds the max allowed characters\n(MAX=22)")
        elif len(PC_valor4.get())>7:
            messagebox.showerror(title=app_name,message="The name for registry folder\nexceeds the max allowed characters\n(MAX=7)")
        else:
            if PC_backup_check:
                make_backup(PC_exe)
                make_backup(PC_settings)
            if PC_reg_check:
                create_reg(game)
            try:
                with open(PC_exe,"r+b") as opened_file:
                    #primero ponemos en cero el espacio para escribir
                    opened_file.seek(0x6CE4B8,0)
                    i=0
                    while i<22:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6CE4B8,0)
                    opened_file.write(PC_valor22.get().encode('utf-8'))

                    opened_file.seek(0x6CE7F0,0)
                    i=0
                    while i<7:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6CE7F0,0)
                    opened_file.write(PC_valor4.get().encode('utf-8'))
                #escribimos los valores en el settings
                with open(PC_settings,"r+b") as opened_file:
                    opened_file.seek(0x6BC70,0)
                    i=0
                    while i<22:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6BC70,0)
                    opened_file.write(PC_valor22.get().encode('utf-8'))

                    opened_file.seek(0x6BC58,0)
                    i=0
                    while i<7:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6BC58,0)
                    opened_file.write(PC_valor4.get().encode('utf-8'))
                update_entrybox()
                messagebox.showinfo(title=app_name,message="Changes saved succesfully!")
            except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
                messagebox.showerror(title=app_name, message="Error while trying to save please\nrun as administrator")

    if game=='KONAMIWE9':
        if len(PC_valor22.get())>16:
            messagebox.showerror(title=app_name,message="The name for option file folder\nexceeds the max allowed characters\n(MAX=16)")
        elif len(PC_valor4.get())>3:
            messagebox.showerror(title=app_name,message="The name for registry folder\nexceeds the max allowed characters\n(MAX=3)")
        else:
            if PC_backup_check:
                make_backup(PC_exe)
                make_backup(PC_settings)
            if PC_reg_check:
                create_reg(game)
            try:
                with open(PC_exe,"r+b") as opened_file:
                    #primero ponemos en cero el espacio para escribir
                    opened_file.seek(0x6CE4B8,0)
                    i=0
                    while i<16:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6CE4B8,0)
                    opened_file.write(PC_valor22.get().encode('utf-8'))

                    opened_file.seek(0x6CE7F0,0)
                    i=0
                    while i<3:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6CE7F0,0)
                    opened_file.write(PC_valor4.get().encode('utf-8'))
                #escribimos los valores en el settings
                with open(PC_settings,"r+b") as opened_file:
                    opened_file.seek(0x06BC64,0)
                    i=0
                    while i<16:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x06BC64,0)
                    opened_file.write(PC_valor22.get().encode('utf-8'))

                    opened_file.seek(0x6BC4F,0)
                    i=0
                    while i<3:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6BC4F,0)
                    opened_file.write(PC_valor4.get().encode('utf-8'))
                update_entrybox()
                messagebox.showinfo(title=app_name,message="Changes saved succesfully!")
            except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
                messagebox.showerror(title=app_name, message="Error while trying to save please\nrun as administrator")


    elif game=='KONAMI':
        if len(PC_valor22.get())>35:
            messagebox.showerror(title=app_name,message="The name for option file folder\nexceeds the max allowed characters\n(MAX=35)")
        elif len(PC_valor4.get())>6:
            messagebox.showerror(title=app_name,message="The name for registry folder\nexceeds the max allowed characters\n(MAX=6)")
        else:
            if PC_backup_check.get():
                make_backup(PC_exe)
                make_backup(PC_settings)
            if PC_reg_check.get():
                create_reg(game)
            try:
                with open(PC_exe,"r+b") as opened_file:
                    #primero ponemos en cero el espacio para escribir
                    opened_file.seek(0x6CCAB8,0)
                    i=0
                    while i<35:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6CCAB8,0)
                    opened_file.write(PC_valor22.get().encode('utf-8'))

                    opened_file.seek(0x6CCDFC,0)
                    i=0
                    while i<7:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x6CCDFC,0)
                    opened_file.write(PC_valor4.get().encode('utf-8'))
                #escribimos los valores en el settings
                with open(PC_settings,"r+b") as opened_file:
                    opened_file.seek(0x06BC78,0)
                    i=0
                    while i<35:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x06BC78,0)
                    opened_file.write(PC_valor22.get().encode('utf-8'))

                    opened_file.seek(0x06BC60,0)
                    i=0
                    while i<6:
                        opened_file.write(b'\x00')
                        i=i+1
                    opened_file.seek(0x06BC60,0)
                    opened_file.write(PC_valor4.get().encode('utf-8'))
                update_entrybox(game)
                messagebox.showinfo(title=app_name,message="Changes saved succesfully!")
            except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
                messagebox.showerror(title=app_name, message="Error while trying to save please\nrun as administrator")

def update_entrybox(game):
        if game=='KONAMIWE9':
            PC_valor22.delete(0, 'end')
            PC_valor4.delete(0, 'end')
            offolder=read_data(PC_exe,0x6CE4B8,22)
            regfolder=read_data(PC_exe,0x6CE7EF,0x7)
            PC_valor22.insert(0,offolder.decode('utf-8'))
            PC_valor4.insert(0,regfolder.decode('utf-8'))
        elif game=='KONAMIPES5':
            PC_valor22.delete(0, 'end')
            PC_valor4.delete(0, 'end')
            offolder=read_data(PC_exe,0x6CE4B8,22)
            regfolder=read_data(PC_exe,0x6CE7F0,0x7)
            PC_valor22.insert(0,offolder.decode('utf-8'))
            PC_valor4.insert(0,regfolder.decode('utf-8'))
        elif game=='KONAMI':
            PC_valor22.delete(0, 'end')
            PC_valor4.delete(0, 'end')
            offolder=read_data(PC_exe,0x6CCAB8,0x23)
            regfolder=read_data(PC_exe,0x6CCDFC,0x7)
            PC_valor22.insert(0,offolder.decode('utf-8'))
            PC_valor4.insert(0,regfolder.decode('utf-8'))

def search_file():
    global PC_label
    global PC_label2
    global PC_exe
    global PC_settings
    global gamever
    PC_label.destroy()
    PC_label2.destroy()
    PC_exe=filedialog.askopenfilename(initialdir=".",title="Select a file", filetypes=[("PES5 Executable", "pes5.exe"),("WE9 Executable", "we9.exe"),("WE9LE Executable", "we9le.exe"),("All files", "*.*")])
    gamever=read_data(PC_exe,0x6CE7E5,0x9).decode('utf-8')
    if gamever!='KONAMIWE9':
        gamever=read_data(PC_exe,0x6CE7E5,0xA).decode('utf-8')
        if gamever!='KONAMIPES5':
            gamever=read_data(PC_exe,0x6CCDF5,0x6).decode('utf-8')
    if gamever=='KONAMIWE9' or gamever=='KONAMIPES5':
        PC_settings=filedialog.askopenfilename(initialdir=".",title="Select a file", filetypes=[("Settings", "*.exe"),("All files", "*.*")])
        if PC_exe!='' or PC_settings!='':
            #print(Path(PC_exe).stat().st_size)
            PC_label=Label(root,text=PC_exe)
            PC_label2=Label(root,text=PC_settings)
            PC_label.place(x=1,y=260)
            PC_label2.place(x=1,y=280)
            update_entrybox(gamever)
        else: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=app_name, message="Please select a PES5/WE9/LE.exe")
    else:
        if PC_exe!='':
            PC_settings=filedialog.askopenfilename(initialdir=".",title="Select a file", filetypes=[("Settings", "*.exe"),("All files", "*.*")])
            #print(Path(PC_exe).stat().st_size)
            PC_label=Label(root,text=PC_exe)
            PC_label2=Label(root,text=PC_settings)
            PC_label.place(x=1,y=260)
            PC_label2.place(x=1,y=280)
            update_entrybox(gamever)
        else: # parent of IOError, OSError *and* WindowsError where available
            messagebox.showerror(title=app_name, message="Please select a PES5/WE9/LE.exe")

def close():
    root.destroy()
    sys.exit()

app_name="PES5/WE9/LE PC Standalone Patch"
root = Tk()
root.title(app_name)
w = 400 # width for the Tk root
h = 300 # height for the Tk root
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.wm_protocol("WM_DELETE_WINDOW", lambda: close())





PC_exe=r''
PC_settings=r''
gamever=""
my_btn=Button(root, text="Select PES5/WE9/LE.exe \nand settings.exe", command=lambda: search_file())
PC_backup_check=IntVar()
checkbox_backup=Checkbutton(root, text="Make backup\nof files",variable=PC_backup_check)
PC_reg_check=IntVar()
checkbox_reg=Checkbutton(root, text="Create registry files",variable=PC_reg_check)
PC_label=Label(root)
PC_label2=Label(root)
PC_valor22_lbl=Label(root,text="Option file folder")
PC_valor22=Entry(root,width=32)
PC_valor4_lbl=Label(root,text="Registry folder")
PC_valor4=Entry(root,width=32)
PC_serial_lbl=Label(root,text="Please input a serial\n(optional)")
PC_serial=Entry(root,width=32)
PC_save=Button(root, text="Save", command=lambda: save_changes(gamever))
PC_exit=Button(root, text="Exit", command=close)




my_btn.place(x=120,y=150)
checkbox_backup.place(x=280,y=150)
PC_valor22_lbl.place(x=10,y=20)
PC_valor22.place(x=140,y=20)
PC_valor4_lbl.place(x=10,y=40)
PC_valor4.place(x=140,y=40)
PC_serial_lbl.place(x=10,y=60)
PC_serial.place(x=140,y=60)
checkbox_reg.place(x=120,y=110)
PC_save.place(x=150,y=200)
PC_exit.place(x=190,y=200)



root.resizable(False, False)
root.mainloop()