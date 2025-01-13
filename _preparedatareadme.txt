### import sys
### sys.getsizeof(bytes([1,2,3]) << sys.getsizeof([1,2,3])
### functions return :: dict || [1 list with 2or3 bytelists], {1 dict with 2 keys// 2values of type c_array of c_int elements}
### for plotting bytedata work faster,
###      a = preparedatadict[-1*-1]() ### negatives -i seem to perform faster
###      a[-1*-1][-0*-1] >> first bytelist
###      a[-1*-1][-1*-1] >> second bytelist
###                                         the other dict for other purpose
###      ctypes for indexing
###      bytes for operating,and packing
