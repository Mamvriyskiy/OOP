from ctypes import *
import main
import time

LOAD_FIGURE = 1
TRANSFER_FIGURE = 2
TURN_FIGURE = 3
SCALE_FIGURE = 4

class Point(Structure):
    _fields_ = [("x_list", POINTER(c_double)), 
                ("y_list", POINTER(c_double)),
                ("z_list", POINTER(c_double))]

class Points_array(Structure):
    _fields_ = [
                ("command", c_int),
                ("points", Point),
                ("len_list", c_int)]

x_list =(c_double * 50)()
y_list =(c_double * 50)()
z_list =(c_double * 50)()
st = Points_array(0, Point(x_list, y_list, z_list), 0)

def transfer():
    pass
    # data_figure = list(st.data[:st.len_data])

def turn():
    libc = CDLL('libarr.so')
    libc.command_distribution()

def scale():
    libc = CDLL('libarr.so')
    libc.command_distribution()

def load_figure(root):
    libc = CDLL('libarr.so')
    libc.command_distribution.argtypes = [POINTER(Points_array)]
    libc.command_distribution.restype = c_int;


    st.command = LOAD_FIGURE;
    libc.command_distribution(st)

    print(st.points.x_list[:50])


    # point_figure.clear()
    # point_figure.append(list(st.point[0][:st.len_point]))
    # point_figure.append(list(st.point[1][:st.len_point]))
    # point_figure.append(list(st.point[2][:st.len_point]))


    # connect_figure.clear()
    # connect_figure.append(list(st.connect[0][:st.len_connect]))
    # connect_figure.append(list(st.connect[1][:st.len_connect]))

    # a = point_figure

    # point_figure.clear()

    # for i in connect_figure[0]:
        



    # print(point_figure)
    # print(connect_figure)

    
    root.settings_graph()

