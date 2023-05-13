import time








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
        print("m aded")

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
            print("m remove")
        except:
            print("There is no 'm'")


    elif word == "add adres$":
        ms.append("adres$")
        mh = True
        print("adres$ aded")

    elif word == "adres$":
        print(ms[0])
    
    elif word == "write adres$" and mh == True:
      print ("the code adres#$")



    elif word == "adres#$":
       print("hi, i live in #sr#e#")
    
   
    elif word == "remove adres$":
        try:
            ms.remove("adres$")
            mh = False
            print("adres$ remove")
        except:
            print("There is no 'adres$'")

    elif word == "exit":
        break
