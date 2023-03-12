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

        """
            Перенос фигуры
        """
        self.library_frame = Frame(self.root, bg = "LightCyan", width = 300, height = 200, borderwidth = 3, relief = "ridge")
        ConvertFrameTransfer(self.library_frame, "Перенос", "dx", "dy", "dz", "Перенести", library.transfer, self)
        self.a_entry = Entry(self.library_frame, width = 6)
        self.a_entry.place(x = 35, y = 90)

        self.b_entry = Entry(self.library_frame, width = 6)
        self.b_entry.place(x = 115, y = 90)

        self.c_entry = Entry(self.library_frame, width = 6)
        self.c_entry.place(x = 195, y = 90)

        self.library_frame.place(x = 50, y = 20)
    
        """
            Поворот фигуры
        """
        self.turn_frame = Frame(self.root, bg = "LightCyan", width = 300, height = 240, borderwidth = 3, relief = "ridge")
        ConvertFrame(self.turn_frame, "Поворот", "angle x", "angle y", "angle z", "Повернуть", library.turn, self)

        #Ввод центра поворота
        self.ta_entry = Entry(self.turn_frame, width = 6)
        self.ta_entry.place(x = 35, y = 150)

        self.tb_entry = Entry(self.turn_frame, width = 6)
        self.tb_entry.place(x = 115, y = 150)

        self.tc_entry = Entry(self.turn_frame, width = 6)
        self.tc_entry.place(x = 195, y = 150)

        #Ввод коэффицентов
        self.ta_entry = Entry(self.turn_frame, width = 6)
        self.ta_entry.place(x = 35, y = 80)

        self.tb_entry = Entry(self.turn_frame, width = 6)
        self.tb_entry.place(x = 115, y = 80)

        self.tc_entry = Entry(self.turn_frame, width = 6)
        self.tc_entry.place(x = 195, y = 80)

        self.turn_frame.place(x = 50, y = 240)

        """
            Масштабирование фигуры
        """
        self.scaling_frame = Frame(self.root, bg = "LightCyan", width = 300, height = 240, borderwidth = 3, relief = "ridge")
        ConvertFrame(self.scaling_frame, "Масштабирование", "kx", "ky", "kz", "Масштабировать", library.scale, self)

        #Ввод коэффицентов
        self.aa_entry = Entry(self.scaling_frame, width = 6)
        self.aa_entry.place(x = 35, y = 150)

        self.ab_entry = Entry(self.scaling_frame, width = 6)
        self.ab_entry.place(x = 115, y = 150)

        self.ac_entry = Entry(self.scaling_frame, width = 6)
        self.ac_entry.place(x = 195, y = 150)

        #Ввод центра масштабирования
        self.aa_dx_entry = Entry(self.scaling_frame, width = 6)
        self.aa_dx_entry.place(x = 35, y = 80)

        self.ab_dy_entry = Entry(self.scaling_frame, width = 6)
        self.ab_dy_entry.place(x = 115, y = 80)

        self.ac_dz_entry = Entry(self.scaling_frame, width = 6)
        self.ac_dz_entry.place(x = 195, y = 80)

        self.turn_frame.place(x = 50, y = 240)
        self.scaling_frame.place(x = 50, y = 490) 

        self.vertical_frame = Frame(self.root, bg = "black", width = 5, height = 800)
        self.vertical_frame.place(x = 395, y = 0)
        

        """
            Загрузка фигуры
        """
        self.load_button = Button(self.root,  bg = "LightCyan", width = 33, height = 2, \
                            text = "Загрузить фигуру", font = ("Arial", 14, "bold"), command = lambda: library.load_figure(self))
        self.load_button.place(x = 50, y = 735)


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

        self.subplt.set_xlabel("X")
        self.subplt.set_ylabel("Y")
        self.subplt.set_zlabel("Z")

        if (library.st.len_list != 0):
            lenl = library.st.len_list
            a = library.st.x_list[:lenl]
            b = library.st.y_list[:lenl]
            c = library.st.z_list[:lenl]
            
            self.subplt.plot(a, b, c, color = 'k', linewidth = 2)

        self.subplt.set_xlim((-200, 200))
        self.subplt.set_ylim((-200, 200))
        self.subplt.set_zlim((-200, 200))
        self.subplt.grid(True)

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

class ConvertFrameTransfer:
    def __init__(self, master, name, a, b, c, operation, func, root):
        self.name_block = Label(master, text = name, width = 18, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.name_block.place(x = 70, y = 15)

        self.a_block = Label(master, text = a, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.a_block.place(x = 20, y = 60)

        self.b_block = Label(master, text = b, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.b_block.place(x = 100, y = 60)

        self.c_block = Label(master, text = c, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.c_block.place(x = 180, y = 60)

        self.button = Button(master, text = operation, width = 24, height = 2, font = ("Arial", 14, "bold"), command = lambda: func(root))
        self.button.place(x = 35, y = 135)

class ConvertFrame:
    def __init__(self, master, name, a, b, c, operation, func, root):
        self.name_block = Label(master, text = name, width = 18, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.name_block.place(x = 70, y = 15)

        self.a_block = Label(master, text = "dx", width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.a_block.place(x = 20, y = 50)

        self.b_block = Label(master, text = "dy", width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.b_block.place(x = 100, y = 50)

        self.c_block = Label(master, text = "dz", width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.c_block.place(x = 180, y = 50)

        self.a_block = Label(master, text = a, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.a_block.place(x = 20, y = 120)

        self.b_block = Label(master, text = b, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.b_block.place(x = 100, y = 120)

        self.c_block = Label(master, text = c, width = 12, bg = "LightCyan", font = ("Arial", 14, "bold"))
        self.c_block.place(x = 180, y = 120)

        self.button = Button(master, text = operation, width = 24, height = 2, font = ("Arial", 14, "bold"), command = lambda: func(root))
        self.button.place(x = 35, y = 180)
    

if __name__ == "__main__":
    window = window_tk()
    window.run()


