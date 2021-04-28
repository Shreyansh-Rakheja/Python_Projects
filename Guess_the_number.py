from random import randint

guess_number = randint(0, 100)
tries = 8

while True:
  player_number = int(input(f'You have {tries} tries.\nGuess the number:\n'))

  if player_number == guess_number:
    print('BINGO!')
    break
  elif player_number > guess_number:
    print('Too high!')
  elif player_number < guess_number:
    print('Too low!')

  tries -= 1
  if tries <= 0:
    print("Sorry, but you didn't manage to guess the number :(")
    break
