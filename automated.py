import os


PathToAdb = "adb" #edit this if you dont have platform tools added to path
# pull file
os.system("%s root", PathToAdb)
os.system("%s pull /system/build.prop .", PathToAdb)

# edit file
with open('./build.prop', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

data[112] = "ro.secure=1\n"
data[115] = 'ro.debuggable=0\n'

with open('./build.prop', 'w') as file:
    file.writelines( data )

file.close()

os.system("%s push ./build.prop /system/build.prop", PathToAdb)
os.system("%s shell reboot", PathToAdb)

# clean up
os.system("rm ./build.prop")

print("You're all done!!")