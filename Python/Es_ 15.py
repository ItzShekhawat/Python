from sys import argv

script, filename = argv #two variables of args types

txt = open(filename)    #command to open the file(txt) in the code

print(f"Here's your file {filename}:")  # print out the script with the filename varieble

print(txt.read())      # print out the content of the file

print("Type the filename again:")       # asking for the file name script

file_again = input("> ")  # command for getting script form user LIVE


txt_again = open(file_again)  # opening the file content in the new variable "txt_again"

print(txt_again.read())     # printing the content in the "txt_again" variable


""" ----------------Only input-----------------------------------------------------------
print("Type the filename again:")       # asking for the file name script

file_again = input("> ")  # command for getting script form user LIVE


txt_again = open(file_again)  # opening the file content in the new variable "txt_again"

print(txt_again.read())     # printing the content in the "txt_again" variable

"""

txt_again.close(filename)
