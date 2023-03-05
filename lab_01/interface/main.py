from tkinter import *
from matplotlib import mlab
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import library

class window_tk:
    def __init__(self, master):
        self.master = master 

        #Settings window
        master.title("Лабораторная 1")
        master.geometry("1300x800")
        # self.resizable(False, False)

        #Settings menu 
        menu_frame = Frame(master, bg = "LightCyan", width = 400, height = 800)
        menu_frame.place(x = 0, y = 0)

        library_frame = Frame(master, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(library_frame, "Перенос", "dx", "dy", "dz", "Перенести", library.transfer)
        library_frame.place(x = 50, y = 20)

        turn_frame = Frame(master, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(turn_frame, "Поворот", "angle x", "angle y", "angle z", "Повернуть", library.turn)
        turn_frame.place(x = 50, y = 240)

        scaling_frame = Frame(master, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(scaling_frame, "Масштабирование", "kx", "ky", "kz", "Масштабировать", library.scale)
        scaling_frame.place(x = 50, y = 490) 

        vertical_frame = Frame(master, bg = "black", width = 5, height = 800)
        vertical_frame.place(x = 395, y = 0)

        load_button = Button(master,  bg = "LightCyan", width = 33, height = 2, \
                            text = "Загрузить фигуру", font = ("Arial", 14, "bold"), command = library.load_figure)
        load_button.place(x = 50, y = 700)

        #Settings graph
        graph_frame = Frame(master, width = 900, height = 800)
        graph_frame.place(x = 400, y = 0)

        fig, ax = plt.subplots(dpi = 50, figsize = (9, 7.5), facecolor = "white")

        plt.axes(projection = '3d')

        figure_canvas = FigureCanvasTkAgg(fig, graph_frame)
        NavigationToolbar2Tk(figure_canvas, graph_frame)

        ax.get_yaxis().set_visible(False)
        ax.get_xaxis().set_visible(False)

        figure_canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = 1)

class ConvertFrame:
    def __init__(self, master, name, a, b, c, operation, func):
        name_block = Label(master, text = name, width = 18, bg = "LightCyan", font = ("Arial", 14, "bold"))
        name_block.place(x = 70, y = 15)

        a_block = Label(master, text = a, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        a_block.place(x = 20, y = 60)

        b_block = Label(master, text = b, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        b_block.place(x = 100, y = 60)

        c_block = Label(master, text = c, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        c_block.place(x = 180, y = 60)

        a_entry = Entry(master, width = 6)
        a_entry.place(x = 35, y = 90)

        b_entry = Entry(master, width = 6)
        b_entry.place(x = 115, y = 90)

        c_entry = Entry(master, width = 6)
        c_entry.place(x = 195, y = 90)

        button = Button(master, text = operation, width = 24, height = 2, font = ("Arial", 14, "bold"), command = func)
        button.place(x = 35, y = 135)
    

if __name__ == "__main__":
    window = Tk()

    window_tk(window)

    window.mainloop()

