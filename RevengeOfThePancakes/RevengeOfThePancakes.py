def RevengePancakes(serial):
    flipmap = {"+":"-", "-":"+"}
    times = 0
    blank_bottom = len(serial)-1
    while "-" in serial:
        happy_bottom = -1
        times += 1
        for i in range(blank_bottom,-1,-1):
            if serial[i] == "-":
                blank_bottom = i
                break
        if serial[0] == "+":
            for i in range(blank_bottom,-1,-1):
                if serial[i] == "+":
                    happy_bottom = i
                    break
        if happy_bottom != -1:
            flip_bottom = happy_bottom
        else:
            flip_bottom = blank_bottom
        rev = [flipmap[c] for c in serial[0:flip_bottom+1]]
        serial = ''.join(rev)[::-1]+serial[flip_bottom+1:]
        #print(serial)
    #print(times)
    return times

def ansRevengePancakes(n, tests):
    output = ""
    for i in range(n):
        test = TestCase[i]
        outputline = "Case #" + str(i+1) + ": " + str(RevengePancakes(test))
        output = output + outputline + "\n"
    output_file = open("RevengePancakes_output-B.txt", "w")
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
ansRevengePancakes(n, TestCase);
