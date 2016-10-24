
def block_calculator(rows):
    if rows <= 0:
        return 0
    return rows + block_calculator(rows - 1)

print(block_calculator(6))

def repeat_string(s, n):
    """
    repeat string s, n times, with spaces in between
    """
    if n == 1:
        return s
    return s + ' ' + repeat_string(s, n - 1)


print(repeat_string('hi', 2))