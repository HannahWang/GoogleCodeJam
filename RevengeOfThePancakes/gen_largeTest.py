import random
N = 100
output = str(N) + "\n"
rndmap = {1:"+", 2:"-"}
for i in range(N):
    loS = random.randrange(1,101)
    S = ""
    for j in range(loS):
        c = rndmap[random.randrange(1,3)]
        S += c
    output = output + S + "\n"
outfile = open("large.in.txt","w")
outfile.write(output)
outfile.close()
