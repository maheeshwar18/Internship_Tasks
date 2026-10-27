# Task 3: Test all 15 functions
from solutions import (
    word_frequency, character_frequency, first_non_repeating,
    are_anagrams, first_repeating, move_zeros,
    second_highest, remove_duplicates, missing_number,
    two_sum, closest_to_zero, common_elements,
    rotate_right, max_consecutive_sum, all_pairs
)

# Qno 1
print("Q1 Example:", word_frequency("python is easy and python is powerful"))
print("Q1 Test:", word_frequency("This is a test. This test is only a test."))

# Qno 2
print("Q2 Example:", character_frequency("banana"))
print("Q2 Test:", character_frequency("success"))

# Qno 3
print("Q3 Example:", first_non_repeating("swiss"))
print("Q3 Test:", first_non_repeating("How to talk to anyone?"))

# Qno 4
print("Q4 Example:", are_anagrams("listen", "silent"))
print("Q4 Test:", are_anagrams("Indian", "Poltics"))

# Qno 5
print("Q5 Example:", first_repeating("programming"))
print("Q5 Test:", first_repeating("Internationalization"))

# Qno 6
print("Q6 Example:", move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Q6 Test:", move_zeros([1, 0, 0, 6, 2, 3]))

# Qno 7
print("Q7 Example:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 Test:", second_highest([5, 5, 5, 7, 7, 8]))

# Qno 8
print("Q8 Example:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 Test:", remove_duplicates([1, 1, 2, 3, 2, 4, 3, 4]))

# Qno 9
print("Q9 Example:", missing_number([1, 2, 4, 5, 6], 6))
print("Q9 Test:", missing_number([1, 3, 4], 4))

# Qno 10
print("Q10 Example:", two_sum([2, 7, 11, 15], 9))
print("Q10 Test:", two_sum([1, 2, 3], 10))

# Qno 11
print("Q11 Example:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 Test:", closest_to_zero([-4, -1, 1, 2, 3]))

# Qno 12
print("Q12 Example:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 Test:", common_elements([2, 2, 3, 4], [2, 4]))

# Qno 13
print("Q13 Example:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 Test:", rotate_right([1, 2, 3], 0))

# Qno 14
print("Q14 Example:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 Test:", max_consecutive_sum([-5, -2, -1, -8]))

# Qno 15
print("Q15 Example:", all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 Test:", all_pairs([1, 2, 3], 20))
