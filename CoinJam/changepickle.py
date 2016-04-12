import os
import pickle
class DetectedPrimes:
    def __init__(self, MaxPrime, PrimeList):
        self.MaxPrime = MaxPrime
        self.PrimeList = PrimeList

    def updatePrimeList(self, maxn):
        self.MaxPrime = self.MaxPrime+1 if (self.MaxPrime+1)%2 == 0 else self.MaxPrime
        print("MaxPrime: "+str(self.MaxPrime)+", Next_MaxPrime: "+str(maxn))
        with ProcessPoolExecutor(max_workers = 2) as executor:
            for num, is_prime in zip(range(self.MaxPrime+1, maxn+1, 2), executor.map(self.prime, range(self.MaxPrime+1, maxn+1, 2))):
                if is_prime:
                    self.PrimeList.append(num)    
        self.MaxPrime = maxn
        with open("primes.pickle", "wb") as fout:
            pickle.dump(self, fout)

    def prime(self, num): #find whether num is a prime
        up = int(num**0.5)
        for i in self.PrimeList:
            if i > up:
                break
            if num%i == 0:
                return False
        return True

with open("primes.pickle", "rb") as fin:
    PRIMES = pickle.load(fin)
    NEW_PRIMES = PRIMES.PrimeList

with open("primes2.pickle", "wb") as fout:
    pickle.dump(NEW_PRIMES, fout)
