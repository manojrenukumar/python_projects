import sqlite3, hashlib
from tkinter import * 

window = Tk()

window.title("Password Vault")

def firstscreen():
    window.geometry("350x150")
    
    lbl = Label(window, text = "Create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()
    
    txt = Entry(window, width=20 , show='*')
    txt.pack()
    txt.focus()
    
    lbl1 = Label(window, text="Re-enter Password")
    lbl1.pack()
    txt1 = Entry(window, width=20 , show='*')
    txt1.pack()
    txt1.focus()
    
    lbl2 = Label(window)
    lbl2.pack()
    
    def SavePassword():
        if txt.get() == txt1.get():
            pass
        else:
            lbl2.config(text = "Password fo not match")
    
    btn = Button(window, text="Save", command=SavePassword)
    btn.pack(pady=10)

def loginScreen():
    window.geometry("350x150")
    
    lbl = Label(window, text = "Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()
    
    txt = Entry(window, width=20 , show='*')
    txt.pack()
    lbl1 = Label(window)
    lbl1.pack()
    
    def checkPassword():
        password = 'test'
        if password == txt.get():
            PasswordVault()
        else:
            txt.delete(0, 'end')
            lbl1.config(text="Wrong Password")
            
    btn = Button(window, text="submit", command= checkPassword)
    btn.pack()
    
    def PasswordVault():
        for widget in window.winfo_children():
            widget.destroy()
        window.geometry("780x350")
        
        lbl = Label(window, text = "Password Vault")
        lbl.config(anchor='center')
        lbl.pack()
        
firstscreen()  
window.mainloop()
