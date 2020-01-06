from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")

print("If you don't want that, hit CTRL-C (^C).")

print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

target = open(filename, 'w')

print("Truncating the file. Goodbye!")

target.truncate()  #unneccesary because of the "w" in open command

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")

line2 = input("line 2: ")

line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.writelines(line1, line2, line3) #using one command for writing alla the lines

print("And finally, we close it.")


"""------------------------print file -------------------------


print(f"Here's your file {filename}:")  # print out the script with the filename varieble

print(target.read())      # print out the content of the file

------------------------------------------------------------------
"""

target.close()
