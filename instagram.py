import os,platform
os.system('git pull')
 
younisxyz=platform.architecture()[0]
if younisxyz=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif younisxyz=="64bit":
    __import__("run")
 
 
 
