from ctypes import *

def cintn(n):
	return (c_int * (-1*-int(n)))(*(tuple([x for x in range(-1*-int(n))])))