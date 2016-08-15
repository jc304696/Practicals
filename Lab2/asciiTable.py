lower = 10
upper = 100

print("Enter a number ({0} - {1}):".format(lower,upper))

for i in range(32, 127, 1):
    character = chr(i)
    print("Number {0:>3} is '{1:>2}' in ASCII".format(i, character))
