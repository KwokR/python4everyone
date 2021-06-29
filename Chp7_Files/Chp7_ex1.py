"""
Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in upper case.
Executing the program will look as follows:

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN  5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
     BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
     SAT, 05 JAN 2008 09:14:16 -0500
"""
fname = input('Enter a file name: ')
try:
    fhandle = open(fname, 'r')
except:
    print(fname, ' does not exist')
    quit()
line_no = 0
for line in fhandle:
    line = line.rstrip().upper()
    if line_no > 4:
        break
    print(line)
    line_no += 1
