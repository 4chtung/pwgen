#***************************************************************************
#*   pwgen - 4chtung Admin Password Generator                              *
#*   Copyright 2007-2009 by Thomas Rusbridger (4chtung)                    *
#*   4chtung@remcorp.info                                                  *
#***************************************************************************

import sys
import hashlib
import argparse

parser = argparse.ArgumentParser(prog='Password Generator')
parser = argparse.ArgumentParser(description='Input String and Salt Intergers', epilog='Helps generate unique passwords for multiple computers.')

parser.add_argument('-i', help='Input help', dest='input', required=True)
parser.add_argument('-s', help='Salt help', dest='salt')

args = parser.parse_args()

if args.salt is None:
    print hashlib.sha512(args.input.encode()).hexdigest()[:10]

else:
    print hashlib.sha512(args.input.encode() + args.salt.encode()).hexdigest()[:10]
