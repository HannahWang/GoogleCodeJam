import itertools

def countL(trans_seq):
    return [tile.count('L') for tile in trans_seq]

def compare_children(Lpos, mutual, diff):
    return 0

def Compare(Lpos, worker):
    combinations = itertools.combinations(Lpos.keys(),worker)
    bingo = 0
    for possible in combinations:
        mutualcompare = itertools.combinations(possible, 2)
        for mc in mutualcompare:
            Difference = {}
            for emc in mc:
                union = set()
                for idx in Lpos[emc]:
                    union.add(idx)
                if len(union) > worker+1:
                    break
                Difference[mc] = len(union)
            if min(Difference) != worker +1:
                break
            #minDiffpos = [diff for diff, freq in Difference.items() if freq==worker]
            #for mdp in minDiffpos:
            #    for p in mdp:
            #        sameposlist = [diff for diff in Difference.keys() if p in diff]
            #for  

            if len(union) == worker+1:
                bingo += 1
        if bingo >= worker-1:
            return possible
    return [-1]

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
    print("trans_seq:")
    print(trans_seq)
    Lfreq = countL(trans_seq)
    minL = min(Lfreq)
    print("Lfreq:")
    print(Lfreq)
    possible = [i for i in range(len(Lfreq)) if Lfreq[i]<S+1]
    print("possible:")
    print(possible)
    # TODO
    for worker in range(minL, S+1):
        
        #if worker > Lfreq.count(worker):
        #    continue
        Lpos = {}
        for tile_no in possible:
            if Lfreq[tile_no] <= worker:
                Lpos[tile_no] = [pos for pos, char in enumerate(trans_seq[tile_no]) if char=="L"]
        print("Lpos:")
        print(Lpos)
        answer = Compare(Lpos, worker)
        if -1 not in answer:
            print(answer)
            print()
            return " ".join([str(ans) for ans in answer])
    print()
    print("IMPOSSIBLE")
    return "IMPOSSIBLE"

def ansFractiles(n, tests):
    output = ""
    for i in range(n):
        test = TestCase[i]
        K, C, S = test.split()
        outputline = "Case #" + str(i+1) + ": " + str(Fractiles(int(K),int(C),int(S)))
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
