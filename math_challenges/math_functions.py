def area_sum(rectangles):
    """
    Calculates the total combined area of a list of rectangles.
    Each rectangle is represented as a dictionary with 'height' and 'width'.
    """
    area_sum = 0
    for i in range(0, len(rectangles)):
        area = rectangles[i]["height"] * rectangles[i]["width"]
        area_sum += area
    return area_sum

def find_min(numbers):
    """
    Finds the smallest number in a list by starting at infinity.
    """
    smallest = float("inf")
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest 

def factorial(num):
    """
    Calculates the factorial of a given number.
    """
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def remove_nonints(nums):
    """
    Takes a list and returns a new list with all non-integer types removed.
    """
    int_list = []
    for item in nums:
        if type(item) == int:
            int_list.append(item)
    return int_list
    
def number_sum(n):
    """
    Calculates the sum of all numbers from 0 up to and including n.
    """
    count = 0
    for i in range(0, n + 1):
        count += i
    return count

# ==========================================
# TEST CASES
# ==========================================

# 1. Testing area_sum
my_rectangles = [
    {"height": 5, "width": 10},  # Area: 50
    {"height": 2, "width": 4}    # Area: 8
]
print("Rectangle Area Sum:", area_sum(my_rectangles))  # Prints: 58 

# 2. Testing find_min
my_numbers = [14, 5, 82, 3, 22]
print("Smallest Number Implemented:", find_min(my_numbers))  # Prints: 3
    
# 3. Testing factorial
print("Factorial of 5:", factorial(5))  # Should print: 120

# 4. Testing remove_nonints
mixed_list = ["1", 1, "3", "400", 4, 500, "Alien"]
print("Cleaned Integers:", remove_nonints(mixed_list))  # Should print: [1, 4, 500]

# 5. Testing number_sum
print("Sum of numbers up to 5:", number_sum(5))  # Should print: 15 (1+2+3+4+5)

