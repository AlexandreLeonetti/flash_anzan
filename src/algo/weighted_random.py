import random

# Weighted distribution for digits 0-9 (just an example):
# 7,8,9 have weight = 5
# 2,3,4 have weight = 3
# everything else has weight = 1
digit_weights = {
    0: 1, 1: 1, 2: 3, 3: 3, 4: 3, 
    5: 1, 6: 1, 7: 5, 8: 5, 9: 5
}

# Build a cumulative weighted list
all_digits = []
for d, w in digit_weights.items():
    all_digits.extend([d]*w)
# Now picking randomly from 'all_digits' biases toward bigger weights

def weighted_random_digit():
    return random.choice(all_digits)

def random_hardish_number():
    # tens place: pick from 1..9 (avoid leading 0 for 2-digit)
    # but weighted
    tens = random.choice([d for d in all_digits if d != 0])
    ones = weighted_random_digit()
    return 10*tens + ones

# Example usage: generate 20 random "hard-ish" numbers
for _ in range(20):
    print(random_hardish_number())
