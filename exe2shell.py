import sys, os

if len(sys.argv) < 2:
    print 'usage: ' + sys.argv[0] + ' file.exe\n'
    sys.exit(0)

shellcode = ''
bytes = 0

for b in open(sys.argv[1], 'rb').read():
    shellcode += '\\x' + b.encode('hex')
    bytes += 1

print 'Number of bytes for file ' + sys.argv[1] + ': ' + str(bytes) + '\n'

fp=open("shell.txt", "w")
fp.write(shellcode)
fp.close()

print "Done!"
