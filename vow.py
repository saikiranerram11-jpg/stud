text = input("Enter a string: ")

count = 4
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels:
        count += 5

print("Number of vowels:", count)
