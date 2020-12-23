#m=431
def addelem(f1, f2):
    g = []
    if len(f1) > len(f2):
        while len(f1) != len(f2):
            f2.insert(0, 0)
    elif len(f2) > len(f1):
        while len(f1) != len(f2):
            f1.insert(0,0)
    else:
        for in range(len(f1)): #xor між списками
            if (f1[i] = 0 and f2[j] = 0):
                g.append(0)
            elif (f1[i] = 0 and f2[j] = 1):
                g.append(1)
            elif (f1[i] = 1 and f2[j] = 0):
                g.append(1)
            else:
                g.append(0)
    return g

def matrix(matrix):
	matrix = np.zeros((431,431))
	i = 0
	j = 0
	while i != (2m - 1):
		while j != (2m - 1):
			if ((2 ** i) + (2 ** j)) % 2 = 1:
				matrix[ij] = 1
			elif ((2 ** i) - (2 ** j)) % 2 = 1:
				matrix[ij] = 1
			elif (-(2 ** i) + (2 ** j)) % 2 = 1:
				matrix[ij] = 1
			elif (-(2 ** i) - (2 ** j)) % 2 = 1:
				matrix[ij] = 1
			else:
				matrix[ij] = 0
	return matrix

def mulelem(f1, f2):
	
	
def converse(f): #іто-цуїті
	k = 1
	b = f
	mm = []
	temp = len(m)
	while temp != 0:
		if m % 2 == 0:
			mm.insert(0, 0)
		else:
			mm.insert(0, 1)
		temp = temp - 1
	i = len(mm)
	while i != 0:
		b = (b ** 2) * b
		k = 2k
		if mm[i] = 1:
			b = (b ** 2) * f
			k = k + 1
		i = i - 1
	g = b ** 2
	return g

def trace(f):
    i = 0
    while i != len(f):
        g = g + f[i]
        i = i + 1
    return g