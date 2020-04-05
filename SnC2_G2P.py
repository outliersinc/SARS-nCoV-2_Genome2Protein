#! usr/bin/env python3.7

import sys
import fileinput

# Python3.7 Script that takes a file from command line arguments prints the output to Standard Out.
# First Written on April 4, 2020

# Welcome to SARS-nCoV-2 genome to protein converter.

# Add the SARS_NCov_2 genome file to a variable.
genome_File = sys.argv[1]
print("The genome file argument is " + genome_File)


# Open the genome file via the variable.
open_genome_File = open(genome_File)

# Loop through the genome file and store in String.
lines_dnaSeq = dnaSequence.readlines()
dnaSeqStr = ""

countProteins = 0

# Loop through the string and look for start codon ATG. Once a start codon is
# found loop until you find the Stop Codon (TAG, TAA, TGA). Than print the whole sequence to file or standard out.
# HINT: Check if the coding region is divisible by %3 = 0 to ensure coding region is cds.
for lined_dnaSeq in lines_dnaSeq:
	for charSeq in lined_dnaSeq:


# Get the Genome length for statistics.
genomeLength = len(dnaSeqStr)

# genomeLength%3 = is the genome divisible by 3.

# while index < seqLength:
#	index += 1

# Print out interesting genome facts.
print("The genome length is {0}.".format(genomeLength))

# Close files to end program
open_genome_File.close()
