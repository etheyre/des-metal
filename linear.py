from binutils import *
import des

def hamming_dist(l1, l2):
	""" Renvoie la distance de Hamming entre l1 et l2, qui sont deux
	listes d'éléments de {0,1} de même taille. """

	return sum(i != j for i, j in zip(l1, l2))

def eval_lin(xs, bs):
	""" Renvoie l'évaluation de la fonction linéaire f telle que :
	f(xs) = (xs[0] & bs[0]) ^ ... ^ (xs[len(xs)-1] & bs[len(xs)-1]).
	Enfin, pas exactement. """

	x = 0

	for i in range(len(bs)):
		if i >= len(xs):
			x ^= 0
		else:
			x ^= xs[i] & bs[i]
	
	return x

def lin_dist(lf, t):
	""" Renvoie la distance entre la fonction linéaire lf (définie
	comme étant les bs de eval_lin) et le tableau t, ce qui correspond
	à la distance de Hamming entre les tables de vérité. """

	return hamming_dist(t, [eval_lin(xs, lf) for xs in bin_walk(len(t))])

def bin_minimize(f, n):
	""" Finds which integer in [0,n[ has an associated bit array that minimizes
	f. """

	min_f = f([0])
	min_b = []
	
	for b in bin_walk(n):
		vf = f(b)

		if vf < min_f:
			min_f = vf
			min_b = b

	return min_b, min_f

def approx_linearize_sbox(n, b):
	""" Renvoie une fonction linéaire qui approxime la valeur du bit
	n° b de la S-Box n° (n+1) et sa distance avec la table de valeurs
	dudit bit (évaluée par lin_dist). """

	sbox_t = [v[b] for v in des.SBXb[n]]
	mb, mf = bin_minimize(lambda x: lin_dist(x, sbox_t), 2**6)

	return mb, mf

def min_approx_dist():
	""" Renvoie la plus petite distance entre l'approximation d'un bit
	par une fonction linéaire et la table de valeurs dudit bit. """

	return min([min([approx_linearize_sbox(i,j)[1] for j in range(4)]) for i in range(8)])

