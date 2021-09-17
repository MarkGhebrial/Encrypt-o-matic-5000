from encryptomatic import EncryptOMatic

e1 = EncryptOMatic(key='212fdjkslkjhuioiwen5432fdsa3456789')
s = e1.encryptString("Most binary Wine packages will associate Wine with .exe files for you. If that is the case, you should be able to simply double-click on the .exe file in your file manager, just like in Windows. You can also right-click on the file, choose \"Run with\", and choose \"Wine\". This may sometimes open the file in the wrong program - if this happens, check the filetype associations for the file using whatever tool your desktop environment provides and edit as needed. Note that if you have built Wine from source you will have to create the filetype association yourself.")
print(e1.decryptString(s))