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
    


