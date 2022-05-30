import tkinter as tk
from tkinter import BOTH, Canvas, ttk, Toplevel
import math
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')
from app import *


class Interface(tk.Frame):

    def __init__(self, model, master = None):

        super().__init__()

        self.model = model
        #pobudzenie
        self.radio_var = tk.StringVar()
        self.label_response = ttk.Label(self, text="Pobudzenie:", font=("Arial", 16))
        self.label_response.grid(row=1, column=0, columnspan=3)
        self.radio_sin = ttk.Radiobutton(self, text="Sinusoidalne", variable=self.radio_var, value="sinus")
        self.radio_rectangle = ttk.Radiobutton(self, text="Prostokątne", variable=self.radio_var, value="prostokat")
        self.radio_unit = ttk.Radiobutton(self, text="Jednostkowe", variable=self.radio_var, value="jednostkowe")
        self.radio_var.set("sin")
        self.radio_sin.grid(row=2, column=0)
        self.radio_rectangle.grid(row=2, column=1)
        self.radio_unit.grid(row=2, column=2, padx=15)

        #parametr k1
        self.label_k1 = ttk.Label(self, text="Podaj wartość k1", font=("Arial", 14))
        self.label_k1.grid(row=5, column=0, columnspan=1)
        self.k1_var = tk.StringVar()
        self.entry_first_k = tk.Entry(self, width=10, text=self.k1_var)
        self.entry_first_k.grid(row=5, column=1)
        self.k1_var.set("1")

        #parametr k2
        self.label_k2 = ttk.Label(self, text="Podaj wartość k2", font=("Arial",14))
        self.label_k2.grid(row=6, column=0, columnspan=1)
        self.k2_var = tk.StringVar()
        self.entry_second_k = tk.Entry(self, width=10, text=self.k2_var)
        self.entry_second_k.grid(row=6, column=1)
        self.k2_var.set("1")

        #parametr m
        self.label_m = ttk.Label(self, text="Podaj wartość m", font=("Arial",14))
        self.label_m.grid(row=7, column=0, columnspan=1)
        self.m_var = tk.StringVar()
        self.entry_m = tk.Entry(self, width=10, text=self.m_var)
        self.entry_m.grid(row=7, column=1)
        self.m_var.set("1")

        #parametr b
        self.label_b = ttk.Label(self, text="Podaj wartość b", font=("Arial",14))
        self.label_b.grid(row=8, column=0, columnspan=1)
        self.b_var = tk.StringVar()
        self.entry_b = tk.Entry(self, width=10, text=self.b_var)
        self.entry_b.grid(row=8, column=1)
        self.b_var.set("1")

        #wzor rownania
        self.button_show_equation = ttk.Button(self, text = "Pokaż schemat projektu", command=lambda: self.show_schema())
        self.button_show_equation.grid(row=10, column=1)

        #Start symulacji
        self.button_simulation = ttk.Button(self, text="Symulacja", command=lambda: self.simulation())
        self.button_simulation.grid(row=11, column=1)

        #wykres
        self.f = Figure(figsize=(10,8), dpi=100)
        self.a = self.f.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=11, column=3)
        self.canvas.get_tk_widget().grid(row=1, column=3, rowspan=10)

    def simulation(self):

        self.f.canvas.draw()

    def show_schema(self):

        self.schema_frame = Toplevel(self)
        self.schema_frame.title("Schemat projektu")
        self.canvas = Canvas(self.schema_frame, width=348, height=161)
        self.canvas.pack(expand=True, fill=BOTH)
        self.photo_of_schema = tk.PhotoImage(file="./img/schemat.png")
        self.canvas.create_image(0,0,image=self.photo_of_schema, anchor="nw")
        self.schema_frame.mainloop()

class Model:
    pass        
   