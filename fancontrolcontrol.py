#!/usr/bin/env python

import glob
import sys
import getopt
import re
import pathlib

def main(argv):
	inputfile = ''
	outputfile = ''
	hwmondir = ''
	hwmonpattern = re.compile('hwmon([0-9])', re.IGNORECASE)

	try:
		opts, args = getopt.getopt(argv,'hi:o:m:', ['ifile=', 'ofile=', 'mondir='])
	except getopt.GetoptError:
		print('fancontrolcontrol.py -i <inputfile> -o <outputfile> -m <hwmondir>')
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			print('fancontrolcontrol.py -i <inputfile> -o <outputfile> -m <hwmondir>')
			sys.exit()
		elif opt in ('-i', '--ifile'):
			inputfile = arg
		elif opt in ('-o', '--ofile'):
			outputfile = arg
		elif opt in ('-m', '--mondir'):
			hwmondir = arg

	if inputfile == '' or outputfile == '' or hwmondir == '':
		print('must have i o and m options')
		sys.exit(2)

	hwmons = glob.glob('/sys/class/hwmon/hwmon*/name')
	hwmonnums = {}
	for h in hwmons:
		i = 'hwmon' + hwmonpattern.search(h).group(1)
		h2 = '{' + pathlib.Path(h).read_text().strip() + '}'
		hwmonnums[h2] = i
		#i += 1

	#print(hwmonnums)
	#print('')

	ifile = open(inputfile, 'rt')
	ofile = open(outputfile, 'wt')
	while True :
		line = ifile.readline()
		if line == '':
			break

		for (num, repl) in hwmonnums.items():
			line = line.replace(num, repl)

		ofile.write(line)
		#print(line)

	ifile.close()
	ofile.close()

if __name__ == "__main__":
	main(sys.argv[1:])
