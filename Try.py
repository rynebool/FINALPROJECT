while True:
    descision = input ("Do you want to order? (Y/N) ")

    while descision not in ("Y", "N"):
        descision = input("Do you want to order? (Y/N) ")
    if descision == "Y":
        print ("What is your name?")
        break
    elif descision == "N":
        print ("Next Customer Please!")
        