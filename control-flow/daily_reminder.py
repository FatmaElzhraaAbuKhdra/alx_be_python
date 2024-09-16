
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            reminder_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder_message = f"Reminder: '{task}' is a high priority task."
    case 'medium':
        if time_bound == 'yes':
            reminder_message = f"Reminder: '{task}' is a medium priority task that requires timely action!"
        else:
            reminder_message = f"Reminder: '{task}' is a medium priority task."
    case 'low':
        if time_bound == 'yes':
            reminder_message = f"Reminder: '{task}' is a low priority task but requires action soon."
        else:
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder_message = "Error: Invalid priority. Please enter high, medium, or low."


print(reminder_message)
