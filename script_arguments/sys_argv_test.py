import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print ('Argument 0:', str(sys.argv[0])) # the script name
if len(sys.argv) > 1:
    print ('Argument 1:', str(sys.argv[1])) #