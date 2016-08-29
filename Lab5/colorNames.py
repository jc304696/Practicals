COLOR_NAMES = {"ALICEBLUE": "#f0f8ff", "AQUAMARINE1": "#7fffd4", "AZURE1": "#f0ffff", "BEIGE": "#f5f5dc", "BLUE": "#0000ff", "BROWN": "#a52a2a"}

color = input("enter a color: ").upper()
while color != '':
    key = color.replace(" ", "")
    if key in COLOR_NAMES:
        print("{0} is {1})".format(color.title(),COLOR_NAMES[key]))
    else:
        print("color wasn't found")
    color = input("enter a color: ").upper()
