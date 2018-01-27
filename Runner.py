import Scrape
import Compare
from tkinter import *
from tkinter import ttk


def checkDomain():
    fo = open('title.txt')
    link = fo.readline().rstrip("\n")
    fo.close()
    return Compare.check(link)


def checkLinks():
    fo = open('links.txt')
    for line in fo:
        link = Scrape.getStrippedLink(line)
        if not Compare.check(link):
            return False
    return True


def result(link):
    link = str(link)
    Scrape.starter(link)
    global results
    if checkDomain():
        if checkLinks():
            results.set("This site is not a fake news site")
        else:
            results.set("This site has sources from a fake site")
    else:
        results.set("This site is a fake news site")


root = Tk()
root.title("FakeNews")
link = StringVar()
results = StringVar()
mainframe = ttk.Frame(root, padding="6 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Input").grid(column=0, row=2, sticky=W)
word_entry = ttk.Entry(mainframe, width=55, textvariable=link)
word_entry.grid(column=1, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Run", command=lambda: result(link.get())).grid(column=3, row=5, sticky=W)

ttk.Label(mainframe, text="Result :").grid(column=0, row=4, sticky=W)
ttk.Label(mainframe, textvariable=results).grid(column=1, row=4, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind('<Return>', lambda: result(link.get()))
root.mainloop()
