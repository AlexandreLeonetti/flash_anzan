#filtering approach
import random

def contains_hard_digit(num, hard_digits={'7','8','9'}):
    """
    Returns True if the integer `num` (converted to string)
    contains at least one digit from `hard_digits`.
    """
    return any(d in str(num) for d in hard_digits)

def generate_hard_pairs(n_samples=1000):
    """
    Generate a list of (a, b) pairs where each digit of a and b
    is from {2,3,4,7,8,9}, and the sum also contains 7,8, or 9.
    """
    valid_digits = [2,3,4,7,8,9]
    pairs = []
    
    for _ in range(n_samples):
        a = 10*random.choice(valid_digits) + random.choice(valid_digits)
        b = 10*random.choice(valid_digits) + random.choice(valid_digits)
        
        # Check if sum has hard digit
        s = a + b
        if contains_hard_digit(s):
            pairs.append((a, b))
    
    return pairs

# Example usage:
hard_pairs = generate_hard_pairs()
print("Number of generated pairs:", len(hard_pairs))
print("Sample pairs:", hard_pairs[:10])
