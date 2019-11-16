import shutil
import os
import time
from watchdog.events import FileSystemEventHandler as eh
from watchdog.observers import Observer

# Source is file area the program will check
# Dest is file area the program will send to
source = "C:\\Users\\username\\source"
dest = "C:\\Users\\username\\Desktop\\dest"
defaultdest = dest

# Add more file types here
extensions = {
    '.txt': str(defaultdest) + '\\text',
    '.pptx': str(defaultdest) + '\\ppt',
    '.ppt': str(defaultdest) + '\\ppt',
    '.pdf': str(defaultdest) + '\\pdf',
    '.png': str(defaultdest) + '\\images',
    '.PNG': str(defaultdest) + '\\images',
    '.jpg': str(defaultdest) + '\\images',
    '.jfif': str(defaultdest) + '\\images',
    '.xlsx': str(defaultdest) + '\\excel',
    '.doc': str(defaultdest) + '\\docs',
    '.docx': str(defaultdest) + '\\docs',
}


def doggodoggo():
    for file in os.listdir(source):
        # print(file)
        if os.path.isfile(source + '\\' + file):

            # Find the extension, to determine destination
            # if file extension is not in extensions, use default dest
            extension = os.path.splitext(file)[1]
            if extension in extensions:
                dest = extensions[extension]
            else:
                dest = defaultdest

            # set name as file, as we may need to change name of the file
            newName = file

            # boolean variable to check if our newName is already
            # in destination
            destExistFile = os.path.isfile(dest + '\\' + newName)

            # Start check, append _# until newName is a unique name
            i = 1
            while destExistFile:
                i += 1

                newName = os.path.splitext(file)[0] + str('_') + \
                    str(i) + os.path.splitext(file)[1]
                destExistFile = os.path.isfile(dest + '\\' + newName)

            # if newName is not equal to file, rename the file to move
            if newName != file:
                os.rename(source + '\\' + file, source + '\\' + newName)

            # Check if the destination folder has already been created
            # if not, create it
            if (not os.path.isdir(dest)) and dest != defaultdest:
                os.makedirs(dest)
            # move file
            shutil.move(source + "\\" + newName, dest)


if __name__ == '__main__':
    doggodoggo()
