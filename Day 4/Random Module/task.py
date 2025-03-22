import random

rand_num_0_to_1 = random.randint(0,1)
print(rand_num_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

if rand_num_0_to_1  == 0:
    print("Heads")
else:
    print("Tails")