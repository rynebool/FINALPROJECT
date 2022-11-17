descision = " "
descision2 = " "


while (descision != 'Y'):
    print ("Do you want to order? (Y/N)") 
    descision = input()
    
    while (descision2 != 'N'):
        print ("Do you want to order? (Y/N)")
        descision2 = input()
    else:
        print("Next Customer Please!")
        print ("Do you want to order? (Y/N)")
        descision = input()
else:
    print ("What is your name?")
    descision = input()


    
