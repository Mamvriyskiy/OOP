from ctypes import *
import main
import time

LOAD_FIGURE = 1
TRANSFER_FIGURE = 2
TURN_FIGURE = 3
SCALE_FIGURE = 4

    
class Data(Structure):
    _fields_ = [("kx", c_double),
                ("ky", c_double),
                ("kz", c_double),
                ("dx", c_double),
                ("dy", c_double),
                ("dz", c_double),]

class Points_array(Structure):
    _fields_ = [("x_list", POINTER(c_double)), 
                ("y_list", POINTER(c_double)),
                ("z_list", POINTER(c_double)),
                ("len_list", c_int)]

x_list =(c_double * 50)()
y_list =(c_double * 50)()
z_list =(c_double * 50)()

data = Data(0, 0, 0, 0, 0, 0)
st = Points_array(x_list, y_list, z_list, 0)


def transfer(root):
    pass
    # st.command = TRANSFER_FIGURE;
    # libc = CDLL('libarr.so')
    # libc.command_distribution.argtypes = [POINTER(Points_array)]
    # libc.command_distribution.restype = c_int;

    # dx = root.a_entry.get()
    # dy = root.b_entry.get()
    # dz = root.c_entry.get()

    # st.dx = float(dx);
    # st.dy = float(dy);
    # st.dz = float(dz);

    # libc.command_distribution(st)

    # root.settings_graph()

def turn(root):
    pass
    # st.command = SCALE_FIGURE;
    # libc = CDLL('libarr.so')

    # libc.command_distribution.argtypes = [POINTER(Points_array)]
    # libc.command_distribution.restype = c_int;

    # dx = root.ta_entry.get()
    # dy = root.tb_entry.get()
    # dz = root.tc_entry.get()

    # st.dx = float(dx);
    # st.dy = float(dy);
    # st.dz = float(dz);

    # libc.command_distribution(st)

    # root.settings_graph()


def scale(root):
    pass
    # st.command = SCALE_FIGURE;
    # libc = CDLL('libarr.so')

    # libc.command_distribution.argtypes = [POINTER(Points_array)]
    # libc.command_distribution.restype = c_int;

    # dx = root.aa_entry.get()
    # dy = root.ab_entry.get()
    # dz = root.ac_entry.get()

    # kx = root.aa_entry.get()
    # ky = root.ab_entry.get()
    # kz = root.ac_entry.get()

    # st.dx = float(dx);
    # st.dy = float(dy);
    # st.dz = float(dz);


    # libc.command_distribution(st)

    # root.settings_graph()

def load_figure(root):
    libc = CDLL('libarr.so')
    libc.command_distribution.argtypes = [POINTER(Points_array), c_int, Data]
    libc.command_distribution.restype = c_int

    libc.command_distribution(st, LOAD_FIGURE, data)

    print(st.x_list[:st.len_list])

    root.settings_graph()

