f = open('dna.txt', 'r')
s = ""
for line in f:
    s += line.replace('T', 'U')

print(s)
