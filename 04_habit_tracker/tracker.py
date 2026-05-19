# keeps program running

while True: 

# player info from files (if loading fails, player info set to none)
    
    try:
        with open("data.txt", "r") as f:
            xp = int(f.read())
    except:
        xp = 0

    try:
        with open("habit.txt", "r") as f:
            habits = [line.strip() for line in f]
    except:
        habits = []

    try: 
        with open("streak.txt", "r") as f:
            streak = int(f.readline().strip())
            last_date = f.readline().strip()
    except: 
        streak = 0
        last_date = ""

    try: 
        with open("longest_streak.txt", "r") as f:
            longest_streak = int(f.read().strip()) 
    except:
            longest_streak = 0

    try:
        with open("habit_stats.txt", "r") as f:
            habit_stats = {}
            for line in f:
                name, done, skipped = line.strip().split(",")
                habit_stats[name] = [int(done), int(skipped)]
    except:
        habit_stats = {}

    level = xp // 100 + 1
    perk_all_complete_bonus = (level >= 2)

# prints menu options, xp, and habits (then takes input for menu selection)

    print("Current Level: ", level)
    print("\nCurrent XP: ", xp) 
    print("Your Habits: ", habits)

    if streak > 1:
        print(f"Streak: {streak} days") 

    print("\nWhat would you like to do?")
    print("1. Complete Habits")
    print("2. Add a habit")
    print("3. Remove a habit")
    print("4. Quit")
    print("5. Reset XP")
    print("6. Player Info")

    choice = input("Choose an option: ")

# option 1: complete habits and checks for streak

    if choice == "1":
        completed = []
    
        for h in habits:
            if h not in habit_stats:
                habit_stats[h] = [0, 0] # auto creates missing stats
            done = input(f"Did you complete {h}? (yes/no) ")
            if done.lower() == "yes":
                completed.append(h)
                xp += 10
                habit_stats[h][0] += 1 # completed count
            else:
                habit_stats[h][1] += 1 # skipped count

        if len(completed) == len(habits) and len(habits) > 0:
            print("You completed all habits! Bonus 50XP")
            xp += 50
            if perk_all_complete_bonus:
                xp += 5
                print("Perk Bonus: +5 XP for completing all habits!")

            from datetime import date

            today = str(date.today())

            if last_date == today:
                pass
            elif last_date == str(date.fromordinal(date.today().toordinal() - 1)):
                streak += 1
            else:
                streak = 1

            last_date = today
            print(f"Current Streak: {streak} days")

            if streak > longest_streak:
                longest_streak = streak
                print("New Longest Streak")

# awards bonus xp for streak milestones and begins level tracking
            
            if streak == 3:
                xp += 20
                print("Streak Reward: 20XP!")
            elif streak == 7:
                xp += 50
                print("Streak Reward: 50XP!")
            elif streak == 14:
                xp += 100
                print("Streak Reward: 100XP!")
            elif streak == 30:
                xp += 250
                print("Streak Reward: 250XP!")

# option 2: add a habit
    
    if choice == "2":
        new_habit = input("What habit would you like to add? ")
        habits.append(new_habit)
        habit_stats[new_habit] = [0, 0]
        print(f"Added habit: {new_habit}")

        

# option 3: remove a habit

    if choice == "3":
        print("Your habits: ", habits)
        remove_habit = input("What habit would you like to remove? ")

        if remove_habit in habits:
            habits.remove(remove_habit)
            print(f"Removed habit: {remove_habit}")
        else: 
            print("Habit not found.")
    
# option 4: quit
    
    if choice == "4":
        break
        
# option 5: reset xp

    if choice == "5":
        xp = 0
        print("XP has been reset to 0.")

# option 6: player info
    
    if choice == "6":
        
# part 1 of player info menu
        
        print("\n--- Player Info -")
        print("Total XP: ", xp)
        print("Current Streak: ", streak)
        print("Longest Streak: ", longest_streak)
        print("Total Habits: ", len(habits))
# determine most frequent and skipd habits
        
        if habit_stats:
            most_common = max(habit_stats, key=lambda h: habit_stats[h][0])
            most_skipped = max(habit_stats, key=lambda h: habit_stats[h][1])
        else:
            most_common = "None"
            most_skipped = "None"

# part 2 of player info menu
        
        print("Most Frequent Habit: ", most_common)
        print("Most Skipped Habit: ", most_skipped)
        print("Level: ", level)
        print("XP to next level: ", 100 - (xp % 100))
    
# saves player info back into files

    with open("data.txt", "w") as f:
        f.write(str(xp))

    with open("habit.txt", "w") as f:
        for h in habits:
            f.write(h + "\n")
            
    with open("streak.txt", "w") as f:
        f.write(str(streak) + "\n")
        f.write(last_date)

    with open("longest_streak.txt", "w") as f:
        f.write(str(longest_streak))

    with open("habit_stats.txt", "w") as f:
        for h in habit_stats:
            f.write(f"{h},{habit_stats[h][0]},{habit_stats[h][1]}\n")
