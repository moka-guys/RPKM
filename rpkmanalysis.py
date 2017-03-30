#!/usr/bin/python

from conifer import *
import sys, os
import argparse, subprocess
"""
Run rpkmanalysis.py as

python rpkmanaysis.py 	--bamlist <path to folder containing input bams> \
						--output <path to folder containing outputted text files containing RPKM data> \
						--probes <path to bed file containing regions used for RPKM analysis
"""

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Bamprocess(object):

	def RPKM(self, args):
		# Loop through the bam files in the input folder
		for file in os.listdir(args.bamlist):
			if file.endswith(".bam"):
				# Generate the output file for the given input file (removes bam extension and replaces it with txt)
				output = os.path.join(args.output, '') + os.path.splitext(file)[0] + ".txt"
				# Redefine the variable file so that it has the appropriate file path
				file = args.bamlist + file
				# define the namespace object which acts as an argument for conifer
				vals=Namespace(input=[file], output=[output], probes=[args.probes])
				# Call the conifer function CF_bam2RPKM which defines RPKM values for each bam file
				CF_bam2RPKM(vals)

		self.summary(output=os.path.join(args.output, ''))

	def summary(self, output):
		# change directory to where outputted files are located
		os.chdir(output)
		# Bash script to append all the relevant columns from the outputted files.
		cmd = """paste $(ls *deduplicated.txt) | awk 'BEGIN {FS=\"\t\"} {for(i=4;i<=NF;i+=4) {printf "%s ",$i}; print \"\"}'"""
		with open("summary.txt", "w") as f:
			subprocess.call(cmd, shell=True, stdout=f)
		# Add header to file
		subprocess.call("""sed -i "1i $(ls *deduplicated.txt | tr '\n' ' ')" summary.txt""", shell=True)
				

if __name__=="__main__":
	# Instantiate the class
	bamprocess = Bamprocess()
	#Tranlste command line inputs using argparse. Generate an argparse object which relates a set of arguments from a programme (i.e. rpkmanalysis.py) and relates it to a function (i.e. Bamprocess().RPKM()) 
	parser = argparse.ArgumentParser(prog="rpkmanalysis", description="This is a wrapper script for utilising the RPKM function CF_bam2RPKM from conifer.py")
	# Adde expected arguments
	parser.add_argument('--bamlist', help='provide path to the list of bam files for RPKM analysis')
	parser.add_argument('--output', help='provide path to output folder for data')
	parser.add_argument('--probes', help='provide path to probes bed file')

	# Define the function to apply the above arguments to eg. args.bamlist becomes a variable in bamprocess.RPKM
	parser.set_defaults(func=bamprocess.RPKM)
	# Assign the argparse object to a variable (args is essentially holding a dictionary of values)
	args = parser.parse_args()
	print args
	# Call the assigned function with the args variable as the argument
	args.func(args)
	#bamprocess.summary(output="/home/kevin/Documents/RPKManalysis/output")


	
