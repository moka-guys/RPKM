# RPKM
Tools used to generate RPKM data from BAM files. Makes use of Conifer CF_bam2RPKM function to generate RPKM. Contains a wrapper script called rpkmanalysis.py which processes a list of BAMs and outputs RPKM text files to a specific output folder.

To install Conifer you will need to install the following python modules first:

pysam version '0.8.3' (pip install pysam-0.8.3)
matplotlib version '2.0.0b4'
numpy version '1.11.3'

The critical module is pysam. You need to use this version as later versions break the most recent version of conifer


Download conifer source files from http://conifer.sourceforge.net/download.html
Untar and decompress the folder and cd into the folder
  tar -xzf conifer_v0.2.tar.gz
  cd conifer_v0.2.2
  
Run conifer by simply pointing your python invocation at the conifer.py file within this folder 
