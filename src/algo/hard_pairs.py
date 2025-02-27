import random

def hardness_score(a, b):
    """
    Score how 'hard' a pair is based on digits 7,8,9 in a, b, and (a+b).
    Example: +2 for each occurrence of 7,8,9
    """
    total_score = 0
    for num in [a, b, a+b]:
        for d in str(num):
            if d in {'7','8','9'}:
                total_score += 2
    return total_score

pairs = []
for _ in range(5000):
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    score = hardness_score(a, b)
    pairs.append((a, b, score))

# Sort by score descending
pairs.sort(key=lambda x: x[2], reverse=True)

# The top N are the "hardest" pairs
hardest_pairs = pairs[:100]
print(hardest_pairs)
