from ctypes import *
import main
import time

LOAD_FIGURE = 1
TRANSFER_FIGURE = 2
TURN_FIGURE = 3
SCALE_FIGURE = 4

class test_st_t(Structure):
    _fields_ = [
                ("command", c_int),
                ("a", c_double),
                ("b", c_double),
                ("c", c_double),
                ("point", POINTER(POINTER(c_double))),
                ("connect", POINTER(POINTER(c_int))),
                ("len_point", c_int),
                ("len_connect", c_int)]
    
st = test_st_t(0, 0, 0, 0, None, None, 0, 0)
point_figure = []
connect_figure = []

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
    libc.command_distribution.argtypes = [POINTER(test_st_t)]
    libc.command_distribution.restype = c_int;

    st.command = LOAD_FIGURE;
    libc.command_distribution(st)

    print(st.len_point, st.len_connect)
    point_figure.clear()
    point_figure.append(list(st.point[0][:st.len_point]))
    point_figure.append(list(st.point[1][:st.len_point]))
    point_figure.append(list(st.point[2][:st.len_point]))


    connect_figure.clear()
    connect_figure.append(list(st.connect[0][:st.len_connect]))
    connect_figure.append(list(st.connect[1][:st.len_connect]))

    a = point_figure

    # point_figure.clear()

    # for i in connect_figure[0]:
        



    print(point_figure)
    print(connect_figure)

    
    root.settings_graph()

