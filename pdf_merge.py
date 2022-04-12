# Ramesh Vyas
# Simple Script to merge pdf files to a single file
# USAGE python pdf_merge.py <file1> <file2> .... <fileN>
# result file : merge.pdf

from os.path import exists
from PyPDF2 import PdfFileMerger
import sys


argumentCount = len(sys.argv)
pdfs =[]

# Check atleast two files are provided in command line 
if(argumentCount>=3):

 for i in range(1,len(sys.argv)):       
    pdfs.append(sys.argv[i])
  
 
 if(len(pdfs)>0):
    merger = PdfFileMerger() 
 
 for fName in pdfs:
    merger.append(fName)   

 merger.write("merged.pdf")
 merger.close()
 print("Successfull merged files in : merged.pdf")
else:
 print ("Invalid use of tool")
 print ("USAGE python pdf_merge.py <file1>  <file2> .... <fileN>")
   
