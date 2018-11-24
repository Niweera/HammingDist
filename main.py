import itertools
'''
=======================================
'''

size_data_word = int(input("Enter the number of bits: "))  #size_data_word bit lenght data word
#generate all numbers from 0 to 2**size_data_word
data_word_list = []
for i in range(2**size_data_word):
    data_word_list.append(i)
    
def parityOf(int_type):
    parity = 0
    while (int_type):
        parity = ~parity
        int_type = int_type & (int_type - 1)
    return(parity)

parity_check_list = []
for number in data_word_list:
    parity_check_list.append(parityOf(number))

dictionary = dict(zip(data_word_list, parity_check_list))

check_parity_list = []
for number in data_word_list:
    if dictionary[number] == 0:
        check_parity_list.append(str(bin(number)[2:].zfill(size_data_word))+"0\n")
    else:
        check_parity_list.append(str(bin(number)[2:].zfill(size_data_word))+"1\n")

iterlist = list(itertools.combinations(check_parity_list,2))

def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

dlist = []
for x in iterlist:
    dlist.append(hamming_distance(x[0],x[1]))
print(min(dlist))
