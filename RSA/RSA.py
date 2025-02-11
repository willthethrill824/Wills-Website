

from RSA_functions import *

def main():
    choice = input("Would you like to choose your primes y or n?:")
    if choice.lower() == "n":
        p, q = get_primes() 
        print(f"p = {p}, q = {q}")
    elif choice.lower() == "y":
        p = int(input("Enter int p: "))
        q = int(input("Enter int q: "))
    else:
        print("ERROR - assigning p and q.")
        p, q = get_primes() 
        print(f"p = {p}, q = {q}")

    #Calling Find_Public_Key_e and assigning to n, e
    n, e = Find_Public_Key_e(p, q)
    choice2 = input("Would you like to assign n,e y or n?: ")
    if choice.lower() == "y":
        n = int(input("Enter n: "))
        e = int(input("Enter e: "))
    print(f"n = {n}, e = {e}")

    #Calling Find_Private_Key_d and assigning to d
    d = Find_Private_Key_d(e, p, q)
    print(f"your private key d = {d}")

    public_key = (n, e)
    private_key = (n, d)

    print(public_key, "n(prime p * prime q), public key") 
    print(private_key, "n(prime p * prime q), private key")

    print("Enter your message here to encrypt:")
    message = input("Message : ")
    
    #Call function Encode and assign to c_text
    c_text = Encode(n, e, message)

    print(c_text)

    #Calling Decode and assigning the output to d_text
    d_text = Decode(n, d, c_text)

    print(f"Decoded message: {d_text}")



