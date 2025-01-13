import json
import matplotlib.pyplot as plt

from pathlib import Path
from os import getcwd
from ctypes import *

cp,rp,oneipo = c_int * (-1*-1), c_int * (-1*-1), c_int * (-1*-1)
cn,rn, oneci = int(input('Columns Number Sir :: ')),int(input('Rows Number Sir :: ')), oneipo(-0*-1)
ip,thislist = c_int * (-(cn)*-(rn)), [x+1 for x in range(cn*rn)]
index = ip(*(tuple(thislist)))

_projections = {-1*-1:'aitoff',-2*-1:'hammer',-3*-1:'lambert',-4*-1:'mollweide',-5*-1:'polar',-6*-1:'rectilinear',-7*-1:None}
_colors = {-1*-1:'b',-2*-1:'g',-3*-1:'r',-4*-1:'c',-5*-1:'m',-6*-1:'y',-7*-1:'k',-8*-1:'w'}

for i in index:
	a,aa = [str(x) for x in Path(getcwd()).iterdir() if str(x).endswith('.json')],{}
	aa.update({x:a[x] for x in range(len(a))})
	jsonfile = json.load(open(aa[int(input(f'{a} Choose File Sir :: {aa} '))],'rb'))
	keyslist = [key for key in jsonfile]
	keys,chosenkeys,data = {},[],[]
	keys.update({x:keyslist[x] for x in range(len(keyslist))})
	chosenkeys.append(keys[int(input(f'{keys}    Your Key Number Sir :: '))])
	chosenkeys.append(keys[int(input(f'{keys}    Your Key Number Sir :: '))])
	data.append(([i for i in jsonfile[chosenkeys[0]]]))
	data.append(([i for i in jsonfile[chosenkeys[1]]]))
	datakeys = [key for key in data[0][0]]
	prj = int(input(f"Choose Projection Style:: 1:aitoff,2:hammer,3:lambert,4:mollweide,5:polar:6:rectilinear,7:none "))
	b = plt.subplot(int(f"{cn}{rn}{i}"),projection=_projections[prj])
	b.set_xlabel(str(input('Your XLabel Sir :: ')))
	b.set_ylabel(str(input('Your XLabel Sir :: ')))
	while True:
		c = int(input(f"Choose Plotting Style:: 1:Plot,2:Scatter,3:Bar,4:Stem,5:Step,6:Finish "))
		if not c == int(6):
			plotdict={-1*-1:b.plot,-2*-1:b.scatter,-3*-1:b.bar,-4*-1:b.stem,-5*-1:b.step}						
			plotdict[c]([data[0][x][datakeys[0]] for x in range(len(data[0]))],[data[1][x][datakeys[1]] for x in range(len(data[0]))],color=_colors[int(input(f'{_colors}  Choose Color Sir :: '))])
		elif c == int(6):
			del data,jsonfile,keyslist,keys,chosenkeys,datakeys
			break	

if not str(input('Make Image :: y for YES, n for NO ')) == str('n'):
	plt.savefig(str(input('Your File Name Sir ::')))	

if not str(input('View Plot Sir :: y for YES, n for NO ')) == str('n'):
	plt.show()
