from nltk.tokenize import word_tokenize
import numpy as np

def data_stream():
    """Stream the data in 'leipzig100k.txt' """
    with open('leipzig100k.txt', 'r') as f:
        for line in f:
            for w in word_tokenize(line):
                if w.isalnum():
                    yield w
   
def bloom_filter_set():
    """Stream the data in 'Proper.txt' """
    with open('Proper.txt', 'r') as f:
        for line in f:
            yield line.strip()



############### DO NOT MODIFY ABOVE THIS LINE #################


# Implement a universal hash family of functions below: each function from the
# family should be able to hash a word from the data stream to a number in the
# appropriate range needed.

def uhf(rng):
    """Returns a hash function that can map a word to a number in the range
    0 - rng
    """
    pass

############### 

################### Part 1 ######################


# Implement a universal hash family of functions below: each function from the
# family should be able to hash a word from the data stream to a number in the
# appropriate range needed.

def uhf(rng):
    """Returns a hash function that can map a word to a number in the range
    0 - rng
    """
    a = np.random.randint(1,p)
    b = np.random.randint(0,p)
    return lambda x: ((a*x+b)%p)%m

############### 

################### Part 1 ######################
import nltk
nltk.download('punkt')
from bitarray import bitarray
size = 2**18   # size of the filter

a=uhf(2059859,262144)
b=uhf(2059861,262144)
c=uhf(2059879,262144)
d=uhf(2059891,262144)
e=uhf(2059913,262144)
hash_fns = [a,b,c,d,e]  # place holder for hash functions
bit_array=bitarray(size)
bit_array.setall=0
bloom_filter = bit_array

k=[]
for i in data_stream():
    k.append(i)
	
N=[]
for i in bloom_filter_set():
    N.append(i)
	
num_words = len(k)         # number in data stream = 2059856
num_words_in_set = len(N)  # number in Bloom filter's set = 32657

for word in bloom_filter_set(): # add the word to the filter by hashing etc.
    for h in H:
        num=h(int(word,36))
        bloom_filter[num]==1
print(len(bloom_filter))

M=[]
for word in data_stream():  # check for membership in the Bloom filter
    for h in H:
       # num = h(int(word,36))
        if bloom_filter[h(int(word,36))] == 0:
            break
        elif bloom_filter[h(int(word,36))] == 1:
            continue
    M.append(word)
print(len(M))
     
FP=len(set(M)-set(N))
FP

print('Total number of words in stream = %s'%(num_words,))
print('Total number of words in stream = %s'%(num_words_in_set,))
      
################### Part 2 ######################

hash_range = 24 # number of bits in the range of the hash functions
fm_hash_functions = [None]*35  # Create the appropriate hashes here

def num_trailing_bits(n):
    """Returns the number of trailing zeros in bin(n)

    n: integer
    """
    pass

num_distinct = 0

#for word in data_stream(): # Implement the Flajolet-Martin algorithm
#    pass

print("Estimate of number of distinct elements = %s"%(num_distinct,))

################### Part 3 ######################

var_reservoir = [0]*512
second_moment = 0
third_moment = 0

# You can use numpy.random's API for maintaining the reservoir of variables

#for word in data_stream(): # Imoplement the AMS algorithm here
#    pass 
      
print("Estimate of second moment = %s"%(second_moment,))
print("Estimate of third moment = %s"%(third_moment,))
