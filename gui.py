from tkinter import *
from tkinter import ttk
from encryptomatic import EncryptOMatic

def encrypt(*args):
    encrypted.set(EncryptOMatic(key="MarkGhebrial").encryptString(toEncrypt.get()))
    toDecrypt.set(encrypted.get())

def decrypt(*args):
    decrypted.set(EncryptOMatic(key="MarkGhebrial").decryptString(toDecrypt.get()))

root = Tk()
root.title("Encypt-o-Matic 5000")

encryptFrame = ttk.Frame(root, padding="3 3 12 12")
encryptFrame.grid(column=0, row=0, sticky=(N, W, E, S))

# Variables
toEncrypt = StringVar()
encrypted = StringVar()

# Row 0
ttk.Label(encryptFrame, text="Text to encrypt:").grid(column=0, row=0, sticky=(E))
ttk.Entry(encryptFrame, width=50, textvariable=toEncrypt).grid(column=1, row=0, sticky=(W))

# Row 1
ttk.Label(encryptFrame, text="Result:").grid(column=0, row=1, sticky=(E))
ttk.Label(encryptFrame, textvariable=encrypted).grid(column=1, row=1, sticky=(W))

# Row 3
ttk.Button(encryptFrame, text="Encrypt", command=encrypt).grid(column=0, row=2)

###########################################################################
decryptFrame = ttk.Frame(root, padding="3 3 12 12")
decryptFrame.grid(column=0, row=1, sticky=(N, W, E, S))

# Variables
toDecrypt = StringVar()
decrypted = StringVar()

# Row 0
ttk.Label(decryptFrame, text="Text to decrypt:").grid(column=0, row=0, sticky=(E))
ttk.Entry(decryptFrame, width=50, textvariable=toDecrypt).grid(column=1, row=0, sticky=(W))

# Row 1
ttk.Label(decryptFrame, text="Result:").grid(column=0, row=1, sticky=(E))
ttk.Label(decryptFrame, textvariable=decrypted).grid(column=1, row=1, sticky=(W))

# Row 3
ttk.Button(decryptFrame, text="Decrypt", command=decrypt).grid(column=0, row=2)

'''root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate").grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)'''

for child in encryptFrame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

for child in decryptFrame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()