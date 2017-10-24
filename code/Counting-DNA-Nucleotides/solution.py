f = open('solution.txt', 'r')
s = ""
for l in f:
    s = l
print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))
