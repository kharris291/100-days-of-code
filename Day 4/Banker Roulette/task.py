import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

who_will_pay = random.choice(friends)
print(who_will_pay)

random_index = random.randint(0, len(friends)-1)
print(friends[random_index])
