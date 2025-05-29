# daily_reminder.py

def daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity,
    then provides a customized reminder.
    """
    print("Let's set a daily reminder for your priority task!")

    # Prompt for task description
    task_description = input("Enter your task: ")

    # Prompt for priority with input validation using a loop
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            break
        else:
            print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

    # Prompt for time-bound status with input validation using a loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Initialize the base reminder message
    reminder_message = ""

    # Use match-case to determine the base message based on priority
    # This feature is available in Python 3.10 and later.
    match priority:
        case "high":
            reminder_message = f"Reminder: '{task_description}' is a high priority task"
        case "medium":
            reminder_message = f"Note: '{task_description}' is a medium priority task"
        case "low":
            reminder_message = f"Note: '{task_description}' is a low priority task"
        # The 'else' or '_' case is not strictly needed here due to input validation loops
        # ensuring 'priority' is always one of 'high', 'medium', 'low'.

    # Use an if statement to modify the reminder for time-bound tasks
    if time_bound == "yes":
        reminder_message += " that requires immediate attention today!"
    else:
        # Add specific non-time-bound advice based on priority
        if priority == "low":
            reminder_message += ". Consider completing it when you have free time."
        elif priority == "medium":
            reminder_message += ". Aim to complete it within the day."
        else: # High priority, but not time-bound (still important)
            reminder_message += ". Ensure it gets done today."


    # Print the final customized reminder
    print("\n" + reminder_message)

    # Project completion message
    print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
    print("🚀 Click here to tweet! 🚀")

# Ensure the function runs when the script is executed directly
if __name__ == "__main__":
    daily_reminder()