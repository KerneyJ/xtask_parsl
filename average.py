import sys
filename = sys.argv[1]
with open(filename) as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        line = line.strip('\n')
        total += float(line)
    print(total / 10)
