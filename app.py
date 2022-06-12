import tkinter as tk
from tkinter import ttk
from interface import Interface

#stworzenie okna
class App(tk.Tk):

    def __init__(self, model):

        super().__init__()
        self.title("Projekt MMM")
    
        self.interface = Interface(model,self)
        self.interface.pack()