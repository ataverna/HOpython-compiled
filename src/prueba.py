import ctypes as C
math = C.CDLL('./mylib.so')

# add_two #
math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float,C.c_float]
print 'add_float', math.add_float(3.14,5.2)

math.add_int.restype = C.c_int
math.add_int.argtypes = [C.c_int,C.c_int]
print 'add_int', math.add_int(3,-10)

par1 = C.c_float(7.2)
par2 = C.c_float(-2.1)
res = C.c_float()
math.add_float_ref(C.byref(par1),C.byref(par2),C.byref(res))
print 'add_float_ref', res.value, res

par1 = C.c_int(7)
par2 = C.c_int(-2)
res = C.c_int()
math.add_int_ref(C.byref(par1),C.byref(par2),C.byref(res))
print 'add_int_ref', res.value, res

# arrays #

par1 = (C.c_int*3) (5,3,8)
par2 = (C.c_int*3) (-5,0,3)
out = (C.c_int*3) ()
math.add_int_array(C.byref(par1),C.byref(par2),C.byref(out),C.c_int(3))
print 'add_int_array', out[0], out[1], out[2]

