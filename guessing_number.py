import random
def guessing_number_game():
  print("Welcome to Number Guessing Game!")
  print("User is thinking the number between 1 to 100.")

secert_number = randim.randint(1,100)
attempts = 0
while True:
  try:
    guess = int(input("Enter your guess:"))
    attempts += 1
    if guess < 1 or guess > 100:
      print("Please guess a number between 1 and 100.")
    elif guess < secret_number:
      print("Too low!,Try Again.")
    elif guess > secret_number:
      print("Too high!,Try Again")
    else:
      print(f"Congratulations!You guessed it in {attempts}tries.")
      break
  except ValueError:
    print("Please enter a valid number.")

guessing_number_game()
      
