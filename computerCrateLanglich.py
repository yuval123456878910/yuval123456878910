import time
import tkinter as tk







mh = False
ms = []
while(True):
    word = input("Enter a word: ")
    if word.startswith("write["):
        word = word[len("write["):]
        if word != "" :
            print(word)
        

    elif word == "y":
        print("@")
   

    elif word == "n":
        print("#")
    

    elif word == "הי":
        print("הרוק המ")
   
    elif word == "col":
        print("#")
        time.sleep(1)
        print("@") 
        time.sleep(1)
        print("#")
        time.sleep(1)
        print("@")
        time.sleep(1)
        print("#")

   
    elif word == "play":
        print("@")
        time.sleep(2)
        print("#")
        time.sleep(2)
        print("הרוק המ")
        time.sleep(1)
        print("#")
        time.sleep(1)
        print("@") 
        time.sleep(1)
        print("#")
        time.sleep(1)
        print("@")
        time.sleep(1)
        print("#")
        print("play en")

    elif word == "add m":
        ms.append("m")
        mh = True

    elif word == "m":
        print(ms[0])
    
    elif word == "write m" and mh == True:
        print("you found the sicret code")
        print("       '1002034'")
    
    
    
    elif word == "1002034":
       print("hi, i live in #sr#e#")
    
   
    elif word == "remove m":
        try:
            ms.remove("m")
            mh = False
        except:
            print("There is no 'm'")

    elif word == "exit":
        break
