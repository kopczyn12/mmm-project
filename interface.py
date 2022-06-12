import tkinter as tk
from tkinter import BOTH, Canvas, ttk, Toplevel
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
style.use('ggplot')
from app import *
from model import Model


class Interface(tk.Frame):

    def __init__(self, model, master = None):

        super().__init__()

        #zadeklarowanie naszego modelu
        self.model = model
        
        #pobudzenie
        self.radio_var = tk.StringVar()
        self.label_response = ttk.Label(self, text="Pobudzenie:", font=("Arial", 16))
        self.label_response.grid(row=1, column=0, columnspan=3)
        self.radio_sin = ttk.Radiobutton(self, text="Sinusoidalne", variable=self.radio_var, value="sinus")
        self.radio_rectangle = ttk.Radiobutton(self, text="Prostokątne", variable=self.radio_var, value="prostokat")
        self.radio_triangle = ttk.Radiobutton(self, text="Trójkątne", variable=self.radio_var, value="trojkatne")
        self.radio_var.set("sin")
        self.radio_sin.grid(row=2, column=0)
        self.radio_rectangle.grid(row=2, column=1)
        self.radio_triangle.grid(row=2, column=2, padx=15)

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

        #amplituda pobudzenia
        self.label_amp = ttk.Label(self, text="      Podaj\n  amplitude\n pobudzenia:", font=("Arial", 12))
        self.label_amp.grid(row=9, column=0, columnspan=1)
        self.Amp_var = tk.StringVar()
        self.entry_amp = tk.Entry(self, width=10, text=self.Amp_var)
        self.entry_amp.grid(row=9, column = 1)
        self.Amp_var.set("1")
        
        #warunki poczatkowe
        #x(0)
        self.label_x_zero = ttk.Label(self, text="Podaj wartość x(0)", font=("Arial",14))
        self.label_x_zero.grid(row=10, column=0, columnspan=1)
        self.x_zero_var = tk.StringVar()
        self.entry_x_zero = tk.Entry(self, width=10, text=self.x_zero_var)
        self.entry_x_zero.grid(row=10, column=1)
        self.x_zero_var.set("0")

        #x(0)'
        self.label_x_zero_higher = ttk.Label(self, text="Podaj wartość x(0)'", font=("Arial",14))
        self.label_x_zero_higher.grid(row=11, column=0, columnspan=1)
        self.x_zero_higher_var = tk.StringVar()
        self.entry_x_zero_higher = tk.Entry(self, width=10, text=self.x_zero_higher_var)
        self.entry_x_zero_higher.grid(row=11, column=1)
        self.x_zero_higher_var.set("0")

        #schemat projetku
        self.button_show_equation = ttk.Button(self, text = "Pokaż schemat projektu", command=lambda: self.show_schema())
        self.button_show_equation.grid(row=12, column=1)

        #Start symulacji
        self.button_simulation = ttk.Button(self, text="Symulacja", command=lambda: self.simulation())
        self.button_simulation.grid(row=13, column=1)

        #wykres
        self.f = Figure(figsize=(10,8), dpi=100)
        self.a = self.f.add_subplot(111)
        self.a.set_xlabel("Czas")
        self.a.set_ylabel("Wartość")
        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=11, column=3)
        self.canvas.get_tk_widget().grid(row=1, column=3, rowspan=10)

    #funkcja wykreslajaca wyniki
    def animate_plot(self):

        self.a.clear()
        self.a.set_xlabel("Czas")
        self.a.set_ylabel("Wartość")
        self.a.plot(self.model.t, self.model.x_euler, "#00FF00", label="Położenie - Euler")
        self.a.plot(self.model.t, self.model.v_euler, "#FF0000", label="Prędkość - Euler")
        self.a.plot(self.model.t, self.model.x_rg4, "#33B8FF", label="Położenie - Runge-Kutty")
        self.a.plot(self.model.t, self.model.v_rg4, "#EC00FE", label="Prędkość - Runge-Kutty")
        self.a.legend(loc=2, bbox_to_anchor=(0.22,1.1,), ncol=3, borderaxespad=0)

    #pobranie zmiennych i wykreslenie wynikow
    def simulation(self):

        self.model.update_model(var_k1 = float(self.k1_var.get()),
        var_k2 = float(self.k2_var.get()),
        var_m = float(self.m_var.get()),
        var_b = float(self.b_var.get()),
        var_amp = float(self.Amp_var.get()), 
        var_x_zero = float(self.x_zero_var.get()),
        var_x_zero_higher = float(self.x_zero_higher_var.get()),
        pobudzenie = self.radio_var.get())
        self.animate_plot()
        self.f.canvas.draw()

    #pokazanie schematu projektu w nowym oknie
    def show_schema(self):

        self.schema_frame = Toplevel(self)
        self.schema_frame.title("Schemat projektu")
        self.canvas = Canvas(self.schema_frame, width=348, height=161)
        self.canvas.pack(expand=True, fill=BOTH)
        self.photo_of_schema = tk.PhotoImage(file="./img/schemat.png")
        self.canvas.create_image(0,0,image=self.photo_of_schema, anchor="nw")
        self.schema_frame.mainloop()
    