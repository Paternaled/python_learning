# ==========================================
# CORE LOGIC & ALGORITHMS
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


# [8] Binary String Conversion
def binary_string_to_int(num_servers, num_players, num_admins):
    """
    Parses multiple binary string inputs and converts them to base-10 integers.
    """
    server_count = int(num_servers, 2)
    player_count = int(num_players, 2)
    admin_count = int(num_admins, 2)
    
    return server_count, player_count, admin_count


# [9] Guild Permissions Engine
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    """
    Combines individual member permission bits into a single master guild superset using bitwise OR.
    """
    return glorfindel | galadriel | elendil | elrond


def get_create_bits(user_permissions):
    """
    Isolates creation permission bits using a bitwise AND mask.
    """
    return user_permissions & can_create_guild


def get_review_bits(user_permissions):
    """
    Isolates review permission bits using a bitwise AND mask.
    """
    return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
    """
    Isolates deletion permission bits using a bitwise AND mask.
    """
    return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
    """
    Isolates editing permission bits using a bitwise AND mask.
    """
    return user_permissions & can_edit_guild


# [10] Numeric Delimiter Handling
def calculate_dps(damage, time):
    """
    Calculates damage per second using clean numeric assignment metrics.
    """
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")


# [11] Recipe Cross-Matching
def check_ingredient_match(recipe, inventory):
    """
    Compares inventory sequences against a master recipe list.
    Returns the percentage met and an isolated sequence of missing requirements.
    """
    missing_ingredients = []
    matched_count = 0
    
    for ingredient in recipe:
        if ingredient in inventory:
            matched_count += 1
        else:
            missing_ingredients.append(ingredient)
            
    match_percentage = (matched_count / len(recipe)) * 100
    
    return match_percentage, missing_ingredients


# [12] Max Value Map Parsing
def get_most_common_enemy(enemies_dict):
    """
    Scans key-value dictionary records to calculate the maximum occurring flag.
    Returns the associated string identifier, tracking against negative infinity baseline.
    """
    if not enemies_dict:
        return None
        
    max_so_far = float("-inf")
    most_common = None
    
    for enemy_name, count in enemies_dict.items():
        if count > max_so_far:
            max_so_far = count
            most_common = enemy_name
            
    return most_common


# [13] Nested Key Pathway Resolution
def get_quest_status(progress_dict):
    """
    Resolves fixed data pathways within deep nested dictionary objects without loops.
    """
    return progress_dict["quests"]["bridge_run"]["status"]
    
# [14] High-Efficiency Set Difference Check
def find_missing_ids(first_ids, second_ids):
    """
    Performs high-efficiency sequence exclusions using set mathematical differences.
    Filters out duplicate results instantly via the set data structure.
    """
    set_one = set(first_ids)
    set_two = set(second_ids)
    
    return set_one - set_two

# [15] Explicit Exception Handling
def get_player_record(player_id):
    """
    Queries database records for a target player ID.
    Raises an explicit IndexError if the requested identifier does not exist.
    """
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
        
    # If we get here, the ID is invalid. We explicitly raise an error!
    raise IndexError(f"Player ID {player_id} not found in database records.")
    
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

# [8] Testing binary_string_to_int
converted_data = binary_string_to_int("100", "101", "110")
print("Binary Conversion Results:", converted_data)  # Should print: (4, 5, 6)

# [9] Testing Guild Permissions Engine
master_perms = calculate_guild_perms(0b1000, 0b0100, 0b0000, 0b0001)
print("Master Permission Superset:", bin(master_perms))  
print("Check Create Permission:", bin(get_create_bits(master_perms)))
print("Check Delete Permission:", bin(get_delete_bits(master_perms)))

# [10] Testing Numeric Delimiter Handling
print("Running DPS Calculations:")
calculate_dps(8_000_000, 45)
calculate_dps(10_000_000, 49)

# [11] Testing Recipe Cross-Matching
required_recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
current_inventory = ["Dragon Scale", "Phoenix Feather", "Troll Tusk"]
percentage, missing = check_ingredient_match(required_recipe, current_inventory)
print(f"Recipe Progress: {percentage}% | Missing items: {missing}")

# [12] Testing Max Value Map Parsing
active_enemies = {"jackal": 1, "kobold": 2, "soldier": 3, "gremlin": 5}
print("Most Dangerous Common Enemy:", get_most_common_enemy(active_enemies))

# [13] Testing Nested Key Pathway Resolution
player_progress = {
    "character_name": "Kaladin",
    "quests": {
        "bridge_run": {
            "status": "In Progress",
        },
        "talk_to_syl": {
            "status": "Completed",
        },
    },
}
print("Bridge Run Current Status:", get_quest_status(player_progress))
calculate_dps(10_000_000, 49)

# [14] Testing High-Efficiency Set Difference Check
user_ids_list_a = [101, 102, 103, 104, 105, 101, 102]  # Note the duplicate 101 and 102
user_ids_list_b = [102, 104, 106]

missing_from_b = find_missing_ids(user_ids_list_a, user_ids_list_b)
print("Missing Unique IDs:", missing_from_b)  
# Should print: {101, 103, 105}

# [15] Testing Explicit Exception Handling
print("Fetching existing profile records:")
try: 
    print(get_player_record(1))
    print(get_player_record(2))
    print(get_player_record(3))
    
    print("\nAttempting to fetch missing profile record:")
    print(get_player_record(4)) # This will trigger our IndexError
except IndexError as error_message:
    print(f"Captured Graceful Recovery: {error_message}")
