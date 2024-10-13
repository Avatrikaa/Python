def apply_operation(numbers, operation):
    return [operation(number) for number in numbers]

numbers1 = [1,2,3,4,5]
doubled = apply_operation(numbers1, lambda x: 2*x)
squared = apply_operation(numbers1, lambda x: pow(x, 2))
filtered = apply_operation(numbers1, lambda x: x if x % 2 != 0 else None)
filtered = [x for x in filtered if x is not None]

print(doubled)
print(squared)
print(filtered)

