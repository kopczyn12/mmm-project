import tkinter as tk
from tkinter import ttk

from numpy import mat
from interface import Interface
import math
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')

class App(tk.Tk):

    def __init__(self, model):

        super().__init__()
        self.title("Projekt MMM")
    
        self.interface = Interface(model,self)
        self.interface.pack()