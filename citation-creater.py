
def citationChooser():
    print("[1] Cite Book")
    print("[2] Cite Webpage")
    print("[3] Cite Scholary Journal Article")
    print("[4] Cite News Article")
    print("[0] Finished with citations")

citationChooser()
citationChoice = int(input("Which type of citation do you need today?"))

while citationChoice != 0:
    if citationChoice == 1:
        #book cite
    elif citationChoice == 2:
        #webpage cite
    elif citationChoice == 3:
        #Scholarly Journal Article cite
    elif citationChoice == 4:
        #News article cite
    else:
        print("invalid citation choosen.")
    
    citationChooser()
    citationChoice = int(input("Which type of citation do you need today?"))
print("thanks for choosing the citation creation today!")

