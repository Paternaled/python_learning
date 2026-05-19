def find_min(numbers):
    smallest = float("inf")
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest 
    
"""
Finds the smallest number in a list by starting at infinity
"""
