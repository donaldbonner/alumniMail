#!/usr/bin/env python3
import os
fileName = 'input.txt'
inp = open(fileName, 'r+')
contents = inp.read().strip()
inp.close()
contents = contents.replace('[[name]]', 'Alexandria')
contents = contents.replace('[[email]]', 'aebonner@mtu.edu')
contents = contents.replace('[[number]]', '1023.24')

if os.path.isfile(fileName + '.out'):
	print('Output file exists. Deleting and creating up to date file.')

out = open(fileName + '.out', 'w')
out.write(contents + '\n')
out.close()