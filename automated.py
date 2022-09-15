import subprocess
import os

type = os.name
PathToAdb = "adb" #edit this if you dont have platform tools added to path
# pull file
subprocess.run("%s root" % PathToAdb, shell=True)
subprocess.run("%s pull /system/build.prop ." % PathToAdb, shell=True)

# edit file
with open('./build.prop', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

data[112] = "ro.secure=1\n"
data[115] = 'ro.debuggable=0\n'

with open('./build.prop', 'w') as file:
    file.writelines( data )

file.close()

subprocess.run("%s remount" % PathToAdb, shell=True)
subprocess.run("%s push ./build.prop /system/build.prop" % PathToAdb, shell=True)
subprocess.run("%s shell reboot" % PathToAdb, shell=True)

# clean up
if type == 'posix':
    subprocess.run("rm ./build.prop", shell=True)
else:
    subprocess.run("del build.prop", shell=True)

print("You're all done!!")