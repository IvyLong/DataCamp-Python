import random
import time
from datetime import datetime

# Get current time information
current_time = datetime.now()
hour = current_time.hour
name = input("What's your name? ")

# Create greeting based on time of day
if hour < 12:
    greeting = f"Good morning, {name}!"
elif hour < 17:
    greeting = f"Good afternoon, {name}!"
else:
    greeting = f"Good evening, {name}!"

# Date information
date_string = current_time.strftime("%A, %B %d, %Y")

# Motivational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "It always seems impossible until it's done. - Nelson Mandela",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
]

# Select random quote
daily_quote = random.choice(quotes)

# Print the briefing
print("\n" + "=" * 50)
print(f"\n{greeting}")
print(f"Today is {date_string}")
print(f"\nYour inspiration for today:\n\"{daily_quote}\"")
print("\n" + "=" * 50)

# Simple to-do list functionality
print("\nTODO LIST MANAGER")
todos = []

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        task = input("Enter a new task: ")
        todos.append(task)
        print("Task added!")
    elif choice == "2":
        if not todos:
            print("Your to-do list is empty!")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not todos:
            print("No tasks to complete!")
        else:
            for i, task in enumerate(todos, 1):
                print(f"{i}. {task}")
            task_num = int(input("Enter task number to mark as complete: "))
            if 1 <= task_num <= len(todos):
                completed_task = todos.pop(task_num - 1)
                print(f"Completed: {completed_task}")
            else:
                print("Invalid task number!")
    elif choice == "4":
        print("Have a productive day!")
        break
    else:
        print("Invalid choice. Please try again.")