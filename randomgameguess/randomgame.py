import sys
import random

begin_interval = int(sys.argv[1])
end_interval = int(sys.argv[2])

print(f'Give a number from {begin_interval} to {end_interval}:')
user_input = int(input())
random_number = random.randint(begin_interval, end_interval)
print(random_number)

while user_input != random_number:
    print('Try until you make it!')
    print(f'Give a new number from {begin_interval} to {end_interval}:')
    user_input = int(input())

print('You\'re a genius!')
