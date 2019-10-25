r"""Decrypt a Civil War 'rail fence' type cipher.

This is for a "2-rail" fence cipher for short messages

Example plaintext:  'Buy more Maine potatoes'

Rail fence style:  B Y O E A N P T T E 
                    U M R M I E O A O S

Read zig-zag:      \/\/\/\/\/\/\/\/\/\/

Ciphertext:  BYOEA NPTTE UMRMI EOSOS 

"""
import math
import itertools

#------------------------------------------------------------------------------
# USER INPUT:

# the string to be decrypted (paste between quotes):
ciphertext = """LTSRS OETEI EADET NETEH DOTER EEUCO SVRHR VRNRS UDRHS AEFHT ES

"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------




def main():
    """Run program to decrypt 2-rail rail fence cipher."""
    message = prep_ciphertext(ciphertext)
    row1, row2 = split_rails(message)
    decrypt(row1, row2)
    
def prep_ciphertext(ciphertext):
    """Remove whitespace."""
    message = "".join(ciphertext.split())
    print("\nciphertext = {}".format(ciphertext))
    return message

def split_rails(message):
    """Split message in two, always rounding UP for 1st row."""
    row_1_len = math.ceil(len(message)/2)
    row1 = (message[:row_1_len]).lower()
    row2 = (message[row_1_len:]).lower()
    return row1, row2

def decrypt(row1, row2):
    """Build list with every other letter in 2 strings & print."""
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1)
        plaintext.append(r2)
    if None in plaintext:
        plaintext.pop()
    print("rail 1 = {}".format(row1))
    print("rail 2 = {}".format(row2))
    print("\nplaintext = {}".format(''.join(plaintext)))

if __name__ == '__main__':
    main()
