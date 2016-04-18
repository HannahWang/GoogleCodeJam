from concurrent.futures import ProcessPoolExecutor
import pickle
import os

class DetectedPrimes:
    def __init__(self, MaxPrime, PrimeList):
        self.MaxPrime = MaxPrime
        self.PrimeList = PrimeList


def PrimeFromDetected(num, primes):
    up = int(num**0.5)
    if num in primes.PrimeList:
    #if num in primes:
        return 0
    if num%2 == 0:
        return 2 
    for i in range(3, up, 2):
        if num%i == 0:
            return i
        elif i > 10000:
        #elif i > primes.MaxPrime:
            break
    return 0

def CoinJam(N, J):
    if os.path.isfile("primes.pickle"):
        with open("primes.pickle", "rb") as fin:
            PRIMES = pickle.load(fin)
    else:
        PRIMES = DetectedPrimes(30, [2,3,5,7,11,13,17,19,23,29])
    mustadd = {base:base**(N-1)+1 for base in range(2,11)}
    valid_jamcoins = []
    tried_jamcoins = set()
    while len(valid_jamcoins) < J:
        # randomly get a possible jamcoin
        import random
        S = ""
        for i in range(N-2):
            c = str(random.randrange(0,2))
            S += c
        jamcoin = "1" + S + "1"
        if jamcoin in tried_jamcoins:
            continue
        tried_jamcoins.add(jamcoin)
        # validation
        valid_divisors = []
        for base in range(2,11):
            interpretation = sum([int(S[i])*(base**(N-2-i)) for i in range(N-2)]) + mustadd[base]
            vn = PrimeFromDetected(interpretation, PRIMES)
            print(vn)
            if vn == 0:
                break
            valid_divisors.append(str(vn))
        if vn == 0:
            continue
        # add validated jamcoin to valid_jamcoins
        tmp = [jamcoin]
        tmp.extend(valid_divisors)
        valid_jamcoins.append(tmp)
        print(tmp)
    # genereate output lines 
    out = ""
    for vj in valid_jamcoins:
        out = out + " ".join(vj) + "\n"
    return out

def ansCoinJam(n, tests):
    output = ""
    for i in range(n):
        test = TestCase[i]
        N = int(test.split()[0])
        J = int(test.split()[1])
        outputline = "Case #" + str(i+1) + ":\n" + CoinJam(N,J)
        output = output + outputline + "\n"
    output_file = open("CoinJam_output-large.txt", "w")
    #output_file = open("C-small_output"+attempt+".txt", "w")
    output_file.write(output)
    output_file.close()

import sys
# transfer TestCase from file to input suitable for the function
TestCase = []
testname = sys.argv[1]
#attempt = str(sys.argv[1])
#testname = "C-small-attempt" + attempt + ".in.txt"
test_file = open(testname, "r")
n = 0
for line in test_file:
    if n == 0:
        n = int(line)
    else:
        TestCase.append(line.rstrip('\n'))
test_file.close()
# start 
ansCoinJam(n, TestCase);
