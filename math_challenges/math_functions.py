# ==========================================
# CORE FUNCTIONS & DECORATORS
# ==========================================

# [Decorator Setup]
def universal_zero_guard(any_function):
    """
    An outer setup function that runs once at load-time to wrap target functions.
    """
    def wrapper(*args, **kwargs):
        if 0 in args or 0 in kwargs.values():
            print("Universal Security Notice: Operation blocked. Cannot divide by zero.")
            return []
            
        return any_function(*args, **kwargs)
        
    return wrapper


# [1] Area Sum
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


# [2] Find Minimum
def find_min(numbers):
    """
    Finds the smallest number in a list by starting at infinity.
    """
    smallest = float("inf")
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest 


# [3] Factorial
def factorial(num):
    """
    Calculates the factorial of a given number.
    """
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


# [4] Remove Non-Integers
def remove_nonints(nums):
    """
    Takes a list and returns a new list with all non-integer types removed.
    """
    int_list = []
    for item in nums:
        if type(item) == int:
            int_list.append(item)
    return int_list
    


# [5] Number Sum Progression
def number_sum(n):
    """
    Calculates the sum of all numbers from 0 up to and including n.
    """
    count = 0
    for i in range(0, n + 1):
        count += i
    return count


# [6] Divide List (Protected)
@universal_zero_guard
def divide_list(nums, divisor):
    """
    Takes a list of numbers and divides each element by the divisor.
    Protected against ZeroDivisionError via the @universal_zero_guard decorator.
    """
    divided_list = []
    
    for num in nums:
        divided_list.append(num / divisor)
        
    return divided_list


# [7] Filter Messages
def filter_messages(messages):
    """
    Tokenizes raw text strings to isolate and filter specific profanity terms.
    Tracks filtered outputs and log counts simultaneously using parallel sequences.
    """
    filtered_messages = []
    dang_count = []
    
    for message in messages:
        message = message.split()
        filtered_message = []
        counter = 0
        
        for word in message:
            if word == "dang":
                counter += 1
            else: 
                filtered_message.append(word)
                
        filtered_message = " ".join(filtered_message)
        filtered_messages.append(filtered_message)
        dang_count.append(counter)
        
    return filtered_messages, dang_count


# ==========================================
# TEST CASES
# ==========================================

# [1] Testing area_sum
my_rectangles = [
    {"height": 5, "width": 10},  # Area: 50
    {"height": 2, "width": 4}    # Area: 8
]
print("Rectangle Area Sum:", area_sum(my_rectangles))  # Prints: 58 

# [2] Testing find_min
my_numbers = [14, 5, 82, 3, 22]
print("Smallest Number Implemented:", find_min(my_numbers))  # Prints: 3
    
# [3] Testing factorial
print("Factorial of 5:", factorial(5))  # Should print: 120

# [4] Testing remove_nonints
mixed_list = ["1", 1, "3", "400", 4, 500, "Alien"]
print("Cleaned Integers:", remove_nonints(mixed_list))  # Should print: [1, 4, 500]

# [5] Testing number_sum
print("Sum of numbers up to 5:", number_sum(5))  # Should print: 15 (1+2+3+4+5)

# [6] Testing divide_list
numbers_to_divide = [10, 20, 30, 45]
print("Divided by 5:", divide_list(numbers_to_divide, 5))  # Should print: [2.0, 4.0, 6.0, 9.0]
print("Divided by 0:", divide_list(numbers_to_divide, 0))  # Should print security warning and: []

# [7] Testing filter_messages
chat_logs = [
    "That was a dang good game",
    "Stop it, you are being a dang nuisance",
    "Clean message with no issues"
]

clean_chats, telemetry = filter_messages(chat_logs)
print("Filtered Chats:", clean_chats)
print("Profanity Counts:", telemetry)
