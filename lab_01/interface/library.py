from ctypes import *

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
                ("point", POINTER(c_double)),
                ("connect", POINTER(c_int)),
                ("len_point", c_int),
                ("len_connect", c_int)]
    
st = test_st_t(0, 0, 0, 0, None, None, 0, 0)
data_figure = []

def transfer():
    pass
    # data_figure = list(st.data[:st.len_data])

def turn():
    libc = CDLL('libarr.so')
    libc.command_distribution()

def scale():
    libc = CDLL('libarr.so')
    libc.command_distribution()

def load_figure():
    libc = CDLL('libarr.so')
    libc.command_distribution.argtypes = [POINTER(test_st_t)]
    libc.command_distribution.restype = c_int;

    st.command = LOAD_FIGURE;
    libc.command_distribution(st)

    a = list(st.point[:st.len_point])
    b = list(st.connect[:st.len_connect])
    print(st.point[0])
    # print(b)
    # print(st.point[0], st.connect[0], st.a)

