import sys
import hashlib
import argparse

parser = argparse.ArgumentParser(prog='Password Generator')
parser = argparse.ArgumentParser(description='Password and Salt Intergers', epilog='Helps generate unique passwords for multiple computers.')

parser.add_argument('-p', help='Password help', dest='password', required=True)
parser.add_argument('-s', help='Salt help', dest='salt')

args = parser.parse_args()

if args.salt is None:
    print hashlib.sha512(args.password.encode()).hexdigest()[:10]

else:
    print hashlib.sha512(args.password.encode() + args.salt.encode()).hexdigest()[:10]
