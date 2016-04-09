def CountSheep(N):
    goal={'0','1','2','3','4','5','6','7','8','9'}
    track = set()
    last = set()
    idx = 1
    while idx < 101:
        N_str = str(N*idx)
        now = set()
        for d in N_str:
            now.update(d)
        #if last == now:
        #    return "INSOMNIA"
        last = now.copy()
        track.update(now)
        if track == goal:
            return str(N*idx)
        idx += 1
    return "INSOMNIA"

def ansCountSheep(n, tests):
    output = ""
    for i in range(n):
        test = TestCase[i]
        outputline = "Case #" + str(i+1) + ": " + CountSheep(test)
        output = output + outputline + "\n"
    output_file = open("CountingSheep_output_large-A.txt", "w")
    #output_file = open("CountingSheep_output"+attempt+".txt", "w")
    output_file.write(output)
    output_file.close()

import sys
# transfer TestCase from file to input suitable for the function
TestCase = []
testname = sys.argv[1]
#attempt = str(sys.argv[1])
#testname = "A-small-attempt" + attempt + ".in.txt"
test_file = open(testname, "r")
n = 0
for line in test_file:
    if n == 0:
        n = int(line)
    else:
        TestCase.append(int(line))
test_file.close()
# start 
ansCountSheep(n, TestCase);
