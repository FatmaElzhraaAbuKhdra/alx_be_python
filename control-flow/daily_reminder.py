def main():
  """
  This function prompts the user for a task, its priority, and time sensitivity,
  then displays a customized reminder.
  """
  # Get user input for task
  task = input("Enter your task: ")

  # Get user input for priority
  priority = input("Priority (high/medium/low): ").lower()

  # Get user input for time sensitivity
  time_bound = input("Is it time-bound? (yes/no): ").lower()

  # Process based on priority
  match priority:
    case "high":
      reminder = f"'{task}' is a high priority task"
    case "medium":
      reminder = f"Consider completing '{task}' when you have a chance"
    case "low":
      reminder = f"Note to self: '{task}' is a low priority task"
    case _:
      print("Invalid priority. Please choose high, medium, or low.")
      return

  # Add urgency if time-bound
  if time_bound == "yes":
    reminder += " that requires immediate attention today!"

  # Print the reminder with a clear message
  print(f"Reminder: {reminder}")  # Ensures "Reminder:" is included

if __name__ == "__main__":
  main()