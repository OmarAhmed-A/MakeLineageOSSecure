import os

type = os.name
PathToAdb = "adb" #edit this if you dont have platform tools added to path
# pull file
os.system("{} root".format(PathToAdb))
os.system("{} pull /system/build.prop .".format(PathToAdb))

# edit file
with open('./build.prop', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

data[112] = "ro.secure=1\n"
data[115] = 'ro.debuggable=0\n'

with open('./build.prop', 'w') as file:
    file.writelines( data )

file.close()

os.system("{} remount".format(PathToAdb))
os.system("{} push ./build.prop /system/build.prop".format(PathToAdb))
os.system("{} shell reboot".format(PathToAdb))

# clean up
if type == 'posix':
    os.system("rm ./build.prop")
else:
    os.system("del build.prop")

print("You're all done!!")