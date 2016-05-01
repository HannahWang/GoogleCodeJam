import itertools

def countL(trans_seq):
    return [tile.count('L') for tile in trans_seq]

def Fractiles(K,C,S):
    tiles_n = K**C
    trans_seq = [[] for i in range(tiles_n)]
    # Generate original sequence
    orig_seq = ["G", "L"]
    for k in range(K-1):
        tmp = [s for s in orig_seq]
        orig_seq = []
        for s in tmp:
            orig_seq.extend([s+"G",s+"L"])
    # Get trans_seq
    for seq in orig_seq:
        seqmap = {"G":"G"*K, "L":seq}
        tmpseq = seq
        for t in range(C-1):
            next_seq = ""
            for c in tmpseq:
                next_seq += seqmap[c]
            tmpseq = "".join([c for c in next_seq])
        for i in range(tiles_n):
            trans_seq[i].append(tmpseq[i])
    # Check if students can help clean choices
    Lfreq = countL(trans_seq)
    max_worker = max(max(Lfreq), S)
    minL = min(Lfreq)
    possible = [i for i in range(len(Lfreq)) if Lfreq[i]<S+1]
    for worker in range(minL, max_worker+1):
        possible_sets = [s for s in itertools.combinations(possible, worker)]
        for pset in possible_sets:
            p_tran = [trans_seq[i] for i in pset]
            p_transpose = [list(x) for x in zip(*p_tran)]
            p_transpose_countL = countL(p_transpose)
            if p_transpose_countL.count(max(p_transpose_countL)) == 1:
                return " ".join([str(i+1) for i in pset])
    
    return "IMPOSSIBLE"

def ansFractiles(n, tests):
    output = ""
    for i in range(n):
        test = TestCase[i]
        K, C, S = test.split()
        outputline = "Case #" + str(i+1) + ": " + str(Fractiles(int(K),int(C),int(S)))
        print(outputline)
        output = output + outputline + "\n"
    output_file = open("Fractiles_output-B.txt", "w")
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
ansFractiles(n, TestCase);
