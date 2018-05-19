"""Load a dictionary file as a list.

Arguments:
-dictionary file name

Exceptions:
-IOError

-Requires import sys

"""
   
import sys
    
def load(filename):
    """Open dict text file, check for errors, & make word list."""
    try:
        with open(filename) as my_file:
            my_list = my_file.read().strip().split('\n')
            my_list = [x.lower() for x in my_list]
            return my_list
    except IOError as e:
        print("Error opening {}.\n Terminating program {}.".format(filename, e),
              file=sys.stderr)
        sys.exit(1)
