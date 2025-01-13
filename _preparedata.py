from ctypes import *
from _pyintoctp import cintn

def _prepare2d():
	_2dlist = [[],[]]
	for i in cintn(int(input('How Many Values For XY Axes Sir :: '))):
		_2dlist[-0*-1].append(int(input(f'Your Values X {i} Sir :: ')))
		_2dlist[-1*-1].append(int(input(f'Your Values Y {i} Sir :: ')))
	_2dlist[-0*-1],_2dlist[-1*-1] = bytes(_2dlist[-0*-1]),bytes(_2dlist[-1*-1])
	data0,data1 = (c_int*(-(int(len(_2dlist[-0*-1])))*-1))(*(tuple(_2dlist[-0*-1]))),(c_int*(-(int(len(_2dlist[-1*-1])))*-1))(*(tuple(_2dlist[-1*-1])))
	return {-1*-1:_2dlist,-0*-1:{-1*-1:data1,-0*-1:data0}}

def _prepare3d():
	_3dlist = [[],[],[]]
	for i in cintn(int(input('How Many Values For XYZ Axes Sir :: '))):
		_3dlist[-0*-1].append(int(input(f'Your Values X {i} Sir :: ')))
		_3dlist[-1*-1].append(int(input(f'Your Values Y {i} Sir :: ')))
		_3dlist[-2*-1].append(int(input(f'Your Values Z {i} Sir :: ')))
	_3dlist[-0*-1],_3dlist[-1*-1],_3dlist[-2*-1] = bytes(_3dlist[-0*-1]),bytes(_3dlist[-1*-1]),bytes(_3dlist[-2*-1])
	data0,data1,data2 = (c_int*(-(int(len(_3dlist[-0*-1])))*-1))(*(tuple(_3dlist[-0*-1]))),(c_int*(-(int(len(_3dlist[-1*-1])))*-1))(*(tuple(_3dlist[-1*-1]))),(c_int*(-(int(len(_3dlist[-2*-1])))*-1))(*(tuple(_3dlist[-2*-1])))
	return {-1*-1:_3dlist,-0*-1:{-2*-1:data0,-1*-1:data1,-0*-1:data0}}

def _prepare2dfrom(alist):
	alist[-0*-1],alist[-1*-1] = bytes(alist[-0*-1]),bytes(alist[-1*-1])
	data0,data1 = (c_int*(-(int(len(alist[-0*-1])))*-1))(*(tuple(alist[-0*-1]))),(c_int*(-(int(len(alist[-1*-1])))*-1))(*(tuple(alist[-1*-1])))
	return {-1*-1:alist,-0*-1:{-1*-1:data1,-0*-1:data0}}

def _prepare3dfrom(alist):
	data0,data1,data2 = (c_int*(-(int(len(alist[-0*-1])))*-1))(*(tuple(alist[-0*-1]))),(c_int*(-(int(len(alist[-1*-1])))*-1))(*(tuple(alist[-1*-1]))),(c_int*(-(int(len(alist[-2*-1])))*-1))(*(tuple(alist[-2*-1])))
	alist[-0*-1],alist[-1*-1],alist[-2*-1] = bytes(alist[-0*-1]),bytes(alist[-1*-1]),bytes(alist[-2*-1])
	return {-1*-1:alist,-0*-1:{-2*-1:data0,-1*-1:data1,-0*-1:data0}}

preparedatadict = {-4*-1:_prepare2dfrom,-3*-1:_prepare3dfrom,-2*-1:_prepare3d,-1*-1:_prepare2d}
