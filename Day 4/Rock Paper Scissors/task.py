import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer_choice = random.randint(0, 2)
my_choice = input('1 for rock, 2 for paper, 3 for scissors: ')

if not my_choice in ['1', '2', '3']:
    print('Invalid choice')
    exit()

options = [rock, paper, scissors]

int_choice = int(my_choice) - 1
print(options[int_choice])
print(options[computer_choice])

outcome = 'You win'
if computer_choice == int_choice:
    outcome = 'Draw'
elif computer_choice == 2:
    if int_choice == 1:
        outcome = 'You lose'
elif computer_choice == 0:
    if int_choice == 2:
        outcome = 'You lose'
elif computer_choice == 1:
    if int_choice == 0:
        outcome = 'You lose'

print(f"\nOutcome:{outcome}")
