import sys

File = open(sys.argv[1], 'r')
lines = []

for line in File:
    lines.append(line.strip())

File.close()

numOfOutput = int(lines.pop(0))
lines.sort(lambda x,y: cmp(len(x), len(y)))
lines.reverse()

for i in range(0,numOfOutput):
    print lines[i]


exit(0)