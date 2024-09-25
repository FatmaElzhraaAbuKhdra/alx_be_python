from datetime import datetime, timedelta

def display_current_datetime():
    """Prints the current date and time in YYYY-MM-DD HH:MM:SS format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    """Calculates and prints the future date after adding specified days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Enter the number of days to add to the current date: {days}")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    num_days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(num_days)