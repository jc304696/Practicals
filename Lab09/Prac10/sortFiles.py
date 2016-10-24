import os, shutil


def main():
    print("Current directory is", os.getcwd())
    os.chdir("./FilesToSort")

    dir = {}

    for filename in os.listdir('.'):
        if not os.path.isdir(filename):
            extension = filename.split('.')[-1]
            if extension not in dir:
                directory = input("What category would you like to sort {} files into?".format(extension))
                dir[extension] = directory

                if not os.path.exists(directory):
                    os.mkdir(directory)

            shutil.move(filename, dir.get(extension) + '/' + filename)

main()
