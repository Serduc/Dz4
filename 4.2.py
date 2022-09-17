def high_and_low(numbers):
    
    numbers = numbers.split(" ")
    
    numbers = list(map(int, numbers))
    return max(numbers), min(numbers)

print(high_and_low ('1 2 10 4 5 10 -7'))