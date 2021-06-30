infile = open('ch6.txt', 'r')
lines = infile.readlines()
out = 'P2\n100 12\n1\n'

for line in lines:
	for i in line.split('+'):
		color, iterable = i.split('x')
		out += ' ' + ' '.join([color for i in range(int(iterable))])
	out += 'n'

outfile = open('code.pgm', 'w')
outfile.write(out)

infile.close()
outfile.close()