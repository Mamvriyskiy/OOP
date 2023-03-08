from tkinter import *
from matplotlib import mlab
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)
import library

matplotlib.use('TkAgg')

class window_tk():
    def __init__(self):
        self.root = Tk()
        #Settings window
        self.root.title("Лабораторная 1")
        self.root.geometry("1300x800")
        # self.resizable(False, False)

    def settings_menu(self):
        #Settings menu 
        self.menu_frame = Frame(self.root, bg = "LightCyan", width = 400, height = 800)
        self.menu_frame.place(x = 0, y = 0)

        self.library_frame = Frame(self.root, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(self.library_frame, "Перенос", "dx", "dy", "dz", "Перенести", library.transfer)
        self.library_frame.place(x = 50, y = 20)

        self.turn_frame = Frame(self.root, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(self.turn_frame, "Поворот", "angle x", "angle y", "angle z", "Повернуть", library.turn)
        self.turn_frame.place(x = 50, y = 240)

        self.scaling_frame = Frame(self.root, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrame(self.scaling_frame, "Масштабирование", "kx", "ky", "kz", "Масштабировать", library.scale)
        self.scaling_frame.place(x = 50, y = 490) 

        self.vertical_frame = Frame(self.root, bg = "black", width = 5, height = 800)
        self.vertical_frame.place(x = 395, y = 0)

        self.load_button = Button(self.root,  bg = "LightCyan", width = 33, height = 2, \
                            text = "Загрузить фигуру", font = ("Arial", 14, "bold"), command = lambda: library.load_figure(self))
        self.load_button.place(x = 50, y = 700)

    def settings_graph(self):
        #Settings graph

        margins = {
            "left"   : 0.050,
            "bottom" : 0.050,
            "right"  : 0.980,
            "top"    : 0.980
        }

        self.figure = plt.Figure(figsize=(8.5, 7.8))
        self.figure.subplots_adjust(**margins)
        self.subplt = self.figure.add_subplot(111, projection = "3d")

        # print(library.data_figure)
        # self.subplt.plot(library.data_figure[0], library.data_figure[1], library.data_figure[2], color = 'k', linewidth = 2)

        # print(library.point_figure)
        # if (len(library.point_figure) != 0):
        #     a = library.point_figure[0]
        #     b = library.point_figure[1]
        #     c = library.point_figure[2]
        #     self.subplt.plot(a, b, c, color = 'k', linewidth = 2)
            # self.subplt.plot(a[2:], b[2:], c[2:], color = 'k', linewidth = 2)

        # self.subplt.set_xlim((-80, 80))
        # self.subplt.set_ylim((-80, 80))
        # self.subplt.grid(True)

        self.pltcnv = FigureCanvasTkAgg(self.figure, self.root)
        self.pltcnv.get_tk_widget().place(
            relx = 0.308,
            rely = 0.00,
            relheight = 0.96,
            relwidth = 0.70
            )
        
    def create_widgets(self):
        """
            Создание виджетов окна
        """
        self.settings_menu()
        self.settings_graph()
 
    def run(self):
        """
            Запуск окна
        """
        self.create_widgets()
        self.root.mainloop()

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
    window = window_tk()
    window.run()


