from art import logo, vs
from game_data import data
import random
import os

def clear():
   os.system('clear')

def format_data(account):
  """ Takes the account data and returns the printable format """
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follwer counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

# Display art
print(logo)
point = 0
game_over = False
account_b = random.choice(data)

# Make the game repeatable.
while not game_over:
  # Generate a random account from the game data

  # Making account at position B become the next account at position A.
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  
  # Ask yser for a guess
  
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # Check if user is correct
  ## Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
   # Clear the screen between rounds.
  clear()
  print(logo)
  
  # Give user feedback on their guess.
  # Score keeping.
  if is_correct:
    point += 1
    print(f"You're right! Current score: {point}.")
  else:
    game_over = True
    print(f"Sorry, that's wrong. Final socre: {point}.")
    regame = input("Do you want to play again? Type 'y' or 'n': ")
    if regame == "y":
      clear()
      game_over = False
      point = 0
    else:
      game_over = True      
  