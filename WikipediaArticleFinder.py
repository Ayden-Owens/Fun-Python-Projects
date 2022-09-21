import wikipedia
import requests
import webbrowser
from tkinter import*
from bs4 import BeautifulSoup


gui = Tk()
gui.geometry("300x150")
gui.title("Wiki Article Finder!")

def search():
    question=qTextbox.get()
    answer=wikipedia.summary(question)
    print(answer)
    
def randomize():
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    

question = StringVar()
question.set(" ")
qTextbox = Entry(gui, width=36, font=("Times New Roman", 12, ""), textvariable=question)
qTextbox.grid(row=1,column=1)

qButton = Button(gui,text='Search For Article', bd=10, command=search)
qButton.grid(row=3,column=1)
    
gui.mainloop()

