def MainMethod(serials):
    N = int((len(serials)+1)/2)
    number_count = {}
    for row in serials:
        for each in row:
            number_count[each] = number_count.setdefault(each, 0) + 1
    odd = [each for each in number_count.keys() if number_count[each]%2==1]
    #print(odd)
    if len(odd) == N:
        return ' '.join([str(x) for x in sorted(odd)])


import sys
# transfer TestCase from file to input suitable for the function
TestCase = []
testname = sys.argv[1]
test_file = open(testname, "r")
n = 0
N = 0
for line in test_file:
    if n == 0:
        n = int(line)
    else:
        if N == 0:
            N = int(line)
            tc = [[] for i in range(2*N-1)]
            now_idx = 0
        else:
            if now_idx < 2*N-1:
                #tc[now_idx] = [int(x) for x in line.rstrip('\n') if x is not ' ']
                tc[now_idx] = [int(x) for x in line.split()]
                if now_idx == 2*N-2:
                    N = 0
                    TestCase.append(tc)
            now_idx += 1
test_file.close()
# start 
output = ""
for i in range(n):
    test = TestCase[i]
    outputline = "Case #" + str(i+1) + ": " + str(MainMethod(test))
    output = output + outputline + "\n"
outname = testname.replace("in", "out")
output_file = open(outname, 'w');
output_file.write(output)
output_file.close()

