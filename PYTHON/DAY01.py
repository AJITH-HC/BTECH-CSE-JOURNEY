'''name = input("Enter your name: ")

numbers = [10, 20, 30, 40, 50]

print("Welcome,", name)
print("Total:", sum(numbers))
print("First three elements:", numbers[:3])'''
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Total:", total)