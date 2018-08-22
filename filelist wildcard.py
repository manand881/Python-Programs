# Make file lists from current directory using a wildcard

import glob
file_list = glob.glob('*.*')
print(file_list)

# glob — Unix style pathname pattern expansion. The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell, although results are returned in arbitrary order. No tilde expansion is done, but * , ? , and character ranges expressed with [] will be correctly matched.
