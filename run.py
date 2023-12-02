import os, sys
os.system("git pull")
try:
    __import__("INSTA").YounisXyzInsta()
except Exception as e:
    exit(str(e))
 
