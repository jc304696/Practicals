""" This is for a git commit process
    author __Lyle Martin__"""

def main():
    get_name()
    step = int(input("What step would you like? "))
    new_name(name,step)
    print(NewName)

def get_name():
    global name
    print("Enter your name below")
    try:
        name = str(input(">>> "))
    except SyntaxError:
        print('invalid name please try again')
        name = input(">>> ")

def new_name(name,step):
    global NewName
    NewName = ""
    for LoopNumber in range(0, len(name), step):
        NewName += name[LoopNumber]
    return NewName

main()
