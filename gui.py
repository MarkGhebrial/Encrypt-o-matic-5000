from tkinter import *
from tkinter import ttk
from encryptomatic import EncryptOMatic
from alphabet import tebahpla
from random import randint

class GUI:
    def __init__ (self, root):
        def encrypt(*args):
            encrypted.set(EncryptOMatic(key=key.get()).encryptString(toEncrypt.get()))
            toDecrypt.set(encrypted.get())

        def decrypt(*args):
            decrypted.set(EncryptOMatic(key=key.get()).decryptString(toDecrypt.get()))

        def generateRandomKey(*args):
            temp = ""
            for i in range(randint(10, 15)):
                temp += tebahpla[randint(0, len(tebahpla) - 1)]
            key.set(temp)

        ###########################################################################
        keyFrame = ttk.Frame(root, padding="3 3 12 12")
        keyFrame.grid(column=0, row=0)

        ttk.Label(keyFrame, text="Key:").grid(column=0, row=0, sticky=(E))

        key = StringVar()
        key.set("1qwsdxcvgy789io")
        keyBox = ttk.Entry(keyFrame, width=20, textvariable=key)
        keyBox.grid(column=1, row=0)
        keyBox.grid_configure(padx=5, pady=5)

        ttk.Button(keyFrame, text="Generate random key", command=generateRandomKey).grid(column=2, row=0)

        ###########################################################################
        encryptFrame = ttk.Frame(root, padding="3 3 12 12")
        encryptFrame.grid(column=0, row=1, sticky=(N, W, E, S))

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
        decryptFrame.grid(column=0, row=2, sticky=(N, W, E, S))

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

        # Add padding
        for child in encryptFrame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        for child in decryptFrame.winfo_children():
            child.grid_configure(padx=5, pady=5)