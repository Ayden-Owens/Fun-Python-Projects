from operator import truediv


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def word(string):
    retry = True
    while (retry):
        print(string)
        a = input()
        if(a.isnumeric()):
            print("Please do not enter a number!")
            retry = True
        else:
            retry = False
    return a

opening = "This is a Mad Lib Generator!"   
new_opening = opening.center(45, '^') 
Title = colored(255, 0, 0, new_opening)  
print(Title)

#Stores users inputs
noun1 = word("Please enter a noun")
pnoun1 = word("Please enter a noun(plural)")
noun2 = word("Please enter a noun")
pnoun2 = word("Please enter a noun(plural)")
noun3 = word("Please enter a place")
adj = word("Please enter a adjective")
noun4 = word("Please enter a noun")

#colouring words
c_noun1 = colored(0, 255, 0, noun1)
c_pnoun1 = colored(0, 255, 0, pnoun1)
c_noun2 = colored(0, 255, 0, noun2)
c_pnoun2 = colored(0, 255, 0, pnoun2)
c_noun3 = colored(0, 255, 0, noun3)
c_adj = colored(0, 255, 0, adj)
c_noun4 = colored(0, 255, 0, noun4)

# #sentences with the string variables
part1 = "Be kind to your " + c_noun1 + "-footed" + c_pnoun1
part2 = "For a duck my be somebody's " + c_noun2 + ","
part3 = "Be kind to your " + c_pnoun2 + "in " + c_noun3
part4 = "Where the weather is always " + c_adj
part5 = "You may think that this is the " + c_noun4
part6 = "Well it is."

#print sentences
print(part1.lower())
print(part2.lower())
print(part3.lower())
print(part4.lower())
print(part5.lower())
print(part6.lower())

