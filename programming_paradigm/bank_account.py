class BankAccount:
  """
  A simple BankAccount class to represent a bank account and its operations.
  """

  def __init__(self, initial_balance=0.0):
    """
    Initializes the BankAccount object with an optional starting balance.

    Args:
      initial_balance (float, optional): The starting balance of the account. Defaults to 0.0.
    """
    self.account_balance = initial_balance

  def deposit(self, amount):
    """
    Deposits the specified amount into the account balance.

    Args:
      amount (float): The amount to deposit.
    """
    self.account_balance += amount

  def withdraw(self, amount):
    """
    Attempts to withdraw the specified amount from the account balance.

    Returns:
      bool: True if the withdrawal is successful, False otherwise.
    """
    if amount <= self.account_balance:
      self.account_balance -= amount
      return True
    else:
      return False

  def display_balance(self):
    """
    Prints the current balance in a user-friendly format.
    """
    print(f"Current Balance: ${self.account_balance:.2f}")
    