numbers = [3, 1, 4, 1, 5, 9, 2]

# First set of warm-up question
print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
y = "3" in numbers
print(y)
x = numbers + [6, 5, 3]
print(x)

# Question 1
numbers[0] = "ten"
print(numbers)

# Question 2
numbers[-1] = 1
print(numbers)

# Question 3
z = numbers[2:]
print(z)

# Question 4
print(9 in numbers)
