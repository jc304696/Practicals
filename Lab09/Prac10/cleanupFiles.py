"""
CP1404/CP5632 Practical
File renaming and os examples
"""
import os, shutil

__author__ = 'Lindsay Ward'

print("Current directory is", os.getcwd())

# change to desired directory
os.chdir('Lyrics/Christmas')
# print a list of all files (test)
# print(os.listdir('.'))

# make a new directory
# os.mkdir('temp')


# loop through each file in the (original) directory
def main():

        for filename in os.listdir('.'):
            # ignore directories, just process files
            if not os.path.isdir(filename):
                new_name = get_fixed_filename(filename)
                os.rename(filename, new_name)
                print(new_name)

                # Option 1: rename file to new name - in place
                # os.rename(filename, new_name)

                # Option 2: move file to new place, with new name
                # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(name):
    fixed_name = ""
    fixed_name += name[0]

    for i in range(1,len(name)):

        if name[i] is '.':
            return fixed_name + ".txt"
        elif name[i].isupper():
            if name[i-1] is not ' ' and name[i-1].isalpha():
                fixed_name += '_'
                fixed_name += name[i]
            else:
                fixed_name += name[i]
        elif name[i] == ' ':
            fixed_name += '_'
        elif name[i-1] is ' ' or not name[i-1].isalpha():
            fixed_name += name[i].upper()
        elif name[i] is '(' :
            fixed_name += '_'
            fixed_name += name[i]
        else:
            fixed_name += name[i]



# Processing subdirectories using os.walk()
# os.chdir('..')
# for dir_name, subdir_list, file_list in os.walk('.'):
#     print("In", dir_name)
#     print("\tcontains subdirectories:", subdir_list)
#     print("\tand files:", file_list)

main()