from tkinter import *
from matplotlib import mlab
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


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

        transfer_frame = Frame(master, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(transfer_frame, "Перенос")
        transfer_frame.place(x = 50, y = 50)

        turn_frame = Frame(master, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(turn_frame, "Поворот")
        turn_frame.place(x = 50, y = 300)

        scaling_frame = Frame(master, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(scaling_frame, "Масштабирование")
        scaling_frame.place(x = 50, y = 550) 

        vertical_frame = Frame(master, bg = "black", width = 5, height = 800)
        vertical_frame.place(x = 395, y = 0)

        #Settings graph
        graph_frame = Frame(master, width = 900, height = 800)
        graph_frame.place(x = 400, y = 0)

        fig, ax = plt.subplots(dpi = 50, figsize = (9, 7.5), facecolor = "white")

        figure_canvas = FigureCanvasTkAgg(fig, graph_frame)
        NavigationToolbar2Tk(figure_canvas, graph_frame)

        figure_canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = 1)

class ConvertFrame:
    def __init__(self, master, name):
        name_block = Label(master, text = name, width = 18, bg = "LightCyan", font = ("Arial", 14, "bold"))
        name_block.place(x = 70, y = 15)

    

if __name__ == "__main__":
    window = Tk()

    window_tk(window)

    window.mainloop()

