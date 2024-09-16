
task = input("Enter a task description: ").strip()
priority = input("Enter the priority level (high, medium, low): ").lower().strip()
time_bound = input("Is the task time-bound? (yes or no): ").lower().strip()


match priority:
    case "high":
        priority_message = "This task is of high priority"
    case "medium":
        priority_message = "This task is of medium priority"
    case "low":
        priority_message = "This task is of low priority"
    case _:
        priority_message = "Unknown priority level"

if time_bound == "yes":
    time_message = "that requires immediate attention today!"
else:
    time_message = "that can be attended to later."


print(f"Reminder: {task}. {priority_message}, {time_message}")
