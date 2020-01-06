

types_of_people = 10
# giving a value to the "types_of_people" a number variable
x = f"There are {types_of_people} types of people."
# giving to the x variable a string with the "types_of_people" variable
binary = "binary"  #assining to the "binary" variable a string
do_not = "don't"   #assining to the "do_not" variable a string
y = f"Those who know {binary} and those who {do_not}."
# assining to the y variable a string containing the two other variable
print(x) #asking to print out x
print(y) #asking to print out y

print(f"I said: {x}")  #asking to print out x with an additional part
print(f"I also said: '{y}'") #asking to print out y with an additional part at the start

hilarious = False #creating a boolena variable named "hilarious" that is set as False

joke_evaluation = "Isn't that joke so funny?! {}"  #creating the string type variable

print(joke_evaluation.format(hilarious)) # printing out the "joke_evaluation" variable and printing out the "hilarious" value formatting
                                        # it in a string


w = "This is the left side of..."      # two other string type variables
e = "a string with a right side."

print(w + e)  #asking to print out a long string by adding two string variables together
