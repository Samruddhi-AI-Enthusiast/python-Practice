numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Without duplicates:", unique_numbers)