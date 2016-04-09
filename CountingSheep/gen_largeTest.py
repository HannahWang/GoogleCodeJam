import random
N = 100
output = str(N) + "\n"
for i in range(N):
    output = output + str(random.randrange(1000,1000001)) + "\n"
outfile = open("large.in.txt","w")
outfile.write(output)
outfile.close()
