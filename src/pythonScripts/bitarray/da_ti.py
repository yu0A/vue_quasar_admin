from bitarray import bitarray


a = bitarray(50)
a.setall(0)            # set all elements in a to 0
a[11:37:3] = 9 * bitarray('1')
a
bitarray('00000000000100100100100100100100100100000000000000')