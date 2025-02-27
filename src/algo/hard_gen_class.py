import random

class HardNumberGenerator:
    def __init__(self, num_count):
        self.num_count = num_count

    def is_hard_sum(self, num):
        """Returns True if the number (as a string) contains at least one of '7', '8', or '9'."""
        hard_digits = {'7', '8', '9'}
        return any(d in str(num) for d in hard_digits)

    def random_hard_addend(self):
        """
        Returns a random 2-digit number constructed only from the digits 2,3,4,7,8,9.
        """
        valid_digits = [2, 3, 4, 7, 8, 9]
        tens = random.choice(valid_digits)
        ones = random.choice(valid_digits)
        return 10 * tens + ones

    def generate(self):
        """
        Generates a list of addends (each a two-digit number) so that when they are added sequentially,
        each partial sum contains at least one of the digits 7, 8, or 9.
        
        The first number is chosen such that it is "hard" (i.e. meets the criterion),
        and for each subsequent addend, we choose a candidate that, when added to the current sum,
        produces a new sum that is also hard.
        """
        addends = []
        
        # Choose the initial addend so that its value is "hard"
        current_sum = self.random_hard_addend()
        while not self.is_hard_sum(current_sum):
            current_sum = self.random_hard_addend()
        addends.append(current_sum)
        
        # For subsequent addends, ensure that the new partial sum is "hard"
        for _ in range(self.num_count - 1):
            found_next = False
            while not found_next:
                candidate = self.random_hard_addend()
                if self.is_hard_sum(current_sum + candidate):
                    addends.append(candidate)
                    current_sum += candidate
                    found_next = True
        return addends
