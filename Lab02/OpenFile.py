new_file = open("name.txt", mode='w')

users_name = input("Enter your name: ")

new_file.write(users_name)

new_file.close()
