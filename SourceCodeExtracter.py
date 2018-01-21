#Nikhil Amin -:- https://github.com/nikhilamin073
#Python Script to extract source code of the entered URL to a text file.

import urllib

url = raw_input("\nEnter a URL to extract source code: ")
type(url)						#user input for URL

ofile = raw_input("\nEnter a Output filename to save the extracted source code (.txt recommended): ")
type(ofile)						#user input for output file name

urllib.urlretrieve(url, ofile)  			#using urlretrieve to extract source code and store it in a file.

print ("\nSource code of '" + url + "' has been sucessfully stored in '" + ofile + "' file.")
