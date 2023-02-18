#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



random_elements = []
#using for loops to generate random elements and adding them together as a list
for element in range(nr_letters):
    random_elements.extend(random.sample(letters, 1))
    
for element in range(nr_numbers):
 random_elements.extend(random.sample(numbers, 1))

for element in range(nr_symbols):
  random_elements.extend(random.sample(symbols, 1))

print(random_elements)

#creating a string for storing the randomized password
randomized_password = ""
#using for loop to randomly arrange the elements to form a password
for i in range(len(random_elements)):
  element = random.choice(random_elements)
  randomized_password += element
  random_elements.remove(element)

print(randomized_password)
