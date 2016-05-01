def LastWord(serial):
    lastword = ""
    for c in serial:
        if lastword == "":
            lastword = c;
            continue;
        if lastword[0] > c:
            lastword = lastword + c;
        else:
            lastword = c + lastword
    return lastword

def ansLastWord(n, tests):
    output = ""
    for i in range(n):
        test = TestCase[i]
        outputline = "Case #" + str(i+1) + ": " + str(LastWord(test))
        output = output + outputline + "\n"
    output_file = open("A-large-practice.out.txt", "w")
    #output_file = open("B-small_output"+attempt+".txt", "w")
    output_file.write(output)
    output_file.close()

import sys
# transfer TestCase from file to input suitable for the function
TestCase = []
testname = sys.argv[1]
#attempt = str(sys.argv[1])
#testname = "B-small-attempt" + attempt + ".in.txt"
test_file = open(testname, "r")
n = 0
for line in test_file:
    if n == 0:
        n = int(line)
    else:
        TestCase.append(line.rstrip('\n'))
test_file.close()
# start 
ansLastWord(n, TestCase);
