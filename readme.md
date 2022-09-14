
# make bank apps work on lineageOs

bank apps / secure apps usually show an error saying device not secure or device rooted. this is because lineageOs has a small configuration error. this app will fix that.

## dependencies

- [adb](https://www.xda-developers.com/install-adb-windows-macos-linux/)
- [python3](https://www.python.org/downloads/)

## first get the phone ready

wheather you choose the automated way or you want to do it yourself you need to do the following steps first:

1- make sure to turn on usb debugging and debugging as root

2- connect phone to computer and run `adb devices` to make sure your device is connected and ready.

## 1. the automated way

1- clone repo

2- check the PathToAdb variable in the script and make sure it points to your adb executable if adb isnt added to path on your machine.

3- run the python script `automated.py`

## 2. the manual way

### pull system files

1- `adb root` to make sure we are logged in as root to access system files.

2- `adb pull /system/build.prop .` copying build.prop to our current directory.

### edit system files

1- Open the file we pulled to the current directory with the text editor of your choice.

2- Go to line 116 OR where it says `ro.debuggable=1` and change it to `ro.debuggable=0` (1 -> 0).

3- Go to line 113 and check the value of `ro.secure=1` make sure it is one.

### push the file back to its correct location

1- `adb remount` to make sure we are still mounted properly to the device.

2- `adb push .\build.prop /system/build.prop`

3- Turn off usb debugging and restart phone.
