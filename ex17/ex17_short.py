# Got it in 2 lines
from sys import argv
open(argv[2], 'w').write(open(argv[1]).read())
