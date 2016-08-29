
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}

for key in STATE_NAMES:
    print("{0:4} is {1}".format(key,STATE_NAMES[key]))
print('\n\n')

for key, name in STATE_NAMES.items():
    print(key + ' is ' + name)