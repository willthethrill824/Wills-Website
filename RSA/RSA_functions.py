# This file holds all of the necessary functions needed for the RSA Demo

def Convert_Binary_String(_int):
    """
    function that converts an integer to a string of its binary expansion. 
        
    For example:
    _int = 345
    bits = 101011001
    """
    return bin(_int)[2:]

def Lookup_Table(b, bin_str,m):
    """Returns table in format (index, respective index power remainder)
        each index corresponds to the power of 2 : 0 = 0, 1 = 1, 2 = 2, 3 = 4, 4 = 8...
        each key corresponds to the remainder ie b^pwr mod m
    """
    pow = 0
    bin_dict = {}
    for i in range(0, len(bin_str) + 1 ):                   # Iterate through binary string length 
        if pow == 0:                                        # -- Power = 0 --
            this_mod = 1 % m                                # Set this mod to 1 % m
            pow += 1                                        # Increments power to 1
        elif pow == 1:                                      # -- Power = 1 --
            this_mod = b % m                                # Set this mod to b % m which is same as b^1
            pow = pow * 2                                   # Increase power by a power of 2 so 1 * 2 = 2
        else:                                                   
            this_mod = (bin_dict[i - 1] * bin_dict[i-1]) % m    #Uses mod formula by using past index mod value to calculate this one
            pow = pow * 2                                       #Increases Power -- used to test function
        
        bin_dict[i] = this_mod                              # Assign this key of dictionary to current mod
    return(bin_dict)

def FME(b, n, m):
    """
    This function calculates the remainder for number b raised to n mod m
      
    """
    
    this_pwr = Convert_Binary_String(n)                 #Translates n into binary string

    #Create square and mod table to use as reference - each index is that number raised to corresponding power mod m
    this_table = Lookup_Table(b, this_pwr, m) 

    bin_num= []                                         #Initialize list to reverse order of binary number, needed to index lsb first
    for char in this_pwr:                               #For loop to reverse order of binary number
        bin_num.insert(0,char)
    
    product = 1                                         #Initialize product at 1 

    for i in range(len(this_pwr)):                      #Loop through length of binary version of n 
        if int(bin_num[i]) == 1:                        #If there is a 1 at index i then :
            product = product * this_table[i+1]         #Generate new product from known mod value
    result = product % m                                #Calculate final mod and store in variable result

    return(result)

def Euclidean_Alg(a, b):
    """
    This function returns a single integer which is the gcd of a and b
    
    """
    if (a >= 0 and b >= 0):
        
        while (b > 0):           #Iterate Euclid algorithm while n > 0
            k = a % b               #Calculate current remainder
            
            a = b                   #update new value of m
            b = k                   #update new value of n
            
        return a                    #return remainder
    else:
        return 0

def EEA(m, n):
    """
    This version will return both: 
    1. the GCD of a, b 
    2. Bezout's coefficients in any form you wish. We recommend returning your coefficients as a list or a tuple. 
    Form: GCD, (s1, t1)
    """
    m0, n0 = m, n
    l = [m, n]
    m = max(l)
    n = min(l)
    if (m >= 0 and n >= 0):
        s1, t1 = 1, 0                                   #Initialize (s1, t1) to (1, 0)
        s2, t2 = 0, 1                                   #Initialize (s2, t2) to (0, 1)
        while (n > 0):                                  #Iterate Euclid algorithm while n > 0
            k = m % n                                   #Calculate current remainder
            q = m // n                                  #Calculate current int division
            m = n                                       #update new value of m
            n = k                                       #update new value of n
            s1_h, t1_h = s2, t2                         #Updating s1,t1
            s2_h, t2_h = (s1 - q * s2), (t1 - q * t2)   #calculating s2,t2 for next iteration
            s1, t1 = s1_h, t1_h                         #Updating s1,t1 as previous s2,t2
            s2, t2 = s2_h, t2_h                         #updating s2,t2 as calculation
        if (((m0 * s1) + (n0 * t1)) != m):
            temp = s1
            s1 = t1
            t1 = temp
        return m, s1, t1                                #return remainder, and s, t
    else:
        return 0, 0, 0

def Find_Public_Key_e(p, q):
    """
    Input: 2 primes p and q.
    
    Output:
    public key: n
    public key: e
    
    """
    n = p * q
    sub = (p - 1) * (q - 1)
    e_tries = [2, 3, 5, 7]                  # Initialize e_tries small primes, small primes are unsecure

    e = 65537                               # Start with the common public exponent

    # Check if 65537 is a valid public exponent
    if Euclidean_Alg(sub, e) == 1 and e != p and e != q:
        return n, e

    # If 65537 is not valid, find anothersuitable prime
    # Start from the next prime after the largest in e_tries
    e = max(e_tries) + 2  # Start from a larger odd number than the largest in e_tries

    while Euclidean_Alg(sub, e) != 1 or e == p or e == q:
        e += 2                              # Increment e by 2 to skip even numbers

        # Check if e is already in e_tries; if not, check for divisibility
        if e not in e_tries:
            if not any(e % num == 0 for num in e_tries):
                e_tries.append(e)

    return n, e

def Find_Private_Key_d(e, p, q):
    """
    Input: e(public key), p and q such that gcd(e,p*q) = 1
    Output: d(private key) that is modular inverse of e. 

    """
    sub = (p-1)*(q-1)                               #Assign sub to save space         
    gcd, d, t = EEA(e, sub)                         #Use EEA to get gcd, s, t
    if (d < 0):                                     #We want d to be positive
        d = d + (sub)                               #Increment by sub
        t = (1 - (d * e)) / (sub)                   #Recalculate T (for testing)
    return d

def Convert_Text(_string):
    """
    Input: string
    Output: ASCII lsit of each letter

    For example:
    _string = hello
    integer_list = [104, 101, 108, 108, 111]
    
    """
    alphabet = list(map(chr, range(32, 127)))       #Creates list with lowercase letters 
    a_code = {}                                     #Initialize dictionary for each letter
    for item in alphabet:                           #Loop through list and add them to dict
        a_code[item] = ord(item)                    #Assigning statement for key: value
                         

    encode = []                                     #Initialize empty list for encoded message

    for char in _string:                            #loop to iterate through characters in string
        if char in a_code.keys():                   #check to see if char is in the letters
            # print(f"{char} is in a_code")
            encode.append(a_code[char])
    integer_list = encode
    return integer_list

def Convert_Num(_list):
    """
    Input: list of integers
    Outputs: the corresponding string (ascii).
    
    For example:
    _list = [104, 101, 108, 108, 111]
    _string = hello
    """
   
    _string = ''                                    #Initializes empty string
    for i in _list:                                 #Iterate through item in _list
        _string += chr(i)                           #Concatenate string with character 
    return _string                                      # corresponding with each number

def Encode(n, e, message):
    """
    Here, the message will be a string of characters.
    Use the function Convert_Text from 
    the basic tool set and get a list of numbers.
    
    Encode each of these numbers using n and e and
    return the encoded cipher_text.
    """
    cipher_text = []                                #Initialize list
    message_list = Convert_Text(message)            #Uses Convert text to get list of ascii ints
    for item in message_list:                       #Iterate throuhg each number in message list
        value = FME(item, e, n)                     #Assigns item**e mod n to value
        cipher_text.append(value)                   #Appends value to end of cipher text list
    return cipher_text

def Decode(n, d, cipher_text):
    """
    Here, the cipher_text will be a list of integers.
    First, you will decrypt each of those integers using 
    n and d.
    
    Later, you will need to use the function Convert_Num from the 
    basic toolset to recover the original message as a string. 
    
    """
    d_list = []                                     #Initialize list
    for item in cipher_text:                        #Iterate through each item in cypher_text
        value = FME(item, d, n)                     #Assign item**d mod n to value
        d_list.append(value)                        #Append value to end of d_list
    
    message = ''                                    #Initialize message as empty string
    message = Convert_Num(d_list)                   #Assign message as string form of d_list
    return message

import random
from sympy import randprime

def get_primes():
                                                    # Define a range for moderately large primes
    lower_bound = 100                               # Start above 11
    upper_bound = 1000                              # Can be adjusted for larger primes
    
    # Generate two distinct prime numbers
    p = randprime(lower_bound, upper_bound)
    q = randprime(lower_bound, upper_bound)
    
    
    while p == q:                                     # Ensure that p and q are not the same
        q = randprime(lower_bound, upper_bound)
    
    return p, q

def factorize(n):
    for i in range(2, n):
        if n % i == 0:
            return i
    return False

# go to RSA.py