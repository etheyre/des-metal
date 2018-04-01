def xor(a, b):
	""" Renvoie a xor b. """

	x = [False]*len(a)

	for i in range(len(a)):
		x[i] = a[i] ^ b[i]

	return x

def rot(a, n):
	""" Renvoie a <<< n. """

	return a[n:] + a[:n]

def int_to_bin(n):
	""" Renvoie la représentation binaire de n (big endian). """

	l = [int(x) for x in bin(n)[2:]]
	return [0]*(4-len(l)) + l

def int_to_bin_nopad(n):
	""" Renvoie la représentation binaire de n (big endian), sans pad. """

	return [int(x) for x in bin(n)[2:]]

def bin_walk(n):
	for i in range(n):
		yield int_to_bin_nopad(i)


def cbin(c):
	l = int_to_bin(ord(c))
	return [0]*(8-len(l)) + l

def add_parity(o):
	s = sum(o[:-1])
	return o[:-1] + [s%2]

def bits_to_hex(b):
	s = ""

	for i in range(len(b)//4):
		s += ([str(i) for i in range(10)] + [chr(ord('a') + i) for i in range(6)])[binval(b[4*i:4*i+4])]

	return s

def bits_to_ascii(b):
	s = ""

	for i in range(len(b)//8):
		s += chr(binval(b[8*i:8*i+8]))
		
	return s

	return s

def rand_bits(n):
	import random as r
	return [r.randint(0,1) for i in range(n)]

def binval(b):
	""" Renvoie la valeur du nombre binaire b (big endian). Seulement dans [0,15]. """

	s = 0

	for i in b:
		s = 2*s + i
	
	return s
