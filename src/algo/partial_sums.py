import random

hard_digits = {'7','8','9'}
valid_digits = [2,3,4,7,8,9]

def is_hard_sum(num):
    """Example criterion: sum must contain at least one digit from 7,8,9."""
    return any(d in str(num) for d in hard_digits)

def random_hard_addend():
    """
    Returns a random 2-digit number from the digits 2,3,4,7,8,9
    """
    tens = random.choice(valid_digits)
    ones = random.choice(valid_digits)
    return 10*tens + ones

def generate_hard_sequence(length=10):
    """
    Generate a sequence of partial sums S0, S1, ..., S(length)
    such that each partial sum is 'hard' by some digit criterion.
    """
    sequence = []

    # Start with some random 2-digit "hard" number
    current_sum = random_hard_addend()
    while not is_hard_sum(current_sum):
        # if for some reason it's not "hard," keep picking
        current_sum = random_hard_addend()
    
    sequence.append(current_sum)
    
    # Now pick next addends to keep partial sums "hard"
    for _ in range(length-1):
        found_next = False
        # We'll keep trying to pick an addend until partial sum is "hard."
        while not found_next:
            candidate = random_hard_addend()
            new_sum = current_sum + candidate
            if is_hard_sum(new_sum):
                # Accept
                current_sum = new_sum
                sequence.append(current_sum)
                found_next = True
            else:
                # Reject and try again
                pass
    
    return sequence

# Example usage: generate a sequence of 10 "hard" partial sums
seq = generate_hard_sequence(10)
print(seq)
